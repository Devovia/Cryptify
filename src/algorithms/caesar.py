def caesar_cipher(text, key, mode):
  result = ""
  for char in text:
      if char.isalpha():
          shift = key if mode == "encrypt" else -key
          if char.islower():
              result += chr(((ord(char) - ord('a') + shift) % 26 + ord('a')))
          else:
              result += chr(((ord(char) - ord('A') + shift) % 26 + ord('A')))
      else:
          result += char
  return result