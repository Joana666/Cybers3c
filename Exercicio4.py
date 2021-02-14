#!/usr/bin/python3

import math
import datetime
import random
import string
import zipfile

   
def brute_force():
    """
    Apply bruteforce to a zip file with a list of passwords
    """

    password = None
    zip_file = zipfile.ZipFile(zipfilename)
    with open(possible_password_list, 'r') as f:
        for line in f.readlines():
            password = line.strip('\n')
            try:
                zip_file.extractall(pwd=password)
                password = 'Password found: %s' % password
            except:
                pass
    print(password)

    # A partir de agora seriam as exepções, como por exmplo password errada. Após algumas tentativas, não estou a conseguir estrutura-las de forma a que o programa corra devidamente! :( )

if __name__ == "__main__": 
    brute_force()