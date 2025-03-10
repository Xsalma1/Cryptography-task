LETTER_FREQ = "etaoinsrhldcumfpgwybvkxjqz"

def frequency_analysis(cipher_text):
    cleaned_text = ''.join([char.lower() for char in cipher_text if char.isalpha()])
    
    letter_counts = {}
    for char in cleaned_text:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    sorted_letters_by_freq = ''.join(sorted(letter_counts, key=letter_counts.get, reverse=True))
    
    return sorted_letters_by_freq

def decrypt_monoalphabetic(cipher_text):
    cipher_letter_freq = frequency_analysis(cipher_text)
    substitution_map = {}
    for i in range(len(cipher_letter_freq)):
        substitution_map[cipher_letter_freq[i]] = LETTER_FREQ[i]

    unused_letters = [c for c in "abcdefghijklmnopqrstuvwxyz" if c not in substitution_map.values()]
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in substitution_map:
            substitution_map[char] = unused_letters.pop(0)

    decrypted_text = ''.join([substitution_map[char] if char in substitution_map else char for char in cipher_text.lower()])
    
    return decrypted_text

cipher_text = input("Enter your encrypted text: ")
decrypted_text = decrypt_monoalphabetic(cipher_text)

print("Decrypted Text:",decrypted_text)