import penyimpanan

def tampilkan_akun():
    if not penyimpanan.akun:
        print("Tidak ada akun.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    for i, a in enumerate(penyimpanan.akun, start=1):
        username = a.get("username", "(nama tidak valid)")
        role = a.get("role", "user")
        print(f"{i}. {username} — Role: {role}")
    print("")


def ubah_role_akun():
    if not penyimpanan.akun:
        print("Tidak ada akun.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    tampilkan_akun()

    try:
        pilih = int(input("Masukkan nomor akun yang ingin diubah role-nya (ketik 0 untuk batal): "))
        if pilih == 0:
            return
        if not (1 <= pilih <= len(penyimpanan.akun)):
            print("Nomor akun tidak valid.\n")
            input("Tekan Enter untuk melanjutkan...\n")
            return
    except ValueError:
        print("Input tidak valid.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    user = penyimpanan.akun[pilih - 1]

    if user.get("role") == "admin":
        print("Admin tidak bisa diubah role-nya.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    while True:
        role_baru = input("Role baru (user/pro): ").lower().strip()
        if role_baru in ["user", "pro"]:
            break
        print("Input tidak valid. Hanya 'user' atau 'pro'.\n")
        input("Tekan Enter untuk mencoba lagi...\n")

    user["role"] = role_baru
    penyimpanan.save_akun()

    print(f"Role akun '{user.get('username')}' berhasil diubah menjadi {role_baru}.\n")
    input("Tekan Enter untuk melanjutkan...\n")


def hapus_akun():
    if not penyimpanan.akun:
        print("Tidak ada akun.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    non_admin = [a for a in penyimpanan.akun if a.get("role") != "admin"]
    if not non_admin:
        print("Tidak ada akun selain admin yang bisa dihapus.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    tampilkan_akun()

    try:
        pilih = int(input("Masukkan nomor akun yang ingin dihapus (ketik 0 untuk batal): "))
        if pilih == 0:
            return
        if not (1 <= pilih <= len(penyimpanan.akun)):
            print("Nomor akun tidak valid.\n")
            input("Tekan Enter untuk melanjutkan...\n")
            return
    except ValueError:
        print("Input tidak valid.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    user = penyimpanan.akun[pilih - 1]

    if user.get("role") == "admin":
        print("Admin tidak bisa dihapus.\n")
        input("Tekan Enter untuk melanjutkan...\n")
        return

    konfirmasi = input(f"Yakin ingin menghapus akun '{user.get('username')}'? (y/n): ").lower()
    if konfirmasi == "y":
        penyimpanan.akun.remove(user)
        penyimpanan.save_akun()
        print(f"Akun '{user.get('username')}' telah dihapus!\n")
    elif konfirmasi == 'n':
        print("Penghapusan dibatalkan.\n")
    else:
        print("Input tidak valid. Penghapusan dibatalkan.\n")
        
    input("Tekan Enter untuk melanjutkan...\n")