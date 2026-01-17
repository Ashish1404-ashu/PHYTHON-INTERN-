# ATM Simulation without File I/O (for online compilers)

# Initial hardcoded values
PIN = "1234"
balance = 5000.0
transaction_history = []

def show_menu():
    print("\n====== ATM Menu ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Exit")

def atm():
    print("💳 Welcome to Python CLI ATM (Online Mode)")
    entered_pin = input("Enter your 4-digit PIN: ")

    # Authentication Logic
    if entered_pin != PIN:
        print("❌ Incorrect PIN. Access denied.")
        return

    # 'global' allows us to modify the 'balance' variable defined at the top
    global balance 
    
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            print(f"💰 Your balance is: ₹{balance:.2f}")

        elif choice == '2':
            try:
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("⚠️ Please enter a positive amount.")
                    continue
                
                balance += amount
                transaction_history.append(f"Deposited ₹{amount:.2f}")
                print(f"✅ ₹{amount:.2f} deposited successfully.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '3':
            try:
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("⚠️ Please enter a positive amount.")
                    continue
                
                if amount <= balance:
                    balance -= amount
                    transaction_history.append(f"Withdrawn ₹{amount:.2f}")
                    print(f"✅ ₹{amount:.2f} withdrawn successfully.")
                else:
                    print("❌ Not enough balance.")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == '4':
            print("\n📜 Transaction History:")
            if transaction_history:
                for entry in transaction_history:
                    print(f"• {entry}")
            else:
                print("No transactions yet.")

        elif choice == '5':
            print("👋 Thank you for using the ATM. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Select 1-5.")

if __name__ == "__main__":
    atm()