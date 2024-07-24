import sys
from time import sleep
import time

def print_lyrics():
    lines =[
        ("Kepadamu dulu aku jatuh cinta", 0.16),
        ("Menanam asa bisa bersama sepanjang usia", 0.13),
        ("Saat itu engkau di tepian kota", 0.14),
        ("Aku masih sendiri", 0.12),
        ("Kau sudah, jadi miliknya", 0.12),
        ("Terimakasih,", 0.20),
        ("Atas segala rasa", 0.12),
        ("Pada hari itu pun aku turut bahagia", 0.13),
        ("Karena aku,", 0.14),
        ("Selalu tahu", 0.14),
        ("Menyukaimu bukan berarti selalu", 0.12),
        ("Memilikimu", 0.24),
    ]

    delays = [1.9,0.12,2.1,0.1,5.2,0.3,1.1,1.5,0.8,1.5,1.5,2.0]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:     
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')
print_lyrics()