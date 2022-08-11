#ULANG TAHUN.

#Candain Nama
nama = (input ("Nama Kamu Siapa? "))
print ("ngga percaya")
nama2 = (input ("coba' nama asli kamu siapa sih? "))
print ("oke, sekarang aku percaya :) ")

selang = (input("tekan 'enter' buat lanjut"))

#Ulang Tahun
ulang_tahun = (input ("Hari Ini Ulang tahun kamu kan? (iya/bukan) "))
if ulang_tahun == "iya":
    print ("nah.. kan bener.. wkwk")
elif ulang_tahun == "bukan":
    print ("dahlah.. salah server") 
else:
    print ("Error, restart this program if you want to get the answer! ")                                      #Cari cara buat stop program secara
                                     #kalau jawaban dari pertanyaan ini tidak sesuai"bukan

#jumlah yang ingin di ucapkan.
ultah =int (input("pengen diucapin berapa kali nih? "))
for i in range (ultah):
    print ("SELAMAT ULANG TAHUN BESTIE!!     " +str(i))



wish = (input ("sekarang tulis apa harapan kamu dan aku bagian aminnya aja.. wkwkw "))


amin =int (input ("kamu mau di aminin berapa kali do'anya?"))



for a in range (amin):
    print ("aamiin " +str (a))

print ("semoga apa yang kamu inginkan terkabul dan menjadi yang terbaik di tahun ini!!")

print ("__________________________________")


print (".................................")
print (".................................")
print ("...........CREATED BY............")
print ("..........ARIEF FURQANY..........")
print (".................................")
print (".................................")
print (".................................")

print ("__________________________________")


print (" Setelah pertanyaan terakhir di jawab, maka program akan tertutup secara otomatis")

puas = (input (" GIMANA? PUAS NGGAK DI UCAPIN?? HAHAHAHA      (iya/tidak?)    "))
if puas == "iya":
    print ("silahkan kembali lagi di ulang tahun di tahun depan")
elif puas == "tidak":
    print ("syedihh :((((")

print ("_____________________________")
input ("klik 'enter'")
