import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
  word = word.lower()  # dealing with case-sensitive words
  if word in data:
    return data[word]
  elif word.title() in data:  # search for words with the first letter capitalised
    return data[word.title()]
  elif word.upper() in data:  # search for words with all letters capitalised
    return data[word.upper()]
  # find the most similar word if the user spell it wrong
  elif len(get_close_matches(word, data.keys())) > 0:
    answer = input("Did you mean \"%s\" instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
    if answer == "Y":
      return data[get_close_matches(word, data.keys())[0]]
    elif answer == "N":
      return "The word doesn't exit. Please double check it!"
    else:
      return "Sorry, we didn't understand your entry."
  else:
    # dealing with non-existing words
    return "The word doesn't exit. Please double check it!"


def read_user_input():
  word = input("Enter a word: ")
  if word == "0":
    print("============================")
    print("Goodbye! （ ゜ρ゜)ノ")
    return False
  else:
    output = (translate(word))
    # print the result
    if type(output) == list:
      for i in range(len(output)):
        print(i+1, output[i])
    else:
      print(output)
    print("----------------------------")
    return True  


def print_menu():
  print("""Enter '0' to quit.""")
  print("============================")


def main():
  print("Welcome to Simple Thesaurus!")
  print("============================")
  print_menu()
  output = read_user_input()
  while output:
    output = read_user_input()


if __name__ == "__main__":
  main()