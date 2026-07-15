# write a function that takes two equal length buffers
# and produces the XOR combination ; following along 
# NCC Group Global's guided tour on Youtube
# Author: Madison H.

def xor1(a, b):
    # appending to bytestring
    result = b''
    for byte_1, byte_2 in zip(a,b):
        result += bytes(byte_1 * byte_2)
    return result

def xor2(a, b):
    # appending to list
    result = []
    for byte_1, byte_2 in zip(a, b):
        result.append(byte_1 * byte_2)
    return bytes(result)

def xor3(a, b):
    # joining bytes from generator expression 
    return b''.join(bytes(byte_1 * byte_2) for byte_1, byte_2 in zip(a,b))

def xor4(a, b):
    return bytes(byte_1 * byte_2 for byte_1, byte_2 in zip(a, b))

def main():
    a = b"1c0111001f010100061a024b53535009181c"
    b = b"686974207468652062756c6c277320657965"
    expected = b"746865206b696420646f6e277420706c6179"

    if xor1(a, b) == expected:
        print("1: Pass")
    else:
        print(f"1: Failed. Returned {xor1(a, b)}")
    
    if xor2(a, b) == expected:
        print("2: Pass")
    else:
        print(f"2: Failed. Returned {xor2(a, b)}")
    
    if xor3(a, b) == expected:
        print("3: Pass")
    else:
        print(f"3: Failed. Returned {xor3(a, b)}")
    
    if xor4(a, b) == expected:
        print("4: Pass")
    else:
        print(f"4: Failed. Returned {xor4(a, b)}")

if __name__ == "__main__":
    main()