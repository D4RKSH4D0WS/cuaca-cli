#Hai bangsat
#Mau rikod ? Boleh asal jgn hapus author ya asu !
#Author: D4RKSH4D0WS
import requests,re
se=raw_input('Input: ')
a=requests.get('http://wttr.in/'+se+'?format="%l:+%t+%C+%h+%w"').text
b=a.replace('"','')
print
print 'Keterangan:'
print '[lokasi]: [suhu] [infocuaca] [kelembapan] [arahangin]'
print
print b
