from jarvis import *


def main():
    presentation()
    pause = false
    while True:
        if (pause == false):
            query = myspeech()
            query = query.lower()
            cmd(query)


            if (query == "mets-toi en pause"):
                pause = true
 
        
        if(pause):
            pause = myspeech_pause()


            
            
        
main()
