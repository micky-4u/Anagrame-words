# This programs determines whether or not two words are aanagrams

# getting words from the user
word1, word2= input("Enter two words (seperate by space): ").split()

# this loop delets all duplicate characters in words
for i in word1:
    if word1.count(i) > 1:
      word1=  i+word1.replace(i, '')

for i in word2:
    if word2.count(i) > 1:
       word2= i+word2.replace(i, '')
        
print("anagrame characters:"+ word1)

#sorting the words alphabetically and comparing 
if sorted(word1)==sorted(word2):
    print("Your words are anagramms")
else:
    print("Your words are not anagramms")
