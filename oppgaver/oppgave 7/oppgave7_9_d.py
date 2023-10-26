#oppgave  9/10 d)

#%%

navn=["Robert","Boris","Brad","George","David"]

n=5
k=0
while k < n-2:       #endrer fra n-1 til n-2
    temp=navn[k]
    navn[k] = navn[n-k-1]
    navn[n-k-1]=temp
    k=k+1

print(navn)
# %%
