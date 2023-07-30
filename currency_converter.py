from currency import Currency
from requests import Requests


class Result:
    def __init__(self, amount, conversion_flow):
        self.amount = amount
        self.conversion_flow = conversion_flow


def get_api_rate():
    # You can use any currency API to get the latest rate, for simplicity, let's assume the rate is 4.1
    return 4.1


def main():
    results = []
    currency_converter = Currency()
    print("Welcome to currency converter")

    while True:
        try:
            choice = int(Requests.get_choice())
            if choice not in (1, 2, 3):
                raise ValueError

            if choice == 1:
                amount = Requests.get_amount()
                converted_amount = currency_converter.dollars_to_shekels(amount)
                print(f"{amount:.2f} Dollars is equal to {converted_amount:.2f} Shekels.")
                results.append(Result(amount, currency_converter.get_conversion_flow('1')))
            elif choice == 2:
                amount = Requests.get_amount()
                converted_amount = currency_converter.shekels_to_dollars(amount)
                print(f"{amount:.2f} Shekels is equal to {converted_amount:.2f} Dollars.")
                results.append(Result(amount, currency_converter.get_conversion_flow('2')))
            elif choice == 3:
                amount = Requests.get_amount()
                converted_amount = currency_converter.shekels_to_euros(amount)
                print(f"{amount:.2f} Shekels is equal to {converted_amount:.2f} Euros.")
                results.append(Result(amount, currency_converter.get_conversion_flow('3')))

            restart = Requests.get_restart_choice()
            if restart != 'Y':
                print("Thanks for using our currency converter")
                print("Previous results:")
                for result in results:
                    print(f"{result.amount:.2f} {result.conversion_flow.split(' to ')[0]} "
                          f"=> {result.amount:.2f} {result.conversion_flow.split(' to ')[1]}")
                with open("results.txt", "w") as file:
                    for result in results:
                        file.write(f"{result.amount:.2f} {result.conversion_flow.split(' to ')[0]} "
                                   f"=> {result.amount:.2f} {result.conversion_flow.split(' to ')[1]}\n")
                break

        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue


if __name__ == "__main__":
    main()
