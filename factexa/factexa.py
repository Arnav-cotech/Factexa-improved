
import speech_recognition as speech
import pyttsx3
import pygame

import time

#Initialize the Speech Generation Library
engine=pyttsx3.init()
engine.setProperty('rate',150)

#Initialize Pygame
pygame.init()

#Create Screen with size 900x600
width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('Factexa')

#Display the Background Image
bg=pygame.image.load("images/Factexa Opening.png" )
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()


#Dictionary for Sport Alexa
keyfact={
     "longest word":["Spch","pneumonoultramicroscopicsilicovolcanoconiosis is the worlds longest world."],
     "pig ":["ImgSpch","A Pig Organism last 30 minutes.","pig organism.jpeg"],
     "blue whale":["ImgSpch","A Blue Whale weighs as much as 3 elephants and is as long as 3 grey hound buses.",""],
     "bat":["ImgSpch","A Bat can eat up to 1 thousand insects per hour.","bats.jpeg"],
     "snail":["ImgSpch","A snail can sleep up to 3 years.","snail.jpeg"],
     "amazon river":["ImgSpch","The Amazon River is the largest river in the world by volume of water, and its believed to contain about 20% of all Earths Freshwater.","amazon river.jpeg"],
     "octopus":["ImgSpch","Octopuses have three hearts , nine brains and blue blood.","octopus.jpeg"],
     "owl":["ImgSpch","Owls don’t have eye ball they have eye tubes.","owl.jpeg"],
     "polar bears":["ImgSpch","Polar Bears have black skin under there white fur.","polar bear.jpeg"],
     "butterfly":["ImgSpch","Butterfly’s taste the plant/ flower by there feet.","butterfly.jpeg"],
     "dog’s sense of smell":["ImgSpch","A Dog’s sense of smell is 1,00,000 times better than humans ,but they only have 1/6 of our taste bud.","dogs sence of smell.jpeg"],
     "reindeer":["ImgSpch","A Reindeer’s eyeball turns blue in the winter to help them see better in the snow.","reindeer.jpeg"],
     "spider web":["ImgSpch","A single strand of spider silk is thinner than a human hair ,but also five times stronger than steel of the same width. A rope 2 inches thick could stop reportedly stop a Boeing 747","spider silk.jpeg"]
     }
activate="none"
exitstatus="no"

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            #To Read whether 's' key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    activate = 's'
                    print("S pressed")
                    
                    
        #If 's' key is pressed
        if activate=='s':
            #Change the background image to Listening Image
            listenImg=pygame.image.load("images/bg2.png").convert_alpha()
            image1=pygame.transform.scale(listenImg, (900,600))
            screen.blit(image1,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            #Search each keyword in the dictionary one-by-one
            for keyword in keyfact:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                    
                    #Check the response type for that keyword
                    
                    #Speech Response Type
                    if keyfact[keyword][0]=="Spch":
                        engine.say(keyfact[keyword][1])
                        engine.runAndWait()
                        
                    #Console Text Response Type
                    if keyfact[keyword][0]=="consoleText":
                        print(keyfact[keyword][1])
                    
                    #Image Response type
                    if keyfact[keyword][0]=="Img":
                        image=pygame.image.load("images/"+keyfact[keyword][1]).convert_alpha()
                        image1=pygame.transform.scale(image, (813,375))
                        screen.blit(image1,(45,145))
                        
                        pygame.display.update()
                        time.sleep(15)
                        
                    #Image & Speech Response type
                    if keyfact[keyword][0]=="ImgSpch":
                        #Showing Image
                        image=pygame.image.load("images/"+keyfact[keyword][2]).convert_alpha()
                        image1=pygame.transform.scale(image, (813,375))
                        screen.blit(image1,(45,145))
                      
                        pygame.display.update()
                        
                        #Saying Text
                        engine.say(keyfact[keyword][1])
                        engine.runAndWait()
                        
                   
                        
                     
                    if keyfact[keyword][0]=="exit":
                        engine.say(keyfact[keyword][1])
                        engine.runAndWait()
                        exitstatus="yes"
                        break
            #if 'exit' in command then break from while loop        
            if exitstatus=="yes":
                    pygame.quit()
                    break
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("images/Factexa Opening.png").convert_alpha()
            image1=pygame.transform.scale(bg, (900,600))
            screen.blit(image1,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    

           
                


