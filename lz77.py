def lz77_compress(input_string, window_size=10, lookahead_buffer_size=5):
    compressed_data = []
    i = 0
    
    while i < len(input_string):
        searchBuffer_size = window_size - lookahead_buffer_size
        lookahead_buffer = input_string[i:i + lookahead_buffer_size]
        
        if i < searchBuffer_size:
            searchBuffer = input_string[:i]
        else:
            searchBuffer = input_string[i - searchBuffer_size:i]
        
        match_length = 0
        match_distance = 0
        for j in range(1, len(lookahead_buffer) + 1):
            substring = lookahead_buffer[:j]
            pos = searchBuffer.rfind(substring)  
            
            if pos != -1:  
                match_distance = len(searchBuffer) - pos
                match_length = j
            else:
                break  
        
        
        if match_length > 0:
            next_char = input_string[i + match_length] if i + match_length < len(input_string) else ""
            compressed_data.append((match_distance, match_length, next_char))
            i += match_length + 1  # Move past the matched sequence and next char
        else:
    
            compressed_data.append((0, 0, input_string[i]))
            i += 1 

    return compressed_data


def lz77_decompress(compressed_data):
    i = 0
    decompressed_data =""
    for j in range(0,len(compressed_data)):
        if compressed_data[j][0] == 0 and compressed_data[j][1] == 0:
            decompressed_data += compressed_data[j][2]
            i+=1
            
        else :
            pos = len(decompressed_data) - compressed_data[j][0]
            decompressed_data+= decompressed_data[pos: pos +compressed_data[j][1]]+ compressed_data[j][2]
            i+=1
    return decompressed_data



test =lz77_decompress(lz77_compress("abaababaabb bbbbbbbbbba"))
print(lz77_compress("abaababaabb bbbbbbbbbba"))
print(test)