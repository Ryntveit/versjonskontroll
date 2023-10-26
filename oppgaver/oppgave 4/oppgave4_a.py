# 4a )
import random #impoterer bilbotek

def trekke_tilfeldigetall(): #definerer funksjonen
    vinnertall_lokal = random.sample(range(1, 35), 8) #legger til verdier mellom 1 og 34, 8 ganger
    return vinnertall_lokal # returnerer vinnerverdiene

trekke_tilfeldigetall()
#kaller funksjonen