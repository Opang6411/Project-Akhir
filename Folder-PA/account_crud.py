import penyimpanan

def tampilkan_akun():
    for i, a in enumerate(penyimpanan.akun, start=1):
        print(f"{i}. {a.get('username')} — Role: {a.get('role')}")
    print("")

def ubah_role_akun():
    tampilkan_akun()
    try:
        pilih = int(input("Masukkan nomor akun yang ingin diubah role-nya: "))
        if not (1 <= pilih <= len(penyimpanan.akun)):
            print("Nomor akun tidak valid.\n")
            return
    except ValueError:
        print("Input tidak valid.\n")
        return

    user = penyimpanan.akun[pilih - 1]
    if user.get("role") == "admin":
        print("Admin tidak bisa diubah role-nya.\n")
        return

    while True:
        role_baru = input("Role baru (user/pro): ").lower()
        if role_baru in ["user", "pro"]:
            break
        print("Input tidak valid. Hanya 'user' atau 'pro' yang diperbolehkan.\n")

    user["role"] = role_baru
    penyimpanan.save_akun()
    print(f"Role akun '{user.get('username')}' berhasil diubah menjadi {role_baru}.\n")
    input("Tekan Enter untuk melanjutkan...\n")

def hapus_akun():
    tampilkan_akun()
    try:
        pilih = int(input("Masukkan nomor akun yang ingin dihapus: "))
        if not (1 <= pilih <= len(penyimpanan.akun)):
            print("Nomor akun tidak valid.\n")
            return
    except ValueError:
        print("Input tidak valid.\n")
        return

    user = penyimpanan.akun[pilih - 1]
    if user.get("role") == "admin":
        print("Admin tidak bisa dihapus.\n")
        return

    konfirmasi = input(f"Yakin ingin menghapus akun '{user.get('username')}'? (y/n): ").lower()
    if konfirmasi == "y":
        penyimpanan.akun.remove(user)
        penyimpanan.save_akun()
        print(f"Akun '{user.get('username')}' telah dihapus!\n")
    elif konfirmasi == "n":
        print("Penghapusan dibatalkan.\n")
    else:
        print("Input tidak valid. Penghapusan dibatalkan.\n")
    
    input("Tekan Enter untuk melanjutkan...\n")
