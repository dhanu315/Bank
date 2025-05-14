import os

user_file = "user.txt"
account_file = "account.txt"

admin_username = "admin"
admin_pswrd = "admin123"

accounts = {}
next_account_number = 1001

def count_account  (accounts):
    accounts = len(accounts)
    'user01' == "customer"
    'user02' == "customer"
    'user03' == "admin"





# ------------------ Get Next Account Number ------------------
def get_next_account_number():
    if not os.path.exists(account_file):
        return 1001
    with open(account_file, "r") as file:
        lines = file.readlines()
        if lines:
            last_account_number = int(lines[-1].split(',')[0])
            return last_account_number + 1
        else:
            return 1001


# ------------------ Account Number Validation ------------------
def get_account_number():
    try:
        acc_num = int(input("Enter your account number: "))
        if acc_num < 1001:
            print("Account number must be greater than 1000")
            return None
        if acc_num not in accounts:
            print("Account not found")
            return None
        return acc_num
    except ValueError:
        print("Invalid input, account number must be a number")
        return None


# ------------------ Load Accounts From File ------------------
def load_accounts():
    if os.path.exists(account_file):
        with open(account_file, "r") as file:
            for line in file:
                account_number, name, balance = line.strip().split(",")
                accounts[int(account_number)] = {
                    "Name": name,
                    "Balance": float(balance),
                    "Transaction": []
                }


# ------------------ Save Accounts To File ------------------
def save_accounts():
    with open(account_file, "w") as file:
        for account_number, info in accounts.items():
            file.write(f"{account_number},{info['Name']},{info['Balance']}\n")


# ------------------ User Login ------------------
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == admin_username and password == admin_pswrd:
        print("Admin login successful!")
        admin_menu()
        return
    
    # display_totel_users = (users)
    # totel_users = len(users)
    # print(f"totel users")

    # uesrs = {
    #     'user01': "customer"
    #     'user02': "customer"
    #     'user03': "admin"
        
    # }
    # display_totel_users(users)

    





    # Check if user exists in user.txt
    if os.path.exists(user_file):
        with open(user_file, "r") as file:
            for line in file:
                user, pwd = line.strip().split(",")
                if user == username and pwd == password:
                    print(f"Welcome, {username}!")
                    user_menu()
                    return

    print("Invalid credentials or not registered.")


# ------------------ User Register ------------------
def register():
    existing_users = set()
    
    # Read existing usernames safely
    if os.path.exists(user_file):
        with open(user_file, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue  # Skip malformed lines
                user, _ = parts
                existing_users.add(user)

    while True:
        username = input("Enter a new username: ")
        if username in existing_users:
            print("Username already exists. Try another.")
            continue

        password = input("Enter a password: ")
        if username and password:
            with open(user_file, "a") as file:
                file.write(f"{username},{password}\n")

            # Generate and assign a new account number
            account_number = get_next_account_number()
            accounts[account_number] = {
                "Name": username,
                "Balance": 0.0,
                "Transaction": []
            }

            # Save the new account
            save_accounts()

            print(f"\nRegistration successful! Welcome to MiniBank, {username}")
            print(f"Username: {username}")
            print(f"Your new account number is: {account_number}")
            print(f"Starting balance: 0.0")

            # Automatically login and go to user menu
            user_menu()
            break
        else:
            print("Username and password cannot be empty.")

# ------------------ Deposit ------------------
def deposit():
    acc_num = get_account_number()
    if acc_num is None:
        return

    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        accounts[acc_num]["Balance"] += amount
        accounts[acc_num]["Transaction"].append(f"Deposited {amount}")
        save_accounts()
        print(f"Deposited {amount} to account {acc_num}")
    except ValueError:
        print("Invalid input, must be a number.")


# ------------------ Withdraw ------------------
def withdraw():
    acc_num = get_account_number()
    if acc_num is None:
        return

    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than 0")
            return
        if accounts[acc_num]["Balance"] < amount:
            print("Insufficient balance")
            return
        accounts[acc_num]["Balance"] -= amount
        accounts[acc_num]["Transaction"].append(f"Withdrew {amount}")
        save_accounts()
        print(f" Withdrew {amount} from account {acc_num}")
    except ValueError:
        print(" Invalid input, must be a number.")


# ------------------ View Balance ------------------
def view_balance():
    acc_num = get_account_number()
    if acc_num is None:
        return

    acc = accounts[acc_num]
    print(f"\n Account Number: {acc_num}")
    print(f"Holder: {acc['Name']}")
    print(f"Balance: {acc['Balance']}")
    print("Transactions:")
    for txn in acc["Transaction"]:
        print(" -", txn)


# ------------------ Admin Menu ------------------
def admin_menu():
    while True:
        print("\n Admin Menu")
        print("1. View All Accounts")
        print("2. View User File")
        print("3. View Account File")
        print("4. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            for acc_num, info in accounts.items():
                print(f"Account {acc_num}: {info['Name']}, Balance: {info['Balance']}")
        elif choice == "2":
            with open(user_file, "r") as file:
                print(file.read())
        elif choice == "3":
            with open(account_file, "r") as file:
                print(file.read())
        elif choice == "4":
            break
        else:
            print("Invalid option")


# ------------------ User Menu ------------------
def user_menu():
    while True:
        print("\n User Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            deposit()
        elif choice == "2":
            withdraw()
        elif choice == "3":
            view_balance()
        elif choice == "4":
            break
        else:
            print("Invalid option")


# ------------------ Main Program ------------------
def main():
    # Create files if not exist
    open(user_file, "a").close()
    open(account_file, "a").close()

    load_accounts()

    while True:
        print("\n Welcome to MiniBank")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print(" Invalid input, please choose 1-3")


if __name__ == "__main__":
    main()
