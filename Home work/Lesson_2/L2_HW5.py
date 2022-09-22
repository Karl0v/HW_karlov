# видаляє символи пунктуації
a = input('Ввведіть текст >> ')

b = a.replace(',', ' ')
c = b.replace('.', ' ')
d = c.replace(';', ' ')
e = d.replace(':', ' ')
f = e.replace('?', ' ')
g = f.replace('!', ' ')

print(g)