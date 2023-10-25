#%%

# 4a )
import random

def trekke_tilfeldigetall():
    vinnertall_lokal = random.sample(range(1, 35), 8)
    return vinnertall_lokal

trekke_tilfeldigetall()
#kaller funksjonen

#global liste med vinnerverdiene
vinnertall= trekke_tilfeldigetall()
def skjekker(vinnertall, lottokupong):
    like_numbere = []
    
    # Går gjennom hver element i vinnertall listen
    for num in vinnertall:
        # skjekker om tallet også er i personens kuppong

        if num in lottokupong:
            like_numbere.append(num)

    return len(like_numbere)


# 4b) lager en liste/kuppong med 8 totale tall

lottokupong = []
i=0
while True:
    tall= input((f"hva er ditt {i+1} tall"))
    tall=int(tall)

    if 1<=tall<=34:
            lottokupong.append(tall)
            print(f"{tall} ble registrert")
            i=i+1
          
    else:
        print("prøv igjen, tallet må være mellom 1 og 34")

    if i==8:
        break


    
#kaller skjekker 
print(f"vinnertallenene er {vinnertall}")
print(f"din lottokupong har numberne {lottokupong}")

print("")


print("antall riktige er")
#kaller skjekker som returnerer antall riktige
skjekker(vinnertall, lottokupong)

