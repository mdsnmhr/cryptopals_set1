# CryptoPals Challenge Set 1 Challenge 1
# convert hexadecimal to base64
# Author: Madison H.
# Last Updated: 7/14/2026

from base64 import b16decode, b64encode

def convert_hex_to_base64(hex_input):
    data_raw = b16decode(hex_input, casefold=True)
    data_b64 = b64encode(data_raw)
    return data_b64

def main():
    hex_input = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    base64_output = convert_hex_to_base64(hex_input)
    expected = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    
    if base64_output == expected:
        print(f"Input: {hex_input}")
        print(f"Output: {base64_output}")
    else:
        print(f"Input: {hex_input}")
        print(f"Output: {base64_output}")
        print(f"Expected: {expected}")

if __name__ == "__main__":
    main()