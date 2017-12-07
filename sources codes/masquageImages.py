import sys, os , numpy, pygame
from pygame.locals import *
from pygame.surfarray import *

def formule(n, m, op, k):
    if op == 1:          #op = 1 is for encryption and other value of op is for decryption.
        man =  n + (1/k)*m  
        if man > 255:     #in case if the function return a value higher then the max of the component (R,G,B).
            man = 255
        if man < 0:
            man = 0
    else:
        man =  k*(m - n)
        if man > 255:
            man = 255
        if man < 0:
            man = 0
            
    return man    
    
def traitement(op,k,tuple_a,tuple_b):
    tuple_result=[] #list of the result of the equations above.
    i=0
    while i<len(tuple_a): #i is the counter and also the length of the final tuple.
        tuple_result.append(formule(tuple_a[i],tuple_b[i],op,k))
        i+=1
    return tuple(tuple_result) #transforms list into tuples.
    
def procedure(l,h,image_a,image_b,image_f,k,op):
    
    import pygame, numpy, sys
    pygame.init()
    tuple_a = [] #list of the first image.
    tuple_b = [] #list of the second image.
    list1 = pygame.surfarray.array3d(image_a) # transforms the image into an array.
    list2 = pygame.surfarray.array3d(image_b)
    f1 = [[tuple_a.append(tuple(b.reshape(-1, 3)[0])) for b in a] for a in list1] #transforms third dimensional arrays into tuples that added in the lists above.
    f2 = [[tuple_b.append(tuple(b.reshape(-1, 3)[0])) for b in a] for a in list2]
    final = [(traitement(op,k,a,b)) for a, b in zip(tuple_a, tuple_b)]            #applies the last function inside the list of the new image.
    image = numpy.array(final, dtype='uint8').reshape(l,h,3)            #convert this list into a 3d image array.
    new_image = pygame.surfarray.make_surface(image)
    screen = pygame.display.set_mode((l,h))
    screen.blit(new_image, (0,0))
    
    print("\a")         #bip sound.
    
    import win32api
    rep = win32api.MessageBox(0, "Your image is now done!", "", 0) #message box pop-up (note: requires to download python for windows extensions).
    
    processing = True
    while processing:
        for event in pygame.event.get():
            if event.type == QUIT:
                import win32api
                box = win32api.MessageBox(0,"Are you sure want to leave?","", 1)
                if box == 1:
                    result = win32api.MessageBox(0,"Do you want to save the picture?","", 1)
                    if result == 1:
                        processing = False
                        pygame.image.save(screen, image_f)  #saves the image.
                        from menu import menu_principal  #menu is another program.
                        menu = pygame.image.load('menu.png')
                        size = [(menu.get_width()), (menu.get_height())]
                        os.environ['SDL_VIDEO_CENTERED'] = '1'           #centers the display.
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
                        
        
        pygame.display.flip()    #update the screen
 