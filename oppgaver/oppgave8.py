#%%

def tall(teller):
    while True:
        antall = input(f'{teller}:')
        if antall.isnumeric():
            antall = int(antall)
            return antall
        else:
            print('Du må skrive et tall')
 
def plassering(biler, plasser):
    spillere_fordelt = []
    if spillere <= biler*plasser:

        spillere_i_bil = spillere // biler
       
        for i in range(biler):
            spillere_fordelt.append(spillere_i_bil)
 
        if spillere % biler == 0:
            return spillere_fordelt
        else:
            rest = spillere % biler
            k = 0
            while rest != 0:
                spillere_fordelt[k] = spillere_fordelt[k] + 1
                rest = rest-1
                k = k + 1
            return spillere_fordelt
       
    else:
        for i in range(biler):
            spillere_fordelt.append(plasser)
       
        rest = spillere - biler*plasser
        spillere_fordelt.append(rest)
        return spillere_fordelt
    


spillere = tall('skriv antall spillere')      
biler = tall('Skriv antall biler')
plasser = tall('Skriv antall plasser i hver bil')
 

fordelte_spillere = plassering(biler, plasser)
if len(fordelte_spillere) == biler:
    for i in range(biler):
        print(f'Bil {i + 1}, skal ha {fordelte_spillere[i]} spillere.')
else:
    for i in range(biler):
        print(f'Bil {i + 1}, er det {fordelte_spillere[i]} spillere.')
    print(f'{fordelte_spillere[-1]} spillere får ikke plass i bilene.')
# %%
