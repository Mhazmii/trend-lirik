import time
from threading import Thread
import sys

def animate_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Baris baru setelah lirik selesai

def sing_lyric(lyric, delay, speed, line_delay=0):
    time.sleep(delay)
    animate_text(lyric, speed)
    time.sleep(line_delay)  # Jeda setelah baris selesai

def sing_song():
    lyrics = [
        ("Tante...", 0.08),
        ("Sudah terbiasa terjadi tante...", 0.09),
        ("Teman datang cuma kalo butuh saja...", 0.08),
        ("Coba kalau lagi susah...", 0.15),
        ("Mereka semua menghilaaaaang...", 0.15)
    ]
    delays = [0.3, 2.5, 5.8, 9.5, 13.5]  # Waktu mulai setiap baris

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

sing_song()