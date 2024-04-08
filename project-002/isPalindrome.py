print("IS PALINDROME?\n")

user_word = input("Enter a word: ")
user_word_reverse = str()

for i in range(len(user_word) -1, -1, -1):
    user_word_reverse += user_word[i];

if(user_word == user_word_reverse):
  print(f"-{user_word} is a palndrome word")
else:
  print(f"-{user_word} isn't a palndrome word")