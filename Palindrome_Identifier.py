

text = input("Enter a word: ")

reverse_text = text[::-1]

if text.lower() == reverse_text.lower():
    print(text, "is a Palindrome")
else:
    print(text, "is not a Palindrome")