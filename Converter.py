def convert():
    print("Please select conversion type.\n")
    conversion = input('Enter "T" for temperature, "D" for distance, or "W" for weight.\n').upper()
    if conversion == "T":
        choice = input("For Fahrenheit to Celsius type (fc). For Celsius to Fahrenheit type (cf)\n").lower()
        if choice == "fc":
            fahr = float(input("Type the temperature you'd like to convert: "))
            cel = 5/9 * (fahr - 32)
            print(cel)
        elif choice == "cf":
            cel = float(input("Type the temperature you'd like to convert: "))
            fahr = (cel * 9/5) + 32
            print(fahr)
    elif conversion == "D":
        choice = input("For miles to kilometers type (mk). For kilometers to miles type (km)\n").lower()
        if choice == "mk":
            miles = float(input("Type the number of miles you'd like to convert: "))
            km = miles * 1.60934
            print(km)
        elif choice == "km":
            km = float(input("Type the number of kilometers you'd like to convert: "))
            miles = km / 1.60934
            print(miles)
    elif conversion == "W":
        choice = input("For pounds to kilograms type (pk). For kilograms to pounds type (kp)\n").lower()
        if choice == "pk":
            pounds = float(input("Type the number of pounds you'd like to convert: "))
            kg = pounds / 2.20462
            print(kg)
        elif choice == "kp":
            kg = float(input("Type the number of kilograms you'd like to convert: "))
            pounds = kg * 2.20462
            print(pounds)
    else:
        print("Invalid input")
        convert()
convert()
complete = False
while complete == False:
    cont = input("Would you like to convert something else?\n").lower()
    if cont == "yes":
        convert()
    else:
        print("Goodbye!")
        complete = True
