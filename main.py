# This programs determines whether or not two words are aanagrams

# getting words from the user
word1, word2= input("Enter two words (seperate by space): ").split()

#sorting the words alphabetically and comparing 
if sorted(word1)==sorted(word2):
    print("Your words are anagramms")
else:
    print("Your words are not anagramms")
