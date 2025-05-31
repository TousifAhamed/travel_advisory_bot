import requests
import json
from typing import Dict, Optional, Any
from ..models import AIModel, ProcessedInput

# Handle optional imports gracefully for Python 3.13 compatibility
OPENAI_AVAILABLE = False
TRANSFORMERS_AVAILABLE = False

# Try HuggingFace Transformers first (better Python 3.13 support)
try:
    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    TRANSFORMERS_AVAILABLE = True
    print("✅ HuggingFace Transformers available")
except ImportError as e:
    print(f"⚠️  HuggingFace Transformers not available: {e}")

# Try OpenAI as fallback (may have Python 3.13 issues)
try:
    import openai
    OPENAI_AVAILABLE = True
    print("✅ OpenAI library available")
except ImportError as e:
    print(f"⚠️  OpenAI not available (Python 3.13 compatibility issue): {e}")
    openai = None

# Handle config import gracefully
try:
    from config.settings import Config
except ImportError:
    # Fallback config if not available
    class Config:
        DEFAULT_LLM_MODEL = "microsoft/DialoGPT-medium"  # Use HuggingFace model as default
        OPENAI_API_KEY = None
        HUGGINGFACE_TOKEN = None
        OLLAMA_BASE_URL = "http://localhost:11434"
        DEVSTRAL_MODEL_NAME = "devstral"
        HUGGINGFACE_MODEL = "microsoft/DialoGPT-medium"

class OpenAIModel(AIModel):
    """OpenAI GPT model implementation"""
    
    def __init__(self, model_name: str = None):
        if not OPENAI_AVAILABLE:
            raise ImportError("OpenAI library not available. Please install openai compatible with Python 3.13 or use alternative models.")
        
        self.model_name = model_name or Config.DEFAULT_LLM_MODEL
        try:
            self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        except Exception as e:
            print(f"Warning: Failed to initialize OpenAI client: {e}")
            self.client = None
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using OpenAI API"""
        if not self.client:
            raise RuntimeError("OpenAI client not available")
        try:
            messages = []
            if context:
                messages.append({"role": "system", "content": context})
            messages.append({"role": "user", "content": prompt})
            
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=2000,
                temperature=0.7
            )
            
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"
    
    async def analyze_input(self, processed_input: ProcessedInput) -> Dict[str, Any]:
        """Analyze input for travel-related entities and intent"""
        analysis_prompt = f"""
        Analyze the following travel-related input and extract:
        1. Destinations mentioned
        2. Travel dates or duration
        3. Budget information
        4. Travel preferences
        5. Activities of interest
        6. Group size
        7. Special requirements
        
        Input: {processed_input.content}
        Input Type: {processed_input.input_type.value}
        Language: {processed_input.language}
        
        Return the analysis in JSON format.
        """
        
        response = await self.generate_response(analysis_prompt)
        try:
            return json.loads(response)
        except:
            return {"raw_analysis": response}

class HuggingFaceModel(AIModel):
    """Hugging Face model implementation"""
    
    def __init__(self, model_name: str = None):
        self.model_name = model_name or Config.HUGGINGFACE_MODEL
        self.api_key = Config.HUGGINGFACE_API_KEY
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_name}"
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using Hugging Face API"""
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            
            full_prompt = prompt
            if context:
                full_prompt = f"Context: {context}\n\nQuery: {prompt}"
            
            payload = {
                "inputs": full_prompt,
                "parameters": {
                    "max_length": 1000,
                    "temperature": 0.7,
                    "do_sample": True
                }
            }
            
            response = requests.post(self.api_url, headers=headers, json=payload)
            result = response.json()
            
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', 'No response generated')
            else:
                return str(result)
                
        except Exception as e:
            return f"Error with Hugging Face API: {str(e)}"
    
    async def analyze_input(self, processed_input: ProcessedInput) -> Dict[str, Any]:
        """Analyze input using Hugging Face model"""
        analysis_prompt = f"Extract travel information from: {processed_input.content}"
        response = await self.generate_response(analysis_prompt)
        return {"analysis": response, "model": "huggingface"}

class OllamaModel(AIModel):
    """Ollama local model implementation optimized for Devstral"""
    
    def __init__(self, model_name: str = "devstral"):
        self.model_name = model_name
        self.base_url = Config.OLLAMA_BASE_URL
    
    async def generate_response(self, prompt: str, context: Optional[str] = None) -> str:
        """Generate response using Ollama local API with Devstral optimization"""
        try:
            url = f"{self.base_url}/api/generate"
            
            # Enhanced prompt engineering for Devstral's agentic capabilities
            system_prompt = """You are a sophisticated AI travel advisor with deep knowledge of global destinations, travel planning, and cultural insights. Provide detailed, personalized, and actionable travel recommendations."""
            
            full_prompt = f"{system_prompt}\n\n"
            if context:
                full_prompt += f"Context: {context}\n\n"
            full_prompt += f"Query: {prompt}\n\nResponse:"
            
            payload = {
                "model": self.model_name,
                "prompt": full_prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                    "top_k": 40,
                    "num_predict": 1024,
                    "stop": ["Human:", "User:"]
                }
            }
            
            response = requests.post(url, json=payload, timeout=90)
            response.raise_for_status()
            result = response.json()
            
            return result.get('response', 'No response from Ollama').strip()
            
        except requests.exceptions.RequestException as e:
            return f"Connection error with Ollama (ensure Devstral is running): {str(e)}"
        except Exception as e:
            return f"Error with Ollama API: {str(e)}"
    
    async def analyze_input(self, processed_input: ProcessedInput) -> Dict[str, Any]:
        """Analyze input using Devstral with enhanced travel context understanding"""
        analysis_prompt = f"""
        Analyze this travel-related content and extract structured information:
        
        Content Type: {processed_input.type.value}
        Content: {processed_input.content}
        
        Please extract and return:
        1. Destinations mentioned
        2. Travel dates or timeframes
        3. Budget information
        4. Travel preferences (accommodation, activities, food, etc.)
        5. Group size and demographics
        6. Special requirements or constraints
        7. Travel goals or purposes
        
        Format your response as structured data.
        """
        
        response = await self.generate_response(analysis_prompt)
        return {
            "analysis": response, 
            "model": f"ollama-{self.model_name}",
            "enhanced_processing": True
        }

class ModelFactory:
    """Factory for creating AI model instances"""
    
    @staticmethod
    def create_model(model_type: str = "ollama") -> AIModel:
        """Create AI model instance based on type"""
        if model_type.lower() == "ollama":
            # Use Devstral as the default Ollama model
            return OllamaModel(Config.OLLAMA_MODEL or "devstral")
        elif model_type.lower() == "openai" and Config.OPENAI_API_KEY:
            return OpenAIModel()
        elif model_type.lower() == "huggingface" and Config.HUGGINGFACE_API_KEY:
            return HuggingFaceModel()
        else:
            # Fallback to Ollama with Devstral
            return OllamaModel("devstral")
