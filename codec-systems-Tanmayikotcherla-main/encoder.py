
def encode(input_data):
    encoded_data = []
    encoded_data.append(len(input_data))
    for key in sorted(input_data.keys()):
        value = input_data[key]
        key_bytes = key.encode()
        encoded_data.append(len(key_bytes))
        encoded_data.extend(key_bytes)
        
        if value is None:
            encoded_data.append(0x03)  
            encoded_data.append(0x00)  
            
        elif isinstance(value, list):  
            encoded_data.append(0x06)  
            encoded_data.append(len(value))  
            encoded_data.extend(value)  
            
        elif isinstance(value, int):
            encoded_data.append(0x07)  
            value_bytes = str(value).encode()
            encoded_data.extend(value_bytes)
    
    return encoded_data