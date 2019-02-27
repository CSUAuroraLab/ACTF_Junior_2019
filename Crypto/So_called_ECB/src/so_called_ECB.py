#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flag import flag
import binascii
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

__author__ = 'CSUwangj'

banner = r"""
 ___       __   _______   ___       ________  ________  _____ ______   _______           _________  ________     
|\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\   _ \  _   \|\  ___ \         |\___   ___\\   __  \    
\ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|        \|___ \  \_\ \  \|\  \   
 \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \_|/__           \ \  \ \ \  \\\  \  
  \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \\\  \ \  \    \ \  \ \  \_|\ \           \ \  \ \ \  \\\  \ 
   \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\           \ \__\ \ \_______\
    \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|            \|__|  \|_______|
                                                                                                                 
                                                                                                                 
                                                                                                                 
 ________  ___       ________          ________  ________   ___       ___  ________   _______                    
|\   __  \|\  \     |\   ___ \        |\   __  \|\   ___  \|\  \     |\  \|\   ___  \|\  ___ \                   
\ \  \|\  \ \  \    \ \  \_|\ \       \ \  \|\  \ \  \\ \  \ \  \    \ \  \ \  \\ \  \ \   __/|                  
 \ \  \\\  \ \  \    \ \  \ \\ \       \ \  \\\  \ \  \\ \  \ \  \    \ \  \ \  \\ \  \ \  \_|/__                
  \ \  \\\  \ \  \____\ \  \_\\ \       \ \  \\\  \ \  \\ \  \ \  \____\ \  \ \  \\ \  \ \  \_|\ \               
   \ \_______\ \_______\ \_______\       \ \_______\ \__\\ \__\ \_______\ \__\ \__\\ \__\ \_______\              
    \|_______|\|_______|\|_______|        \|_______|\|__| \|__|\|_______|\|__|\|__| \|__|\|_______|              
                                                                                                                 
                                                                                                                 
                                                                                                                 
 ________  ________  ________   ___  __            ___  ___  ___                                                 
|\   __  \|\   __  \|\   ___  \|\  \|\  \         |\  \|\  \|\  \                                                
\ \  \|\ /\ \  \|\  \ \  \\ \  \ \  \/  /|_       \ \  \ \  \ \  \                                               
 \ \   __  \ \   __  \ \  \\ \  \ \   ___  \       \ \  \ \  \ \  \                                              
  \ \  \|\  \ \  \ \  \ \  \\ \  \ \  \\ \  \       \ \__\ \__\ \__\                                             
   \ \_______\ \__\ \__\ \__\\ \__\ \__\\ \__\       \|__|\|__|\|__|                                             
    \|_______|\|__|\|__|\|__| \|__|\|__| \|__|           ___  ___  ___                                           
                                                        |\__\|\__\|\__\                                          
                                                        \|__|\|__|\|__|                                          
                                                                                                                 
"""

account = {}
vault = {"admin": 100000}
key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_ECB)

def pad(data_to_pad):
  block_size = 16
  padding_len = block_size-len(data_to_pad)%block_size
  padding = chr(padding_len)*padding_len
  return data_to_pad + padding

def unpad(padded_data):
  padding_len = ord(padded_data[-1])
  return padded_data[:-padding_len]

def raw_trans(cipherdata):
  global account
  global vault
  data = cipher.decrypt(cipherdata)
  fr = unpad(data[0: 16])
  pswd = unpad(data[16: 32])
  to = unpad(data[32: 48])
  amount = int(unpad(data[48: 64]))
  # print fr, pswd.encode("hex"), to, amount
  if not (account.has_key(fr) and account[fr] == pswd):
    print "Wrong password or username..."
    return False
  if amount < 0 or amount > vault[fr]:
    print "What do you want to do?"
    return False
  vault[fr] -= amount
  if vault.has_key(to):
    vault[to] += amount
  else:
    vault[to] = amount
  print cipherdata.encode("hex")
  return True

def trans(fr, pswd, to, amount):
  amount = str(amount).encode()
  if len(fr) > 15 or len(pswd) > 15 or\
     len(to) > 15 or len(amount) >15:
    print "Each terms' length should shorter than 16"
    return False
  data = pad(fr) + pad(pswd) + pad(to) + pad(amount)
  print "Transfer ${} from {} to {}".format(amount, fr, to)
  return raw_trans(cipher.encrypt(data))

def regist():
  global account
  global vault
  name = ""
  passwd = ""
  isOK = False
  while not isOK:
    name = raw_input("Input your username: ")
    if account.has_key(name):
      print "There is already {}".format(name)
    elif len(name) > 15:
      print "Each term's length should less than 16"
    else:
      isOK = True
  isOK = False
  while not isOK:
    passwd = raw_input("Input your password: ")
    if len(passwd) > 15:
      print "Each term's length should less than 16"
    else:
      isOK = True
  account[name] = passwd
  vault[name] = 1000
  print "Welcome to online bank, {}!!!You'll recieve a gift from admin.".format(name)
  trans("admin", account["admin"], name, 1)

def show_money():
  global account
  global vault
  name = ""
  passwd = ""
  isOK = False
  while not isOK:
    name = raw_input("Input your username: ")
    if not account.has_key(name):
      print "There is not a(n) {}".format(name)
    else:
      isOK = True
  isOK = False
  while not isOK:
    passwd = raw_input("Input your password: ")
    if len(passwd) > 15:
      print "Each term's length should less than 16"
    else:
      isOK = True
  if account[name] == passwd:
    print "You have ${}".format(vault[name])

def transfer():
  name = ""
  passwd = ""
  to = ""
  amount = 0
  isOK = False
  while not isOK:
    name = raw_input("Input your username: ")
    if not account.has_key(name):
      print "There is not a(n) {}".format(name)
    else:
      isOK = True
  isOK = False
  while not isOK:
    passwd = raw_input("Input your password: ")
    if len(passwd) > 15:
      print "Each term's length should less than 16"
    else:
      isOK = True
  isOK = False
  while not isOK:
    to = raw_input("Input account your money goes to: ")
    if len(to) > 15:
      print "Each term's length should less than 16"
    else:
      isOK = True
  isOK = False
  while not isOK:
    try:
      amount = int(raw_input("How much you want to transfer?"))
      isOK = trans(name, passwd, to, amount)
    except Exception as e:
      pass

def raw_transfer():
  s = raw_input("HOPE YOU KNOW WHAT YOU ARE DOING!\nWHAT DATA WILL YOU SEND TO BANK:")
  if raw_trans(s.decode("hex")):
    print "SUCCESS..."
  else:
    print "FAIL..."

def getflag():
  global account
  global vault
  name = ""
  passwd = ""
  isOK = False
  while not isOK:
    name = raw_input("Input your username: ")
    if not account.has_key(name):
      print "There is not a(n) {}".format(name)
    else:
      isOK = True
  isOK = False
  while not isOK:
    passwd = raw_input("Input your password: ")
    if len(passwd) > 15:
      print "Each term's length should less than 16"
    else:
      isOK = True
  if account[name] == passwd and vault[name] > 9999:
    vault[name] -= 10000
    print "NICE TRY! HERE'S YOUR FLAG:\n{}".format(flag)
  elif account[name] != passwd:
    print "Wrong password or username"
  else:
    print "Not enough money!"

def main():
  global account
  global vault
  global cipher
  account["admin"] = get_random_bytes(15)
  print banner
  cnt = 0
  while cnt < 15:
    ops = """What do you want to do?
1) Register(Every newcomer will get $1000 initial money and recieved a gift from admin)
2) Transfer
3) Raw Transfer(DANGEROUS!!!)
4) Show Money
5) Getflag(With of just $10000!!!!)
6) Exit
> """
    option = int(raw_input(ops))
    if option == 1:
      regist()
    elif option == 2:
      transfer()
    elif option == 3:
      raw_transfer()
    elif option == 4:
      show_money()
    elif option == 5:
      getflag()
    elif option == 6:
      exit(0)
    else:
      print "I don't get your means by {}".format(option)
    cnt += 1
  print """!!!BANK FOUND SOMETHING!!!"""

if __name__ == "__main__":
  try:
    main()
  except Exception as e:
    print e