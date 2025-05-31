"""
Minimal models file for testing imports
"""

from enum import Enum
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

class InputType(Enum):
    TEXT = "text"
    IMAGE = "image" 
    PDF = "pdf"
    VIDEO = "video"
    AUDIO = "audio"

@dataclass
class TravelPreferences:
    budget_range: str
    travel_style: str
    interests: List[str]
    group_size: int
    accommodation_type: str
    dietary_restrictions: List[str]
    language_preference: str

@dataclass
class ProcessedInput:
    input_type: InputType
    content: str
    metadata: Dict[str, Any]
    language: str
    confidence: float
    extracted_entities: Dict[str, Any]

print("Minimal models loaded successfully")
