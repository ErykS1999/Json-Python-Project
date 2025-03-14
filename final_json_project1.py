import json


try:
    with open('social.json','r',encoding='UTF-8') as f:
        data = json.load(f)
except(FileNotFoundError,json.JSONDecodeError):
    data = {}

print("The current data is in our database", (json.dumps(data, indent=4)))
      

#data delete option

while True:
    ask = input("Would you like to delete some data from the above list? yes/no:  ".lower())
    if ask == 'no'.lower():
        break
    elif ask == 'yes'.lower():
        delete_what = input("What data would you like to delete?  ")
        if delete_what in data:
            del data[delete_what]
            print(f"\nThe data '{delete_what}' will be deleted right away! ")
        else:
            print("You need to try again, maybe a spelling error? No data as such exists.  ")

# data addition

while True:
    add_name = input("\nWhat is your name so we can add you to the database? Press 'q'to quit.  ")
    if add_name == 'q':
        print("Understood, goodbye!")
        break
    if add_name not in data:
        data[add_name] = {}
        print(f"Dear  {add_name} , your name will be added to our database. ")
   
        socials = input(f" {add_name.lower()}  What is the name of your preferred social media?  ")
        data[add_name]["social"] = socials

#add the amount of hours
        while True:
            try:
                hours = int(input(f" How many hours do you spend on {socials}?  "))
                data[add_name]["hours"] = hours #add the hours into the dataset
                break
            except(ValueError):
                print("You need to write numbers not letters!")

#followers info 

        while True: 
            try:
                followers = int(input(f"  Dear{add_name}  , how many followers do you have?  "))
                data[add_name]["followers"] = followers
                break
            except(ValueError):
                print("You need numbers not letters!")

            
        data[add_name]["usernames"] = []
        while True:
            username = input(f"What is your username on {socials}")
            data[add_name]["usernames"].append(username)

            option = input("Would you like to add a different username? yes/no:  ".lower())
            if option != 'yes':
                print(f"So {add_name}, that is all. Thank you for your input!  ")
                break
            else:
                additional_username = input("What is the additional username?  ")
                data[add_name]["usernames"].append(additional_username)
                break





               



    else:
        print(f"{add_name}, this already exists. Goodbye")
        break       

with open('social.json','w',encoding='UTF-8') as f:
    json.dump(data,f,indent=4)

print("The data has been updated", json.dumps(data,indent=4))