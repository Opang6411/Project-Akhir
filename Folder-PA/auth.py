import penyimpanan


def login():
    username = input("Username: ")
    password = input("Password: ")

    for a in penyimpanan.akun:
        if a.get("username") == username and a.get("password") == password:
            print(f"\n✅ Login berhasil! Selamat datang, {username} ({a.get('role')})\n")
            return a

    print("❌ Username atau password salah!\n")
    return None


def register():
    username = input("Username baru: ")
    if any(a.get("username") == username for a in penyimpanan.akun):
        print("❌ Username sudah digunakan!\n")
        return None
    password = input("Password baru: ")
    penyimpanan.akun.append({"username": username, "password": password, "role": "user"})
    penyimpanan.save_akun()
    print(f"✅ Akun '{username}' berhasil dibuat!\n")
