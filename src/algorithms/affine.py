def affine_cipher(text, key_a, key_b, mode):
    result = ""
    for char in text:
        if char.isalpha():
            offset = ord('a') if char.islower() else ord('A')
            x = ord(char) - offset

            if mode == "encrypt":
                # Encryption formula: E(x) = (a * x + b) mod 26
                e = (key_a * x + key_b) % 26
                result += chr(e + offset)  # Convert back to character
            else:
                # Decryption formula: D(x) = a^-1 * (x - b) mod 26
                a_inv = -1
                for i in range(26):
                    if (key_a * i) % 26 == 1:
                        a_inv = i
                        break
                if a_inv == -1:
                    return "Invalid key for decryption"
                d = (a_inv * (x - key_b)) % 26
                result += chr(d + offset)
        else:
            result += char
    return result