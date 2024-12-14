# test_vectors.py
def test_vector(input_data, expected_output):
    encoded = encode(input_data)
    print(f"Encoded: {encoded}")
    print(f"Expected: {expected_output}")
    assert encoded == expected_output, f"Encoding failed: {encoded} != {expected_output}"
    
    decoded = decode(encoded)
    print(f"Decoded: {decoded}")
    print(f"Input: {input_data}")
    assert decoded == input_data, f"Decoding failed: {decoded} != {input_data}"