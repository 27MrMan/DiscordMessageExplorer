#for GUI
import pygame
#for charts
import matplotlib
matplotlib.use('module://pygame_matplotlib.backend_pygame')
import matplotlib.pyplot as plt
#for proper text input design
import time
#for reading the csv of messages
import pandas
#for checking if something is present in a message
import re

#window setup
pygame.init()
width,height = 1000,650
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Discord Message Explorer")

#variables
timing_thing = 0
input_area = pygame.Rect(50, 100, 900, 39)
user_text = ''
current_menu = "Start"
current_tab = "landing"
mousedown = False
active = True
calculated = False
#gotta make this configurable
filelocation = "C:/Users/UNNIKRISHNAN/Documents/AI Traiing Data/GC_Dec_2024.csv"
data = ''
#discord purple
purple = (88,101,242)
contentlist = []
authorlist = []
listofauthors = []
listofauthorscount = []

#List of Interesting Things
lt = []


#functions
def draw_shadow(surface, color, rect, borderradius):
    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=borderradius)
    surface.blit(shape_surf, rect)

def draw_tab(position, borderradius, text):
    tab_rect = pygame.draw.rect(screen, (48, 51, 57), (position, 20, 120, 70), border_radius=borderradius)
    if tab_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(screen, (45, 48, 53), (position, 20, 120, 70), border_radius=borderradius)
    tab_text = pygame.font.Font('assets/Ubuntu-Bold.ttf', 35).render(text, True, (250, 250, 250))
    screen.blit(tab_text, (position+9, 25, 120, 70 ))
    pygame.draw.rect(screen, purple, (position, 20, 120, 70), 2, borderradius)
    global current_tab

    if mousedown:
        if tab_rect.collidepoint(pygame.mouse.get_pos()):
            current_tab = text

def word_in_text(word, text):
    pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
    pattern = re.compile(pattern, re.IGNORECASE)
    matches = re.search(pattern, text)

    return bool(matches)

#main loop
running = True
while running:
    #timekeeping. (shutup idk how to do this better)
    timing_thing += 1
    if timing_thing >60:
        timing_thing = 0

    if current_menu == "Start":
        #discord background color :P
        screen.fill((53,56,63))

        start_button_rect = pygame.draw.rect(screen, (100,100,100), (300, 450, 400, 100 ), border_radius=7)
        if start_button_rect.collidepoint(pygame.mouse.get_pos()):
            draw_shadow(screen, (20, 20, 20, 100), (303, 453, 400, 100), borderradius=7)
            pygame.draw.rect(screen, (35,35,35), (300, 450, 400, 100 ), border_radius=7)
        else:
            draw_shadow(screen, (20, 20, 20, 100), (305, 455, 400, 100), borderradius=7)
            pygame.draw.rect(screen, (40,40,40), (300, 450, 400, 100 ), border_radius=7)
        pygame.draw.rect(screen, purple, (300, 450, 400, 100 ), 2, 7)

        startbutton_text = pygame.font.Font('assets/Ubuntu-Medium.ttf', 90).render("Continue", True, (52,50,201))
        screen.blit(startbutton_text, (309, 450, 400, 100))

        title_text = pygame.font.Font('assets/Ubuntu-Medium.ttf', 75).render("Discord Message Explorer", True, (250,250,250))
        title_text_rect = title_text.get_rect(center=(500, 80))
        screen.blit(title_text, title_text_rect)
                
        # Handle main menu button clicks
        if start_button_rect.collidepoint(pygame.mouse.get_pos()) and mousedown:
            current_menu = "ResultsPage"

    if current_menu == "ResultsPage":
        screen.fill((53,56,63))

        topbar_rect = pygame.draw.rect(screen, (47, 50, 56), (0, 0, 1000, 70))
        draw_tab(10, 9, 'Words')
        draw_tab(140, 9, 'Users')
        backgroundfill = pygame.draw.rect(screen, (53, 56, 63), (0, 70, 1000, 600))
        pygame.draw.line(screen, purple, (0, 70), (1000, 70), width=2)

        if current_tab == 'landing':
            pass
        
        if current_tab == 'Words':
            pygame.draw.rect(screen, (47,50,56), input_area, border_radius=3)
            pygame.draw.rect(screen, (23, 26, 28), input_area, 2, 3)

            if round(time.time())%2==0 and active:
                text_surface = pygame.font.Font('assets/Ubuntu-Medium.ttf', 35).render(user_text + "", True, (255, 215, 0))
            elif round(time.time())%2!=0 and active:
                text_surface = pygame.font.Font('assets/Ubuntu-Medium.ttf', 35).render(user_text + "|", True, (255, 215, 0))
            else:
                text_surface = pygame.font.Font('assets/Ubuntu-Medium.ttf', 35).render(user_text + "", True, (255, 215, 0))

            screen.blit(text_surface, (input_area.x + 5, input_area.y - 1))
            # for long(er) answers
            input_area.w = max(max(100, text_surface.get_width() + 10),900)

            if mousedown:
                if input_area.collidepoint(pygame.mouse.get_pos()):
                    active = True

            if not(active):
                if not(calculated):
                    data = pandas.read_csv(filelocation)
                    for i in data['Content']:
                        contentlist.append(i)
                    for j in data['Author']:
                        if not(j in listofauthors):
                            listofauthors.append(j)
                            listofauthorscount.append(0)
                        authorlist.append(j)
                    calculated = True
                    for k in contentlist:
                        if word_in_text(user_text, str(k)):
                            #be careful trying to understand this
                            listofauthorscount[listofauthors.index(authorlist[contentlist.index(k)])] += 1
                    print(listofauthors)
                    print(listofauthorscount)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                # Check for backspace when user has room temperature IQ (in Fahrenheit)
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    active = False
                else:
                    user_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousedown = True
            if event.type == pygame.MOUSEBUTTONUP:
                mousedown = False

    #run every frame                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
            
    pygame.display.update()
#    print(timing_thing)
pygame.quit()