userInput=int(input("Masukkan Detik :")) # Perintah user untuk memasukkan angka
D=userInput                              # Karena perintah berupa detik, jadi kita sederhanakan fungsinya

D=D%359999          # Dalam 24 jam ada 86400 detik, detik(modulus)/sisa sama dengan 86400, (359999 ikutin yang ada di soal)
J=D//3600           # Konversi detik ke jam
D=D%3600            # Konversi detik untuk 1 jamnya adalah 3600
M=D//60             # Konversi detik ke menit
D=D%60              # Konversi detik untuk 1 menitnya 60 detik

if userInput < 0 or userInput > 359999 :
    print ("Invalid Input !")
else :
    print(userInput,"detik = ",J," Jam : ",M," Menit : ",D," Detik")