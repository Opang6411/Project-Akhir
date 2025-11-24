import penyimpanan

def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    for a in penyimpanan.akun:
        if a.get("username") == username and a.get("password") == password:
            print(f"\nLogin berhasil! Selamat datang, {username} ({a.get('role')})\n")
            input("Tekan Enter untuk melanjutkan...\n")
            return a
    print("Username atau password salah!\n")
    return None

def register():
    while True:
        username = input("Username baru: ").strip()
        if username == "":
            print("Username tidak boleh kosong.\n")
            continue
        if any(a.get("username") == username for a in penyimpanan.akun):
            print("Username sudah digunakan!\n")
            continue
        break

    password = input("Password baru: ").strip()

    while True:
        langganan = input("Apakah ingin berlangganan Pro? (y/n): ").lower()
        if langganan == "y":
            role = "pro"
            break
        elif langganan == "n":
            role = "user"
            break
        else:
            print("Input tidak valid. Masukkan 'y' atau 'n'.\n")

    penyimpanan.akun.append({
        "username": username,
        "password": password,
        "role": role,
        "history": []
    })
    penyimpanan.save_akun()
    print(f"Akun '{username}' berhasil dibuat dengan role '{role}'!\n")
    input("Tekan Enter untuk melanjutkan...\n")
