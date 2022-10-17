from edit_distance import edit_distance
def main():
   print("Welcome to Edit Distance Demonstration.*")
   print("Please input two words for the edit distance:")
   first_word  = input("The first word: ")
   second_word = input("The second word: ")
   ready = input("Please type submit to start or clear to retype: ")
   ready = ready.lower()
   while(ready != "submit" and ready != "clear"):
        ready = input("Please type submit to start or clear to restart: ")
        ready = ready.lower()
   while(ready != "submit"):
        first_word  = input("The first word: ")
        second_word = input("The second word: ")

        ready = input("type submit to start or clear to retype: ")
        ready = ready.lower()
        while(ready != "submit" and ready != "clear"):
            ready = input(" Please type submit to start or clear to restart: ")
            ready = ready.lower()
   edit_distance(first_word, second_word)
main()