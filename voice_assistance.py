import pyttsx3
import wikipedia



engine = pyttsx3.init()

'''rate'''
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 130)

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

In = input("Search wikipedia/google: ").capitalize()
print(In)

result = wikipedia.summary(In, sentences = 5)
print(result)
engine.say(result)
engine.save_to_file(result , 'test.mp3')
engine.runAndWait()
