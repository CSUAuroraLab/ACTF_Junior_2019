#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flag import flag
from Crypto.Util.number import getPrime, inverse
import binascii

__author__ = 'CSUwangj'

banner = r"""
 _    _      _                             _           _   _                    
| |  | |    | |                           | |         | | | |                   
| |  | | ___| | ___ ___  _ __ ___   ___   | |_ ___    | |_| |__   ___           
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \  | __/ _ \   | __| '_ \ / _ \          
\  /\  /  __/ | (_| (_) | | | | | |  __/  | || (_) |  | |_| | | |  __/          
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \__\___/    \__|_| |_|\___|          
                                                                                
                                                                                
______  _____  ___    _   _           _                            _            
| ___ \/  ___|/ _ \  | | | |         | |                          | |           
| |_/ /\ `--./ /_\ \ | |_| | ___   __| | __ _  ___ _ __   ___   __| | __ _  ___ 
|    /  `--. \  _  | |  _  |/ _ \ / _` |/ _` |/ _ \ '_ \ / _ \ / _` |/ _` |/ _ \
| |\ \ /\__/ / | | | | | | | (_) | (_| | (_| |  __/ |_) | (_) | (_| | (_| |  __/
\_| \_|\____/\_| |_/ \_| |_/\___/ \__,_|\__, |\___| .__/ \___/ \__,_|\__, |\___|
                                         __/ |    | |                 __/ |     
                                        |___/     |_|                |___/      
"""

def ask_for_option(s):
  while True:
    a = raw_input(s)
    if a == "Y":
      return True
    elif a == "N":
      return False
    else:
      print "What do you mean by \"{}\"".format(a)

def multiply():
  p = getPrime(512)
  q = getPrime(512)
  n = p*q
  print "p = {}\r\nq = {}\r\nn = ?".format(p, q)
  option = ask_for_option("Is this problem solvable?(Y/N)")
  if not option:
    print "really?"
    return False
  else:
    nn = int(raw_input("n = "))
    if nn != n:
      print "WRONG!"
      return False
  print "GOOD JOB"
  return True

def phi():
  p = getPrime(512)
  q = getPrime(512)
  n = (p-1)*(q-1)
  print "p = {}\r\nq = {}\r\nPhi(n) = ?".format(p, q)
  option = ask_for_option("Is this problem solvable?(Y/N)")
  if not option:
    print "really?"
    return False
  else:
    nn = int(raw_input("Phi(n) = "))
    if nn != n:
      print "WRONG!"
      return False
  print "GOOD JOB"
  return True

def special_e():
  isOK = False
  while not isOK:
    p = getPrime(512)
    q = getPrime(512)
    n = (p-1)*(q-1)
    if not n % 3:
      isOK = True
  print "p = {}\r\nq = {}\r\ne = 3".format(p, q)
  option = ask_for_option("Is these parameter OK?(Y/N)")
  if option:
    print "really?"
    return False
  print "GOOD JOB"
  return True

def little_factorize():
  p = getStrongPrime(100, 1e-7)
  q = getStrongPrime(100, 1e-7)
  n = p*q
  print "n = {}\r\np = ?\r\nq = ?\r\n".format(n)
  option = ask_for_option("Is this problem solvable?(Y/N)")
  if option:
    pp = int(raw_input("p = "))
    qq = int(raw_input("q = "))
    if not((pp == p and qq == q) or\
      (qq == p and pp == q)):
      return False
  else:
    print "Ops..."
    return False
  print "GOOD JOB"
  return True
  
def large_factorize():
  p = getPrime(1024)
  q = getPrime(1024)
  n = p*q
  print "n = {}\r\np = ?\r\nq = ?\r\n".format(n)
  option = ask_for_option("Is this problem solvable?(Y/N)")
  if option:
    print "really?"
    pp = int(raw_input("p = "))
    qq = int(raw_input("q = "))
    if not((pp == p and qq == q) or\
      (qq == p and pp == q)):
      print "WTF?!!!! Please go to https://en.wikipedia.org/wiki/RSA_Factoring_Challenge !!!"
      f = open("WTF.txt", "w")
      f.write(str(pp) + str(qq))
      f.close
      return True
  print "I can't either, check https://en.wikipedia.org/wiki/RSA_Factoring_Challenge"
  return True
  
def inv():
  isOK = False
  while not isOK:
    p = getPrime(512)
    q = getPrime(512)
    n = (p-1)*(q-1)
    if n % 3:
      isOK = True
  print "p = {}\r\nq = {}\r\ne = 3".format(p, q)
  print "d = ?"
  d = inverse(3, n)
  option = ask_for_option("Is this problem solvable?(Y/N)")
  if option:
    dd = int(raw_input("d = "))
    d = inverse(3, n)
    if dd != d:
      print "WRONG"
      return False
  else:
    print "Ops..."
    return False
  print "GOOD JOB"
  return True
  


def main():
  print banner
  if multiply() and phi() and special_e() and\
     little_factorize() and large_factorize()\
     and inv():
    print "Congratulations! Here's your flag:"
    print flag
  else:
    print "You need more practice"

if __name__ == "__main__":
  try:
    main()
  except Exception as e:
    pass