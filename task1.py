from itertools import permutations
def decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {k: v for k, v in zip(key, alphabet)}
    return "".join(mapping.get(c, c) for c in text)

def brute_force_monoalphabetic():
    ciphertext = input("Enter the encrypted text: ").upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Decrypting")
    for perm in permutations(alphabet):
        key = "".join(perm)
        decrypted_text = decrypt(ciphertext, key)
        print(decrypted_text)

brute_force_monoalphabetic()