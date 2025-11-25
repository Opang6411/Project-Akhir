from InquirerPy import inquirer
import auth
import tampilan

def proses_login():
    user = auth.login()
    if not user:
        return

    if user.get("role") == "admin":
        tampilan.menu_admin()
    else:
        tampilan.menu_user(user)

def main():
    while True:
        tampilan.clear()
        print("=== X-LifTen Anime & Donghua Streaming ===\n")

        pilihan = inquirer.select(
            message="Pilih menu:",
            choices=[
                {"name": "Login", "value": "login"},
                {"name": "Register", "value": "register"},
                {"name": "Keluar", "value": "exit"},
            ],
            default="login",
        ).execute()

        if pilihan == "login":
            proses_login()

        elif pilihan == "register":
            auth.register()

        elif pilihan == "exit":
            print("\nTerima kasih telah menggunakan X-LifTen!")
            input("Tekan Enter untuk keluar...")
            break

if __name__ == "__main__":
    main()
