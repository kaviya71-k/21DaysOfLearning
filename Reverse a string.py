sentence=input("Enter the sentence: ")
words=sentence.split()
words.reverse()
result=" ".join(words)
print("The reversed sentence is",result)


sentence=input("Enter the sentence: ")
words=sentence.split()
for word in words:
    print(word[::-1],end=" "\n)

sentence=input("Enter the sentence: ")
words=sentence.split()
print("Number of words",len(words))





