import pygame
import time
import random
pygame.init()

gameFinished = False

turnUser = True
turnAI = False

screen_width = 900 
screen_height = 600 

tableWidth = 600
tableHeight = 600 

cardsWidth = 100 
cardsHeight = 120 

userPairs = 0 
AIpairs = 0 

pointsUser = 0 
pointsAI = 0


white = (255,255,255)
grey = (47,45,49)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MemorIA')
clock = pygame.time.Clock()

background_image = pygame.image.load("images/background.png").convert()
# Escalar la imagen de fondo para que se ajuste a las dimensiones de la pantalla
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
screen.blit(background_image, (0, 0))

a = pygame.image.load('images/cambur.png')
b = pygame.image.load('images/lechita.png')
c = pygame.image.load('images/queso.png')
d = pygame.image.load('images/cachito.png')
e = pygame.image.load('images/naranja.png')
f = pygame.image.load('images/heladoChocolate.png')
g = pygame.image.load('images/dona.png')
h = pygame.image.load('images/durazno.png')
i = pygame.image.load('images/galletas.png')
j = pygame.image.load('images/papas.png')
k = pygame.image.load('images/helado.png')
l = pygame.image.load('images/bolsa.png')
m = pygame.image.load('images/cafe.png')
n = pygame.image.load('images/ponque.png')
o = pygame.image.load('images/taza.png')


cardBack = pygame.image.load('images/cardBack.png')
youWon = pygame.image.load('images/ganaste.png')
youLost = pygame.image.load('images/perdiste.png')

turnAILight = pygame.image.load('images/turnoIA.png')
turnUserLight = pygame.image.load('images/turnoUser.png')
screen.blit(turnUserLight, (650, 100))

happy = pygame.image.load('images/supremeVictory.png')
sad = pygame.image.load('images/burla.png')

images_arr1 = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o]

cardsLocs_arr1 = [(0,0), (100, 0), (200, 0), (300, 0), (400, 0), (500, 0),
			      (0, 120), (100, 120), (200, 120), (300, 120), (400, 120), (500, 120),
			      (0, 240), (100, 240), (200, 240), (300, 240), (400, 240), (500, 240),
			      (0, 360), (100, 360), (200, 360), (300, 360), (400, 360), (500, 360), 
			      (0, 480), (100, 480), (200, 480), (300, 480), (400, 480), (500, 480),]

cardsToPlay = {} 

AImemory = {}

temp2UserCards = {}

random.shuffle(images_arr1)
random.shuffle(cardsLocs_arr1)

z = 0
while z < len(cardsLocs_arr1):
	cardsToPlay.update({cardsLocs_arr1[z]: images_arr1[z]})
	z+=1

p = 0
while p < len(images_arr1):
	screen.blit(cardBack, cardsLocs_arr1[p])
	p+=1

def gameLoop():
	global turnAI
	global turnUser
	global gameFinished

	scoreAI(pointsAI)
	scoreUser(pointsUser)
	gameFinished = False

	while not gameFinished:
		noMoreCardsToPlay()
		if turnUser == False and turnAI == False:
			break
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
				gameFinished = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				mouse = pygame.mouse.get_pos()
				if mouse[0] > 0 and mouse[0] < tableWidth and mouse[1] > 0 and mouse[1] < tableHeight:
					if turnUser == True:
						pygame.display.update()
						xyCoorForAll(mouse[0], mouse[1])

			if turnAI == True:
				turnAImethod()
				AIchoosing()
		
		pygame.display.update()
		clock.tick(60)	

def xyCoorForAll(x2, y2):
	global AImemory

	if x2 > 0 and x2 < tableWidth and y2 > 0 and y2 < tableHeight:
		x = x2
		i=tableWidth

		y = y2
		j=tableHeight

		bo = True
		bo2 = True
		while bo:
			if x < i:
				global xCoordinate
				xCoordinate = i-cardsWidth
			if i <= 0:
				bo = False
			i-=cardsWidth	

		while bo2:
			if y < j:
				global yCoordinate
				yCoordinate = j-cardsHeight
			if j <= 0:
				bo2 = False
			j-=cardsHeight	

		flippingCards(xCoordinate, yCoordinate)

	else:
		print ("you are out of screen 600 x 600")

def flippingCards(xCoor, yCoor):
	global cardsToPlay
	global AImemory
	c = (xCoor, yCoor)
	for pic_location, picture in cardsToPlay.items():
		if c == pic_location:
			screen.blit(picture, c)
			AImemory.update({c: picture})
			temp2UserCards.update({c: picture})
				
	compareImagesUser(xCoor, yCoor)
		
def compareImagesUser(xCoor, yCoor):
	global cardsToPlay
	global pointsUser
	global temp2UserCards
	global AImemory
	global userPairs

	pygame.display.update()
	if 2 == len(temp2UserCards):
		if list(temp2UserCards.values())[0] == list(temp2UserCards.values())[1]:
			
			xc = list(temp2UserCards.keys())[0]
			yc = list(temp2UserCards.keys())[1]

			pointsUser += 1

			del cardsToPlay[xc]
			del cardsToPlay[yc]

			pygame.display.update()
			time.sleep(1)

			pygame.draw.rect(screen, white,  (xc[0], xc[1],cardsWidth,cardsHeight))
			pygame.draw.rect(screen, white,  (yc[0], yc[1],cardsWidth,cardsHeight))
			userPairs += 1
			scoreUser(userPairs)

			temp2UserCards = {}

			pygame.display.update()
			time.sleep(1)

			turnAImethod()
			AIchoosing()

		else:
			pygame.display.update()
			time.sleep(1)
			screen.blit(cardBack, list(temp2UserCards.keys())[0])
			screen.blit(cardBack, list(temp2UserCards.keys())[1])
			temp2UserCards = {}
			pygame.display.update()
			time.sleep(1)
			turnAImethod()
			AIchoosing()

def AIchoosing():
	global AImemory
	global temp2UserCards
	global temp2AICards
	global AIpairs

	areEqual = False

	if len(cardsToPlay) == 0:
		noMoreCardsToPlay()

	else:
		r = random.randint(0,len(cardsToPlay)-1)
		choose1 = list(cardsToPlay.items())[r]
		keyTemp1 = choose1[0]
		valueTemp1 = choose1[1]

		global keyTemp2 
		global valueTemp2 
		global r2 

		screen.blit(valueTemp1, keyTemp1)
		AImemory.update({keyTemp1: valueTemp1})
		pygame.display.update()
		time.sleep(1)

		same = True
		for item in list(AImemory.items()):
			if choose1[1] == item[1] and choose1[0] != item[0]:
				keyTemp2 = item[0]
				valueTemp2 = item[1]

				xc1 = keyTemp1
				yc1 = keyTemp2

				screen.blit(valueTemp1, keyTemp2)

				pygame.display.update()
				time.sleep(1)

				pygame.draw.rect(screen, white,  (xc1[0], xc1[1],cardsWidth,cardsHeight))
				pygame.draw.rect(screen, white,  (yc1[0], yc1[1],cardsWidth,cardsHeight))
				AIpairs += 1
				scoreAI(AIpairs)

				del cardsToPlay[(xc1[0], xc1[1])]
				del cardsToPlay[(yc1[0], yc1[1])]
				areEqual = True
				break

		while areEqual == False:
			r2 = random.randint(0,len(cardsToPlay)-1)
			if (r != r2):

				choose2 = list(cardsToPlay.items())[r2]
				keyTemp2 = choose2[0]
				valueTemp2 = choose2[1]

				screen.blit(valueTemp2, keyTemp2)
				AImemory.update({keyTemp2: valueTemp2})

				xc = keyTemp1
				yc = keyTemp2

				if valueTemp1 == valueTemp2:
					time.sleep(1)
					pygame.draw.rect(screen, white,  (xc[0], xc[1],cardsWidth,cardsHeight))
					pygame.draw.rect(screen, white,  (yc[0], yc[1],cardsWidth,cardsHeight))
					AIpairs += 1
					scoreAI(AIpairs)

					del cardsToPlay[(xc[0], xc[1])]
					del cardsToPlay[(yc[0], yc[1])]

				else:
					pygame.display.update()
					time.sleep(1)
					screen.blit(cardBack, choose1[0])
					screen.blit(cardBack, choose2[0])
					pygame.display.update()

				areEqual = True

	turnUsermethod()

def turnUsermethod():
	pygame.display.update()
	screen.blit(turnUserLight, (650, 100))
	pygame.display.update()
	global turnAI
	global turnUser
	turnUser = True
	turnAI = False
	noMoreCardsToPlay()

def turnAImethod():
	pygame.display.update()
	screen.blit(turnAILight, (650, 100))
	pygame.display.update()
	global turnAI
	global turnUser
	turnUser = False
	turnAI = True
	noMoreCardsToPlay()

def noMoreCardsToPlay():
	if len(cardsToPlay) == 0:
		turnUser = False
		turnAI = False	
		time.sleep(1)
		if (userPairs > AIpairs):
			screen.blit(youWon, (0,0))
			screen.blit(happy, (650,100))
		else:
			screen.blit(youLost, (0,0))
			screen.blit(sad, (650,100))
		pygame.display.update()
		time.sleep(15) 
		quit()

def scoreUser(scoreUser):
	pygame.draw.rect(screen, grey,  (660,300,230,100))
	font = pygame.font.SysFont(None, 40)
	text = font.render("Mis Puntos: " + str(scoreUser), True, white)
	screen.blit(text, (660, 300))

def scoreAI(scoreAI):
	pygame.draw.rect(screen, grey,  (660,400,200,100))
	font = pygame.font.SysFont(None, 40)
	text = font.render("IA Puntos " + str(scoreAI), True, white)
	screen.blit(text, (660, 400))


gameLoop()

pygame.quit()
quit()