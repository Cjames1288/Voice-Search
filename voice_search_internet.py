from tkinter import *
import speech_recognition as sr  # imports a module and set as alias
import webbrowser  # simple module for web browsing
import json
import arrow

print("BEGIN")
tk_Window = Tk()  # initializes tkinter tk_Window widget
tk_Window.configure(background='blue')  # sets color of the background of the main window
tk_Window.geometry('200x200') # # sets the widget to the lower right corner

def save_to_json(search_text):
    file_path = (r'C:\Users\cjame\OneDrive\Desktop\voice_search_internet'
                 r'\voice_search_internet.json')
    
    with open(file_path, 'r') as file:
        search_data = json.load(file)

    search_data[(len(search_data) + 1)] = {
        'search_text':search_text,
        'time_stamp':arrow.now().format("MM-DD-YYYY HH:mm:ss"),
        'categories':[]
    }

    with open(file_path, 'w') as file:
        json.dump(search_data, file)
        

def get_phrase():
    r = sr.Recognizer()  # creates a recognizer instance
    with sr.Microphone() as source: # open a context manager with a microphone instance
        audio = r.listen(source, phrase_time_limit=None) # microphone begins to listen to output
       
        try:    # exception block in case an error with reccording occurs
            said = r.recognize_google(audio)  # use google's text to speech to decipher
            print(said)  # prints the text so user can verify
            

        except Exception as e:  # assign exception as name
            print(f"Exception: {str(e)}")


  # function to voice search google
    
    if said.startswith(('okie', 'Okie', 'oki', 'Oki')):
        saide = said.split(' ', 1)[1]
        said = said.replace(' ','+')
        for element in ['stackoverflow', 'reddit', 'pythonic']:
            webbrowser.open(f'http://google.com/search?q={element}+{"pep8"}+{said}', new=1, autoraise=False)
    else:
        webbrowser.open(f'http://google.com/search?q={said}', new=1, autoraise=False)
    
    save_to_json(said)


button = Button(tk_Window, text="Search", activebackground='red', command = get_phrase)  # creates button thats call search()
button.config( height=200, width=200, bg='blue')
button.pack()
mainloop()  # keeps the program in an event loop
print("exited")