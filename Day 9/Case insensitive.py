import re
x = input("Enter the text: ")
d = {}
pattern = r'([A-Za-z]+)'
sentences = re.split(r'\.\s*', x)
count = 0
for s in sentences:
    count += 1
    n = re.findall(pattern, s.lower())
    for i in n:
        if i not in d:
            d[i] = []
        d[i].append(count)

print(d)