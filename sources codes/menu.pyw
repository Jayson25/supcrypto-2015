import pygame, pygame.font, sys, time, os
from pygame.locals import *

os.environ['SDL_VIDEO_CENTERED'] = '1'      #centers the display.

clock = pygame.time.Clock() #initiate a clock.
pygame.init()
menu = pygame.image.load('menu.png')
menu2 = pygame.image.load('menu2.png')
size = [(menu.get_width()), (menu.get_height())]
effect = pygame.image.load('eff.png')
rect = [(effect.subsurface(57, 148, 171, 209)), (effect.subsurface(307, 148, 171, 209)),(effect.subsurface(557, 148, 171, 209)), (effect.subsurface(704, 0, 30, 30)), (effect.subsurface(752, 0, 30, 30))]
screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME) #pygame.NOFRAME: removes border and controls of the window.
                
def premiere_image(): #select an image popup.
    import win32ui
    open = win32ui.CreateFileDialog(1, ".bmp","", 0, "BMP files (*.bmp) |*.bmp|All files(*.*)|*.*|")
    open.DoModal()
    image1 = open.GetPathName()   
    return image1

def deuxieme_image():
    import win32ui
    open = win32ui.CreateFileDialog(1, ".bmp", "", 0, "BMP files (*.bmp) |*.bmp|All Files(*.*)|*.*|")
    open.DoModal()
    image2 = open.GetPathName()
    return image2

def key():
    global number #globalize a variable(s) of a procedure.
    number = ""
    x = 44
    key = pygame.image.load('k.png')
    k_eff = (pygame.image.load('k_eff.png')).subsurface(321, 347, 145, 55)
    processing = True
    
    while processing:
        
        if x != 0: #animation effect.
            screen.blit(menu2, (0,0))
            screen.blit(key, (x, 0))
            x -= 4
            
        font = pygame.font.Font(None,40) #initialize text. 
        texte = font.render(number, True, (0,0,0)) #use the number text with anti aliasing at colour black.
        cadre = texte.get_rect() #initialize surface of the text.
        cadre.topleft = (225, 240) #coordinate of this surface in the display.
            
        pos = pygame.mouse.get_pos() #gets the position of the cursor.
        
        if len(number) > 21:     #21 because it is the number of char that fits in the rectangle design.
            number = number[:-1] #deletes last element.
            
        for event in pygame.event.get():    #waiting for an event.
            if pygame.mouse.get_pressed():  #checks the current state of the mouse (here we use this for the position of the mouse). 
                if 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30:  #we determine the zone of collision in x, y position. Here is for reduce button.
                    screen.blit(menu2, (0,0)) #superposition of sprites. Order is very important (from background to foreground).
                    screen.blit(key, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(rect[3], (704,0))
                
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #for close button.
                    screen.blit(menu2, (0,0))
                    screen.blit(key, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(rect[4],(752,0))
                
                elif 321 <= pos[0] <= 466 and 347<= pos[1] <= 402:  #for start button.
                    screen.blit(menu2, (0,0))
                    screen.blit(key, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(k_eff, (321, 347))
                    
                else:                           #to remove button effects.
                    screen.blit(menu2, (0,0))
                    screen.blit(key, (0,0))
                    screen.blit(texte, cadre)
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1: #if the mouse was left clicked.
                
                if 752 <= pos[0] <= 782 and 0<= pos[1] <= 30:   #for close button.
                    import win32api
                    result = win32api.MessageBox(0,"Are you sure?","",1) #message box pop-up (note: requires to download python for windows extensions).
                    if result==1:
                        processing = False #closes the program.
                    
                    elif result==2:
                        processing==True #keeps the program open. 
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #for reduce button.
                    pygame.display.iconify()                    #reduces the window.
                
                elif 321 <= pos[0] <= 466 and 347<= pos[1] <= 402:  #for start button.
                    if number == "":                                #if the string is empty.
                        print("\a")
                    else:
                        processing = False                          #closes the sub program for memory saving.
                        chargement()                                #redirect to another sub program.
                    
            if event.type == KEYDOWN:   #if the key of the keyboard is clicked.
                if event.key == K_0:    #assign value on each key.
                    number += "0"
                elif event.key == K_KP0:
                    number += "0"
                elif event.key == K_1:
                    number += "1"
                elif event.key == K_KP1:
                    number += "1"
                elif event.key == K_2:
                    number += "2"
                elif event.key == K_KP2:
                    number += "2"
                elif event.key == K_3:
                    number += "3"
                elif event.key == K_KP3:
                    number += "3"
                elif event.key == K_4:
                    number += "4"
                elif event.key == K_KP4:
                    number += "4"
                elif event.key == K_5:
                    number += "5"
                elif event.key == K_KP5:
                    number += "5"
                elif event.key == K_6:
                    number += "6"
                elif event.key == K_KP6:
                    number += "6"
                elif event.key == K_7:
                    number += "7"
                elif event.key == K_KP7:
                    number += "7"
                elif event.key == K_8:
                    number += "8"
                elif event.key == K_KP8:
                    number += "8"
                elif event.key == K_9:
                    number += "9"
                elif event.key == K_KP9:
                    number += "9"
                elif event.key == K_BACKSPACE:
                    if number == "":
                        print("\a")
                    else:
                        number = number[:-1]
                        
                elif event.key == K_RETURN:
                    if number == "":
                        print("\a")
                    else:
                        chargement()
                
                elif event.unicode.isalpha(): #event.unicode.isalpha() is an event when the user tap on alphabetic keys (a, A, é, à, ç for example).
                    print("\a")
        pygame.display.flip()    
        clock.tick(30)  #lock the refresh speed at 30FPS.
        

        
def chargement():
    second = 0 #initiate time counter.
    charge = pygame.image.load('chargement.png')
    screen.blit(menu2, (0,0))
    screen.blit(charge, (0,0))
    pygame.time.set_timer(USEREVENT + 1, 1000) #get the time within 1000ms.
    
    while True:
        for event in pygame.event.get():
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                if 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #for close button.
                    import win32api
                    result = win32api.MessageBox(0,"Are you sure?","",1)
                    if result == 1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #for reduce button.
                    pygame.display.iconify()

            if event.type == USEREVENT + 1: #the clock > 1000ms.
                second += 1 #counter up.
            
            if second == 3:
                if use == 1: #for encrypt in XOR.
                    processing = False
                    from chiffrementImages import chiff_image
                    
                    image_1 = pygame.image.load(image1)  #use an image into a variable.
                    dim_img1 = [(image_1.get_width()),(image_1.get_height())] #gets the dimensions of the image. 

                    image_2 = pygame.image.load(image2)
                    dim_img2 = [(image_2.get_width()),(image_2.get_height())]
                    
                    chiff_image(dim_img1[0], dim_img1[1], image_1, image_2, "image_(de)crypte_exclusif.bmp")
                
                elif use == 2:  #for encrypt with an equation mentioned in the set of specifications.
                    processing = False
                    from masquageImages import procedure
                    image_1 = pygame.image.load(image1)
                    dim_img1 = [(image_1.get_width()),(image_1.get_height())]

                    image_2 = pygame.image.load(image2)
                    dim_img2 = [(image_2.get_width()),(image_2.get_height())]
                    
                    procedure(dim_img1[0],dim_img1[1],image_1,image_2,"image_crypte.bmp",int(number),1)
                
                elif use == 3: #for decryption with an equation mentioned in the set of specifications.
                    processing = False
                    from masquageImages import procedure
                    image_1 = pygame.image.load(image1)
                    dim_img1 = [(image_1.get_width()),(image_1.get_height())]

                    image_2 = pygame.image.load(image2)
                    dim_img2 = [(image_2.get_width()),(image_2.get_height())]
                    
                    procedure(dim_img1[0],dim_img1[1],image_1,image_2,"image_decrypte.bmp",int(number),0)
                
                elif use == 4:  #for hiding a text inside an image that already exists.
                    processing = False
                    from masquageTextes import masquage
                                
                    image_1 = pygame.image.load(image1)
                    dim_img1 = [(image_1.get_width()),(image_1.get_height())]
                            
                    masquage(dim_img1[0], dim_img1[1], image_1, 'imageTexte.bmp', recit)
                
                elif use == 5: #for reading the hidden text inside the image selected.
                    processing = False
                    aff_lecture()
                
                elif use == 6:  #for hiding a text inside an image generated by the web cam (or other similar device).
                    processing = False
                    from masquageTextes import masquage
                                
                    web = pygame.image.load("image_web.bmp")    
                    dim_web = [(web.get_width()),(web.get_height())]
                            
                    masquage(dim_web[0], dim_web[1], web, 'imageTexte.bmp', recit)
                    
        pygame.display.flip()   #update the window.
        clock.tick(30)
        
def camera():
    import pygame.camera, win32api
    global ec #ec: used for identification.
    
    pygame.init()
    pygame.camera.init()

    try:
        
        x, y = (1920, 1080) #resolution of the web cam, which it will be fixed in other versions.
        
        list = pygame.camera.list_cameras() #creates a list of available cameras.

        if list:
            cam = pygame.camera.Camera(list[0], (x, y)) #takes the first camera (by default).
            disp = pygame.display.set_mode((x, y)) 
            
                
        cam.start() #start recording.
        
        pygame.time.set_timer(USEREVENT + 1, 1000)
        second = 0
        processing = True
    
    except : #if the program does not detects a camera.
       
        mes = win32api.MessageBox(0,"Sorry, no camera 1080p detected!","", 0)
        
        if retourne == 1:   #if the program was launch from the XOR menu
            menu_exclusif() 
            
        elif retourne == 2: #if the program was launch from the equation menu
            menu_equation()
            
        elif retourne == 3:  #if the program was launch from the text menu
            menu_texte()
            
    while processing: 
        image = cam.get_image() #captures images and pastes on the surface (effect of motion picture).
           
        font = pygame.font.Font(None,45)
        texte = font.render("APPUYEZ SUR LE BOUTON FERMER (X) POUR CAPTURER L'IMAGE!", True, (0,0,0), (255, 255, 255))
        cadre = texte.get_rect()
        cadre.topleft = (30, 20)        
            
        if second <= 2: #if the time is over 2 seconds, removes text.
            disp.blit(image, (0,0)) 
            disp.blit(texte, cadre)
                
        else:   
            disp.blit(image, (0,0))
                
        for event in pygame.event.get():
                
            if event.type == USEREVENT + 1:
                second += 1
                
            elif event.type == QUIT: #windows close button.
                
                box = win32api.MessageBox(0,"Do you want to capture?","", 1)
                
                if box == 1: #if ok.
                    mes = win32api.MessageBox(0,"capture done","", 0)   
                    pygame.image.save(disp, "image_web.bmp")
                        
                    web = pygame.image.load("image_web.bmp")
                    dim_web = [(web.get_width()),(web.get_height())]
                        
                    if gen == 1:    #corresponds to XOR.
                        cam.stop()
                        processing = False
                        from chiffrementImages import ale_image
                        ale_image(dim_web[0], dim_web[1], "cle_exclusif.bmp")
                            
                    elif gen == 2:  #corresponds to the equation technique.
                        processing = False
                        filtre = pygame.display.set_mode((dim_web[0], dim_web[1])) #surface that will be convert into an image key.
                                
                        print("\a")
                                
                        box2 = win32api.MessageBox(0,"Do you want to save the key filter?","", 1) #asks if you want to key the image key.
                        if box2 == 1: #ok.
                            pygame.image.save(filtre, "cle_equation.bmp")
                            processing = False
                            os.environ['SDL_VIDEO_CENTERED'] = '1'
                            screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME)
                            menu_principal()
                            
                        elif box2 == 2: #cancel.
                            processing = False
                            os.environ['SDL_VIDEO_CENTERED'] = '1'
                            screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME)
                            menu_principal()
                        
                    elif gen == 3:  #corresponds to the hidden text technique.
                        processing = False
                        ec = 2
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                        screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME)
                        aff_ecrire()
                            
                elif box == 2: #cancel.
                    close = win32api.MessageBox(0,"do you want to quit?","", 1)
                    if close == 1: #ok
                        procedure = False
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                        screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME)
                        menu_principal()
                            
        pygame.display.flip()    
        clock.tick(60)       
        
def affichage_exclusif(): #XOR menu images. calls one time an image in order to use less memory.
    global choix, effect2, rect2
    choix = pygame.image.load('ou_exlusif.png')
    effect2 = pygame.image.load('effect_ex.png')
    rect2 =[(effect2.subsurface(10, 77, 63, 59)), (effect2.subsurface(84, 159, 293, 45)), (effect2.subsurface(424, 159, 293, 45)), (effect2.subsurface(132, 247, 161, 7)), (effect2.subsurface(132, 279, 161, 7)), (effect2.subsurface(432, 247, 241, 7))]
    menu_exclusif()

def affichage_eq(): #Equation menu images.
    global choix2, effect3, rect3
    choix2 = pygame.image.load('menu_eq.png')
    effect3 = pygame.image.load('menu_eq_ex.png')
    rect3 =[(effect3.subsurface(10, 77, 63, 59)), (effect3.subsurface(84, 159, 293, 45)), (effect3.subsurface(424, 159, 293, 45)), (effect3.subsurface(132, 247, 161, 7)), (effect3.subsurface(132, 279, 161, 7)), (effect3.subsurface(432, 247, 241, 7)), (effect3.subsurface(428, 281, 243, 7))]
    menu_equation()
    
def aff_texte():    #Text menu images.
    global choix3, effect4, rect4
    choix3 = pygame.image.load('crypto_texte.png')
    effect4 = pygame.image.load('crypto_texte_eff.png')
    rect4 = rect2 =[(effect4.subsurface(10, 77, 63, 59)), (effect4.subsurface(84, 159, 293, 45)), (effect4.subsurface(424, 159, 293, 45)), (effect4.subsurface(132, 247, 161, 7)), (effect4.subsurface(132, 279, 161, 7)), (effect4.subsurface(432, 247, 241, 7))]
    menu_texte()
    
def aff_browser():  #choose two files menu images.
    global panel, effect5, rect5
    panel = pygame.image.load('crypto_men.png')
    effect5 = pygame.image.load('crypto_men_eff.png')
    rect5 =[(effect5.subsurface(10, 77, 63, 59)), (effect5.subsurface(644, 181, 119, 41)), (effect5.subsurface(644, 259, 119, 41)), (effect5.subsurface(233, 349, 310, 75))]
    browser()

def aff_select(): #choose a file menu images.
    global panel2, effect6, rect6
    panel2 = pygame.image.load('gen_cle.png')
    effect6 = pygame.image.load('gen_cle_eff.png')
    rect6 = [(effect6.subsurface(17, 80, 50, 50)), (effect6.subsurface(630, 225, 119, 41)), (effect6.subsurface(229, 318, 310, 75))]
    select()

def aff_ecrire(): #writing section images.
    global panel3, effect7, rect7
    panel3 = pygame.image.load('ecrire.png')
    effect7 = pygame.image.load('ecrire_eff.png')
    rect7 = effect7.subsurface(246, 365, 310, 75)
    ecrire()

def aff_lecture(): #reading section images.
    global panel4, effect8, rect8
    panel4 = pygame.image.load('lecture.png')
    effect8 = pygame.image.load('gen_cle_eff.png')
    rect8 = effect8.subsurface(17, 80, 50, 50) 
    lecture()
    
def menu_principal():
    processing = True
    while processing:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 57<= pos[0] <= 227 and 148<= pos[1] <= 318:  # XOR icon fx.
                    screen.blit(menu, (0,0))
                    screen.blit(rect[0] , (57, 148))
                    
                elif 307<= pos[0] <= 477 and 148<= pos[1] <= 318:   #Equation icon fx
                    screen.blit(menu, (0,0))
                    screen.blit(rect[1] , (307, 148))
                    
                elif 557<= pos[0] <= 727 and 148<= pos[1] <= 318:   #Hidden text icon fx.
                    screen.blit(menu, (0,0))
                    screen.blit(rect[2] , (557, 148))
                
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30: #reduce button fx.
                    screen.blit(menu, (0,0))
                    screen.blit(rect[3], (704,0))
                
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30:  #close button fx.
                    screen.blit(menu, (0,0))
                    screen.blit(rect[4],(752,0))
                else:
                    screen.blit(menu, (0,0))
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                if 752 <= pos[0] <= 782 and 0<= pos[1] <= 30:   #close button.
                    import win32api
                    result = win32api.MessageBox(0,"Are you sure?","",1)
                    if result==1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30: #reduce button.
                    pygame.display.iconify()
                    
                elif  57<= pos[0] <= 227 and 148 <= pos[1] <= 318:   #XOR button.
                    processing = False
                    affichage_exclusif()
                    
                elif 307<= pos[0] <= 477 and 148 <= pos[1] <= 318:   #Equation button.
                    processing = False
                    affichage_eq()
                
                elif 557<= pos[0] <= 727 and 148 <= pos[1] <= 318:   #Hidden text button.    
                    processing = False
                    aff_texte()
                    
        pygame.display.flip()
        clock.tick(30)   

def menu_exclusif():
    global retourne, use, gen #identifiers.
    processing = True
    x= 44
    while processing:
        if x != 0:
            screen.blit(menu2, (0,0))
            screen.blit(choix, (x,0))
            x -= 4
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136: #go back button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix, (0,0))
                    screen.blit(rect2[0], (10, 77))
                    
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30:    #reduce button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix, (0,0))
                    screen.blit(rect[3], (704,0))
                
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix, (0,0))
                    screen.blit(rect[4],(752,0))
                    
                elif 87 <= pos[0] <= 356 and 223 <= pos[1] <= 249:  #key gen file already exists fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix, (0,0))
                    screen.blit(rect2[1],(84, 159))
                    screen.blit(rect2[3], (132, 247))
                
                elif 87 <= pos[0] <= 356 and 253 <= pos[1] <= 284:  #key gen camera fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix, (0,0))
                    screen.blit(rect2[1],(84, 159))
                    screen.blit(rect2[4], (132, 279)) 
                    
                elif  426<= pos[0] <= 711 and 224 <= pos[1] <= 261 : #(de/en)crypt  button.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix, (0,0))
                    screen.blit(rect2[2],(424, 159))
                    screen.blit(rect2[5], (432, 247)) 
                                        
                else:
                    screen.blit(menu2, (0,0))
                    screen.blit(choix, (0,0))
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136: #go back button.
                    processing = False
                    menu_principal()
                    
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close button.
                    import win32api
                    result = win32api.MessageBox(0,"Are you sure?","",1)
                    if result==1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #reduce button.
                    pygame.display.iconify()
                
                elif  426<= pos[0] <= 711 and 224 <= pos[1] <= 261 :    #(en/de)crypt button.
                    processing = False
                    retourne = 1
                    use = 1
                    aff_browser()
                    
                elif 87 <= pos[0] <= 356 and 223 <= pos[1] <= 249:  #key gen file already exists.
                    processing = False
                    retourne = 1
                    gen = 1
                    aff_select()
                
                elif 87 <= pos[0] <= 356 and 253 <= pos[1] <= 284:  #key gen web cam.
                    processing = False
                    retourne = 1
                    gen = 1
                    camera()
                    
        pygame.display.flip()
        clock.tick(30)
        
def menu_equation():
    global retourne, use, gen #identifiers.
    processing = True
    x= 44
    while processing:
        if x != 0:
            screen.blit(menu2, (0,0))
            screen.blit(choix2, (x,0))
            x -= 4
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136:  #go back button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    screen.blit(rect3[0], (10, 77))
                    
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30:    #reduce button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    screen.blit(rect[3], (704,0))
                
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    screen.blit(rect[4],(752,0))
                    
                elif 87 <= pos[0] <= 356 and 223 <= pos[1] <= 249:  #key gen file exists fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    screen.blit(rect3[1],(84, 159))
                    screen.blit(rect3[3], (132, 247))
                
                elif 87 <= pos[0] <= 356 and 253 <= pos[1] <= 284:  #key gen web cam fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    screen.blit(rect3[1],(84, 159))
                    screen.blit(rect3[4], (132, 279)) 
                    
                elif  426<= pos[0] <= 711 and 224 <= pos[1] <= 261 :    #encrypt button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    screen.blit(rect3[2],(424, 159))
                    screen.blit(rect3[5], (432, 247)) 
                
                elif  426<= pos[0] <= 711 and 263 <= pos[1] <= 294 :    #decrypt button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    screen.blit(rect3[2],(424, 159))
                    screen.blit(rect3[6], (428, 281)) 
                    
                else:
                    screen.blit(menu2, (0,0))
                    screen.blit(choix2, (0,0))
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136:  #go back button.
                    processing = False
                    menu_principal()
                    
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close button.
                    import win32api
                    result = win32api.MessageBox(0,"Are you sure?","",1)
                    if result==1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #reduce button.
                    pygame.display.iconify()
                
                elif 87 <= pos[0] <= 356 and 223 <= pos[1] <= 249:  #key gen file exists.
                    processing = False
                    retourne = 2
                    gen = 2
                    aff_select()
                    
                elif 426<= pos[0] <= 711 and 224 <= pos[1] <= 261 : #encrypt button.
                    processing = False
                    retourne = 2 
                    use = 2
                    aff_browser()
                    
                elif  426<= pos[0] <= 711 and 263 <= pos[1] <= 294 :    #decrypt button.
                    processing = False
                    retourne = 2
                    use = 3
                    aff_browser()
                
                elif 87 <= pos[0] <= 356 and 253 <= pos[1] <= 284:  #key gen web cam.
                    processing = False
                    retourne = 2
                    gen = 2
                    camera()
                    
        pygame.display.flip()
        clock.tick(30)

def menu_texte():
    global retourne, use, gen #identifiers.
    processing = True
    x= 44
    while processing:
        if x != 0:
            screen.blit(menu2, (0,0))
            screen.blit(choix3, (x,0))
            x -= 4
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136:  #go back button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix3, (0,0))
                    screen.blit(rect4[0], (10, 77))
                    
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30:    #reduce button.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix3, (0,0))
                    screen.blit(rect[3], (704,0))
                
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix3, (0,0))
                    screen.blit(rect[4],(752,0))
                    
                elif 87 <= pos[0] <= 356 and 223 <= pos[1] <= 249: #hide text file exists button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix3, (0,0))
                    screen.blit(rect4[1],(84, 159))
                    screen.blit(rect4[3], (132, 247))
                
                elif 87 <= pos[0] <= 356 and 253 <= pos[1] <= 284:  #hide text web cam button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix3, (0,0))
                    screen.blit(rect4[1],(84, 159))
                    screen.blit(rect4[4], (132, 279)) 
                    
                elif  426<= pos[0] <= 711 and 224 <= pos[1] <= 261 :    #read button fx.
                    screen.blit(menu2, (0,0))
                    screen.blit(choix3, (0,0))
                    screen.blit(rect4[2],(424, 159))
                    screen.blit(rect4[5], (432, 247)) 
                                        
                else:
                    screen.blit(menu2, (0,0))
                    screen.blit(choix3, (0,0))
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136: #go back button.
                    processing = False
                    menu_principal()
                    
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close button.
                    import win32api
                    result = win32api.MessageBox(0,"Are you sure?","",1)  
                    if result==1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #reduce button.
                    pygame.display.iconify()
                    
                elif 87 <= pos[0] <= 356 and 223 <= pos[1] <= 249:  #hide text file exists.
                    processing = False
                    retourne = 3
                    gen = 4
                    aff_select()
                    
                elif  426<= pos[0] <= 711 and 224 <= pos[1] <= 261 :    #read button. 
                    processing = False
                    retourne = 3
                    gen = 5
                    aff_select()

                elif 87 <= pos[0] <= 356 and 253 <= pos[1] <= 284:  #hide text web cam.
                    processing = False
                    gen = 3
                    camera()
                    
        pygame.display.flip()
        clock.tick(30)
                    
def browser():

    global image1, image2 #images generalized.
    import win32api
    processing = True
    x = 44
    id = ""
    id2 = ""
    while processing:
    
        font = pygame.font.Font(None,16)
        texte = font.render(id, True, (0,0,0))
        cadre = texte.get_rect()
        cadre.topleft = (48, 190)

        font2 = pygame.font.Font(None,16)
        texte2 = font2.render(id2, True, (0,0,0))
        cadre2 = texte2.get_rect()
        cadre2.topleft = (48, 271)
        
        if x != 0:
            screen.blit(menu2, (0,0))
            screen.blit(panel, (x, 0))
            x -= 4
                    
        pos = pygame.mouse.get_pos()    
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136: #return arrow effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(texte2, cadre2)
                    screen.blit(rect5[0], (10, 77))
                    
                elif 644 <= pos[0] <= 763 and 181 <= pos[1] <= 222: # browse image 1 effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(texte2, cadre2)
                    screen.blit(rect5[1], (644, 181))
                    
                elif 644 <= pos[0] <= 763 and 259 <= pos[1] <= 378: # browse image 2 effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(texte2, cadre2)
                    screen.blit(rect5[2], (644, 259))
                    
                elif 233 <= pos[0] <= 543 and 349 <= pos[1] <= 424: #start effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(texte2, cadre2)
                    screen.blit(rect5[3], (233, 349))
                    
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30: #reduce effect.
                        screen.blit(menu2, (0,0))
                        screen.blit(panel, (0,0))
                        screen.blit(texte, cadre)
                        screen.blit(texte2, cadre2)
                        screen.blit(rect[3], (704,0))
                    
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(texte2, cadre2)
                    screen.blit(rect[4],(752,0))
                
                else:
                    screen.blit(menu2, (0,0))
                    screen.blit(panel, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(texte2, cadre2)
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if 10 <= pos[0] <= 73 and 77 <= pos[1] <= 136: #return arrow.
                    if retourne == 1:
                        processing = False
                        affichage_exclusif()
                        
                    elif retourne == 2:
                        processing = False
                        affichage_eq()
                    
                elif 644 <= pos[0] <= 763 and 181 <= pos[1] <= 222: # browse image 1.
                    image1 = premiere_image()
                    id  = image1
                
                elif 644 <= pos[0] <= 763 and 259 <= pos[1] <= 378: # browse image 2.
                    image2 = deuxieme_image()
                    id2 = image2
                
                elif 233 <= pos[0] <= 543 and 349 <= pos[1] <= 424: #start button.
                    if id == "" or id2 == "":
                        print("\a")
                        win32api.MessageBox(0,"Veuillez selectionner une image correcte!","", 0)
                        
                    elif use == 1:
                        chargement()
                        
                    elif use == 2 or use == 3:
                        key()
                        
                elif 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close function                  
                    result = win32api.MessageBox(0,"Are you sure?","",1) #dialog box popup
                    if result == 1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #reduce function
                    pygame.display.iconify()
        
        pygame.display.flip()
        clock.tick(30)

def select():
    global image1, use, ec #image generalized and identifiers.
    processing = True
    x = 44
    id = ""
    import win32api
    
    while processing:
        font = pygame.font.Font(None,16)
        texte = font.render(id, True, (0,0,0))
        cadre = texte.get_rect()
        cadre.topleft = (30, 240)
        
        if x != 0:
            screen.blit(menu2, (0,0))
            screen.blit(panel2, (x, 0))
            x -= 4
            
        pos = pygame.mouse.get_pos()          
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 17 <= pos[0] <= 67 and 80 <= pos[1] <= 130: #return arrow effects. 
                    screen.blit(menu2, (0,0))
                    screen.blit(panel2, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(rect6[0],(17,80))
                
                elif 630 <= pos[0] <= 749 and 225 <= pos[1] <= 267: #browse button.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel2, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(rect6[1],(630,225))
                
                elif 229 <= pos[0] <= 539 and 318 <= pos[1] <= 393: #start effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel2, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(rect6[2],(229,318))
                    
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30:    #reduce effects.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel2, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(rect[3], (704,0))
                    
                elif 752 <= pos[0] <= 782 and 0 <= pos[1] <= 30: #close effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel2, (0,0))
                    screen.blit(texte, cadre)
                    screen.blit(rect[4], (752,0))
                
                else:
                    screen.blit(menu2, (0,0))
                    screen.blit(panel2, (0,0))
                    screen.blit(texte, cadre)
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close buttons.
                    result = win32api.MessageBox(0,"Are you sure?","",1) #dialog box popup.
                    if result == 1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #reduce function.
                    pygame.display.iconify()
                    
                elif 17 <= pos[0] <= 67 and 80 <= pos[1] <= 130:    # return arrow.
                    if retourne == 1:       #launched from XOR menu.
                        processing = False
                        menu_exclusif()
                        
                    elif retourne == 2: #launched from equation menu.
                        processing = False
                        menu_equation()
                    
                    elif retourne == 3: #launched from hidden text menu.
                        processing = False
                        menu_texte()
                        
                elif 630 <= pos[0] <= 749 and 225 <= pos[1] <= 267: #browse button.
                    image1 = premiere_image()
                    
                    id = image1
                    
                elif 229 <= pos[0] <= 539 and 318 <= pos[1] <= 393:
                    try: 
                        if id == "":
                            print("\a")
                            win32api.MessageBox(0,"Veuillez selectionner une image correcte!","", 0)
                            
                        elif gen == 1:      #XOR.
                            processing = False
                            from chiffrementImages import ale_image
                                
                            image_1 = pygame.image.load(image1)
                            dim_img1 = [(image_1.get_width()),(image_1.get_height())]
                                
                            ale_image(dim_img1[0], dim_img1[1], "cle_exclusif.bmp")
                            
                        elif gen == 2:      #equation.
                            image_1 = pygame.image.load(image1)
                            dim_img1 = [(image_1.get_width()),(image_1.get_height())]
                            disp  = pygame.display.set_mode((dim_img1[0], dim_img1[1]))
                            
                            print("\a")
                            
                            box = win32api.MessageBox(0,"Do you want to save?","", 1)
                            if box == 1:
                                pygame.image.save(disp, "cle_equation.bmp")
                                processing = False
                                from menu import menu_principal
                                menu_principal()
                        
                            elif box == 2:
                                processing = False
                                from menu import menu_principal
                                menu_principal()
                    
                        elif gen == 3:       #hide text.
                            processing = False
                            
                            from masquageTextes import masquage
                                
                            image_1 = pygame.image.load(image1)
                            dim_img1 = [(image_1.get_width()),(image_1.get_height())]
                            
                            masquage(dim_img1[0], dim_img1[1], image_1, 'imageTexte.bmp', texte)
                            
                        elif gen == 4:          #hide text web cam.
                            processing = False
                            ec = 1
                            aff_ecrire()
                            
                        elif gen == 5:          #reveal text.
                            processing = False
                            use = 5
                            chargement()
                            
                    except pygame.error:    #if the format of the image is incorrect or the the image doesn't exists.
                        ad  = win32api.MessageBox(0,"Error format image!","", 0)
                        aff_select()
                        
        pygame.display.flip()
        clock.tick(30)
        
class TEXTMESS:#create an object class.
    def _init_(self, message = None):   #_init_ that initialize an object orientation is used to create a module.self is an object input.
        self.message  = message
    def _str_(self):    #_str_ is a string module creation.
        return self.message #return the message of your object.
        
def texto(texte, font, surf, couleur, fond_coul, justification=0):
    final = []  #list that regroup all the lines.
    entree = texte.splitlines() #.splitlines() split a line of string.
    for ens_mots in entree: 
        if font.size(ens_mots)[0] > surf.width: #if the line's length is greater the writing surface.
            textes = ens_mots.split(' ')    #we will cut the line.
            
            #it is a new line made.
            
            lignes_surplus = "" 
            
            for mot in textes:  #for a word inside my line.
                if font.size(mot)[0] >= surf.width: #if the line's length is greater the writing surface.
                    raise TextMess #raise an error to the user.
                teste = lignes_surplus + mot + " "    #this line test + new word your current line.
                
                if font.size(teste)[0] < surf.width:    #if your line length is lower then then your writing surface.
                   lignes_surplus = teste               #the current line is still tested.
                else:
                    final.append(lignes_surplus)        #this line is stored in our list.
                    lignes_surplus = mot + " "          #this current line is emptied and then is assign to the new word.
            final.append(lignes_surplus)    
        else:
            final.append(ens_mots)  #add in the list the words of the line.
    
    surface = pygame.Surface(surf.size) 
    surface.fill(fond_coul)     #background colour of the surface.
    
    #here we are interest of the number of lines.
    
    hauteur_surplus = 0 #height of the text. 
    for line in final:  #coordinates of the list represents the number of the line.
        if hauteur_surplus + font.size(line)[1] >= surf.height: #if the height of the texte and the actual line is greater then the height of the surface.
            raise TextMess
        if line != "":  #if the line is not empty.
            template = font.render(line, 1, couleur)
            if justification == 0: #justification is if you want centred, left (we will use this), or right orientation texte. Here is left.
                surface.blit(template, (0, hauteur_surplus)) 
            elif justification == 1:    #centred text.
                surface.blit(template, ((surf.width - template.get_width()) / 2, hauteur_surplus))
            elif justification == 2:    #right orientation text.
                surface.blit(template, (surf.width - template.get_width(), hauteur_surplus))
            else:   #if you didn't the right justification.
                raise TextMess
        hauteur_surplus += font.size(line)[1]   #add the height of the current line in the counter.
    
    return surface

def ecrire():
    global recit, use #identifiers
    processing = True
    x = 44
    recit = ""
    
    
    import win32api
    
    while processing:
    
        font = pygame.font.Font(None, 22)
        cadre = pygame.Rect(82, 87, 640, 235)
        
        rendement = texto(recit, font, cadre, (0,0,0), (255,255,255), 0)
        
        if x != 0:
            screen.blit(menu2, (0,0))
            screen.blit(panel3, (x, 0))
            x -= 4
        
        pos = pygame.mouse.get_pos()          
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 246 <= pos[0] <= 556 and 365 <= pos[1] <= 440:   #start effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel3, (0,0))
                    screen.blit(rendement, cadre.topleft)
                    screen.blit(rect7,(246,365))
                    
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30:    #reduce effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel3, (0,0))
                    screen.blit(rendement, cadre.topleft)
                    screen.blit(rect[3], (704,0))
                    
                elif 752 <= pos[0] <= 782 and 0 <= pos[1] <= 30: #close effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel3, (0,0))
                    screen.blit(rendement, cadre.topleft)
                    screen.blit(rect[4], (752,0))
                
                else:
                    screen.blit(menu2, (0,0))
                    screen.blit(panel3, (0,0))
                    screen.blit(rendement, cadre.topleft)
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if 752 <= pos[0] <= 782 and 0<= pos[1] <= 30: #close function.
                    result = win32api.MessageBox(0,"Are you sure?","",1) #dialog box popup.
                    if result == 1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #reduce function.
                    pygame.display.iconify()
                    
                elif 246 <= pos[0] <= 556 and 365 <= pos[1] <= 440: #start button.
                    processing = False
                    if ec == 1:
                        use = 4
                        chargement()
                        
                    elif ec == 2:
                        use = 6
                        chargement()
                        
            if event.type == KEYDOWN: #keyboard assignment.
                
                if event.key == K_0 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                  recit += "0"
                elif event.key == K_KP0:
                    recit += "0"
                if event.key == K_0 and pygame.key.get_mods() & pygame.KMOD_RALT:
                    recit += "@"
                elif event.key == K_1 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "1"
                elif event.key == K_KP1:
                    recit += "1"
                elif event.key == K_1:
                    recit += "&"
                elif event.key == K_2 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "2"
                elif event.key == K_KP2:
                    recit += "2"
                elif event.key == K_2 and pygame.key.get_mods() & pygame.KMOD_RALT:
                    recit += "~"
                elif event.key == K_3 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "3"
                elif event.key == K_KP3:
                    recit += "3"
                elif event.key == K_3 and pygame.key.get_mods() & pygame.KMOD_RALT:
                    recit += "#"
                elif event.key == K_3:
                    recit += '"'
                elif event.key == K_4 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "4"
                elif event.key == K_KP4:
                    recit += "4"
                elif event.key == K_4:
                    recit += "'"
                elif event.key == K_5 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "5" 
                elif event.key == K_KP5:
                    recit += "5"
                elif event.key == K_5:
                    recit += "("
                elif event.key == K_6 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "6"
                elif event.key == K_KP6:
                    recit += "6"
                elif event.key == K_6:
                    recit += "-"
                elif event.key == K_7 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "7"
                elif event.key == K_KP7:
                    recit += "7"
                elif event.key == K_8 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "8"
                elif event.key == K_8:
                    recit += "_"
                elif event.key == K_KP8:
                    recit += "8"
                elif event.key == K_9 and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                    recit += "9"
                elif event.key == K_KP9:
                    recit += "9"                    
                elif event.key == K_SPACE:
                    recit += " "               
                elif event.key == K_COMMA:
                    recit += ";"                  
                elif event.key == K_MINUS:
                    recit += ")"     
                elif event.key == K_PERIOD:
                    recit += ":"
                elif event.key == K_SLASH:
                    recit += "!"
                elif event.key == K_m:
                    recit += "," 
                elif event.key == K_EQUALS:
                    recit += "="
                elif event.key == K_KP_PERIOD:
                    recit += "." 
                elif event.key == K_KP_DIVIDE:
                    recit += "*"  
                elif event.key == K_KP_MINUS:
                    recit += "-"
                elif event.key == K_KP_PLUS:
                    recit += "+"
                elif event.key == K_KP_MULTIPLY:
                    recit += "*"
                elif event.key == K_RETURN:
                    recit += "\n"
                elif event.key == K_TAB:
                    recit += "       "  
                elif event.key == K_BACKSPACE:
                    if recit == "":
                        print("\a")
                    else:
                       recit = recit[:-1]   
                elif event.unicode.isalpha():
                    recit += event.unicode
                
        pygame.display.flip()
        clock.tick(30)

def lecture():
    
    from masquageTextes import transformation #program transforms image into a text.
                                
    image_1 = pygame.image.load(image1)
    dim_img1 = [(image_1.get_width()),(image_1.get_height())]
                            
    final = transformation(dim_img1[0], dim_img1[1], image_1)
    x = 44
    print(type(final))
    import win32api
    processing = True
    while processing:

        font = pygame.font.Font(None, 22)
        cadre = pygame.Rect(81, 145, 641, 233)
        
        rendement = texto(final, font, cadre, (0,0,0), (255,255,255), 0)
        
        if x != 0:
            screen.blit(menu2, (0,0))
            screen.blit(panel4, (x, 0))
            x -= 4
            
        pos = pygame.mouse.get_pos() 
        
        for event in pygame.event.get():
            if pygame.mouse.get_pressed():
                if 17 <= pos[0] <= 67 and 80 <= pos[1] <= 130:  #return arrow.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel4, (0,0))
                    screen.blit(rect8, (17,80))
                    screen.blit(rendement, cadre.topleft)
                    
                elif 704 <= pos[0] <= 734 and 0 <= pos[1] <= 30:    #reduce effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel4, (0,0))
                    screen.blit(rendement, cadre.topleft)
                    screen.blit(rect[3], (704,0))
                    
                elif 752 <= pos[0] <= 782 and 0 <= pos[1] <= 30:    #close effect.
                    screen.blit(menu2, (0,0))
                    screen.blit(panel4, (0,0))
                    screen.blit(rendement, cadre.topleft)
                    screen.blit(rect[4], (752,0))
                    
                else:
                    screen.blit(menu2, (0,0))
                    screen.blit(panel4, (0,0))
                    screen.blit(rendement, cadre.topleft)
                    
            if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                if 752 <= pos[0] <= 782 and 0<= pos[1] <= 30:   #close function.
                    result = win32api.MessageBox(0,"Are you sure?","",1) 
                    if result == 1:
                        pygame.quit()
                        sys.exit()
                        
                elif 704 <= pos[0] <= 734 and 0<= pos[1] <= 30: #reduce function.
                    pygame.display.iconify()
                    
                elif 17 <= pos[0] <= 67 and 80 <= pos[1] <= 130:    #return arrow.
                        processing = False
                        menu_principal()

        pygame.display.flip()
        clock.tick(30)
        
menu_principal()