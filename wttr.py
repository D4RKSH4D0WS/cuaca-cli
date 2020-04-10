#Mau rikod ? Boleh asal jgn hapus author ya asu !
#Author: D4RKSH4D0WS
import os
kota=raw_input('Masukkan lokasi: ')
os.system('curl -s http://wttr.in/'+kota+' | sed -n \"1,7p\"')
