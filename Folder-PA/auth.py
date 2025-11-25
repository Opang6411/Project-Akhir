import penyimpanan
import tampilan

def login():
    tampilan.clear()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    for a in penyimpanan.akun:
        if a.get("username") == username and a.get("password") == password:
            print(f"\nLogin berhasil! Selamat datang, {username} ({a.get('role')})\n")
            input("Tekan Enter untuk melanjutkan...\n")
            return a
    print("Username atau password salah!\n")
    input("Tekan Enter untuk mencoba lagi...\n")
    return None

def register():
    while True:
        tampilan.clear()
        username = input("Username baru: ").strip()

        if not username:
            print("Username tidak boleh kosong.\n")
            input("Tekan Enter untuk mencoba lagi...\n")
            continue

        if " " in username:
            print("Username tidak boleh mengandung spasi.\n")
            input("Tekan Enter untuk mencoba lagi...\n")
            continue

        if username.lower() == "admin":
            print("Username 'admin' tidak diperbolehkan.\n")
            input("Tekan Enter untuk mencoba lagi...\n")
            continue

        if any(a["username"].lower() == username.lower() for a in penyimpanan.akun):
            print("Username sudah digunakan!\n")
            input("Tekan Enter untuk mencoba lagi...\n")
            continue
        
        break

    while True:
        password = input("Password baru: ").strip()
        if len(password) < 3:
            print("Password minimal 3 karakter.\n")
            input("Tekan Enter untuk mencoba lagi...\n")
            continue
        break

    while True:
        langganan = input("Apakah ingin berlangganan Pro? (y/n): ").lower().strip()
        if langganan == "y":
            role = "pro"
            break
        elif langganan == "n":
            role = "user"
            break
        print("Input tidak valid. Masukkan 'y' atau 'n'.\n")
        input("Tekan Enter untuk mencoba lagi...\n")

    penyimpanan.akun.append({
        "username": username,
        "password": password,
        "role": role,
        "history": []
    })
    penyimpanan.save_akun()

    print(f"Akun '{username}' berhasil dibuat dengan role '{role}'!\n")
    input("Tekan Enter untuk melanjutkan...\n")