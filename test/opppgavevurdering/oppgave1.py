#%%
# a. Skriv ut vitsen til konsollen
print("Why did the programmer quit his job? Because he didn't get arrays.")




#%%
# b. Lag en funksjon som heter dagens_vits, som skriver ut vitsen i a)
def dagens_vits():
    print("Why did the programmer quit his job? Because he didn't get arrays.")

# c. Kall funksjonen b)
dagens_vits()





#%%
# d. Lag en ny funksjon som heter dagens_vits2. Den skal ha en parameter, Funksjonen skal skrive ut denne parameteren til konsollen.
def dagens_vits2(vits):
    print(vits)

# e. Kall funksjonen i d, med a som argument.
dagens_vits2("Why did the programmer quit his job? Because he didn't get arrays.")


#%%
# f. Lag en ny funksjon som heter dagens_vits3. Funksjonen skal ha en parameter.
# Den skal skrive ut denne. I tillegg skal funksjonen returnere teksten.
def dagens_vits3(vits):
    print(vits)
    return "because he didnt get arrays"

# g. Kall funksjonen i f med "This is a test" som argument.
print(dagens_vits3("Why did the programmer quit his job?"))
# %%
