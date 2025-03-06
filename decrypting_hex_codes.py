def decode_obfuscated(hex_str):
    """Attempt to decode the obfuscated value based on observed patterns."""
    num = int(hex_str, 16)

    # Extract last byte
    last_byte = num & 0xFF  # Get the last byte
    rest = num >> 8         # Shift right to remove last byte

    # Determine sign
    if last_byte & 0x80:  # If the high bit is set, it's negative
        sign = -1
        last_byte = last_byte - 0x80
    else:
        sign = 1

    # Approximate value
    original_value = (rest << 4) + (last_byte // 8)

    return sign * original_value

# Test cases
test_values = {
    "-750": "803BC4",
    "750": "803B44",
    "-10": "20C1",
    "10": "2041",
    "0": "0",
    "5": "A040",
    "8": "41",
    "15": "7041",
    "70": "8C42",
    "100": "C842"
}

for original, hex_value in test_values.items():
    print(f"Decoded {hex_value} → {decode_obfuscated(hex_value)} (Expected: {original})")
