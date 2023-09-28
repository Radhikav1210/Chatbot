import aiml
import os
import webcr
from webcr import search, totext
import text2sp
from text2sp import tospeech

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
	st=raw_input("Enter your message >> ")
	if st=='voice':
		text=totext()
		print text
		response=kernel.respond(text)
		#print response
		tospeech(response)
	elif st=='search':
		search()
	else:
		print kernel.respond(st)