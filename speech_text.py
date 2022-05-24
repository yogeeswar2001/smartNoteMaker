import speech_recognition as sr
def write_file(text):
    f= open('./note.txt','a')
    f.write(text)
    f.close()
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Listening")
    while 1:
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            if (text=='class over'):
                print('done')
                break 
            print(text)
            write_file(" "+text)
        except:
            print('Sorry could not reconize your voice')
print('notes stored in notes file')