import datetime 

print("Hello user!")


name = input("What's your name?: ")

print("Hello, " + name + "!")

yob = int(input("What's your year of birth, " + name + "?"))

drives = input("Do you know how to drive, " + name + "?")

if drives.lower() == "yes": 
    
    dr_age= int(input("How old were you when you got your driving license?"))
 


    license_year =yob + dr_age

    print(datetime.date.today())

    print(datetime.date.today().year)

    dr_years = datetime.date.today().year - license_year

    print(name + " , you got your DS in " + str(license_year) + " and you have been driving for " + str(dr_years) + " years")

else:

    age = datetime.date.today().year - yob

    ds_y = yob + 30

    if age > 30:

        y_ago = datetime.date.today().year - ds_y

        print("You were supposed to get your license in " + str(ds_y) + ", " + str(y_ago) + " years ago at the age of 30 at the latest" )

    else:
         
        y_30 = ds_y - datetime.date.today().year

        print("You are " + str(age) +  " years old now and you should work on getting your driving license before you turn 30")
        print("You have " + str(y_30) + " years untill the year" + str(ds_y))









