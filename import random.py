import random

def caesar_cipher(text, shift):
    def shift_char(char):
        if char.isalpha():
            shift_amount = shift % 26
            base = 65 if char.isupper() else 97
            return chr((ord(char) - base + shift_amount) % 26 + base)
        return char
    
    return ''.join(shift_char(char) for char in text)

def shuffle_text(text, key, encrypt=True):
    random.seed(key)
    text_list = list(text)
    if encrypt:
        random.shuffle(text_list)
    else:
        indices = list(range(len(text_list)))
        random.shuffle(indices)
        shuffled_text = [''] * len(text_list)
        for original_index, shuffled_index in enumerate(indices):
            shuffled_text[shuffled_index] = text_list[original_index]
        text_list = shuffled_text
    return ''.join(text_list)

def encrypt(text, key):
    shift = sum(ord(char) for char in key) % 26
    encrypted_text = caesar_cipher(text, shift)
    return shuffle_text(encrypted_text, key)

def decrypt(text, key):
    shift = sum(ord(char) for char in key) % 26
    shuffled_text = shuffle_text(text, key, encrypt=False)
    return caesar_cipher(shuffled_text, -shift)


mensagem_original = "David Goncalves Maia"
chave = "mysecretkey"

mensagem_encriptada = encrypt(mensagem_original, chave)
print("Mensagem encriptada:", mensagem_encriptada)

mensagem_decriptada = decrypt(mensagem_encriptada, chave)
print("Mensagem decriptada:", mensagem_decriptada)
