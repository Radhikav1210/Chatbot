import speech_recognition as sr
import webbrowser as wb

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

r = sr.Recognizer()


def search():
	with sr.Microphone() as source:
		print ('Say Something!')
		audio = r.listen(source)
		print ('Done!')

	try:
		text = r.recognize_google(audio)
		print('google think you said:\n' + text)

		f_text = 'https://www.google.co.in/search?q=' + text
		wb.get(chrome_path).open(f_text)

	except Exception as e:
		print(e)

def totext():
	with sr.Microphone() as source:
		print ('Say Something!')
		audio = r.listen(source)
		print ('Done!')
		
	try:
		text=r.recognize_google(audio)
		return text
		
	except Exception as e:
		print(e)
