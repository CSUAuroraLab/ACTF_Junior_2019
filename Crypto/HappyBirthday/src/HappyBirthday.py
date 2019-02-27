#! /usr/bin/env python
# -*- coding: utf-8 -*-
from hashlib import sha256
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
                                                    
                                                    
______ _      _   _         _                       
| ___ (_)    | | | |       | |                      
| |_/ /_ _ __| |_| |__   __| | __ _ _   _           
| ___ \ | '__| __| '_ \ / _` |/ _` | | | |          
| |_/ / | |  | |_| | | | (_| | (_| | |_| |          
\____/|_|_|   \__|_| |_|\__,_|\__,_|\__, |          
                                     __/ |          
                                    |___/           
______          _                                   
| ___ \        | |                                  
| |_/ /_ _ _ __| |_ _   _                           
|  __/ _` | '__| __| | | |                          
| | | (_| | |  | |_| |_| |                          
\_|  \__,_|_|   \__|\__, |                          
                     __/ |                          
                    |___/                           
                                                         """

option = r"""
Input what you want to do:
1) Print source
2) I've found collision!
"""

def hhhhhhhash(key):
  return sha256(key).hexdigest()[:50]

def verify():
  try:
    s1 = str(input("First string:"))
    s2 = str(input("Second string:"))
    if s1 == s2 or hhhhhhhash(s1) != hhhhhhhash(s2):
      return False
  except Exception as e:
    # print e
    print "Something goes wrong..."
    exit(1)
  return True

def main():
  print banner
  print """
Why length is a important argument in cryptography?
Let's find hash collision to tell Z why!
  """
  while True:
    a = input(option)
    if a == 1:
      print open(__file__).read()
    elif a == 2:
      break
    else:
      print("I don't get your mean...")
  if not verify():
    print "Ops, you're wrong..."
    exit(0)
  print(flag)

if __name__ == "__main__":
  main()