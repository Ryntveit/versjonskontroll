


#%% en oversikt over lagene som har vunnet minst ett seriemesterskap 
eliteserielag = [
  { "lag": "Lillestrøm", "seriemesterskap": [1976, 1977, 1986, 1989], "norgesmesterskap": [1977, 1978, 1981, 1985, 2007, 2017] },
  { "lag": "Molde", "seriemesterskap": [2011, 2012, 2014, 2019], "norgesmesterskap": [1994, 2005, 2013, 2014, 2021] },
  { "lag": "Viking", "seriemesterskap": [1972, 1973, 1974, 1975, 1979, 1982, 1991], "norgesmesterskap": [1979, 1989, 2001, 2019] },
  { "lag": "Strømsgodset", "seriemesterskap": [1970, 2013], "norgesmesterskap": [1969, 1970, 1973, 1991, 2010] },
  { "lag": "Aalesund", "seriemesterskap": [], "norgesmesterskap": [2009, 2011] },
  { "lag": "Rosenborg", "seriemesterskap": [1967, 1969, 1971, 1985, 1988, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2006, 2009, 2010, 2015, 2016, 2017, 2018], "norgesmesterskap": [1964, 1971, 1988, 1990, 1992, 1995, 1999, 2003, 2015, 2016, 2018] },
  { "lag": "Sarpsborg", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Bodø/Glimt", "seriemesterskap": [2020, 2021], "norgesmesterskap": [1975, 1993] },
  { "lag": "Odd", "seriemesterskap": [], "norgesmesterskap": [2000] },
  { "lag": "Tromsø", "seriemesterskap": [], "norgesmesterskap": [1986, 1996] },
  { "lag": "Vålerenga", "seriemesterskap": [1965, 1981, 1983, 1984, 2005], "norgesmesterskap": [1980, 1997, 2002, 2008] },
  { "lag": "HamKam", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Sandefjord", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Haugesund", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Jerv", "seriemesterskap": [], "norgesmesterskap": [] },
  { "lag": "Kristiansund", "seriemesterskap": [], "norgesmesterskap": [] }
]

print("--------")
print("lag med et serie mesterskap")
print("--------")

for verdi in eliteserielag:
    if len(verdi['seriemesterskap']) > 0:
        print(verdi['lag'])
    

print("--------")
print("lag med et norgemesterskap og seiermesterskap")
print("--------")

# en oversikt over lagene som har vunnet minst ett seriemesterskap og ett norgesmesterskap

for verdi in eliteserielag:
    if len(verdi['seriemesterskap']) > 0 and len(verdi['norgesmesterskap']) > 0:
        print(verdi['lag'])

print("--------")

#hvem som har vunnet flest ganger
flest= len(eliteserielag[0]['seriemesterskap'])
vinnerlag= eliteserielag[0]['lag']

for verdi in eliteserielag:
     antall=len(verdi['seriemesterskap'])
     lag=verdi['lag']

     if antall > flest:  
          flest = antall
          vinnerlag =lag

print(f"{vinnerlag} vant flest ganger med {flest} seiere!")

    
#%% vant første året

min=eliteserielag[0]['seriemesterskap'][0]
minLag = eliteserielag[0]['lag']

for verdi in eliteserielag:

    if len(verdi["seriemesterskap"]) > 0:
        minimum = verdi['seriemesterskap'][0]
        minimumLag = verdi['lag']
        if  minimum < min:
            min = minimum
            minLag = minimumLag

print(f"{minLag} vant i det første året altså i {min}")

#vant siste året  

max=eliteserielag[0]['seriemesterskap'][0]
maxLag = eliteserielag[0]['lag']

for verdi in eliteserielag:

 
 
 if len(verdi["seriemesterskap"]) > 0:

        maximum = verdi['seriemesterskap'][-1]
        maximumLag = verdi['lag']

        if  maximum > max:
            max = maximum
            maxLag = maximumLag

print(f"{maxLag} vant i det siste året altså i {max}")

# %%
