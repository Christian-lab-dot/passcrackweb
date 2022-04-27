import hashlib
import bcrypt
import sys
import itertools

f = open('passwords.txt', 'r')


def plainCrack(password):
    for pw in f:
        passStrip = pw.strip()
        if passStrip == password:
            print('password found!\npassword is ' + passStrip)
            return
    print('password not found')

def md5Crack(hash):
    for pw in f:
        passw = pw.strip()
        word = pw.encode('utf-8')
        hashStrip = hashlib.md5(word.strip()).hexdigest()
        if hashStrip == hash:
            print('password found!\npassword is ' + passw)
            return
    print('password not found')

def bcryptCrack(hash):
    for pw in f:
        passw = pw.strip()
        if bcrypt.checkpw(passw.encode('utf-8'), hash.encode('utf-8')):
            print('password found!\npassword is ' + passw)
            return
    print('password not found')

def sha256Crack(hash):
    for pw in f:
        passw = pw.strip()
        word = pw.encode('utf-8')
        hashStrip = hashlib.sha256(word.strip()).hexdigest()
        if hashStrip == hash:
            print('password found!\npassword is ' + passw)
            return
    print('password not found')

def brutePlain(password):
    charList = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for i in range(51):
        for guess in itertools.product(charList, repeat=i):
            print(guess)
            if ''.join(guess) == password:
                sol = ''.join(guess)
                print('password is: ' + sol)
                return ''.join(guess)

def brute_u(x):
    charList = 'abcdefghijklmnopqrstuvwxyz1234567890'
    guess_list = []
    for i in range(x):
        for guess in itertools.product(charList, repeat=i):
            g = ''.join(guess)
            guess_list.append(g)
    print(guess_list)
    return guess_list

def main():
    #python3 cracked.py hashtype hash
    #1 is hash type, 2 is the hash/password
    #for bcrypt use the escape character \ for special characters in the hash
    if len(sys.argv) == 3:
        if sys.argv[1] == 'plain':
            plainCrack(sys.argv[2])
            sys.exit(0)
        if sys.argv[1] == 'md5':
            md5Crack(sys.argv[2])
            sys.exit(0)
        if sys.argv[1] == 'bcrypt':
            bcryptCrack(sys.argv[2])
            sys.exit(0)
        if sys.argv[1] == 'sha256':
            sha256Crack(sys.argv[2])
            sys.exit(0)
        if sys.argv[1] == 'brute':
            brutePlain(sys.argv[2])
            sys.exit(0)

    choice = input('what do?\n[1] plainCrack\n[2] md5Crack\n[3] bcryptCrack\n[4] sha256Crack\n[5] brutePlain\n')
    if choice == '1':
        plainCrack(input('Enter password\n'))
    if choice == '2':
        md5Crack(input('Enter md5 hash\n'))
    if choice == '3':
        bcryptCrack(input('Enter bcrypt hash\n'))
    if choice == '4':
        sha256Crack(input('Enter sha256 hash\n'))
    if choice == '5':
        brutePlain(input('Enter password:\n'))
    if choice == '6':
        brute_u(int(input('length: ')))

if __name__ == '__main__':
    main()