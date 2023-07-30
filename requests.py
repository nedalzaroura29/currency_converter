class Requests:
    @staticmethod
    def get_choice():
        print("Please choose an option (1/2/3):")
        print("1. Dollars to Shekels")
        print("2. Shekels to Dollars")
        print("3. Shekels to Euros")
        return input()

    @staticmethod
    def get_amount():
        print("Please enter an amount to convert:")
        return float(input())

    @staticmethod
    def get_restart_choice():
        print("Do you want to start over? (Y/N):")
        return input().upper()

