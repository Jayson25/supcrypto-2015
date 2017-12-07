import pygame, sys, itertools, numpy, os
from pygame.surfarray import *
from pygame.locals import *

pygame.init()

def pre_traitement(l, h, p):
    global final
    final = [254 if a == 255 else a for a in p]   #pre traitement is important in order to avoid 256 value.

def masquage(l, h, image1, image2, texte):
    one = []
    list1 = pygame.surfarray.array3d(image1)
    f1 = [[one.append(list(b.reshape(-1, 3)[0])) for b in a] for a in list1]
    one = list(itertools.chain.from_iterable(one)) #removes hooks or parenthesis of tuples or lists inside the list.
    
    pre_traitement(l, h, one) 
    
    prepa = list(texte) #transform string into a list.

    liste = [('%08d' % int(bin(ord(i))[2:])) for i in prepa] #transforms an integer into a binary of 8-bit length.
    liste = list(itertools.chain.from_iterable(liste))       

    while len(liste) < len(final): #in order to have the same length as the image, we append zeros to the text list.
        liste.append('0')

    two = []

    for i , (a,b) in enumerate(zip(final, liste)):#zip(a,b) regroup two objects (here we have two binary with the SAME LENGTH) and examines two elements in the same index. 

            if a%2 == 0 and b == '0': #case for a pair
                two.append(a)
            
            if a%2 == 0 and b == '1':
                two.append(a+1)
            
            if a%2 != 0 and b == '0': #case for an impair
                two.append((a+1))
            
            if a%2 != 0 and b == '1':
                two.append((a))
    
    two = [two[i : i+3] for i in range(0, len(two), 3)] #[1,2,3,4,5,6,7,8,9] => [[1,2,3], [4,5,6], [7,8,9]]
        
    image = numpy.array(two, dtype='uint8').reshape(l,h,3) #convert this list into a 3d image array.
    new_image = pygame.surfarray.make_surface(image)
    disp = pygame.display.set_mode((l,h))
    disp.blit(new_image, (0,0))
        
    print("\a")             #bip sound.
        
    import win32api
    rep = win32api.MessageBox(0, "Your image is now done!", "", 0) #message box pop-up (note: requires to download python for windows extensions).
    processing = True
    while processing:
            
        for event in pygame.event.get():
            if event.type == QUIT:
                box = win32api.MessageBox(0,"Are you sure want to leave?","", 1)
                if box == 1:
                    result = win32api.MessageBox(0,"Do you want to save the picture?","", 1)
                    if result == 1:
                        pygame.image.save(disp, image2) #saves the image.
                        processing = False 
                        from menu import menu_principal  #menu is another program.
                        menu = pygame.image.load('menu.png') #menu is another program.
                        size = [(menu.get_width()), (menu.get_height())]
                        os.environ['SDL_VIDEO_CENTERED'] = '1'            #centers the display.
                        screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME) #pygame.NOFRAME: removes border and controls of the window.
                        menu_principal()
                            
                    elif result == 2:
                        processing = False
                        from menu import menu_principal  
                        menu = pygame.image.load('menu.png')
                        size = [(menu.get_width()), (menu.get_height())]
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                        screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME)
                        menu_principal()
                        
        pygame.display.flip()       #update the screen.
    
def preparation(l, h, image):#toujours en chantier.
    one = []
    list1 = pygame.surfarray.array3d(image)
    f1 = [[one.append(list(b.reshape(-1, 3)[0])) for b in a] for a in list1]
    one = list(itertools.chain.from_iterable(one)) # removes hooks in sublists.
    texte_binaire = ""
    for i in one:
        if i%2 == 0:      #if the component is pair.
            texte_binaire += "0"
        else:
            texte_binaire += "1"
    
    texte_liste = list(texte_binaire)
    final = []
    
    texte_liste = [texte_liste[i : i+8] for i in range(0, len(texte_liste), 8)]
    texte_liste = [ "".join(i) for i in texte_liste]  
    
    for i in texte_liste:
        if i != '00000000': 
            final.append(i)
        elif i == '00000000':  #if it detects a NULL.
            return final
    
def transformation(l , h, image):
    final = preparation(l, h, image)
    
    final = [int(i, 2)for i in final]
    print(final) 
    final = [chr(i) for i in final] #transform a integer into a unicode
    final = "".join(final)
    return final