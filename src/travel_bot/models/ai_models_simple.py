"""
AI Models for Travel Advisory Bot - Python 3.13 Compatible Architecture
Prioritizes local models (Ollama, HuggingFace) over cloud APIs for better reliability
"""

import requests
import json
import asyncio
from typing import Dict, Optional, Any, List
from ..models import AIModel, ProcessedInput

# Python 3.13 Compatible Dependencies
TRANSFORMERS_AVAILABLE = False
TORCH_AVAILABLE = False

# HuggingFace Transformers (Primary choice for local models)
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    import torch
    TRANSFORMERS_AVAILABLE = True
    TORCH_AVAILABLE = True
    print("✅ HuggingFace Transformers + PyTorch available")
except ImportError as e:
    print(f"⚠️  HuggingFace Transformers not available: {e}")

# Configuration - Fallback if config not available
try:
    from config.settings import Config
except ImportError:
    class Config:
        OLLAMA_BASE_URL = "http://localhost:11434"
        DEVSTRAL_MODEL_NAME = "devstral"
        HUGGINGFACE_MODEL = "microsoft/DialoGPT-medium"
        HUGGINGFACE_TOKEN = None
        # Removed OpenAI config due to Python 3.13 compatibility

class DevstralModel(AIModel):
    """
    Devstral model via Ollama - Primary AI backend
    Optimized for travel advisory and agentic reasoning
    """
    
    def __init__(self, model_name: str = "devstral"):
        self.model_name = model_name
        self.base_url = getattr(Config, 'OLLAMA_BASE_URL', "http://localhost:11434")
        self.is_available = self._check_availability()
    
    def _check_availability(self) -> bool:
        """Check if Ollama and Devstral are running"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            models = response.json().get('models', [])
            return any(model.get('name', '').startswith(self.model_name) for model in models)
        except:
            return False
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate travel advisory response using Devstral"""
        if not self.is_available:
            return "Devstral model not available. Please ensure Ollama is running with Devstral model."
        
        try:
            # Enhanced system prompt for travel advisory
            system_prompt = """You are an expert AI travel advisor with comprehensive knowledge of:
- Global destinations, attractions, and hidden gems
- Cultural insights and local customs
- Travel logistics, visas, and requirements
- Budget planning and optimization
- Safety considerations and travel advisories
- Sustainable and responsible tourism

Provide detailed, personalized, and actionable travel recommendations. Always consider the traveler's preferences, budget, and constraints."""

            full_prompt = f"{system_prompt}\n\n"
            if context:
                full_prompt += f"Context: {context}\n\n"
            full_prompt += f"Travel Query: {prompt}\n\nDetailed Response:"
            
            payload = {
                "model": self.model_name,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "top_k": 40,
                    "num_predict": 1024,
                    "stop": ["Human:", "User:", "Query:"]
                }
            }
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            
            return result.get('response', 'No response generated').strip()
            
        except Exception as e:
            return f"Error with Devstral model: {str(e)}"
    
    async def analyze_input(self, processed_input: ProcessedInput) -> Dict[str, Any]:
        """Analyze travel input using Devstral's enhanced reasoning"""
        analysis_prompt = f"""
        As an AI travel expert, analyze this input and extract structured travel information:
        
        Input Type: {processed_input.input_type.value}
        Content: {processed_input.content}
        Detected Language: {processed_input.language}
        
        Extract and structure the following information:
        1. Destinations (mentioned or implied)
        2. Travel timeline (dates, duration, seasons)
        3. Budget considerations (explicit or implied range)
        4. Travel style preferences (luxury, budget, adventure, cultural, etc.)
        5. Group composition (solo, couple, family, friends)
        6. Special interests (food, history, nature, nightlife, etc.)
        7. Constraints or requirements (accessibility, dietary, visa, etc.)
        8. Trip purpose (leisure, business, education, etc.)
        
        Format as structured data with confidence scores.
        """
        
        response = await self.generate_response(analysis_prompt)
        return {
            "detailed_analysis": response,
            "model": f"devstral-{self.model_name}",
            "capabilities": ["travel_expert", "cultural_insights", "personalization"],
            "processing_time": "optimized_local"
        }

class HuggingFaceLocalModel(AIModel):
    """
    Local HuggingFace model for offline processing
    Fallback when cloud services are unavailable
    """
    
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium"):
        self.model_name = model_name
        self.model = None
        self.tokenizer = None
        self.is_loaded = False
        
        if TRANSFORMERS_AVAILABLE:
            self._load_model()
    
    def _load_model(self):
        """Load model locally"""
        try:
            print(f"Loading {self.model_name} locally...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            self.model = AutoModelForCausalLM.from_pretrained(self.model_name)
            self.is_loaded = True
            print(f"✅ {self.model_name} loaded successfully")
        except Exception as e:
            print(f"❌ Failed to load {self.model_name}: {e}")
            self.is_loaded = False
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using local HuggingFace model"""
        if not self.is_loaded:
            return "Local HuggingFace model not available. Please ensure transformers library is installed."
        
        try:
            # Prepare input
            travel_context = "Travel Advisory Context: Provide helpful travel information and recommendations.\n\n"
            full_prompt = travel_context
            if context:
                full_prompt += f"Context: {context}\n"
            full_prompt += f"Query: {prompt}\nResponse:"
            
            # Tokenize and generate
            inputs = self.tokenizer.encode(full_prompt, return_tensors="pt")
            
            with torch.no_grad():
                outputs = self.model.generate(
                    inputs,
                    max_length=inputs.shape[1] + 200,
                    temperature=0.7,
                    pad_token_id=self.tokenizer.eos_token_id,
                    do_sample=True
                )
            
            response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Extract only the generated part
            response = response[len(full_prompt):].strip()
            
            return response if response else "Unable to generate response with local model."
            
        except Exception as e:
            return f"Error with local HuggingFace model: {str(e)}"
    
    async def analyze_input(self, processed_input: ProcessedInput) -> Dict[str, Any]:
        """Basic analysis using local model"""
        prompt = f"Analyze this travel input: {processed_input.content}"
        response = await self.generate_response(prompt)
        return {
            "analysis": response,
            "model": f"local-{self.model_name}",
            "processing": "offline"
        }

class OllamaGenericModel(AIModel):
    """
    Generic Ollama model support for various models
    Supports Llama, Mistral, CodeLlama, and other Ollama models
    """
    
    def __init__(self, model_name: str = "llama2"):
        self.model_name = model_name
        self.base_url = getattr(Config, 'OLLAMA_BASE_URL', "http://localhost:11434")
        self.available_models = self._get_available_models()
    
    def _get_available_models(self) -> List[str]:
        """Get list of available Ollama models"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            models = response.json().get('models', [])
            return [model.get('name', '') for model in models]
        except:
            return []
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using any Ollama model"""
        if self.model_name not in self.available_models:
            return f"Model {self.model_name} not available. Available models: {', '.join(self.available_models)}"
        
        try:
            system_prompt = "You are a helpful AI assistant specializing in travel advice and planning."
            
            full_prompt = f"{system_prompt}\n\n"
            if context:
                full_prompt += f"Context: {context}\n\n"
            full_prompt += f"Request: {prompt}\n\nResponse:"
            
            payload = {
                "model": self.model_name,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "num_predict": 512
                }
            }
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=45
            )
            response.raise_for_status()
            result = response.json()
            
            return result.get('response', 'No response generated').strip()
            
        except Exception as e:
            return f"Error with Ollama model {self.model_name}: {str(e)}"
    
    async def analyze_input(self, processed_input: ProcessedInput) -> Dict[str, Any]:
        """Analyze input using generic Ollama model"""
        prompt = f"Extract travel information from: {processed_input.content}"
        response = await self.generate_response(prompt)
        return {
            "analysis": response,
            "model": f"ollama-{self.model_name}",
            "local_processing": True
        }

class ModelFactory:
    """
    Enhanced Model Factory - Python 3.13 Compatible
    Priority: Devstral > Local HuggingFace > Generic Ollama
    """
    
    @staticmethod
    def get_best_available_model() -> AIModel:
        """Get the best available model automatically"""
        # Priority 1: Devstral via Ollama (best for travel advisory)
        devstral = DevstralModel()
        if devstral.is_available:
            print("🎯 Using Devstral model (optimal for travel advisory)")
            return devstral
        
        # Priority 2: Check for other Ollama models
        generic_ollama = OllamaGenericModel("llama2")
        if generic_ollama.available_models:
            best_model = generic_ollama.available_models[0]
            print(f"🔄 Using Ollama model: {best_model}")
            return OllamaGenericModel(best_model)
        
        # Priority 3: Local HuggingFace model
        if TRANSFORMERS_AVAILABLE:
            print("🏠 Using local HuggingFace model")
            return HuggingFaceLocalModel()
        
        # Fallback: Return Devstral anyway (will show appropriate error)
        print("⚠️  No models available, returning Devstral (may need setup)")
        return devstral
    
    @staticmethod
    def create_model(model_type: str = "auto") -> AIModel:
        """Create specific model instance"""
        if model_type == "auto":
            return ModelFactory.get_best_available_model()
        elif model_type == "devstral":
            return DevstralModel()
        elif model_type == "huggingface":
            return HuggingFaceLocalModel()
        elif model_type.startswith("ollama:"):
            model_name = model_type.split(":", 1)[1]
            return OllamaGenericModel(model_name)
        else:
            return ModelFactory.get_best_available_model()
    
    @staticmethod
    def list_available_models() -> Dict[str, Any]:
        """List all available models and their status"""
        models_status = {
            "devstral": DevstralModel().is_available,
            "local_huggingface": TRANSFORMERS_AVAILABLE,
            "ollama_models": OllamaGenericModel().available_models,
            "recommendations": {
                "primary": "devstral (Agentic AI optimized for travel)",
                "fallback": "local_huggingface (Offline processing)",
                "alternative": "ollama_models (Various local models)"
            }
        }
        return models_status

# Convenience aliases for backward compatibility
OllamaModel = DevstralModel  # Backward compatibility
DevstralModel = DevstralModel  # Primary recommendation
