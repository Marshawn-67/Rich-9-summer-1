geniuses = ["Max" , "Avery" , "Marshawn" , "Semaj" , "Kauri"]
for genius in geniuses:
    print(genius)
answer = input("Would you like to see the list again Y/N")
while answer == "Y":
    for genius in geniuses:
        print(genius)
    answer = input("Would you like to see the list again Y/N")
