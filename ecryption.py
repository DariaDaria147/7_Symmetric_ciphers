# ИСАДИЧЕВА ДАРЬЯ, ДПИ22-1

def caesar_encrypt(shift_key, plaintext):
    """
    Шифрует строку с использованием шифра Цезаря.

    :param shift_key: Целочисленный ключ для сдвига
    :param plaintext: Текст, который требуется зашифровать
    :return: Зашифрованный текст
    """
    # Каждый символ в строке преобразуем в новый, сдвинутый по заданному ключу
    return ''.join(chr((ord(char) + shift_key) % 65536) for char in plaintext)


def caesar_decrypt(shift_key, ciphertext):
    """
    Дешифрует строку с использованием шифра Цезаря.

    :param shift_key: Целочисленный ключ для сдвига
    :param ciphertext: Зашифрованный текст
    :return: Дешифрованный текст
    """
    # Каждый символ в строке возвращаем в исходное положение, применяя обратный сдвиг
    return ''.join(chr((ord(char) - shift_key) % 65536) for char in ciphertext)


def brute_force_caesar(ciphertext):
    """
    Восстанавливает исходный текст, зашифрованный с помощью шифра Цезаря, без знания ключа.

    :param ciphertext: Зашифрованный текст
    :return: Наиболее вероятное восстановленное сообщение
    """
    # Считаем частоту появления символов в зашифрованном тексте
    char_frequency = {}
    for char in ciphertext:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Определяем наиболее часто встречающийся символ
    most_frequent_char = max(char_frequency, key=char_frequency.get)

    # Предполагаем, что наиболее частый символ - это пробел
    space_ascii = ord(' ')
    most_frequent_char_ascii = ord(most_frequent_char)

    # Рассчитываем предполагаемый ключ
    guessed_key = (most_frequent_char_ascii - space_ascii) % 65536

    # Применяем дешифровку с использованием предполагаемого ключа
    return caesar_decrypt(guessed_key, ciphertext)


def vigenere_encrypt_decrypt(text, key):
    """
    Шифрует или дешифрует текст с использованием шифра Вижинера с помощью операции XOR.

    :param text: Текст, который будет зашифрован или дешифрован
    :param key: Ключ для шифрования/дешифрования
    :return: Результат операции (зашифрованный или дешифрованный текст)
    """
    # Подготовка ключа, повторяя его, чтобы его длина совпала с длиной текста
    extended_key = (key * ((len(text) // len(key)) + 1))[:len(text)]
    # Применяем операцию XOR для каждого символа текста с соответствующим символом ключа
    return ''.join(chr(ord(t) ^ ord(k)) for t, k in zip(text, extended_key))


# Пример использования шифрования и дешифрования
if __name__ == "__main__":
    # Демонстрация работы шифра Цезаря
    original_message = "Hello, World!"
    caesar_shift = 3
    encrypted_message = caesar_encrypt(caesar_shift, original_message)
    decrypted_message = caesar_decrypt(caesar_shift, encrypted_message)
    print("Зашифрованное сообщение (Цезарь):", encrypted_message)
    print("Дешифрованное сообщение (Цезарь):", decrypted_message)

    # Пример восстановления текста с помощью частотного анализа (взлом шифра Цезаря)
    encrypted_example = '''To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take arms against a sea of troubles'''

    decrypted_example = brute_force_caesar(encrypted_example)
    print("Восстановленное сообщение:", decrypted_example)

    # Демонстрация работы шифра Вижинера
    vigenere_secret_key = "mysecretkey"
    encrypted_vigenere = vigenere_encrypt_decrypt("Hello, World!", vigenere_secret_key)
    decrypted_vigenere = vigenere_encrypt_decrypt(encrypted_vigenere, vigenere_secret_key)
    print("Зашифрованное сообщение (Вижинер):", encrypted_vigenere)
    print("Дешифрованное сообщение (Вижинер):", decrypted_vigenere)
