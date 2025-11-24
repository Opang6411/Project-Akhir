import penyimpanan
import tampilan

def tambah_anime():
    while True:
        print("=== Tambah Anime ===")
        judul = input("Judul anime (0 untuk kembali): ").strip()
        if judul == "0":
            return
        if judul == "":
            print("Judul tidak boleh kosong.\n")
            continue
        genre = input("Genre: ").strip()
        while True:
            try:
                rating = float(input("Rating anime (0-10): "))
                if not (0 <= rating <= 10):
                    raise ValueError
                break
            except ValueError:
                print("Rating tidak valid. Masukkan angka antara 0-10.\n")

        penyimpanan.data_anime.append({
            "id": len(penyimpanan.data_anime) + 1,
            "judul": judul,
            "genre": genre,
            "rating": rating,
            "episodes": []
        })
        penyimpanan.save_anime()
        print(f"Anime '{judul}' berhasil ditambahkan!\n")
        if not mau_lagi():
            break

def update_anime():
    while True:
        tampilan.clear()
        anime_id = tampilan.menu_tampil_anime(penyimpanan.data_anime)
        if anime_id is None:
            print("Kembali ke menu sebelumnya...\n")
            input("Tekan Enter untuk melanjutkan...")
            break
        anime = next((a for a in penyimpanan.data_anime if a["id"] == anime_id), None)
        if anime is None:
            print("Anime tidak ditemukan.\n")
            continue
        print(f"\nMengupdate {anime['judul']}")
        print("1. Tambah episode baru")
        print("2. Ubah status akses episode")
        menu = input("Pilih: ")
        if menu == "1":
            judul_ep = input("Judul episode baru: ").strip()
            while True:
                akses = input("Akses episode (gratis/premium): ").lower()
                if akses in ["gratis", "premium"]:
                    break
                print("Input tidak valid. Hanya 'gratis' atau 'premium'.\n")
            anime.setdefault("episodes", []).append({
                "judul": judul_ep,
                "akses": akses
            })
            penyimpanan.save_anime()
            print(f"Episode '{judul_ep}' berhasil ditambahkan.\n")
        elif menu == "2":
            episodes = anime.get("episodes", [])
            if not episodes:
                print("Anime ini belum memiliki episode.\n")
                continue
            print("\nDaftar Episode:")
            for i, ep in enumerate(episodes, start=1):
                print(f"{i}. {ep['judul']} ({ep['akses']})")
            try:
                idx = int(input("Pilih episode yang ingin diubah (0 untuk kembali): "))
                if idx == 0:
                    continue
                if not (1 <= idx <= len(episodes)):
                    print("Episode tidak ditemukan.\n")
                    continue
            except ValueError:
                print("Input tidak valid.\n")
                continue
            while True:
                akses_baru = input("Akses baru (gratis/premium): ").lower()
                if akses_baru in ["gratis", "premium"]:
                    break
                print("Input tidak valid. Hanya 'gratis' atau 'premium'.\n")
            episodes[idx - 1]["akses"] = akses_baru
            penyimpanan.save_anime()
            print("Status akses diperbarui.\n")
        else:
            print("Pilihan tidak valid.\n")
        if not mau_lagi():
            break

def hapus_anime():
    while True:
        anime_id = tampilan.menu_tampil_anime(penyimpanan.data_anime)
        if anime_id is None:
            print("Kembali ke menu sebelumnya...\n")
            input("Tekan Enter untuk melanjutkan...")
            break
        anime = next((a for a in penyimpanan.data_anime if a["id"] == anime_id), None)
        if anime is None:
            print("Anime tidak ditemukan.\n")
            continue
        keyakinan = input(f"Yakin ingin menghapus anime '{anime['judul']}'? (y/n): ").lower()
        if keyakinan == "y":
            penyimpanan.data_anime.remove(anime)
            penyimpanan.reindex_anime_ids()
            print(f"Anime '{anime['judul']}' berhasil dihapus!\n")
        else:
            print("Penghapusan dibatalkan.\n")
            input("Tekan Enter untuk melanjutkan...")
        if not mau_lagi():
            break

def mau_lagi():
    while True:
        lagi = input("Lakukan operasi ini lagi? (y/n): ").lower()
        if lagi == "y":
            return True
        elif lagi == "n":
            print("Kembali...\n")
            input("Tekan Enter untuk melanjutkan...")
            return False
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.\n")