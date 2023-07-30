class Currency:
    def __init__(self):
        # Replace with the actual conversion rates
        self.dollars_to_shekels_rate = 3.65
        self.shekels_to_dollars_rate = 0.27
        self.shekels_to_euros_rate = 0.24

    def dollars_to_shekels(self, amount):
        return amount * self.dollars_to_shekels_rate

    def shekels_to_dollars(self, amount):
        return amount * self.shekels_to_dollars_rate

    def shekels_to_euros(self, amount):
        return amount * self.shekels_to_euros_rate

    def get_conversion_flow(self, choice):
        if choice == '1':
            return "USD to ILS"
        elif choice == '2':
            return "ILS to USD"
        elif choice == '3':
            return "ILS to EUR"

