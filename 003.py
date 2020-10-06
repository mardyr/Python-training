
import random  # import biblioteki z generatorem losowości

print("Losowo od 1 do 10 = ",random.randint(1,10))

import math as m
print("m.flooar(10.6)=",m.floor(10.6))

0xff # hex system
0o14 # octagonal
0b1000 #binary
x = 31
print("31 = ",hex(x),oct(x),bin(x)) # liczba 31 w 3 systemach

from random import random # z biblioteki random importuj funkcje random
print("los zagral w pokera liczba to", random())

from random import * # zaimportuj wszystkie funkcje, ryzyko konfliktu

import sys # from sys import input

print('Jaś','Małgosia',sep='|i|',end ='\n'+'-'*50+'\n',file=sys.stdout)

name = input("Prosze podaj imie i nazwisko osoby: ")
print(name)

import time

currentTime = time.localtime()
print("Time \t\t",currentTime.tm_hour,currentTime.tm_min,currentTime.tm_sec,sep=":")

time.sleep(5)
print("Sleeep")
print("Time \t\t",currentTime.tm_hour,currentTime.tm_min,currentTime.tm_sec,sep=":")