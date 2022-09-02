# import googletrans
# from googletrans import Translator
from gtts import gTTS
tts = gTTS('hello', lang='en')
tts.save('hello.mp3')


# text1 = "Hello welcome to my website!"
# translator = Translator()
# trans1 = translator.translate(text1, src='en', dest='ja')
# print("English to Japanese: ", trans1.text)

# print(googletrans.LANGUAGES)