'''
  * Program: md5Ripper ;
  * File: md5Ripper.py ;
  * Author: F0r3bod1n' ;
  * Version: v1.0 ;
'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import os.path
import codecs
import hashlib
import colorama

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--md5", dest = "md5hash", type = str, required = True, help = "MD5 Hash to decrypt.")
parser.add_argument("-d", "--dictionary", dest = "dictionary", type = str, default = "passwords.txt", help = "Path to passwords dictionary.")
_args = parser.parse_args()

colorama.init()
fDict = codecs.open(_args.dictionary, "r+", encoding = "cp1251")

def _md5(string):
  result = hashlib.md5(str(string).encode())
  return result.hexdigest()


def check_args():
  hasError = False
  if len(_args.md5hash) != 32:
    print(colorama.Fore.RED + "[-] Value of argument -m/--md5 is not valid." + colorama.Style.RESET_ALL)
    hasError = True
    
  if not os.path.exists(_args.dictionary):
    print(colorama.Fore.RED + "[-] Path to dictionary not found." + colorama.Style.RESET_ALL)
    hasError = True
  
  if not hasError:
    main()
  else:
    sys.exit(0)
  
  
def main():
  for l in fDict.read().split("\n"):
    hash = _md5(l)
    if _args.md5hash == hash:
      print(colorama.Fore.GREEN + "[+] Success! {0}:{1}.".format(l, hash) + colorama.Style.RESET_ALL)
      sys.exit(0)
    del hash
    del l
  
  print(colorama.Fore.RED + "[-] Hash decrypting failed. No matches found." + colorama.Style.RESET_ALL)
  

if __name__ == "__main__":
  check_args()