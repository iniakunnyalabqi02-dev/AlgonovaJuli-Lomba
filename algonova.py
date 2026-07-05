import random

def jalankan_chatbot():
    # 1. Pesan pembuka saat program pertama kali dijalankan
    print("=====================================================")
    print("🤖 Halo! Aku adalah Chatbot Sederhana.")
    print("💬 Ketik 'keluar' jika kamu ingin mengakhiri obrolan.")
    print("=====================================================\n")

    # 2. Perulangan (loop) agar bot terus menyala
    while True:
        # 3. Mengambil tulisan dari pengguna dan mengubahnya jadi huruf kecil (.lower)
        pesan_pengguna = input("Kamu: ").lower()

        # 4. Mengecek apakah pengguna ingin berhenti
        if pesan_pengguna == 'keluar':
            print("Chatbot: Sampai jumpa! Semoga harimu menyenangkan. 👋")
            break  # Menghentikan perulangan

        # 5. Logika 'Otak' Chatbot (Merespons pertanyaan dengan ketentuan tertentu)
        if "halo" in pesan_pengguna or "hai" in pesan_pengguna:
            print("Chatbot: Halo! Ada yang bisa aku bantu hari ini? 😊")
            
        elif "siapa namamu" in pesan_pengguna or "kamu siapa" in pesan_pengguna:
            print("Chatbot: Aku adalah bot pemula yang sedang belajar coding!")
            
        elif "kabarmu" in pesan_pengguna:
            print("Chatbot: Kabarku sangat baik dong! Aku kan program komputer. Kamu sendiri bagaimana?")

        elif "baik" in pesan_pengguna or "sehat" in pesan_pengguna:
            print("Chatbot: Syukurlah kamu dalam kedaan yang baik! 😊")

        elif "tidak baik" in pesan_pengguna or "sedih" in pesan_pengguna:
            print("Chatbot: Oh, semoga kamu cepat merasa lebih baik ya. Aku di sini untuk menemanimu.")

        elif "apa yang bisa kamu lakukan" in pesan_pengguna or "kemampuanmu apa" in pesan_pengguna:
            print("Chatbot: Aku bisa mengobrol denganmu, menjawab pertanyaan sederhana, dan belajar dari interaksi kita!")

        elif "kamu suka apa" in pesan_pengguna or "hobi kamu apa" in pesan_pengguna:
            print("Chatbot: Aku suka belajar hal baru dan membantu orang dengan jawaban yang aku tahu!")

        elif "terima kasih" in pesan_pengguna or "makasih" in pesan_pengguna:
            print("Chatbot: Sama-sama! Senang bisa mengobrol denganmu.")
            
        # 6. Jika Chatbot tidak mengerti pesan pengguna
        else:
            # Menyiapkan beberapa jawaban acak agar bot tidak terasa kaku
            jawaban_bingung = [
                "Hmm, aku belum diajari kata itu.",
                "Maaf ya, sebagai bot pemula, kosa kataku masih terbatas. 😅",
                "Kayaknya aku belum mengerti maksudmu. tapi lain kali i will try to learn it!",
                "Wah, menarik! Tapi sayangnya aku belum paham maksudmu."
            ]
            # Memilih salah satu jawaban secara acak
            print("Chatbot:", random.choice(jawaban_bingung))

# 7. Memanggil fungsi agar chatbot mulai bekerja
if __name__ == "__main__":
    jalankan_chatbot()
