#%%
import turtle
import time
import random
#importerer 3 bilbloteker med forskjellige funksjoner

WIDTH, HEIGHT = 700, 600 #definerer høyde og bredde på vindu
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
#farge for skilpaddene
def get_number_of_racers(): # skjekker om det er gyldig antall skilpadder
	racers = 0
	while True:
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

def race(colors):
	turtles = create_turtles(colors) 

	while True:
		for racer in turtles:
			distance = random.randrange(1, 20) 
			racer.forward(distance)

			x, y = racer.pos()
			if y >= HEIGHT // 2 - 10:
				return colors[turtles.index(racer)]

def create_turtles(colors):
	turtles = []
	spacingx = WIDTH // (len(colors) + 1)
	for i, color in enumerate(colors):
		racer = turtle.Turtle()
		racer.color(color)
		racer.shape('turtle')
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
		racer.pendown()
		turtles.append(racer)

	return turtles

def init_turtle():
	screen = turtle.Screen()
	screen.setup(WIDTH, HEIGHT)
	screen.title('Turtle Racing!')

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
# %%
