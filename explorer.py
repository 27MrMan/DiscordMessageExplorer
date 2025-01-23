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
#for finding the most used word
from collections import Counter
from functools import reduce

#window setup
pygame.init()
width,height = 1000,650
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Discord Message Explorer")

#variables
start_time = 0
timing_thing = 0
input_area = pygame.Rect(50, 100, 900, 39)
user_text = ''
current_menu = "Start"
current_current_tab = ''
current_tab = "landing"
mousedown = False
active = True
calculated = False
recentToggle = 0
#for checking if each checkbox has been clicked.
toggled_checkboxes = [False, False, False]
#gotta make this configurable
filelocation = "C:/Users/UNNIKRISHNAN/Documents/AI Traiing Data/GC_Dec_2024.csv"
data = ''
#discord purple
purple = (88,101,242)
contentlist = []
authorlist = []
messagecount = []
listofauthors = []
listofauthorscount = []
authorlisthelper = {}
newauthorlisthelper = {}

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
    pygame.draw.rect(screen, purple, (position, 20, 1200, 70), 2, borderradius)
    global current_tab

    if mousedown:
        if tab_rect.collidepoint(pygame.mouse.get_pos()):
            current_tab = text

def word_in_text(word, text):
    pattern = r'(^|[^\w]){}([^\w]|$)'.format(word)
    pattern = re.compile(pattern, re.IGNORECASE)
    matches = re.search(pattern, text)

    return bool(matches)

def most_frequent_word(list):
    all_words = reduce(lambda a, b: a + b, [sub.split() for sub in list])
    word_counts = Counter(all_words)
    return word_counts.most_common(7)

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
        draw_tab(270, 9, 'Messages')
        backgroundfill = pygame.draw.rect(screen, (53, 56, 63), (0, 70, 1000, 600))
        pygame.draw.line(screen, purple, (0, 70), (1000, 70), width=2)

        if current_tab == 'landing':
            pass

        if current_tab == 'Messages':
            if toggled_checkboxes[2] == False:
                checkbox3=pygame.draw.rect(screen, (47, 50, 56), (45, 100, 910, 30), border_radius=3)
            else: 
                checkbox3=pygame.draw.rect(screen, purple, (45, 100, 910, 30), border_radius=3)
            pygame.draw.rect(screen, (23, 26, 28), (45, 100, 910, 30), 2, 3)

            checkbox3_text = pygame.font.Font('assets/Ubuntu-Light.ttf', 20).render("Find the most used word                                                           (click here)", True, (250, 250, 250))
            screen.blit(checkbox3_text, (60, 102, 910, 30))

            if checkbox3.collidepoint(pygame.mouse.get_pos()) and mousedown and round(time.time(), 2)-recentToggle > 0.3:
                recentToggle = round(time.time(), 2)
                toggled_checkboxes[2]=not(toggled_checkboxes[2])
                active = False
                calculated= False

            if not(active):
                if not(calculated):
                    contentlist = []
                    wordlist = []
                    wordcount = []
                    start_time = time.time()

                    calculated = True
                    print(user_text)
                    data = pandas.read_csv(filelocation)

                    for i in data['Content']:
                        contentlist.append(str(i))

                    output1 = most_frequent_word(contentlist[:1000])
                    print(output1)

                    for i in output1:
                        wordlist.append(i[0])
                        wordcount.append(i[1])

                    calculated = True
                    print("Calculated in ", round(time.time()-start_time, 3), "seconds!")

                    fig, axes = plt.subplots(1, 1)
                    axes.bar(wordlist, wordcount, color='green', label='Chart')

                    plt.title("Most Used Word", fontsize=20 )
                    plt.xticks(fontsize = 10)
                    for tick in axes.xaxis.get_major_ticks()[1::2]:
                        tick.set_pad(15)


                    fig.patch.set_facecolor('#41454D')
                    axes.set_facecolor('#35383E')
                    fig.canvas.draw()

                screen.blit(fig, (175, 150))
        
        if current_tab == 'Words':
            pygame.draw.rect(screen, (47,50,56), input_area, border_radius=3)
            pygame.draw.rect(screen, (23, 26, 28), input_area, 2, 3)

            if toggled_checkboxes[0] == False:
                checkbox1=pygame.draw.rect(screen, (47, 50, 56), (45, 200, 30, 30), border_radius=3)
            else: 
                checkbox1=pygame.draw.rect(screen, purple, (45, 200, 30, 30), border_radius=3)
            pygame.draw.rect(screen, (23, 26, 28), (45, 200, 30, 30), 2, 3)

            checkbox1_text = pygame.font.Font('assets/Ubuntu-Light.ttf', 20).render("Normalize\n Plot", True, (250, 250, 250))
            screen.blit(checkbox1_text, (80, 200, 30, 30))

            if checkbox1.collidepoint(pygame.mouse.get_pos()) and mousedown and round(time.time(), 2)-recentToggle > 0.3:
                recentToggle = round(time.time(), 2)
                toggled_checkboxes[0] = not(toggled_checkboxes[0])

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
                    #if user wants to see more than one plot
                    contentlist = []
                    authorlist = []
                    listofauthors = []
                    listofauthorscount = []
                    messagecount = []
                    authorlisthelper = {}
                    newauthorlisthelper = {}
                    start_time = time.time()

                    calculated = True
                    print(user_text)
                    data = pandas.read_csv(filelocation)

                    for i in data['Content']:
                        contentlist.append(i)
                    for j in data['Author']:
                        if not(j in listofauthors):
                            listofauthors.append(j)
                            listofauthorscount.append(0)
                        authorlist.append(j)
                    for k in contentlist:
                        if word_in_text(user_text, str(k)):
                            #be careful trying to understand this
                            listofauthorscount[listofauthors.index(authorlist[contentlist.index(k)])] += 1

                    for i in range(len(listofauthors)):
                        authorlisthelper.update({listofauthors[i]:listofauthorscount[i]})

                    for j in authorlisthelper.keys():
                        if authorlisthelper[j] != 0 or len(listofauthors) < 5:
                            newauthorlisthelper.update({j:authorlisthelper[j]})
                    
                    start_time = time.time()-start_time

                    print("Finished calculation of","{:,}".format(len(authorlist)), "messages in", round(start_time, 3), "seconds!")
                    print(newauthorlisthelper)
                            
                    listofauthors = list(newauthorlisthelper.keys())
                    listofauthorscount = list(newauthorlisthelper.values())

                    for i in range(len(listofauthors)):
                        messagecount.append(0)
                    for i in authorlist:
                        if i in listofauthors:
                            messagecount[listofauthors.index(i)] += 1

                    print(messagecount)

                    if toggled_checkboxes[0]:
                        for i in range(len(listofauthorscount)):
                            listofauthorscount[i] /= messagecount[i]
                            listofauthorscount[i] *= 100

                    fig, axes = plt.subplots(1, 1)
                    axes.bar(listofauthors, listofauthorscount, color='green', label='Chart')

                    plt.title("Times used: "+user_text, fontsize=20 )
                    plt.xticks(fontsize = 10)
                    for tick in axes.xaxis.get_major_ticks()[1::2]:
                        tick.set_pad(15)


                    fig.patch.set_facecolor('#41454D')
                    axes.set_facecolor('#35383E')
                    fig.canvas.draw()

                screen.blit(fig, (175, 150))

        if current_tab == 'Users':
            if toggled_checkboxes[1] == False:
                checkbox2=pygame.draw.rect(screen, (47, 50, 56), (45, 100, 910, 30), border_radius=3)
            else: 
                checkbox2=pygame.draw.rect(screen, purple, (45, 100, 910, 30), border_radius=3)
            pygame.draw.rect(screen, (23, 26, 28), (45, 100, 910, 30), 2, 3)

            checkbox2_text = pygame.font.Font('assets/Ubuntu-Light.ttf', 20).render("Calculate & Display                                                                   (click here)", True, (250, 250, 250))
            screen.blit(checkbox2_text, (60, 102, 910, 30))

            if checkbox2.collidepoint(pygame.mouse.get_pos()) and mousedown and round(time.time(), 2)-recentToggle > 0.3:
                recentToggle = round(time.time(), 2)
                toggled_checkboxes[1]=not(toggled_checkboxes[1])
                active = False
                calculated= False

            if not(active):
                if not(calculated):
                    #if user wants to see more than one plot
                    contentlist = []
                    authorlist = []
                    listofauthors = []
                    listofauthorscount = []
                    messagecount = []
                    authorlisthelper = {}
                    newauthorlisthelper = {}
                    start_time = time.time()

                    calculated = True
                    print(user_text)
                    data = pandas.read_csv(filelocation)


                    for j in data['Author']:
                        if not(j in listofauthors):
                            listofauthors.append(j)
                            listofauthorscount.append(0)
                        authorlist.append(j)

                    for k in authorlist:
                        listofauthorscount[listofauthors.index(k)] += 1

                    fig, axes = plt.subplots(1, 1)
                    axes.bar(listofauthors, listofauthorscount, color='green', label='Chart')

                    plt.title("Messages Sent", fontsize=20 )
                    plt.xticks(fontsize = 10)
                    for tick in axes.xaxis.get_major_ticks()[1::2]:
                        tick.set_pad(15)


                    fig.patch.set_facecolor('#41454D')
                    axes.set_facecolor('#35383E')
                    fig.canvas.draw()

                screen.blit(fig, (175, 150))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            if event.type == pygame.KEYDOWN:
                # Check for backspace when user has room temperature IQ (in Fahrenheit)
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif event.key == pygame.K_RETURN:
                    active = False
                    calculated = False
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