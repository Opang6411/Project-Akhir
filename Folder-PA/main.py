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
        print("=== X-LifTen Anime & Donghua Streaming ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")

        pilihan = input("Masukkan pilihanmu : ").strip()

        if pilihan == "1":
            proses_login()
        elif pilihan == "2":
            auth.register()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan X-LifTen!")
            input("Tekan Enter untuk keluar...")
            break
        else:
            print("Pilihan tidak valid!\n")
            input("Tekan Enter untuk mencoba lagi...")

if __name__ == "__main__":
    main()
