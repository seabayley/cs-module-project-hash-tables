frequency_table = {}
key_table = {}
decoded = ""
base_line = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
             'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
ignored = ':;,!?.-+=/\|[]" \'{}()*^&â1€”\n'

with open("ciphertext.txt") as f:
    text = f.read()


for char in text:
    if char not in ignored:
        if char in frequency_table:
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1

for i, fp in enumerate(sorted(frequency_table.items(), key=lambda x: x[1], reverse=True)):
    key_table[fp[0]] = base_line[i]

for char in text:
    if char in key_table:
        decoded += key_table[char]
    else:
        decoded += char

print(decoded)
