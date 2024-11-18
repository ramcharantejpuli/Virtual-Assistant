import datetime
import speak
import webbrowser
import weather
import os
import subprocess




def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn or "what's your name" in   data_btn or "your name" in   data_btn  :
      speak.speak("my name is Bitttu!,Your Desktop Assistant ,I'm here to assist you!")  
      return "my name is Bitttu!, Your Desktop Assistant ,I'm here to assist you!"
    

    elif "what's my name" in  data_btn or "what is my name" in  data_btn or "my name" in  data_btn :
        speak.speak("Your name is Puli Ram Charan Tej, and I think it's wonderful!") 
        return "Your name is Puli Ram Charan Tej, and I think it's wonderful!"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn or"what's the time" in data_btn or "time" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://open.spotify.com/")   
        speak.speak("spotify.com is now ready for you, enjoy your music")                   
        return "spotify.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"
    
    elif 'open edge' in data_btn or 'microsoft edge' in data_btn:
         edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
         subprocess.Popen([edge_path])
         speak.speak("Microsoft Edge open")
         return "Microsoft Edge open"
    

    elif 'open settings' in data_btn or 'settings' in data_btn:
        os.system("start ms-settings:")
        speak.speak("System Settings opened.")
        return "System Settings opened."
    

    elif 'open camera' in data_btn or 'camera' in data_btn:
         os.system("start microsoft.windows.camera:")  # Open the Camera app
         speak.speak("Camera opened.")
         return "Camera opened."
    

    elif 'open file manager' in data_btn or 'This PC' in data_btn:
         os.system("start explorer")  # Open File Explorer
         speak.speak("File Explorer opened.")
         return "File Explorer opened."


    elif 'open calculator' in data_btn or 'calculator' in data_btn:
        os.system("start calc")  # Open Calculator using the start command
        speak.speak("Calculator opened.")
        return "Calculator opened."
    
    
    elif 'open chrome' in data_btn or 'chrome' in data_btn:
         chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
         subprocess.Popen([chrome_path])
         speak.speak("Google Chrome open")
         return "Google Chrome open"
    

    elif 'open do select' in data_btn or 'do select' in data_btn:
         doselect_path = r"C:\Users\hp\OneDrive\Desktop\Doselect Secure Browser.lnk"
         os.startfile(doselect_path)
         speak.speak("Doselect Secure Browser open")
         return "Doselect Secure Browser open"


    elif 'open instagram' in data_btn or 'instagram' in data_btn:
         url = 'https://instagram.com/'
         webbrowser.get().open(url)
         speak.speak("Instagram open")
         return "Instagram open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 

    else :
        speak.speak( "i'm able to understand!")
        return "i'm able to understand!"       

