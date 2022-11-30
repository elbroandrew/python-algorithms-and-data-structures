from string import ascii_lowercase

"""hello -> uryyb -> hello"""


class Rot13:
    def __init__(self):
        self.start = ascii_lowercase[0:13]
        self.end = ascii_lowercase[13:]
        self.first_part = dict(zip(self.start, self.end))
        self.second_part = dict(zip(self.end, self.start))

    def cipher_decipher(self, text_obj: str) -> str:

        ciphered_text = ""
        for ch in text_obj.lower():
            if ch in ascii_lowercase:
                if ch in self.first_part:
                    ciphered_text += self.first_part[ch]
                else:
                    ciphered_text += self.second_part[ch]
            elif ch == " ":
                ciphered_text += ch

        return ciphered_text



text = "hello  world"
a = Rot13()
cipher_text = a.cipher_decipher(text)
result = a.cipher_decipher(cipher_text)


print(cipher_text)
print(result)
