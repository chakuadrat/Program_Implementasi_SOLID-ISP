# Nisrina Azka Salsabila
# 21120122130057
# Group D - Interface Segregation Principle
# RPLBK Kelas B

from abc import ABC, abstractmethod

# Interface pembayaran
class Payment(ABC):
    @abstractmethod
    def pay(self, order: 'Order') -> None:
        pass

# Interface pembayaran jenis otentikasi two factor
class TwoFactorPayment(Payment):
    @abstractmethod
    def two_factor_auth(self) -> None:
        pass

# Interface pesanan
class OrderInterface(ABC):
    @abstractmethod
    def add_items(self, item_name: str, price: float, quantity: int) -> None:
        pass

    @abstractmethod
    def calculate_total(self) -> float:
        pass

# Implementasi Class Order
class Order(OrderInterface):
    def __init__(self):
        self.items = []
        self.status = "Not Paid"

    def add_items(self, item_name: str, price: float, quantity: int) -> None:
        item = {
            "name": item_name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

# Implementasi VisaPayment dengan Interface pembayaran
class VisaPayment(Payment):
    def __init__(self, email: str):
        self.email = email

    def pay(self, order: Order) -> None:
        pin = input("Enter your PIN to proceed with payment: ")
        print(f'\nPayment is processing using credit card.')
        print(f'Validating code {self.email}.')
        order.status = 'Paid'
        print(f'Payment Successful')

# List barang dan harga
available_items = {
    'Apple': 5.0,
    'Banana': 2.0,
    'Orange': 3.0,
    'Grape': 7.5,
    'Watermelon':6.5,
    'Mango':4.0
}

# Fungsi untuk menampilkan barang yang tersedia
def display_items():
    print("Available items:")
    for item, price in available_items.items():
        print(f"{item}: ${price:.2f}")

# Fungsi untuk memproses pesanan pengguna
def process_order():
    order = Order()
    while True:
        display_items()
        choice = input("Enter the item name you want to buy (or type 'checkout' to finish): ").capitalize()
        
        if choice == 'Checkout':
            break
        elif choice in available_items:
            try:
                quantity = int(input(f"Enter the quantity of {choice} you want to buy: "))
                order.add_items(choice, available_items[choice], quantity)
                print(f"Added {quantity} {choice}(s) to your cart.\n")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        else:
            print("Item not available. Please choose from the list.")

    total = order.calculate_total()
    print(f"\nTotal Order Amount: ${total:.2f}")
    return order

# Fungsi utama untuk menjalankan program
def main():
    print("\nWelcome to the Fruit Store!")
    order = process_order()

    # Proses pembayaran
    email = input("Enter your email for payment verification: ")
    payment = VisaPayment(email)
    payment.pay(order)

# Memulai program
if __name__ == "__main__":
    main()
