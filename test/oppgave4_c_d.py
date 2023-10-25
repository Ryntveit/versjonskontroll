#%%

# 4a)
import random

def trekke_tilfeldigetall():
    vinnertall_lokal = random.sample(range(1, 35), 8)
    return vinnertall_lokal

#trekke_tilfeldigetall()
#kaller funksjonen


# slutten av 4a

#global liste med vinnerverdiene
vinnertall= trekke_tilfeldigetall()



#4b) skjekker for like verdier i listen med vinnertallene og med lottokuppongene

def skjekker(vinnertall, lottokupong):
    like_numbere = []
    
    # Går gjennom hver element i vinnertall listen
    for num in vinnertall:
        # skjekker om tallet også er i personens kuppong

        if num in lottokupong:
            like_numbere.append(num)

    return len(like_numbere)


"""" 
# lager en liste/kuppong med 8 totale tall

 # lager ikke en egen kuppong i oppgave c
lottokupong = []
i=0

while True:
    tall= input((f"hva er ditt {i+1} tall"))
    tall=int(tall)

    if 1<=tall<=34:
            lottokupong.append(tall) # legger til tallet om kriteriene om verdi er nådd
            print(f"{tall} ble registrert")
            i=i+1
          
    else:
        print("prøv igjen, tallet må være mellom 1 og 34")

    if i==8:
        break
#bruker en while løkke som slutter etter 8 tall har bltt godtatt

    
print(f"vinnertallenene er {vinnertall}")
print(f"din lottokupong har numberne {lottokupong}")

print("antall riktige er")

#kallet skjekker antall riktige fra oppgave b
skjekker(vinnertall, lottokupong)
"""



#%% 4c)


def rekker():
    antall_rekker=input("hvor mange rekker?") #spørr etter et antall med rekker og 
    antall_rekker=int(antall_rekker) #gjør om fra string
    
    for i in range (1,antall_rekker+1): # utører like mange ganger som gitt i inputten over
        rekke=trekke_tilfeldigetall() #genererer enn ny rekke ved hjelp av funksjonen fra oppgave a
        print(rekke)

rekker() #kaller funksjonen
 


#%% 4c_2)
#skjekker hvor mange vinnertall i rekkene fra c

def rekker():
    antall_rekker=input("hvor mange rekker?") #spørr etter et antall med rekker og 
    antall_rekker=int(antall_rekker) #gjør om fra string
    
    for i in range (1,antall_rekker+1): # utører like mange ganger som gitt i inputten over
        rekke=trekke_tilfeldigetall() #genererer enn ny rekke ved hjelp av funksjonen fra oppgave a
        print(f"din {i} rekke er {rekke}")
        print(f"du har {skjekker(vinnertall,rekke)} vinnnernumbere") #skjekker antall riktige per rekke
        print("")

print(f"vinnertallene er {vinnertall}")
print("")
rekker() #kaller funksjonen

# %%
