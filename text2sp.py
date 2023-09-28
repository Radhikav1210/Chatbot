import pyttsx
engine = pyttsx.init()
engine.setProperty('rate', 70)

'''voices = engine.getProperty('voices')
for voice in voices:
    print "Using voice:", repr(voice)
    st=input("Write the text:")
    engine.setProperty('voice', voice.id)
    engine.say(st)
engine.runAndWait()'''

def tospeech(text):
	voices = engine.getProperty('voices')
	for voice in voices:
		print "Using voice:", repr(voice)
		#st=input("Write the text:")
		engine.setProperty('voice', voice.id)
		engine.say(text)
	engine.runAndWait()
