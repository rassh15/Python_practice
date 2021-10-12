'''
Health Management System
Three Clients - Harry, Rohan and Hamad
Total 6 files : Diet food and exercise file for each client
Date for each categary
function to retreive exercise and food details for any client
function to takes input of client name .
fuunction to writing into file of food and exercise file.
'''
path = "C:\\Users\\Ars\\Documents\\python\\Git\\Python Practice\\05_exer_output"

def food_log(client_name):

    with open(path+"\\"+client_name+"_food.txt", 'a') as f:
        food_intake = input('What did you eat')
        f.write(f"{date_time(),  food_intake}")

def exercise_log(client_name):
    with open(path+"\\"+client_name+"_exercise.txt", 'a') as f:
        exercise_perform = input('What exercise did you do')
        f.write(f"{date_time(),  exercise_perform}")

def view_log(client_name):
    print("Enter which file you want to view:\n1. Food \n2. Exercise")
    ch = int(input())
    if ch ==1:
        with open(path+"\\"+client_name+"_food.txt", 'r') as f:
            print(f.read())

    if ch ==2:
        with open(path+"\\"+client_name+"_exercise.txt", 'r') as f:
            print(f.read())


def date_time():
    import datetime
    return f"{datetime.datetime.now()}"


if __name__ == '__main__':

    print("Health Management System")
    client_name_list = {}
    while True:
        print("No client available") if len(client_name_list)==0 else print(client_name_list)

        client = input("Enter client name: or No to exit ")
        client_name_list[client] = 1
        
        if client =="No":
            break

        print("What do you want to do: \n")
        print("1. Food\n2. Exercise\n3:View Food/Exercise\n")
        choice = int(input())
        if choice==1:
            food_log(client)
        elif choice == 2:
            exercise_log(client)
        else:
            view_log(client)




    



