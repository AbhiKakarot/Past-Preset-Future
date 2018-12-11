import pygame
import time
import random

pygame.init()

display_height=700
display_width=1000
gameDisplay=pygame.display.set_mode((display_width,display_height))

icon = pygame.image.load('Four_Star.ico')
pygame.display.set_icon(icon)

pygame.display.set_caption('Past!Present!Future!')

FPS=24
clock=pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

red = (200,0,0)
green = (34,177,76)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)
yellow = (200,200,0)

khsound = pygame.mixer.Sound('game_sounds/kamehameha.wav')
hakaisound = pygame.mixer.Sound('game_sounds/hakai.wav')
ozarusound = pygame.mixer.Sound('game_sounds/ozaru-Transforms.wav')
beamsound = pygame.mixer.Sound('game_sounds/beam.wav')
blastsound = pygame.mixer.Sound('game_sounds/blast.wav')
selectionsound = pygame.mixer.Sound('game_sounds/selection.wav')
jumpsound = pygame.mixer.Sound('game_sounds/jump.wav')



ec = 0
ee = 0
eey = 0
ed = 0
edy = 0
fight = False

time = ['space','e_past','past','present','future']
l = len(time)
time_i = random.randrange(0,l)

chi_chi_loc = time[random.randrange(1,l)]

G_health = 100
villain_health = 100

villain_hit = False
sk_hit = False

bean = pygame.image.load('senzu_bean.png')

forp = pygame.image.load('forp.png')

heart = pygame.image.load('heart.jpg')

goku_sit = pygame.image.load('goku_sit/1.png')

intro_pic = pygame.image.load('intro.jpg')

dance1 = pygame.image.load('dance3.png')
dance2 = pygame.image.load('dance4.png')
dance3 = pygame.image.load('dance1.png')
dance4 = pygame.image.load('dance2.png')

dance = []
dance.append(dance1)
dance.append(dance2)
dance.append(dance1)
dance.append(dance4)
dance.append(dance1)
dance.append(dance2)
dance.append(dance1)
dance.append(dance3)

goku_dead1 = pygame.image.load('goku_dead1/1.png')
goku_dead2 = pygame.image.load('goku_dead1/2.png')
goku_dead3 = pygame.image.load('goku_dead1/3.png')
goku_dead4 = pygame.image.load('goku_dead1/4.png')
goku_dead5 = pygame.image.load('goku_dead1/5.png')

goku_dead = []
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead1)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead2)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead3)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead4)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)
goku_dead.append(goku_dead5)

goku_forward0 = pygame.image.load('goku_forward/3DS - Dragon Ball Z Extreme Butoden - Goku0.png')
goku_forward5 = pygame.image.load('goku_forward/3DS - Dragon Ball Z Extreme Butoden - Goku.png')
goku_forward4 = pygame.image.load('goku_forward/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
goku_forward3 = pygame.image.load('goku_forward/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
goku_forward1 = pygame.image.load('goku_forward/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
goku_forward2 = pygame.image.load('goku_forward/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')

goku_fmove = []
goku_fmove.append(goku_forward0)
goku_fmove.append(goku_forward0)
goku_fmove.append(goku_forward1)
goku_fmove.append(goku_forward1)
goku_fmove.append(goku_forward2)
goku_fmove.append(goku_forward2)
goku_fmove.append(goku_forward3)
goku_fmove.append(goku_forward3)
goku_fmove.append(goku_forward4)
goku_fmove.append(goku_forward4)
goku_fmove.append(goku_forward5)
goku_fmove.append(goku_forward5)

goku_backward1 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
goku_backward2 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
goku_backward3 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
goku_backward4 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')
goku_backward5 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku5.png')
goku_backward6 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku6.png')

goku_bmove = []
goku_bmove.append(goku_backward1)
goku_bmove.append(goku_backward1)
goku_bmove.append(goku_backward2)
goku_bmove.append(goku_backward2)
goku_bmove.append(goku_backward3)
goku_bmove.append(goku_backward3)
goku_bmove.append(goku_backward4)
goku_bmove.append(goku_backward4)
goku_bmove.append(goku_backward5)
goku_bmove.append(goku_backward5)
goku_bmove.append(goku_backward6)
goku_bmove.append(goku_backward6)

goku_jump1 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
goku_jump2 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
goku_jump3 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
goku_jump4 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')
goku_jump5 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku5.png')
goku_jump6 = pygame.image.load('goku_backward/3DS - Dragon Ball Z Extreme Butoden - Goku6.png')

goku_jump = []
goku_jump.append(goku_jump1)
goku_jump.append(goku_jump1)
goku_jump.append(goku_jump2)
goku_jump.append(goku_jump2)
goku_jump.append(goku_jump3)
goku_jump.append(goku_jump3)
goku_jump.append(goku_jump4)
goku_jump.append(goku_jump4)
goku_jump.append(goku_jump5)
goku_jump.append(goku_jump5)
goku_jump.append(goku_jump6)
goku_jump.append(goku_jump6)

goku_punch1 = pygame.image.load('goku_punch/3DS - Dragon Ball Z Extreme Butoden - Goku.png')
goku_punch2 = pygame.image.load('goku_punch/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
goku_punch3 = pygame.image.load('goku_punch/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
goku_punch4 = pygame.image.load('goku_punch/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')

goku_punch = []
goku_punch.append(goku_punch1)
goku_punch.append(goku_punch2)
goku_punch.append(goku_punch3)
goku_punch.append(goku_punch4)

goku_kick1 = pygame.image.load('kick/3DS - Dragon Ball Z Extreme Butoden - Goku.png')
goku_kick2 = pygame.image.load('kick/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
goku_kick3 = pygame.image.load('kick/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
goku_kick4 = pygame.image.load('kick/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
goku_kick5 = pygame.image.load('kick/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')
goku_kick6 = pygame.image.load('kick/3DS - Dragon Ball Z Extreme Butoden - Goku5.png')

goku_kick = []
goku_kick.append(goku_kick1)
goku_kick.append(goku_kick2)
goku_kick.append(goku_kick3)
goku_kick.append(goku_kick4)
goku_kick.append(goku_kick5)
goku_kick.append(goku_kick6)

goku_skick1 = pygame.image.load('special kick/3DS - Dragon Ball Z Extreme Butoden - Goku.png')
goku_skick2 = pygame.image.load('special kick/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
goku_skick3 = pygame.image.load('special kick/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
goku_skick4 = pygame.image.load('special kick/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
goku_skick5 = pygame.image.load('special kick/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')
goku_skick6 = pygame.image.load('special kick/3DS - Dragon Ball Z Extreme Butoden - Goku5.png')

goku_skick = []
goku_skick.append(goku_skick1)
goku_skick.append(goku_skick2)
goku_skick.append(goku_skick3)
goku_skick.append(goku_skick4)
goku_skick.append(goku_skick5)
goku_skick.append(goku_skick6)

energybeam1 = pygame.image.load('energy beam/3DS - Dragon Ball Z Extreme Butoden - Goku.png')
energybeam2 = pygame.image.load('energy beam/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
energybeam3 = pygame.image.load('energy beam/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
energybeam4 = pygame.image.load('energy beam/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
energybeam5 = pygame.image.load('energy beam/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')
energybeam6 = pygame.image.load('energy beam/3DS - Dragon Ball Z Extreme Butoden - Goku5.png')
beam = pygame.image.load('energy beam/beam.png')

goku_ebeam = []
goku_ebeam.append(energybeam1)
goku_ebeam.append(energybeam1)
goku_ebeam.append(energybeam1)
goku_ebeam.append(energybeam2)
goku_ebeam.append(energybeam2)
goku_ebeam.append(energybeam2)
goku_ebeam.append(energybeam3)
goku_ebeam.append(energybeam3)
goku_ebeam.append(energybeam3)
goku_ebeam.append(energybeam4)
goku_ebeam.append(energybeam4)
goku_ebeam.append(energybeam4)
goku_ebeam.append(energybeam5)
goku_ebeam.append(energybeam5)
goku_ebeam.append(energybeam5)
goku_ebeam.append(energybeam6)
goku_ebeam.append(energybeam6)
goku_ebeam.append(energybeam6)

goku_fall1 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku.png')
goku_fall2 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku1.png')
goku_fall3 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku2.png')
goku_fall4 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
goku_fall5 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')
goku_fall6 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku5.png')
goku_fall7 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku6.png')
goku_fall8 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku7.png')
goku_fall9 = pygame.image.load('fall/3DS - Dragon Ball Z Extreme Butoden - Goku8.png')

goku_fall = []
goku_fall.append(goku_fall1)
goku_fall.append(goku_fall1)
goku_fall.append(goku_fall2)
goku_fall.append(goku_fall2)
goku_fall.append(goku_fall3)
goku_fall.append(goku_fall3)
goku_fall.append(goku_fall4)
goku_fall.append(goku_fall4)
goku_fall.append(goku_fall5)
goku_fall.append(goku_fall5)
goku_fall.append(goku_fall6)
goku_fall.append(goku_fall6)
goku_fall.append(goku_fall7)
goku_fall.append(goku_fall7)
goku_fall.append(goku_fall8)
goku_fall.append(goku_fall8)
goku_fall.append(goku_fall9)
goku_fall.append(goku_fall9)

kamehameha1 = pygame.image.load('kamehameha/3DS - Dragon Ball Z Extreme Butoden - Goku8.png')
kamehameha2 = pygame.image.load('kamehameha/3DS - Dragon Ball Z Extreme Butoden - Goku7.png')
kamehameha3 = pygame.image.load('kamehameha/3DS - Dragon Ball Z Extreme Butoden - Goku6.png')
kamehameha4 = pygame.image.load('kamehameha/3DS - Dragon Ball Z Extreme Butoden - Goku5.png')
kamehameha5 = pygame.image.load('kamehameha/3DS - Dragon Ball Z Extreme Butoden - Goku4.png')
kamehameha6 = pygame.image.load('kamehameha/3DS - Dragon Ball Z Extreme Butoden - Goku3.png')
kamehameha7 = pygame.image.load('kamehameha/2.png')
kamehameha8 = pygame.image.load('kamehameha/12.png')
kamehameha9 = pygame.image.load('kamehameha/1.png')
kamehameha10 = pygame.image.load('kamehameha/11.png')

kamehameha = []
kamehameha.append(kamehameha1)
kamehameha.append(kamehameha1)
kamehameha.append(kamehameha1)
kamehameha.append(kamehameha1)
kamehameha.append(kamehameha2)
kamehameha.append(kamehameha2)
kamehameha.append(kamehameha2)
kamehameha.append(kamehameha2)
kamehameha.append(kamehameha3)
kamehameha.append(kamehameha3)
kamehameha.append(kamehameha3)
kamehameha.append(kamehameha3)
kamehameha.append(kamehameha4)
kamehameha.append(kamehameha4)
kamehameha.append(kamehameha4)
kamehameha.append(kamehameha4)
kamehameha.append(kamehameha5)
kamehameha.append(kamehameha5)
kamehameha.append(kamehameha5)
kamehameha.append(kamehameha5)
kamehameha.append(kamehameha6)
kamehameha.append(kamehameha6)
kamehameha.append(kamehameha6)
kamehameha.append(kamehameha6)
kamehameha.append(kamehameha7)
kamehameha.append(kamehameha7)
kamehameha.append(kamehameha7)
kamehameha.append(kamehameha7)
kamehameha.append(kamehameha8)
kamehameha.append(kamehameha8)
kamehameha.append(kamehameha8)
kamehameha.append(kamehameha8)
kamehameha.append(kamehameha9)
kamehameha.append(kamehameha9)
kamehameha.append(kamehameha9)
kamehameha.append(kamehameha9)
kamehameha.append(kamehameha10)
kamehameha.append(kamehameha10)
kamehameha.append(kamehameha10)
kamehameha.append(kamehameha10)
kamehameha.append(kamehameha8)
kamehameha.append(kamehameha8)


space = pygame.image.load('space.jpg')
extremepast = pygame.image.load('extreme_past.jpg')
extremepast1 = pygame.image.load('extreme_past1.jpg')
extremepast2 = pygame.image.load('extreme_past2.jpg')
past = pygame.image.load('dinausaur_era.jpg')
past1 = pygame.image.load('dinausaur_era1.jpg')
past2 = pygame.image.load('dinausaur_era2.jpg')
present = pygame.image.load('7wonders.jpeg')
present1 = pygame.image.load('7wonders1.jpg')
present2 = pygame.image.load('7wonders2.jpeg')
present3 = pygame.image.load('7wonders3.jpg')
present4 = pygame.image.load('7wonders4.jpg')
present5 = pygame.image.load('7wonders5.jpg')
present6 = pygame.image.load('7wonders6.jpg')
future = pygame.image.load('future.jpg')
future1 = pygame.image.load('future0.jpg')
future2 = pygame.image.load('future1.jpg')
future3 = pygame.image.load('future2.jpg')
future4 = pygame.image.load('future3.jpg')
future5 = pygame.image.load('future4.jpg')

time_machine = pygame.image.load('time_machine.png')
chichi = pygame.image.load('chi_chi.png')

enemy_cell1 = pygame.image.load('enemy_cell/1.png') 
enemy_cell2 = pygame.image.load('enemy_cell/2.png') 
enemy_cell3 = pygame.image.load('enemy_cell/3.png') 
enemy_cell4 = pygame.image.load('enemy_cell/4.png') 

enemy_cell = []
enemy_cell.append(enemy_cell1)
enemy_cell.append(enemy_cell1)
enemy_cell.append(enemy_cell2)
enemy_cell.append(enemy_cell2)
enemy_cell.append(enemy_cell3)
enemy_cell.append(enemy_cell3)
enemy_cell.append(enemy_cell4)
enemy_cell.append(enemy_cell4)

blast1 = pygame.image.load('blast/1.png')
blast2 = pygame.image.load('blast/2.png')
blast3 = pygame.image.load('blast/3.png')
blast4 = pygame.image.load('blast/4.png')
blast5 = pygame.image.load('blast/5.png')
blast6 = pygame.image.load('blast/6.png')
blast7 = pygame.image.load('blast/7.png')
blast8 = pygame.image.load('blast/8.png')
blast9 = pygame.image.load('blast/9.png')
blast10 = pygame.image.load('blast/10.png')
blast11 = pygame.image.load('blast/11.png')
blast12 = pygame.image.load('blast/12.png')
blast13 = pygame.image.load('blast/13.png')
blast14 = pygame.image.load('blast/14.png')
blast15 = pygame.image.load('blast/15.png')

blast = []
blast.append(blast1)
blast.append(blast1)
blast.append(blast2)
blast.append(blast2)
blast.append(blast3)
blast.append(blast3)
blast.append(blast4)
blast.append(blast4)
blast.append(blast5)
blast.append(blast5)
blast.append(blast6)
blast.append(blast6)
blast.append(blast7)
blast.append(blast7)
blast.append(blast8)
blast.append(blast8)
blast.append(blast9)
blast.append(blast9)
blast.append(blast10)
blast.append(blast10)
blast.append(blast11)
blast.append(blast11)
blast.append(blast12)
blast.append(blast12)
blast.append(blast13)
blast.append(blast13)
blast.append(blast14)
blast.append(blast14)
blast.append(blast15)
blast.append(blast15)

enemy_eye1 = pygame.image.load('eye/eye.png')
enemy_eye2 = pygame.image.load('eye/eye1.png')
enemy_eye3 = pygame.image.load('eye/eye2.png')
enemy_eye4 = pygame.image.load('eye/eye3.png')
enemy_eye5 = pygame.image.load('eye/eye4.png')
enemy_eye6 = pygame.image.load('eye/eye5.png')

enemy_eye = []
enemy_eye.append(enemy_eye1)
enemy_eye.append(enemy_eye2)
enemy_eye.append(enemy_eye3)
enemy_eye.append(enemy_eye4)
enemy_eye.append(enemy_eye5)
enemy_eye.append(enemy_eye6)

enemy_dragon1 = pygame.image.load('dragon/1.png')
enemy_dragon2 = pygame.image.load('dragon/2.png')
enemy_dragon3 = pygame.image.load('dragon/3.png')
enemy_dragon4 = pygame.image.load('dragon/4.png')
enemy_dragon5 = pygame.image.load('dragon/5.png')
enemy_dragon6 = pygame.image.load('dragon/6.png')
enemy_dragon7 = pygame.image.load('dragon/7.png')
enemy_dragon8 = pygame.image.load('dragon/8.png')

enemy_dragon = []
enemy_dragon.append(enemy_dragon1)
enemy_dragon.append(enemy_dragon1)
enemy_dragon.append(enemy_dragon2)
enemy_dragon.append(enemy_dragon2)
enemy_dragon.append(enemy_dragon3)
enemy_dragon.append(enemy_dragon3)
enemy_dragon.append(enemy_dragon4)
enemy_dragon.append(enemy_dragon4)
enemy_dragon.append(enemy_dragon5)
enemy_dragon.append(enemy_dragon5)
enemy_dragon.append(enemy_dragon6)
enemy_dragon.append(enemy_dragon6)
enemy_dragon.append(enemy_dragon7)
enemy_dragon.append(enemy_dragon7)
enemy_dragon.append(enemy_dragon8)
enemy_dragon.append(enemy_dragon8)

beerus1 = pygame.image.load('beerus/standing/1.png')
beerus2 = pygame.image.load('beerus/standing/2.png')
beerus3 = pygame.image.load('beerus/standing/3.png')
beerus4 = pygame.image.load('beerus/standing/4.png')
beerus5 = pygame.image.load('beerus/standing/5.png')
beerus6 = pygame.image.load('beerus/standing/6.png')
beerus7 = pygame.image.load('beerus/standing/7.png')
beerus8 = pygame.image.load('beerus/standing/8.png')
beerus9 = pygame.image.load('beerus/standing/9.png')
beerus10 = pygame.image.load('beerus/standing/10.png')

beerus_transmit1 = pygame.image.load('beerus/1.png')
beerus_transmit2 = pygame.image.load('beerus/2.png')

beerus_stand = []
beerus_stand.append(beerus1)
beerus_stand.append(beerus1)
beerus_stand.append(beerus2)
beerus_stand.append(beerus2)
beerus_stand.append(beerus3)
beerus_stand.append(beerus3)
beerus_stand.append(beerus4)
beerus_stand.append(beerus4)
beerus_stand.append(beerus5)
beerus_stand.append(beerus5)
beerus_stand.append(beerus6)
beerus_stand.append(beerus6)
beerus_stand.append(beerus7)
beerus_stand.append(beerus7)
beerus_stand.append(beerus8)
beerus_stand.append(beerus8)
beerus_stand.append(beerus9)
beerus_stand.append(beerus9)
beerus_stand.append(beerus10)
beerus_stand.append(beerus10)

beerus_a1 = pygame.image.load('beerus/attack1/1.png')
beerus_a2 = pygame.image.load('beerus/attack1/2.png')
beerus_a3 = pygame.image.load('beerus/attack1/3.png')
beerus_a4 = pygame.image.load('beerus/attack1/4.png')
beerus_a5 = pygame.image.load('beerus/attack1/5.png')
beerus_a6 = pygame.image.load('beerus/attack1/6.png')
beerus_a7 = pygame.image.load('beerus/attack1/7.png')
beerus_a8 = pygame.image.load('beerus/attack1/8.png')
beerus_a9 = pygame.image.load('beerus/attack1/9.png')
beerus_a10 = pygame.image.load('beerus/attack2/1.png')
beerus_a12 = pygame.image.load('beerus/attack2/2.png')
beerus_a13 = pygame.image.load('beerus/attack2/3.png')
beerus_a14 = pygame.image.load('beerus/attack2/4.png')
beerus_a15 = pygame.image.load('beerus/attack2/5.png')
beerus_a16 = pygame.image.load('beerus/attack2/6.png')

beerus_aa = []
beerus_aa.append(beerus_a1)
beerus_aa.append(beerus_a1)
beerus_aa.append(beerus_a2)
beerus_aa.append(beerus_a2)
beerus_aa.append(beerus_a3)
beerus_aa.append(beerus_a3)
beerus_aa.append(beerus_a4)
beerus_aa.append(beerus_a4)
beerus_aa.append(beerus_a5)
beerus_aa.append(beerus_a5)
beerus_aa.append(beerus_a6)
beerus_aa.append(beerus_a6)
beerus_aa.append(beerus_a7)
beerus_aa.append(beerus_a7)
beerus_aa.append(beerus_a8)
beerus_aa.append(beerus_a8)
beerus_aa.append(beerus_a9)
beerus_aa.append(beerus_a9)

beerus_ab = []
beerus_ab.append(beerus_a10)
beerus_ab.append(beerus_a10)
beerus_ab.append(beerus_a12)
beerus_ab.append(beerus_a12)
beerus_ab.append(beerus_a13)
beerus_ab.append(beerus_a13)
beerus_ab.append(beerus_a14)
beerus_ab.append(beerus_a14)
beerus_ab.append(beerus_a15)
beerus_ab.append(beerus_a15)
beerus_ab.append(beerus_a16)
beerus_ab.append(beerus_a16)

hakai1 = pygame.image.load('beerus/hakai/1.png')
hakai2 = pygame.image.load('beerus/hakai/2.png')
hakai3 = pygame.image.load('beerus/hakai/3.png')
hakai4 = pygame.image.load('beerus/hakai/4.png')
hakai5 = pygame.image.load('beerus/hakai/5.png')
hakai6 = pygame.image.load('beerus/hakai/6.png')
hakai7 = pygame.image.load('beerus/hakai/7.png')

hakai = []
hakai.append(hakai1)
hakai.append(hakai2)
hakai.append(hakai3)
hakai.append(hakai4)
hakai.append(hakai5)
hakai.append(hakai6)
hakai.append(hakai7)

frieza_stand1 = pygame.image.load('frieza/standing/1.png')
frieza_stand2 = pygame.image.load('frieza/standing/2.png')
frieza_stand3 = pygame.image.load('frieza/standing/3.png')
frieza_stand4 = pygame.image.load('frieza/standing/4.png')
frieza_stand5 = pygame.image.load('frieza/standing/5.png')
frieza_stand6 = pygame.image.load('frieza/standing/6.png')

frieza_stand = []
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand2)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand3)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand4)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand5)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)
frieza_stand.append(frieza_stand6)

frieza_aa1 = pygame.image.load('frieza/attack/1.png')
frieza_aa2 = pygame.image.load('frieza/attack/2.png')
frieza_aa3 = pygame.image.load('frieza/attack/3.png')
frieza_aa4 = pygame.image.load('frieza/attack/4.png')

frieza_aa = []
frieza_aa.append(frieza_aa1)
frieza_aa.append(frieza_aa2)
frieza_aa.append(frieza_aa3)
frieza_aa.append(frieza_aa4)

ozaru_stand = pygame.image.load('ozaru/1.png')

ozaru_attack1 = pygame.image.load('ozaru/attack/1.png')
ozaru_attack2 = pygame.image.load('ozaru/attack/2.png')
ozaru_attack3 = pygame.image.load('ozaru/attack/3.png')
ozaru_attack4 = pygame.image.load('ozaru/attack/4.png')
ozaru_attack5 = pygame.image.load('ozaru/attack/5.png')
ozaru_attack6 = pygame.image.load('ozaru/attack/6.png')
ozaru_attack7 = pygame.image.load('ozaru/attack/7.png')

ozaru_attack = []
ozaru_attack.append(ozaru_attack1)
ozaru_attack.append(ozaru_attack1)
ozaru_attack.append(ozaru_attack1)
ozaru_attack.append(ozaru_attack1)
ozaru_attack.append(ozaru_attack2)
ozaru_attack.append(ozaru_attack2)
ozaru_attack.append(ozaru_attack2)
ozaru_attack.append(ozaru_attack2)
ozaru_attack.append(ozaru_attack3)
ozaru_attack.append(ozaru_attack3)
ozaru_attack.append(ozaru_attack3)
ozaru_attack.append(ozaru_attack3)
ozaru_attack.append(ozaru_attack4)
ozaru_attack.append(ozaru_attack4)
ozaru_attack.append(ozaru_attack4)
ozaru_attack.append(ozaru_attack4)
ozaru_attack.append(ozaru_attack5)
ozaru_attack.append(ozaru_attack5)
ozaru_attack.append(ozaru_attack5)
ozaru_attack.append(ozaru_attack5)
ozaru_attack.append(ozaru_attack6)
ozaru_attack.append(ozaru_attack6)
ozaru_attack.append(ozaru_attack6)
ozaru_attack.append(ozaru_attack6)
ozaru_attack.append(ozaru_attack7)
ozaru_attack.append(ozaru_attack7)
ozaru_attack.append(ozaru_attack7)
ozaru_attack.append(ozaru_attack7)

ozaru_transform1 = pygame.image.load('ozaru/transform/1.png')
ozaru_transform2 = pygame.image.load('ozaru/transform/2.png')
ozaru_transform3 = pygame.image.load('ozaru/transform/3.png')
ozaru_transform4 = pygame.image.load('ozaru/transform/4.png')
ozaru_transform5 = pygame.image.load('ozaru/transform/5.png')
ozaru_transform6 = pygame.image.load('ozaru/transform/6.png')
ozaru_transform7 = pygame.image.load('ozaru/transform/7.png')
ozaru_transform8 = pygame.image.load('ozaru/transform/8.png')
ozaru_transform9 = pygame.image.load('ozaru/transform/9.png')
ozaru_transform10 = pygame.image.load('ozaru/transform/10.png')
ozaru_transform11 = pygame.image.load('ozaru/transform/11.png')
ozaru_transform12 = pygame.image.load('ozaru/transform/12.png')
ozaru_transform13 = pygame.image.load('ozaru/transform/13.png')
ozaru_transform14 = pygame.image.load('ozaru/transform/14.png')
ozaru_transform15 = pygame.image.load('ozaru/transform/15.png')
ozaru_transform16 = pygame.image.load('ozaru/transform/16.png')
ozaru_transform17 = pygame.image.load('ozaru/transform/17.png')
ozaru_transform18 = pygame.image.load('ozaru/transform/18.png')
ozaru_transform19 = pygame.image.load('ozaru/transform/19.png')
ozaru_transform20 = pygame.image.load('ozaru/transform/20.png')
ozaru_transform21 = pygame.image.load('ozaru/transform/21.png')
ozaru_transform22 = pygame.image.load('ozaru/transform/22.png')
ozaru_transform23 = pygame.image.load('ozaru/transform/23.png')
ozaru_transform24 = pygame.image.load('ozaru/transform/24.png')

ozaru_transform = []
ozaru_transform.append(ozaru_transform1)
ozaru_transform.append(ozaru_transform1)
ozaru_transform.append(ozaru_transform2)
ozaru_transform.append(ozaru_transform2)
ozaru_transform.append(ozaru_transform3)
ozaru_transform.append(ozaru_transform3)
ozaru_transform.append(ozaru_transform4)
ozaru_transform.append(ozaru_transform4)
ozaru_transform.append(ozaru_transform5)
ozaru_transform.append(ozaru_transform5)
ozaru_transform.append(ozaru_transform6)
ozaru_transform.append(ozaru_transform6)
ozaru_transform.append(ozaru_transform7)
ozaru_transform.append(ozaru_transform7)
ozaru_transform.append(ozaru_transform8)
ozaru_transform.append(ozaru_transform8)
ozaru_transform.append(ozaru_transform9)
ozaru_transform.append(ozaru_transform9)
ozaru_transform.append(ozaru_transform10)
ozaru_transform.append(ozaru_transform10)
ozaru_transform.append(ozaru_transform11)
ozaru_transform.append(ozaru_transform11)
ozaru_transform.append(ozaru_transform12)
ozaru_transform.append(ozaru_transform12)
ozaru_transform.append(ozaru_transform13)
ozaru_transform.append(ozaru_transform13)
ozaru_transform.append(ozaru_transform14)
ozaru_transform.append(ozaru_transform14)
ozaru_transform.append(ozaru_transform15)
ozaru_transform.append(ozaru_transform15)
ozaru_transform.append(ozaru_transform16)
ozaru_transform.append(ozaru_transform16)
ozaru_transform.append(ozaru_transform17)
ozaru_transform.append(ozaru_transform17)
ozaru_transform.append(ozaru_transform18)
ozaru_transform.append(ozaru_transform18)
ozaru_transform.append(ozaru_transform19)
ozaru_transform.append(ozaru_transform19)
ozaru_transform.append(ozaru_transform20)
ozaru_transform.append(ozaru_transform20)
ozaru_transform.append(ozaru_transform21)
ozaru_transform.append(ozaru_transform21)
ozaru_transform.append(ozaru_transform22)
ozaru_transform.append(ozaru_transform22)
ozaru_transform.append(ozaru_transform23)
ozaru_transform.append(ozaru_transform23)
ozaru_transform.append(ozaru_transform24)
ozaru_transform.append(ozaru_transform24)

majin_stand1 = pygame.image.load('buu/standing/1.png')
majin_stand2 = pygame.image.load('buu/standing/2.png')
majin_stand3 = pygame.image.load('buu/standing/3.png')
majin_stand4 = pygame.image.load('buu/standing/5.png')
majin_stand5 = pygame.image.load('buu/standing/5.png')
majin_stand6 = pygame.image.load('buu/standing/6.png')
majin_stand7 = pygame.image.load('buu/standing/7.png')
majin_stand8 = pygame.image.load('buu/standing/8.png')
majin_stand9 = pygame.image.load('buu/standing/9.png')
majin_stand10 = pygame.image.load('buu/standing/10.png')
majin_stand11 = pygame.image.load('buu/standing/11.png')
majin_stand12 = pygame.image.load('buu/standing/12.png')
majin_stand13 = pygame.image.load('buu/standing/13.png')
majin_stand14 = pygame.image.load('buu/standing/14.png')
majin_stand15 = pygame.image.load('buu/standing/15.png')
majin_stand16 = pygame.image.load('buu/standing/16.png')
majin_stand17 = pygame.image.load('buu/standing/17.png')
majin_stand18 = pygame.image.load('buu/standing/18.png')
majin_stand19 = pygame.image.load('buu/standing/19.png')
majin_stand20 = pygame.image.load('buu/standing/20.png')
majin_stand21 = pygame.image.load('buu/standing/21.png')
majin_stand22 = pygame.image.load('buu/standing/22.png')
majin_stand23 = pygame.image.load('buu/standing/23.png')
majin_stand24 = pygame.image.load('buu/standing/24.png')
majin_stand25 = pygame.image.load('buu/standing/25.png')
majin_stand26 = pygame.image.load('buu/standing/26.png')
majin_stand27 = pygame.image.load('buu/standing/27.png')
majin_stand28 = pygame.image.load('buu/standing/28.png')
majin_stand29 = pygame.image.load('buu/standing/29.png')
majin_stand30 = pygame.image.load('buu/standing/30.png')

majin_stand = []
majin_stand.append(majin_stand1)
majin_stand.append(majin_stand1)
majin_stand.append(majin_stand1)
majin_stand.append(majin_stand2)
majin_stand.append(majin_stand2)
majin_stand.append(majin_stand2)
majin_stand.append(majin_stand3)
majin_stand.append(majin_stand3)
majin_stand.append(majin_stand3)
majin_stand.append(majin_stand4)
majin_stand.append(majin_stand4)
majin_stand.append(majin_stand4)
majin_stand.append(majin_stand5)
majin_stand.append(majin_stand5)
majin_stand.append(majin_stand5)
majin_stand.append(majin_stand6)
majin_stand.append(majin_stand6)
majin_stand.append(majin_stand6)
majin_stand.append(majin_stand7)
majin_stand.append(majin_stand7)
majin_stand.append(majin_stand7)
majin_stand.append(majin_stand8)
majin_stand.append(majin_stand8)
majin_stand.append(majin_stand8)
majin_stand.append(majin_stand9)
majin_stand.append(majin_stand9)
majin_stand.append(majin_stand9)
majin_stand.append(majin_stand10)
majin_stand.append(majin_stand10)
majin_stand.append(majin_stand10)
majin_stand.append(majin_stand11)
majin_stand.append(majin_stand11)
majin_stand.append(majin_stand11)
majin_stand.append(majin_stand12)
majin_stand.append(majin_stand12)
majin_stand.append(majin_stand12)
majin_stand.append(majin_stand13)
majin_stand.append(majin_stand13)
majin_stand.append(majin_stand13)
majin_stand.append(majin_stand14)
majin_stand.append(majin_stand14)
majin_stand.append(majin_stand14)
majin_stand.append(majin_stand15)
majin_stand.append(majin_stand15)
majin_stand.append(majin_stand15)
majin_stand.append(majin_stand16)
majin_stand.append(majin_stand16)
majin_stand.append(majin_stand16)
majin_stand.append(majin_stand17)
majin_stand.append(majin_stand17)
majin_stand.append(majin_stand17)
majin_stand.append(majin_stand18)
majin_stand.append(majin_stand18)
majin_stand.append(majin_stand18)
majin_stand.append(majin_stand19)
majin_stand.append(majin_stand19)
majin_stand.append(majin_stand19)
majin_stand.append(majin_stand20)
majin_stand.append(majin_stand20)
majin_stand.append(majin_stand20)
majin_stand.append(majin_stand21)
majin_stand.append(majin_stand21)
majin_stand.append(majin_stand21)
majin_stand.append(majin_stand22)
majin_stand.append(majin_stand22)
majin_stand.append(majin_stand22)
majin_stand.append(majin_stand23)
majin_stand.append(majin_stand23)
majin_stand.append(majin_stand23)
majin_stand.append(majin_stand24)
majin_stand.append(majin_stand24)
majin_stand.append(majin_stand24)
majin_stand.append(majin_stand25)
majin_stand.append(majin_stand25)
majin_stand.append(majin_stand25)
majin_stand.append(majin_stand26)
majin_stand.append(majin_stand26)
majin_stand.append(majin_stand26)
majin_stand.append(majin_stand27)
majin_stand.append(majin_stand27)
majin_stand.append(majin_stand27)
majin_stand.append(majin_stand28)
majin_stand.append(majin_stand28)
majin_stand.append(majin_stand28)
majin_stand.append(majin_stand29)
majin_stand.append(majin_stand29)
majin_stand.append(majin_stand29)
majin_stand.append(majin_stand30)
majin_stand.append(majin_stand30)
majin_stand.append(majin_stand30)

majin_attack1 = pygame.image.load('buu/attack/1.png')
majin_attack2 = pygame.image.load('buu/attack/2.png')
majin_attack3 = pygame.image.load('buu/attack/3.png')
majin_attack4 = pygame.image.load('buu/attack/4.png')
majin_attack5 = pygame.image.load('buu/attack/5.png')
majin_attack6 = pygame.image.load('buu/attack/6.png')
majin_attack7 = pygame.image.load('buu/attack/7.png')
majin_attack8 = pygame.image.load('buu/attack/8.png')
majin_attack9 = pygame.image.load('buu/attack/9.png')
majin_attack10 = pygame.image.load('buu/attack/10.png')
majin_attack11 = pygame.image.load('buu/attack/11.png')
majin_attack12 = pygame.image.load('buu/attack/12.png')
majin_attack13 = pygame.image.load('buu/attack/13.png')

majin_attack = []
majin_attack.append(majin_attack1)
majin_attack.append(majin_attack1)
majin_attack.append(majin_attack2)
majin_attack.append(majin_attack2)
majin_attack.append(majin_attack3)
majin_attack.append(majin_attack3)
majin_attack.append(majin_attack4)
majin_attack.append(majin_attack4)
majin_attack.append(majin_attack5)
majin_attack.append(majin_attack5)
majin_attack.append(majin_attack6)
majin_attack.append(majin_attack6)
majin_attack.append(majin_attack7)
majin_attack.append(majin_attack7)
majin_attack.append(majin_attack8)
majin_attack.append(majin_attack8)
majin_attack.append(majin_attack9)
majin_attack.append(majin_attack9)
majin_attack.append(majin_attack10)
majin_attack.append(majin_attack10)
majin_attack.append(majin_attack11)
majin_attack.append(majin_attack11)
majin_attack.append(majin_attack12)
majin_attack.append(majin_attack12)
majin_attack.append(majin_attack13)
majin_attack.append(majin_attack13)

def b_fight(BG_X):
	gameOver = False
	goku_x = 20
	goku_y = 555
	goku_i = 0
	goku_j = 0
	goku_xc = 0
	goku_yc = 0
	isWalking = False
	velocity = 0
	gravity = 0.8
	m = 2
	isJump = False
	onGround = True
	walk_direction = 0
	global time,time_i,G_health,fight,villain_health,villain_hit,sk_hit,l
	fight = True
	sit = False
	b_s = 0
	bx = 800
	by = 555
	b_count = 0
	a_count = 0
	villain_health = 100
	pygame.mixer.music.pause()
	pygame.mixer.music.load("game_sounds/beerus.wav")
	pygame.mixer.music.play(-1)
	while not gameOver:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					goku_xc -= 5
					walk_direction = -1
					isWalking = True	
				elif event.key == pygame.K_RIGHT:
					isWalking = True
					walk_direction = 1
					goku_xc += 5
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					sit = True
				elif event.key == pygame.K_x:
					punch(goku_x,goku_y,BG_X,bx,by)
				elif event.key == pygame.K_v:
					kick(goku_x,goku_y,BG_X,bx,by)
				elif event.key == pygame.K_f:
					specialkick(goku_x,goku_y,BG_X,bx,by)
				elif event.key == pygame.K_s:
					energybeam(goku_x,goku_y,BG_X,bx,by)
				elif event.key == pygame.K_k:
					KHH(goku_x,goku_y,BG_X)
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_SPACE and onGround == True:
					pygame.mixer.Sound.play(jumpsound)
					velocity = 8
					isJump = True
					onGround = False
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					isWalking = False
					goku_xc = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					sit = False
				if event.key == pygame.K_SPACE:
					pass
		if goku_x <= 0:
			goku_x = 0
		elif goku_x >= display_width-150:
			goku_x = display_width-150

		if goku_x+110 >= bx and goku_y+100>=by:
			fall(goku_x,goku_y,BG_X)
			goku_x -= 70

		if isJump == True:
			if velocity >= 0:
		                F = ( 0.5 * m * (velocity*velocity) )
				if goku_j <5:
					goku_j += 1
        		else:
        			F = -( 0.5 * m * (velocity*velocity) )
				if goku_j < 10:
					goku_j += 1		
			goku_y += goku_yc - F
			velocity -= 1
			if goku_y >= 555:
				goku_y = 555
		                isJump = False
		                velocity = 0
				goku_j = 0
				onGround = True

		goku_x += goku_xc
		if isWalking == True:
			if goku_i > 10:
				goku_i = 11
			else:
				goku_i += 1
		if isWalking == False:
			if goku_i < 1:
				goku_i = 0
				walk_direction = 0
			else:
				goku_i -= 1

		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))

			if BG_X <= -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width()):
				BG_X = -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width())

		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))

			if BG_X <= -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width()):
				BG_X = -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width())

		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))

			if BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width()):
				BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width())

		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))

		if BG_X <= -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width()):
			BG_X = -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width())

		if sit == True:
			gameDisplay.blit(goku_sit,(goku_x,goku_y+40))
		elif walk_direction == 1 and isJump == False:
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == False:
				gameDisplay.blit(goku_bmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == False:
				goku_i = 0
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		if b_s >= 19:
			b_s = 0

		if b_count >= 200 and b_count<=340:
			if b_count >=200 and b_count<=220:
				gameDisplay.blit(beerus_transmit1,(bx,by))
			elif b_count >=220 and b_count<=240:
				gameDisplay.blit(beerus_transmit2,(bx,by))
			elif b_count < 340:
				gameDisplay.blit(beerus_stand[b_s],(bx,by-400))
			else:
				b_count = 0
				a_count += 1
				if a_count >= 2 and a_count%4 == 0:
					b_attack1(BG_X,bx,by,goku_x,goku_y)
					if not goku_y+100 <= by:
						fall(goku_x,goku_y,BG_X)
						G_health -= 8
				elif a_count >= 2 and a_count%2 == 0:
					b_attack2(BG_X,bx,by,goku_x,goku_y)
					if not goku_y+100 <= by:
						fall(goku_x,goku_y,BG_X)
						G_health -= 8
		else:
			gameDisplay.blit(beerus_stand[b_s],(bx,by))
			villain_hit = False
			sk_hit = False
		b_s += 1
		b_count += 1
		if b_count >= 200 and b_count <= 240 and villain_hit == True and sk_hit == True:
			villain_health -= 5
			sk_hit = False
			villain_hit = False
			goku_x = 300
		elif b_count >= 200 and b_count <= 240 and villain_hit == True:
			villain_health -= 3
			villain_hit = False
			goku_x = 300

		if villain_health <= 95:
			if chi_chi_loc == time[time_i]:
				celebration()
			else:
				t_machine(BG_X,goku_x,goku_y)
				temp = time_i
				while(temp < l-1):
					time[temp] = time[temp+1]
					temp += 1					
				time.pop(l-1)
				l = len(time)
				where()

		if G_health <= 0:
			dead(goku_x,goku_y,BG_X)
			gameover()


		if a_count >20:
			hakai_a(BG_X,bx,by,goku_x,goku_y)
			gameover()
		message = str(G_health)
		message1 = str(villain_health)
		message_to_screen(message,white,-400,-300,"large")
		message_to_screen(message1,white,400,-300,"large")
		pygame.display.update()
		clock.tick(FPS)

def b_attack1(BG_X,bx,by,goku_x,goku_y):
	i=0
	global time,time_i
	while(i<18):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(beerus_aa[i],(bx-(bx-goku_x)+100,by))
		i+=1
		gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		pygame.display.update()
		clock.tick(FPS)

def b_attack2(BG_X,bx,by,goku_x,goku_y):
	i=0
	global time,time_i
	while(i<12):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(beerus_ab[i],(bx-(bx-goku_x)+80,by))
		i+=1
		gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		pygame.display.update()
		clock.tick(FPS)

def hakai_a(BG_X,bx,by,goku_x,goku_y):
	pygame.mixer.Sound.play(hakaisound)
	i=0
	global time,time_i
	while(i<30):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		if i<6:
			gameDisplay.blit(hakai[i],(bx-(bx-goku_x)+80,by))
			gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		elif i<24:
			gameDisplay.blit(hakai[6],(bx-(bx-goku_x)+80,by))
			gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		else:
			gameDisplay.blit(hakai[0],(bx-(bx-goku_x)+80,by))
		i+=1
		pygame.display.update()
		clock.tick(1)


def f_fight(BG_X):
	gameOver = False
	goku_x = 20
	goku_y = 555
	goku_i = 0
	goku_j = 0
	goku_xc = 0
	goku_yc = 0
	isWalking = False
	velocity = 0
	gravity = 0.8
	m = 2
	isJump = False
	onGround = True
	walk_direction = 0
	global time,time_i,G_health,fight,villain_health,villain_hit,sk_hit,l
	fight = True
	sit = False
	f_s = 0
	fx = 800
	fy = 600
	f_count = 0
	temp = random.randrange(300,500)
	villain_health = 100
	pygame.mixer.music.pause()
	pygame.mixer.music.load("game_sounds/frieza.mp3")
	pygame.mixer.music.play(-1)
	while not gameOver:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					goku_xc -= 5
					walk_direction = -1
					isWalking = True	
				elif event.key == pygame.K_RIGHT:
					isWalking = True
					walk_direction = 1
					goku_xc += 5
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					sit = True
				elif event.key == pygame.K_x:
					punch(goku_x,goku_y,BG_X,fx,fy)
				elif event.key == pygame.K_v:
					kick(goku_x,goku_y,BG_X,fx,fy)
				elif event.key == pygame.K_f:
					specialkick(goku_x,goku_y,BG_X,fx,fy)
				elif event.key == pygame.K_s:
					energybeam(goku_x,goku_y,BG_X,fx,fy)
				elif event.key == pygame.K_k:
					KHH(goku_x,goku_y,BG_X)
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_SPACE and onGround == True:
					pygame.mixer.Sound.play(jumpsound)
					velocity = 8
					isJump = True
					onGround = False
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					isWalking = False
					goku_xc = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					sit = False
				if event.key == pygame.K_SPACE:
					pass
		if goku_x <= 0:
			goku_x = 0
		elif goku_x >= display_width-150:
			goku_x = display_width-150

		if goku_x+110 >= fx and goku_y+100>=fy:
			fall(goku_x,goku_y,BG_X)
			goku_x -= 70

		if isJump == True:
			if velocity >= 0:
		                F = ( 0.5 * m * (velocity*velocity) )
				if goku_j <5:
					goku_j += 1
        		else:
        			F = -( 0.5 * m * (velocity*velocity) )
				if goku_j < 10:
					goku_j += 1		
			goku_y += goku_yc - F
			velocity -= 1
			if goku_y >= 555:
				goku_y = 555
		                isJump = False
		                velocity = 0
				goku_j = 0
				onGround = True

		goku_x += goku_xc
		if isWalking == True:
			if goku_i > 10:
				goku_i = 11
			else:
				goku_i += 1
		if isWalking == False:
			if goku_i < 1:
				goku_i = 0
				walk_direction = 0
			else:
				goku_i -= 1

		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))

			if BG_X <= -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width()):
				BG_X = -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width())

		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))

			if BG_X <= -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width()):
				BG_X = -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width())

		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))

			if BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width()):
				BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width())

		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))

		if BG_X <= -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width()):
			BG_X = -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width())

		if sit == True:
			gameDisplay.blit(goku_sit,(goku_x,goku_y+40))
		elif walk_direction == 1 and isJump == False:
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == False:
				gameDisplay.blit(goku_bmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == False:
				goku_i = 0
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		if f_s >= 60:
			f_s = 0

		if f_count >= temp:
			f_attack(BG_X,fx,fy,goku_x,goku_y)
			if not goku_y+100 <= fy:
				fall(goku_x,goku_y,BG_X)
				G_health -= 3
			f_count = 0
			temp = random.randrange(300,500)
		else:
			gameDisplay.blit(frieza_stand[f_s],(fx,fy))
		f_s += 1
		f_count += 1

		if villain_hit == True and sk_hit == True:
			villain_health -= 3
			sk_hit = False
			villain_hit = False
			goku_x = 300
		elif villain_hit == True:
			villain_health -= 1
			villain_hit = False
			goku_x = 300

		if villain_health <= 95:
			if chi_chi_loc == time[time_i]:
				celebration()
			else:
				t_machine(BG_X,goku_x,goku_y)
				temp = time_i
				while(temp < l-1):
					time[temp] = time[temp+1]
					temp += 1					
				time.pop(l-1)
				l = len(time)
				where()

		if G_health <= 0:
			dead(goku_x,goku_y,BG_X)
			gameover()

		message = str(G_health)
		message1 = str(villain_health)
		message_to_screen(message,white,-400,-300,"large")
		message_to_screen(message1,white,400,-300,"large")
		pygame.display.update()
		clock.tick(FPS)

def f_attack(BG_X,fx,fy,goku_x,goku_y):
	i=0
	count = 0
	global time,time_i
	while(i<4):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(frieza_aa[i],(fx-(fx-goku_x)+80,fy))
		i+=1
		gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		pygame.display.update()
		clock.tick(FPS)


def o_fight(BG_X):
	gameOver = False
	goku_x = 20
	goku_y = 555
	goku_i = 0
	goku_j = 0
	goku_xc = 0
	goku_yc = 0
	isWalking = False
	velocity = 0
	gravity = 0.8
	m = 2
	isJump = False
	onGround = True
	walk_direction = 0
	global time,time_i,G_health,fight,villain_health,villain_hit,sk_hit,l
	villain_health = 100
	fight = True
	sit = False
	ox = 750
	oy = 450
	o_count = 0
	temp = random.randrange(300,500)
	o_transformation(BG_X,ox,oy,goku_x,goku_y)
	pygame.mixer.music.pause()
	pygame.mixer.music.load("game_sounds/janemba.mp3")
	pygame.mixer.music.play(-1)
	while not gameOver:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					goku_xc -= 5
					walk_direction = -1
					isWalking = True	
				elif event.key == pygame.K_RIGHT:
					isWalking = True
					walk_direction = 1
					goku_xc += 5
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					sit = True
				elif event.key == pygame.K_x:
					punch(goku_x,goku_y,BG_X,ox,oy)
				elif event.key == pygame.K_v:
					kick(goku_x,goku_y,BG_X,ox,oy)
				elif event.key == pygame.K_f:
					specialkick(goku_x,goku_y,BG_X,ox,oy)
				elif event.key == pygame.K_s:
					energybeam(goku_x,goku_y,BG_X,ox,oy)
				elif event.key == pygame.K_k:
					KHH(goku_x,goku_y,BG_X)
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_SPACE and onGround == True:
					pygame.mixer.Sound.play(jumpsound)
					velocity = 8
					isJump = True
					onGround = False
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					isWalking = False
					goku_xc = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					sit = False
				if event.key == pygame.K_SPACE:
					pass
		if goku_x <= 0:
			goku_x = 0
		elif goku_x >= display_width-150:
			goku_x = display_width-150

		if goku_x+110 >= ox and goku_y+100>=oy:
			fall(goku_x,goku_y,BG_X)
			goku_x -= 70

		if isJump == True:
			if velocity >= 0:
		                F = ( 0.5 * m * (velocity*velocity) )
				if goku_j <5:
					goku_j += 1
        		else:
        			F = -( 0.5 * m * (velocity*velocity) )
				if goku_j < 10:
					goku_j += 1		
			goku_y += goku_yc - F
			velocity -= 1
			if goku_y >= 555:
				goku_y = 555
		                isJump = False
		                velocity = 0
				goku_j = 0
				onGround = True

		goku_x += goku_xc
		if isWalking == True:
			if goku_i > 10:
				goku_i = 11
			else:
				goku_i += 1
		if isWalking == False:
			if goku_i < 1:
				goku_i = 0
				walk_direction = 0
			else:
				goku_i -= 1

		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))

			if BG_X <= -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width()):
				BG_X = -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width())

		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))

			if BG_X <= -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width()):
				BG_X = -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width())

		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))

			if BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width()):
				BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width())

		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))

		if BG_X <= -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width()):
			BG_X = -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width())

		if sit == True:
			gameDisplay.blit(goku_sit,(goku_x,goku_y+40))
		elif walk_direction == 1 and isJump == False:
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == False:
				gameDisplay.blit(goku_bmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == False:
				goku_i = 0
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))

		if o_count >= temp:
			o_attack(BG_X,ox,oy,goku_x,goku_y)
			if not goku_y+100 <= oy:
				fall(goku_x,goku_y,BG_X)
				G_health -= 8
			o_count = 0
			temp = random.randrange(300,500)
		else:
			gameDisplay.blit(ozaru_stand,(ox,oy))

		o_count += 1
		if villain_hit == True and sk_hit == True:
			villain_health -= 3
			sk_hit = False
			villain_hit = False
			goku_x = 300
		elif villain_hit == True:
			villain_health -= 1
			villain_hit = False
			goku_x = 300

		if villain_health <= 95:
			if chi_chi_loc == time[time_i]:
				celebration()
			else:
				t_machine(BG_X,goku_x,goku_y)
				temp = time_i
				while(temp < l-1):
					time[temp] = time[temp+1]
					temp += 1					
				time.pop(l-1)
				l = len(time)
				where()

		if G_health <= 0:
			dead(goku_x,goku_y,BG_X)
			gameover()

		message = str(G_health)
		message1 = str(villain_health)
		message_to_screen(message,white,-400,-300,"large")
		message_to_screen(message1,white,400,-300,"large")
		pygame.display.update()
		clock.tick(FPS)

def o_transformation(BG_X,ox,oy,goku_x,goku_y):
	pygame.mixer.Sound.play(ozarusound)
	i=0
	global time,time_i
	while(i<48):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(ozaru_transform[i],(ox,oy))
		i+=1
		gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		pygame.display.update()
		clock.tick(0.5)


def o_attack(BG_X,ox,oy,goku_x,goku_y):
	i=0
	global time,time_i
	while(i<28):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(ozaru_attack[i],(ox,oy))
		i+=1
		gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		pygame.display.update()
		clock.tick(FPS)

def m_fight(BG_X):
	gameOver = False
	goku_x = 20
	goku_y = 555
	goku_i = 0
	goku_j = 0
	goku_xc = 0
	goku_yc = 0
	isWalking = False
	velocity = 0
	gravity = 0.8
	m = 2
	isJump = False
	onGround = True
	walk_direction = 0
	global time,time_i,G_health,fight,villain_health,villain_hit,sk_hit,l
	villain_health = 100
	fight = True
	sit = False
	m_s = 0
	mx = 750
	my = 570
	m_count = 0
	temp = random.randrange(300,500)
	pygame.mixer.music.pause()
	pygame.mixer.music.load("game_sounds/Kid - Buu.mp3")
	pygame.mixer.music.play(-1)
	while not gameOver:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					goku_xc -= 5
					walk_direction = -1
					isWalking = True	
				elif event.key == pygame.K_RIGHT:
					isWalking = True
					walk_direction = 1
					goku_xc += 5
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					sit = True
				elif event.key == pygame.K_x:
					punch(goku_x,goku_y,BG_X,mx,my)
				elif event.key == pygame.K_v:
					kick(goku_x,goku_y,BG_X,mx,my)
				elif event.key == pygame.K_f:
					specialkick(goku_x,goku_y,BG_X,mx,my)
				elif event.key == pygame.K_s:
					energybeam(goku_x,goku_y,BG_X,mx,my)
				elif event.key == pygame.K_k:
					KHH(goku_x,goku_y,BG_X)
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_SPACE and onGround == True:
					pygame.mixer.Sound.play(jumpsound)
					velocity = 8
					isJump = True
					onGround = False
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					isWalking = False
					goku_xc = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					sit = False
				if event.key == pygame.K_SPACE:
					pass
		if goku_x <= 0:
			goku_x = 0
		elif goku_x >= display_width-150:
			goku_x = display_width-150

		if goku_x+110 >= mx and goku_y+100>=my:
			fall(goku_x,goku_y,BG_X)
			goku_x -= 70

		if isJump == True:
			if velocity >= 0:
		                F = ( 0.5 * m * (velocity*velocity) )
				if goku_j <5:
					goku_j += 1
        		else:
        			F = -( 0.5 * m * (velocity*velocity) )
				if goku_j < 10:
					goku_j += 1		
			goku_y += goku_yc - F
			velocity -= 1
			if goku_y >= 555:
				goku_y = 555
		                isJump = False
		                velocity = 0
				goku_j = 0
				onGround = True

		goku_x += goku_xc
		if isWalking == True:
			if goku_i > 10:
				goku_i = 11
			else:
				goku_i += 1
		if isWalking == False:
			if goku_i < 1:
				goku_i = 0
				walk_direction = 0
			else:
				goku_i -= 1

		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))

			if BG_X <= -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width()):
				BG_X = -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width())

		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))

			if BG_X <= -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width()):
				BG_X = -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width())

		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))

			if BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width()):
				BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width())

		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))

		if BG_X <= -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width()):
			BG_X = -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width())

		if sit == True:
			gameDisplay.blit(goku_sit,(goku_x,goku_y+40))
		elif walk_direction == 1 and isJump == False:
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == False:
				gameDisplay.blit(goku_bmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == False:
				goku_i = 0
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))

		if m_s >= 90:
			m_s = 0

		if m_count >= temp:
			m_attack(BG_X,mx,my,goku_x,goku_y)
			if not goku_y+100 <= my:
				fall(goku_x,goku_y,BG_X)
				G_health -= 3
			m_count = 0
			temp = random.randrange(300,500)
		else:
			gameDisplay.blit(majin_stand[m_s],(mx,my))
		m_s += 1
		m_count += 1
		if villain_hit == True and sk_hit == True:
			villain_health -= 3
			villain_hit = False
			sk_hit = False
			goku_x = 300			
		elif villain_hit == True:
			villain_health -= 2
			villain_hit = False
			goku_x = 300

		if villain_health <= 95:
			if chi_chi_loc == time[time_i]:
				celebration()
			else:
				t_machine(BG_X,goku_x,goku_y)
				temp = time_i
				while(temp < l-1):
					time[temp] = time[temp+1]
					temp += 1					
				time.pop(l-1)
				l = len(time)
				where()

		if G_health <= 0:
			dead(goku_x,goku_y,BG_X)
			gameover()

		message = str(G_health)
		message1 = str(villain_health)
		message_to_screen(message,white,-400,-300,"large")
		message_to_screen(message1,white,400,-300,"large")
		pygame.display.update()
		clock.tick(FPS)

def m_attack(BG_X,mx,my,goku_x,goku_y):
	i=0
	global time,time_i
	while(i<26):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))

		if i<=18:
			gameDisplay.blit(majin_attack[i],(mx,my))
		else:
			gameDisplay.blit(majin_attack[17],(mx,my))
			gameDisplay.blit(majin_attack[i],(mx-(mx-goku_x)+80,my))
		i+=1
		gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		pygame.display.update()
		clock.tick(FPS)

def t_machine(BG_X,goku_x,goku_y):
	i=0
	global time,time_i
	while(i<26):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))

		if i <= 3:
			gameDisplay.blit(time_machine,(goku_x,goku_y-400))
			gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		elif i <= 6:
			gameDisplay.blit(time_machine,(goku_x,goku_y-300))
			gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		elif i <= 10:
			gameDisplay.blit(time_machine,(goku_x,goku_y-200))
			gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		elif i<= 13:
			gameDisplay.blit(time_machine,(goku_x,goku_y-100))
			gameDisplay.blit(goku_fmove[0],(goku_x,goku_y))
		elif i<= 17:
			gameDisplay.blit(time_machine,(goku_x,goku_y-300))
		elif i<= 22:
			gameDisplay.blit(time_machine,(goku_x,goku_y-400))
		elif i<= 26:
			gameDisplay.blit(time_machine,(goku_x,goku_y-500))
		i += 1
		pygame.display.update()
		clock.tick(FPS)

def celebration():
	i=0
	while(i<100):
		gameDisplay.blit(heart,(0,0))
		gameDisplay.blit(goku_fmove[0],(300,555))
		gameDisplay.blit(chichi,(450,580))
		i+=1
		pygame.display.update()
		clock.tick(FPS)
	i = 0
	pygame.mixer.music.pause()
	pygame.mixer.music.load("game_sounds/Zingaat.wav")
	pygame.mixer.music.play(-1)
	while(True):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		gameDisplay.fill(green)
		gameDisplay.blit(dance[i],(300,300))
		i+=1
		if i == 8:
			i = 0
		pygame.display.update()
		clock.tick(5)

def where():
	temp = True
	global time_i,fight
	fight = False
	while temp:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					time_i -= 1
					temp = False
					game_loop()
				elif event.key == pygame.K_RIGHT:
					if time_i == l:
						time_i = 0
					temp = False
					game_loop()
		gameDisplay.blit(forp,(0,0))
		pygame.display.update()
		clock.tick(FPS)

def gameover():
	message_to_screen("GAME OVER",white,-100,size="large")
	pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		clock.tick(5)


def pause():
	paused = True
	message_to_screen("PAUSED",white,-100,size="large")
	pygame.display.update()
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					paused = False
		clock.tick(5)

def text_objects(text,color,size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg,color,x_displace=0,y_displace=0,size="small"):
	textSurf, textRect = text_objects(msg,color,size)
#	screen_text = font.render(msg, True, color)
#	gameDisplay.blit(screen_text, [display_width/2,display_height/2])
	textRect.center = (display_width/2)+x_displace,(display_height/2)+y_displace
	gameDisplay.blit(textSurf, textRect)

def game_intro():
	i=0
	while(i<30):
		gameDisplay.blit(intro_pic,(0,0))
		pygame.display.update()
		clock.tick(5)
		i+=1
	intro = True
	gameDisplay.fill((white))
	message_to_screen("PAST? PRESENT? FUTURE?",green,0,-150,"large")
	pygame.display.update()
		
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					pygame.mixer.Sound.play(selectionsound)
					intro = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
		message_to_screen("Press C to continue or Q to quit",(random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)),0,250,"small")
		message_to_screen("Controls:",black,-300,-50,"medium")
		message_to_screen("X - punch",black,-300,0,"small")
		message_to_screen("V - kick",black,-300,50,"small")
		message_to_screen("S - energy beam",black,-300,100,"small")
		message_to_screen("F - special kick",black,-300,150,"small")
		message_to_screen("right ->",black,300,0,"small")
		message_to_screen("left  <-",black,300,50,"small")
		message_to_screen("down  \|/",black,300,100,"small")
		message_to_screen("up    /|\ ",black,300,150,"small")
		pygame.display.update()
		clock.tick(5)

def punch(goku_x,goku_y,BG_X,bx=0,by=0,e_i=0,e_e=0,e_d=0):
	i=0
	global ec,ee,eey,ed,edy,fight,villain_hit
	while(i<4):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(goku_punch[i],(goku_x,goku_y))
		i+=1
		if fight == False:
			gameDisplay.blit(enemy_cell[e_i],(ec,580))
			ec -= 5
			gameDisplay.blit(enemy_eye[e_e],(ee,eey))
			eey += 5
			if goku_x+140>=ec and goku_y>=555:
				pygame.mixer.Sound.play(blastsound)
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ec,580))
					j+=1
				ec = random.randrange(700,2500)
			if goku_x+140>=ee and goku_y <= eey+100:
				pygame.mixer.Sound.play(blastsound)
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ee,eey))
					j+=1
				ee = random.randrange(150,2000)
				eey = -100
			gameDisplay.blit(enemy_dragon[e_d],(ed,edy))
			ed -= 5
			edy -= 1
		else:
			if time[time_i] == "future":
				gameDisplay.blit(beerus_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
			elif time[time_i] == "present":
				gameDisplay.blit(frieza_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
			elif time[time_i] == "past":
				gameDisplay.blit(ozaru_stand,(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
			elif time[time_i] == "e_past":
				gameDisplay.blit(majin_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True

		pygame.display.update()
		clock.tick(FPS)


def kick(goku_x,goku_y,BG_X,bx=0,by=0,e_i=0,e_e=0,e_d=0):
	i=0
	global ec,ee,eey,ed,edy,fight,villain_hit
	while(i<6):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(goku_kick[i],(goku_x,goku_y))
		i+=1
		if fight == False:
			gameDisplay.blit(enemy_cell[e_i],(ec,580))
			ec -= 5
			if goku_x+140>=ec and goku_y>=555:
				pygame.mixer.Sound.play(blastsound)
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ec,580))
					j+=1
				ec = random.randrange(700,2500)

			gameDisplay.blit(enemy_eye[e_e],(ee,eey))
			eey += 5
		
			if goku_x+140>=ee and goku_y <= eey+100:
				pygame.mixer.Sound.play(blastsound)
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ee,eey))
					j+=1
				ee = random.randrange(150,2000)
				eey = -100
		
			gameDisplay.blit(enemy_dragon[e_d],(ed,edy))
			ed -= 5
			edy -= 1
		else:
			if time[time_i] == "future":
				gameDisplay.blit(beerus_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
			elif time[time_i] == "present":
				gameDisplay.blit(frieza_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
			elif time[time_i] == "past":
				gameDisplay.blit(ozaru_stand,(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
			elif time[time_i] == "e_past":
				gameDisplay.blit(majin_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
		pygame.display.update()
		clock.tick(FPS)

def specialkick(goku_x,goku_y,BG_X,bx=0,by=0,e_i=0,e_e=0,e_d=0):
	i=0
	global ec,ee,eey,ed,edy,fight,villain_hit,sk_hit
	global G_health
	G_health -= 2
	while(i<6):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(goku_skick[i],(goku_x,goku_y))
		i+=1
		if fight == False:
			gameDisplay.blit(enemy_cell[e_i],(ec,580))
			ec -= 5
			if goku_x+140>=ec and goku_y>=555:
				pygame.mixer.Sound.play(blastsound)
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ec,580))
					j+=1
				ec = random.randrange(700,2500)

			gameDisplay.blit(enemy_eye[e_e],(ee,eey))
			eey += 5
		
			if goku_x+140>=ee and goku_y <= eey+100:
				pygame.mixer.Sound.play(blastsound)
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ee,eey))
					j+=1
				ee = random.randrange(150,2000)
				eey = -100

			gameDisplay.blit(enemy_dragon[e_d],(ed,edy))
			ed -= 5
			edy -= 1
		else:
			if time[time_i] == "future":
				gameDisplay.blit(beerus_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
					sk_hit = True
			elif time[time_i] == "present":
				gameDisplay.blit(frieza_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
					sk_hit = True
			elif time[time_i] == "past":
				gameDisplay.blit(ozaru_stand,(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
					sk_hit = True
			elif time[time_i] == "e_past":
				gameDisplay.blit(majin_stand[0],(bx,by))
				if goku_x + 140>=bx and goku_y>=555:
					villain_hit = True
					sk_hit = True
		pygame.display.update()
		clock.tick(FPS)

def energybeam(goku_x,goku_y,BG_X,bx=0,by=0,e_i=0,e_e=0,e_d=0):
	pygame.mixer.Sound.play(beamsound)
	i=0
	global ec,ee,eey,ed,edy,fight,villain_hit
	global G_health
	G_health -= 2
	beam_i = 140
	beam_y = goku_y
	while(i<9):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(goku_ebeam[i],(goku_x,goku_y))
		i+=1
		if beam_i <= display_width:
			gameDisplay.blit(beam,(goku_x+beam_i,beam_y))
			beam_i = beam_i + goku_x + 15
		
		
		if fight == False:
			gameDisplay.blit(enemy_cell[e_i],(ec,580))
			ec -= 5
			gameDisplay.blit(enemy_eye[e_e],(ee,eey))
			eey += 5
			gameDisplay.blit(enemy_dragon[e_d],(ed,edy))
			ed -= 5
			edy -= 1

			if beam_i>=ec and beam_y>=555:
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ec,580))
					j+=1
				ec = random.randrange(700,2500)

			if beam_i>=ee and beam_y <= eey+100 and beam_y >= eey:
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ee,eey))
					j+=1
				ee = random.randrange(150,2000)
				eey = -100

			if beam_i>=ed and beam_y <= edy+200 and beam_y >= edy:
				j=0
				while(j < 15):
					gameDisplay.blit(blast[j],(ed,edy))
					j+=1
				ed= random.randrange(150,2000)
				edy = -100
		else:
			if time[time_i] == "future":
				gameDisplay.blit(beerus_stand[0],(bx,by))
			elif time[time_i] == "present":
				gameDisplay.blit(frieza_stand[0],(bx,by))
			elif time[time_i] == "past":
				gameDisplay.blit(ozaru_stand,(bx,by))
			elif time[time_i] == "e_past":
				pass
		pygame.display.update()
		clock.tick(FPS)

def fall(goku_x,goku_y,BG_X):
	i=0
	global G_health
	G_health -= 2
	while(i<18):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		if i<9:
			gameDisplay.blit(goku_fall[i],(goku_x-30,goku_y+50))
		if i<18 and i>9:
			gameDisplay.blit(goku_fall[i],(goku_x-70,goku_y+50))
		i+=1

		pygame.display.update()
		clock.tick(10)

def KHH(goku_x,goku_y,BG_X):
	pygame.mixer.Sound.play(khsound)
	i=0
	while(i<42):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(kamehameha[i],(goku_x,goku_y))
		i+=1
		pygame.display.update()
		clock.tick(2)

def dead(goku_x,goku_y,BG_X):
	i=0
	dis = 0
	while(i<50):
		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))
		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))
		gameDisplay.blit(goku_dead[i],(goku_x,goku_y+dis))
		i+=1
		if i>=21 and i<31:
			dis = 30
		elif i>=31:
			dis = 50
		pygame.display.update()
		clock.tick(15)

def game_loop():
	gameOver = False
	goku_x = 20
	goku_y = 555
	goku_i = 0
	goku_j = 0
	goku_xc = 0
	goku_yc = 0
	isWalking = False
	velocity = 0
	gravity = 0.8
	m = 2
	isJump = False
	onGround = True
	walk_direction = 0
	BG_X = 0
	BG_Y = 0
	BG_C = 0
	global ec,ee,eey,ed,edy,time,time_i,G_health
	ec = random.randrange(700,2500)
	e_i = 0
	ee = random.randrange(150,700)
	eey = -100
	e_e = 0
	ee_c = 0
	ed = random.randrange(700,2500)
	edy = 0
	e_d = 0
	bean_x = random.randrange(2000,3000)
	bean_y = 450
	bean_c = 0
	caught = False
	sit = False
	pygame.mixer.music.pause()
	if time[time_i] == "space":
		pygame.mixer.music.load("game_sounds/space.mp3")
		pygame.mixer.music.play(-1)
	elif time[time_i] == "e_past":
		pygame.mixer.music.load("game_sounds/e_past.wav")
		pygame.mixer.music.play(-1)
	elif time[time_i] == "past":
		pygame.mixer.music.load("game_sounds/dabura.mp3")
		pygame.mixer.music.play(-1)
	elif time[time_i] == "present":
		pygame.mixer.music.load("game_sounds/present.wav")
		pygame.mixer.music.play(-1)
	elif time[time_i] == "future":
		pygame.mixer.music.load("game_sounds/Were - The.mp3")
		pygame.mixer.music.play(-1)

	while not gameOver:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					goku_xc -= 5
					walk_direction = -1
					isWalking = True	
				elif event.key == pygame.K_RIGHT:
					isWalking = True
					walk_direction = 1
					goku_xc += 5
					BG_C -= 5
					ee_c -= 5
					bean_c -= 5
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					sit = True
				elif event.key == pygame.K_x:
					punch(goku_x,goku_y,BG_X,0,0,e_i,e_e,e_d)
				elif event.key == pygame.K_v:
					kick(goku_x,goku_y,BG_X,0,0,e_i,e_e,e_d)
				elif event.key == pygame.K_f:
					specialkick(goku_x,goku_y,BG_X,0,0,e_i,e_e,e_d)
				elif event.key == pygame.K_s:
					energybeam(goku_x,goku_y,BG_X,0,0,e_i,e_e,e_d)
				elif event.key == pygame.K_k:
					KHH(goku_x,goku_y,BG_X)
				elif event.key == pygame.K_p:
					pause()
				elif event.key == pygame.K_SPACE and onGround == True:
					pygame.mixer.Sound.play(jumpsound)
					velocity = 8
					isJump = True
					onGround = False
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					isWalking = False
					goku_xc = 0
					BG_C = 0
					ee_c = 0
					bean_c = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					sit = False
				if event.key == pygame.K_SPACE:
					pass

		if goku_x >= display_width/4:
			BG_X += BG_C
			bean_x += bean_c
			ee += ee_c
			goku_x = display_width/4
		elif goku_x <= 0:
			goku_x = 0

		if isJump == True:
			if velocity >= 0:
		                F = ( 0.5 * m * (velocity*velocity) )
				if goku_j <5:
					goku_j += 1
        		else:
        			F = -( 0.5 * m * (velocity*velocity) )
				if goku_j < 10:
					goku_j += 1		
			goku_y += goku_yc - F
			velocity -= 1
			if goku_y >= 555:
				goku_y = 555
		                isJump = False
		                velocity = 0
				goku_j = 0
				onGround = True

		goku_x += goku_xc
		if isWalking == True:
			if goku_i > 10:
				goku_i = 11
			else:
				goku_i += 1
		if isWalking == False:
			if goku_i < 1:
				goku_i = 0
				walk_direction = 0
			else:
				goku_i -= 1

		if time[time_i] == "space":
			gameDisplay.blit(space,(0,0))
			dead(goku_x,goku_y,BG_X)
			gameover()
		elif time[time_i] == "e_past":
			gameDisplay.blit(extremepast,(BG_X,0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width(),0))
			gameDisplay.blit(extremepast1,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width(),0))
			gameDisplay.blit(extremepast2,(BG_X+extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width(),0))

			if BG_X <= -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width()):
				BG_X = -(extremepast2.get_width()+extremepast.get_width()+extremepast1.get_width()+extremepast.get_width()+extremepast1.get_width())
				m_fight(BG_X)

		elif time[time_i] == "past":
			gameDisplay.blit(past,(BG_X,0))
			gameDisplay.blit(past1,(BG_X+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past,(BG_X+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past1,(BG_X+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))
			gameDisplay.blit(past2,(BG_X+past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width(),0))

			if BG_X <= -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width()):
				BG_X = -(past1.get_width()+past.get_width()+past2.get_width()+past1.get_width()+past.get_width())
				o_fight(BG_X)

		elif time[time_i] == "present":
			gameDisplay.blit(present,(BG_X,0))
			gameDisplay.blit(present1,(BG_X+present.get_width(),0))
			gameDisplay.blit(present2,(BG_X+present.get_width()+present1.get_width(),0))
			gameDisplay.blit(present3,(BG_X+present.get_width()+present1.get_width()+present2.get_width(),0))
			gameDisplay.blit(present4,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width(),0))
			gameDisplay.blit(present5,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width(),0))
			gameDisplay.blit(present6,(BG_X+present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width(),0))

			if BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width()):
				BG_X <= -(present.get_width()+present1.get_width()+present2.get_width()+present3.get_width()+present4.get_width()+present5.get_width())
				f_fight(BG_X)

		elif time[time_i] == "future":
			gameDisplay.blit(future,(BG_X,0))
			gameDisplay.blit(future1,(BG_X+future.get_width(),0))
			gameDisplay.blit(future2,(BG_X+future.get_width()+future1.get_width(),0))
			gameDisplay.blit(future3,(BG_X+future.get_width()+future1.get_width()+future2.get_width(),0))
			gameDisplay.blit(future4,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width(),0))
			gameDisplay.blit(future5,(BG_X+future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width(),0))

			if BG_X <= -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width()):
				BG_X = -(future.get_width()+future1.get_width()+future2.get_width()+future3.get_width()+future4.get_width())
				b_fight(BG_X)

		if sit == True:
			gameDisplay.blit(goku_sit,(goku_x,goku_y+40))
		elif walk_direction == 1 and isJump == False:
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == False:
				gameDisplay.blit(goku_bmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == False:
				goku_i = 0
				gameDisplay.blit(goku_fmove[goku_i],(goku_x,goku_y))
		elif walk_direction == 1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == -1 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))
		elif walk_direction == 0 and isJump == True and onGround == False:
				gameDisplay.blit(goku_jump[goku_j],(goku_x,goku_y))

		if goku_x<= ec and goku_x+100>= ec and goku_y >= 555:
			fall(goku_x,goku_y,BG_X)
			goku_x -= 70
			ec = random.randrange(700,2500)
		elif ec <= 0:
			ec = random.randrange(700,2500)
		else:
			gameDisplay.blit(enemy_cell[e_i],(ec,580))
			if e_i>6:
				e_i = -1
			e_i += 1
			ec -= 5

		if goku_x<=ee and goku_x+100>=ee and eey+100>=goku_y or goku_x>=ee and ee+100>=goku_x and eey+100>=goku_y:
			fall(goku_x,goku_y,BG_X)
			goku_x -= 70
			ee = random.randrange(150,2000)
			eey = -100
		elif eey >= display_height:
			ee = random.randrange(150,2000)
			eey = -100
		else:
			gameDisplay.blit(enemy_eye[e_e],(ee,eey))
			if e_e>4:
				e_e = -1
			e_e += 1
			eey += 5

		if goku_x<=ed and goku_x+100>=ed and goku_y<=edy+150 or goku_x>=ed and goku_x <= ed+150 and goku_y<= edy+150 or goku_x <= ed+150 and goku_x+100 >= ed+150 and goku_y<=edy+150:
			fall(goku_x,goku_y,BG_X)
			goku_x -= 70
			ed = random.randrange(700,2500)
			edy = 0
		elif edy >= display_height:
			ed = random.randrange(700,2500)
			edy = 0
		else:
			gameDisplay.blit(enemy_dragon[e_d],(ed,edy))
			if e_d>14:
				e_d = -1
			e_d += 1
			ed -= 5
			edy += 1

		if caught == False:
			gameDisplay.blit(bean,(bean_x,bean_y))
		if goku_x >= bean_x and goku_x <= bean_x+60 and goku_y <= bean_y+60 and goku_y >= bean_y or goku_x+100>=bean_x and goku_x+100<=bean_x+60 and goku_y <= bean_y+60 and goku_y >= bean_y:
			pygame.mixer.Sound.play(selectionsound)
			G_health = 100
			caught = True

		message = str(G_health)
		message_to_screen(message,white,-400,-300,"large")
		if G_health <= 0:
			dead(goku_x,goku_y,BG_X)
			gameover()
		pygame.display.update()
		clock.tick(FPS)

game_intro()
game_loop()
