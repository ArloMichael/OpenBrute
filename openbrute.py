import itertools
import hashlib

# MD5 Bruteforce Script
def attack(target_hash, char_set, max_length):
    for length in range(1, max_length+1):
        for combination in itertools.product(char_set, repeat=length):
            password = ''.join(combination)
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            if hashed_password == target_hash:
                return password
