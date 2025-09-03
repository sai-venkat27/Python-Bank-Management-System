import random

# Dictionary to store accounts (username → balance, account number)
accounts = {}

def new_account(user_name, ac_no):
    """Create a new account with zero balance."""
    accounts[user_name] = {"ac_no": ac_no, "balance": 0}
    print(f"✅ Account created successfully for {user_name} with AC No: {ac_no}")
    use_bank(user_name, ac_no)

def use_bank(user_name, ac_no):
    """Banking operations after login/signup."""
    if user_name not in accounts or accounts[user_name]["ac_no"] != ac_no:
        print("❌ Invalid account. Please sign up first.")
        return
    
    while True:
        print("\n----- Banking Menu -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Logout")
        
        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            accounts[user_name]["balance"] += amount
            print(f"✅ Deposited {amount}. Current balance: {accounts[user_name]['balance']}")

        elif choice == "2":
            amount = float(input("Enter withdraw amount: "))
            if amount <= accounts[user_name]["balance"]:
                accounts[user_name]["balance"] -= amount
                print(f"✅ Withdrawn {amount}. Current balance: {accounts[user_name]['balance']}")
            else:
                print("❌ Insufficient balance!")

        elif choice == "3":
            print(f"💰 Current balance: {accounts[user_name]['balance']}")

        elif choice == "4":
            print("🚪 Logging out...")
            break

        else:
            print("❌ Invalid choice, try again.")

# 🔄 Main Program (keeps running until 'exit')
def main():
    while True:
        print("\n\t\tWelcome to Bank Management System 🏦")
        print("\t\t\tLOGIN")
        print("\t\t\tSIGNUP")
        print("\t\t\tEXIT")
        check = input("Enter your choice: ").lower()

        if check == "login":
            user_name = input("Enter UserName: ")
            ac_no = int(input("Enter AC No: "))
            use_bank(user_name, ac_no)

        elif check == "signup":
            print("\t\tCreate New Account : )\n")
            user_name = input("UserName: ")
            ac_no = random.randint(1000000, 9999999)
            print(f"Your Acno is {ac_no}")
            new_account(user_name, ac_no)

        elif check == "exit":
            print("🙏 Thanks for using Bank Management System. Goodbye!")
            break

        else:
            print("❌ Invalid option, try again.")

if __name__ == "__main__":
    main()
