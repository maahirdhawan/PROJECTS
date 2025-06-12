text = input("Enter a string: ")
reversed_text = ""
i = len(text) - 1
while i >= 0:
    reversed_text += text[i]
    i -= 1
print("Reversed string:", reversed_text)