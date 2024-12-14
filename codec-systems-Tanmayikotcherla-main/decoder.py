
def decode(encoded_data):
    decoded_data = {}
    num_items = encoded_data[0]
    idx = 1
    
    for _ in range(num_items):
        if idx >= len(encoded_data):
            break
        key_length = encoded_data[idx]
        idx += 1
        key = bytes(encoded_data[idx:idx + key_length]).decode()
        idx += key_length
        if idx >= len(encoded_data):
            break
        tag = encoded_data[idx]
        idx += 1
        
        if tag == 0x03:  
            decoded_data[key] = None
            idx += 1  
            
        elif tag == 0x06:  
            if idx >= len(encoded_data):
                break
            value_length = encoded_data[idx]
            idx += 1
            value = encoded_data[idx:idx + value_length]
            decoded_data[key] = list(value)  
            idx += value_length
            
        elif tag == 0x07:  
            value_bytes = []
            while idx < len(encoded_data) and chr(encoded_data[idx]).isdigit():
                value_bytes.append(encoded_data[idx])
                idx += 1
            value = int(bytes(value_bytes).decode())
            decoded_data[key] = value
    
    return decoded_data