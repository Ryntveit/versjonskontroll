#%%
import random

def trekke_vinnertall():
    vinnertall = random.sample(range(1, 35), 8)
    return sorted(vinnertall)

trekke_vinnertall()

print("Vinnertall:", vinnertall)
# %%
