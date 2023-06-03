import random

def buat_password(daftar_huruf, jumlah_kombinasi, jumlah_kata, simbol):
    passwords = []
    for _ in range(jumlah_kombinasi):
        password = ''
        for _ in range(jumlah_kata):
            kata = random.choice(daftar_huruf).strip()
            password += kata + simbol
        password = password[:-len(simbol)]
        password += simbol + str(random.randint(0, 9))
        passwords.append(password)
    return passwords

def load_word_list(pw_generator):
    with open(pw_generator, 'r') as file:
        words = file.readlines()
    return words

daftar_huruf = load_word_list('words.txt')

while True:
    jumlah_kombinasi = int(input("Masukan banyak kombinasi yang akan dibuat: "))
    jumlah_kata = int(input("Masukan jumlah kata yang akan dijadikan password: "))
    simbol = input("Masukan simbol, dash (-) atau underscore(_): ")

    if (jumlah_kombinasi < 1) or (jumlah_kata < 1):
        print("Input tidak boleh kurang dari satu!")
        break
    elif simbol != '-' and simbol != '_' :
        print("Masukan simbol dengan benar!")
        break
    else:
        break

passwords = buat_password(daftar_huruf, jumlah_kombinasi, jumlah_kata, simbol)

print("-------------------------")
print("Password yang dibuat adalah:")
for i, password in enumerate(passwords):
    print(f'{password}')
