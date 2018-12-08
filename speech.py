import speech_recognition as sr

with sr.Microphone() as source:
	print("Say Anything : ")
	r = sr.Recognizer()
	r.energy_threshold = 500
	audio = r.listen(source)
	word = r.recognize_google(audio)
	print('\n' + word)

	