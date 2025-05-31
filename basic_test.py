print("Starting test...")

try:
    print("Testing enum...")
    from enum import Enum
    
    class TestEnum(Enum):
        A = "a"
        B = "b"
    
    print("Enum works!")
    
    print("Testing dataclass...")
    from dataclasses import dataclass
    
    @dataclass
    class TestClass:
        name: str
        value: int
    
    print("Dataclass works!")
    
    obj = TestClass("test", 123)
    print(f"Created object: {obj}")
    
    print("All tests passed!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
