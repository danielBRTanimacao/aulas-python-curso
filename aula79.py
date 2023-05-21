s1 = set()
while True:
    letra = input('Digite uma letra: ')
    s1.add(letra)
    if 'l' in s1:
        break
print(s1)