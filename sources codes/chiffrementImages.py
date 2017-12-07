import pygame, numpy, random, sys, time, os
from pygame.locals import *
from pygame.surfarray import *
pygame.init()

def ou_exclusif(a, b): 
    return ''.join('0' if index == element else '1' for index, element in zip(a,b)) #''.join() transform a list or tuple into integer '' means no space between the terms. zip(a,b) regroup deux objects (here we have two binary with the SAME LENGTH) and examines two elements in the same index. 
    
def binaire(a): 
    return '%08d' % int(bin(a)[2:]) #0 position of the integer in the binary, %d decimal conversion, bin is convert into binary, [2:] removes 0b.
    
def ex_2(a,b):  
    return int(ou_exclusif(binaire(a),binaire(b)), 2) #transforms into a binary number into a integer.
    
def tupl(a, b):
    
    c =[]
    for index, element in zip(a,b):
        c.append(ex_2(index,element)) # c is the new tuple because when there is a xor, the two tuple are mixed together.
    return tuple(c) #convert a list into a tuple.
        
def ale_image(l,h,image_f):

    processing = True
    picture = pygame.display.set_mode((l, h))
    pygame.display.iconify()                   #reduces the window.
    import win32api
    
    one = []
    while len(one) < l*h:
        r = random.randint(0, 255) #red random value.
        g = random.randint(0, 255) #green.
        b = random.randint(0, 255) #blue.
        one.append(tuple((r,g,b))) #creates a new list of tuples RGB.
        
    image = numpy.array(one, dtype='uint8').reshape(l,h,3) #convert this list into a 3d image array.
    new_image = pygame.surfarray.make_surface(image) #convert array into surface.
    disp = pygame.display.set_mode((l,h)) #initialize display.
    disp.blit(new_image, (0,0)) #paste image on the display.
    
    print("\a") #bip sound.
    
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
                        pygame.image.save(disp, image_f) #saves the image.
                        processing = False
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

        pygame.display.flip() #update the screen
        
def chiff_image(l, h, image_1, image_2, image_f):
    one = []                                        #list of the first image.
    two = []                                        #list of the second image.
    list1 = pygame.surfarray.array3d(image_1)       # transforms the image into an array.
    list2 = pygame.surfarray.array3d(image_2)
    f1 = [[one.append(tuple(b.reshape(-1, 3)[0])) for b in a] for a in list1] #transforms third dimensional arrays into tuples that added in the lists above.
    f2 = [[two.append(tuple(b.reshape(-1, 3)[0])) for b in a] for a in list2]
    final = [tupl(a,b) for a,b in zip(one, two)]                              #applies the last function inside the list of the new image.
    image = numpy.array(final, dtype='uint8').reshape(l,h,3) 
    new_image = pygame.surfarray.make_surface(image)
    disp = pygame.display.set_mode((l,h))
    disp.blit(new_image, (0,0))
    
    print("\a")
    
    import win32api
    rep = win32api.MessageBox(0, "Your image is now done!", "", 0)
    processing = True
    while processing:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                box = win32api.MessageBox(0,"Are you sure want to leave?","", 1)
                if box == 1:
                    result = win32api.MessageBox(0,"Do you want to save the picture?","", 1)
                    if result == 1:
                        pygame.image.save(disp, image_f)
                        processing = False
                        from menu import menu_principal
                        menu = pygame.image.load('menu.png')
                        size = [(menu.get_width()), (menu.get_height())]
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                        screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME)
                        menu_principal()
                        
                    elif result == 2:
                        processing = False
                        from menu import menu_principal
                        menu = pygame.image.load('menu.png')
                        size = [(menu.get_width()), (menu.get_height())]
                        os.environ['SDL_VIDEO_CENTERED'] = '1'
                        screen = pygame.display.set_mode((size[0], size[1]), pygame.NOFRAME)
                        menu_principal()

        pygame.display.flip()
      
#174594@supinfo.com à contacter en cas ou pour le MP