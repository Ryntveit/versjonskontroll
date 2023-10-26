#%%
import turtle
import time
import random
#importerer 3 bilbloteker med forskjellige funksjoner

WIDTH, HEIGHT = 700, 600 #definerer høyde og bredde på vindu
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
#farge for skillpaddene
def get_number_of_racers(): # skjekker om det er gyldig antall skilpadder
	racers = 0
	while True: #slutter bare når gyldig antall er gitt
		racers = input('Enter the number of racers (2 - 10): ') # spørr etter antall racere
		if racers.isdigit(): #skjekker at input er tall
			racers = int(racers) # gjør om fra string
		else:
			print('Input is not numeric... Try Again!') #feilmelding om ikke tall
			continue

		if 2 <= racers <= 10: # om antall er mellom 2 og 10 returnerer funskjonen antallet
			return racers
		else:
			print('Number not in range 2-10. Try Again!') #feilmelding om ikke mellom fra og med 2 til og med 10

def race(colors): # Funksjon for å simulere racet og returnere vinnerns farge
	turtles = create_turtles(colors)  

	while True: #funksjonen slutter når en skilpadde når toppen av vinduet og vinner
		for racer in turtles:
			  # flytter hver turtle en tilfeldig lengde mellom 1 og 20 på y aksen
			distance = random.randrange(1, 20) 
			racer.forward(distance)

			x, y = racer.pos() # henter posisjonen til skillpadden
			if y >= HEIGHT // 2 - 10:   # om skillpadden når toppen av vindu blir den vinneren
				return colors[turtles.index(racer)] #returnerer vinner
			
def create_turtles(colors): # Funksjon for å illurstrere skillpaddene 
	turtles = [] 
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()  # her og under er koden for det visuelle av illustrasjonen farge form osv
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)  # posisjonerer skillpaddene med gjevnt mellomrom på x aksen
	    #skillpadden starter på y verdien 20

		racer.pendown()                                  
		turtles.append(racer)

	return turtles

def init_turtle(): # Funksjon for å starte opp vindu med illustrasjonen , slutter når vindu er lagd
	screen = turtle.Screen() 
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing!')


racers = get_number_of_racers() # kaller funskjonen og henter antall skillpadder fra input
init_turtle() #starter vindu med illustrasjon

random.shuffle(COLORS) 
colors = COLORS[:racers] #"Shuffler" listen med mulige farger og velger farger for skillpaddene

winner = race(colors) #Simulerer racet of finner fargen til vinnern
print("The winner is the turtle with color:", winner) 
time.sleep(5) #pauser programmet i 5 sekunder så man kan se resultatet spille seg ut i illustrasjonen
# %%
#rekkefølge

#først kalles get_number_of_racers() som lagrer antall skillpadder i "racers"
#så kalles init_turtle() som starter opp vindu med høyde bredde og titel osv 
#så får skillpaddene en tilfeldig farge fra listen
#så simuleres racet i funskjonen race(colors) inni denne funksjonen kalles create_turtles(colors) for å visualisere
#så "pauser" programmet i 5 sekunder så man kan se resultatet spille seg ut i illustrasjonen

#hvor langt de skal
#start på -HEIGHT//2 + 20, altså -280
#slutt/målstrek på  HEIGHT // 2 - 10:, altså 290

# skilpaddene må dra total distanse på 570 langs y aksen for å nå målstreken fra start