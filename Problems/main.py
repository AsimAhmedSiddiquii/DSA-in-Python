n = int(input())
words = []
for i in range(n):
    words.append(input())
for word in words:
    if len(word) <= 10:
        print(word)
    else:
        newString = word[0] + str(len(word[1:])-1) + word[-1]
        print(newString)
