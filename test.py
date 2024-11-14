a = input()
b = input()
val = ""
for char in a:
    if char in b:
        val += char
print(val)