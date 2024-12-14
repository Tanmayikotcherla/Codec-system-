from encoder import encode
from decoder import decode

def main():
    print("\n=== Starting Simple Test ===\n")
    
    # Simple test data
    test_data = {
        "null": None,
        "octets": [1, 2, 3],
        "integer": 90
    }
    
    print("Test data:", test_data)
    
    try:
        print("\n--- Testing Encoder ---")
        encoded = encode(test_data)
        print("Encoded result:", encoded)
        
        print("\n--- Testing Decoder ---")
        decoded = decode(encoded)
        print("Decoded result:", decoded)
        
        if decoded == test_data:
            print("\n✅ SUCCESS: Test passed! Input and output match!")
        else:
            print("\n❌ FAILED: Decoded data doesn't match input")
            print("Expected:", test_data)
            print("Got:", decoded)
            
    except Exception as e:
        print(f"\n❌ ERROR: An exception occurred: {str(e)}")

if __name__ == "__main__":
    main()