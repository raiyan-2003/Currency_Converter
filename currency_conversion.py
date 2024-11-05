import get_api
import conversion_class

USER_WRONG = -1
DEFAULT_BASE = 'USD'
END_APP = 3

curr_code_arr = [key for key in get_api.get_response().json()['rates']]


def currency_check(curr_code):
    user_code = curr_code
    while get_api.get_response().json()['rates'].get(user_code, USER_WRONG) == USER_WRONG:
        print("Code not found! Please try again (with capital letters")
    return True


def currency_conversion():
    converted_money = 0.00
    user_rate = 0.000000
    user_base = currency_base()
    converted_curr = input("Which currency do you want to convert? ")
    if currency_check(converted_curr):
        user_money = float(input("How much money would you like to convert? "))
        if user_base != DEFAULT_BASE:
            base_rate = get_api.get_response().json()['rates'][user_base]
            converted_rate = get_api.get_response().json()['rates'][converted_curr]

            user_rate = converted_rate / base_rate
        else:
            user_rate = get_api.get_response().json()['rates'][converted_curr]

        converted_money = conversion_class.CurrencyConversion(user_money, user_rate).get_conversion()
        print(f'{format(user_money, ".2f")} {user_base} is {format(converted_money, ".2f")} {converted_curr}')


def currency_base():
    curr_code = input("What code do you want to base? ")
    print(f"***\n***Processing {curr_code}***\nComplete!")
    if currency_check(curr_code):
        print("Code found!")
        return curr_code


def search_currency():
    user_code = input("What code do you want to search? ")
    if user_code.upper() in curr_code_arr:
        print("Code found!")
        print("Rate based on USD: ", get_api.get_response().json()['rates'][user_code.upper()])
        if user_code != user_code.upper():
            print("please remember to use capital letter while converting!")
    else:
        print("Code not found!")


def display_currency():
    user_input = input("Do you want to search any code or view all? (y or n) ")
    if user_input == "y":
        search_currency()
    else:
        i = 0
        j = 0
        while i < len(curr_code_arr):
            i = j
            for j in range(i, i+10):
                print(f"{j+1}. Currency Code: {curr_code_arr[j]} Rate based on USD: "
                      f"{get_api.get_response().json()['rates'][curr_code_arr[j]]} ")
                i = j
            user = input("Press Q to quit, or any key for next ")
            if user.lower() == 'q':
                i = len(curr_code_arr)


def main_menu():
    user_char = 0
    print("Welcome to Raiyan's Currency Conversion!")
    print("What would you like to do?")
    print("1. Convert Currency")
    print("2. View Currency List and Rates (based on USD)")
    print("3. Exit")
    user_char = int(input())

    while user_char != END_APP:
        if user_char == 1:
            currency_conversion()
        elif user_char == 2:
            display_currency()

        else:
            print("invalid output")

        print("What would you like to do?")
        print("1. Convert Currency")
        print("2. View Currency List and Rates (based on USD)")
        print("3. Exit")
        user_char = int(input())
    print("Thank you for using Raiyan's Currency Conversion!\nHave a nice day :)")