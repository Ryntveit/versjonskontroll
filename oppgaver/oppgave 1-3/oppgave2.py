#%%
ord="funksjon"

def minfunksjon(tekst):
    ord=tekst
    return ord

print(minfunksjon("hei"))
print(ord)


print("---------------------")

print("Så, hei blir skrevet ut fra funksjonen, og funksjon blir skrevet ut fra den globale variabelen. ")
print("Du får ikke hei skrevet ut to ganger fordi endringen du gjør i den lokale variabelen ord innenfor minfunksjon ikke påvirker den globale variabelen ord")
# %%")
