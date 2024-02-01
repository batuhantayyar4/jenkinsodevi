import time
import sys

def wait(seconds):
    for _ in range(seconds):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Kullanım: python wait.py [milisaniye]")
        sys.exit(1)
    
    try:
        milisaniye = int(sys.argv[1])
        saniye = milisaniye / 1000
        wait(saniye)
        print("\nBekleme tamamlandı.")
    except ValueError:
        print("Hatalı giriş! Milisaniye sayısı bir tamsayı olmalıdır.")
        sys.exit(1)
