#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flag import flag
import binascii

__author__ = 'CSUwangj'

banner = r"""
 _    _      _                            _____          
| |  | |    | |                          |_   _|         
| |  | | ___| | ___ ___  _ __ ___   ___    | | ___       
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \      
\  /\  /  __/ | (_| (_) | | | | | |  __/   | | (_) |     
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \_/\___/      
                                                         
                                                         
 _   _                   _____                  _        
| \ | |                 /  __ \                | |       
|  \| | ___  _ __ ______| /  \/_ __ _   _ _ __ | |_ ___  
| . ` |/ _ \| '_ \______| |   | '__| | | | '_ \| __/ _ \ 
| |\  | (_) | | | |     | \__/\ |  | |_| | |_) | || (_) |
\_| \_/\___/|_| |_|      \____/_|   \__, | .__/ \__\___/ 
                                     __/ | |             
                                    |___/|_|             
 _   _           _       _           _                   
| | | |         | |     | |         | |                  
| |_| | __ _ ___| |__   | |     __ _| |__                
|  _  |/ _` / __| '_ \  | |    / _` | '_ \               
| | | | (_| \__ \ | | | | |___| (_| | |_) |              
\_| |_/\__,_|___/_| |_| \_____/\__,_|_.__/               
                                                         
                                                         """

def ELFHash(key):
  hash = 0
  x    = 0
  for i in range(len(key)):
    hash = (hash << 4) + ord(key[i])
    x = hash & 0xF0000000
    if x != 0:
      hash ^= (x >> 24)
      hash &= ~x
  return (hash & 0x7FFFFFFF)

def verify():
  f = open("/dev/urandom")
  a = binascii.hexlify(f.read(20))
  print "plaintext = {},\r\nHASH = {}".format(binascii.hexlify(a), hex(ELFHash(a))[2:])
  try:
    s = str(input())
    s = binascii.unhexlify(s)
    if s == a or ELFHash(a) != ELFHash(s):
      return False
  except Exception as e:
    # print e
    print "Something goes wrong..."
    exit(1)
  return True

def main():
  print(banner)
  print("""
  Why are there cryptographic hash and non-cryptographic hash?
  I don't care but I just want to use normal hash function.
  Unless... You could find collision as fast as you can!
  Timing Begin!""")
  for _i in range(10):
    if not verify():
      print("Ops...")
      exit(0)
  print(flag)

if __name__ == "__main__":
  main()
