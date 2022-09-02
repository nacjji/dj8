from django.shortcuts import render,redirect
from googletrans import Translator
import googletrans
from gtts import gTTS

# print(googletrans.LANGUAGES)

def index(request):
    context = {
        "ndict" : googletrans.LANGUAGES
    }
    if request.method == "POST":
        try:
            b = request.POST.get("bf")
            f = request.POST.get("fr")
            t = request.POST.get("to")
            fn= request.POST.get('fname')
            translator = Translator()
            af = translator.translate(b, src=f, dest=t)
            tts = gTTS(af.text, lang=t)
            # print(b,t,af.text)
            tts.save(f"media/tts/{fn}.mp3")
            context.update({
                "bf" : b,
                "fr" : f,
                "to" : t,
                "af" : af.text
            })
        except:
            pass
    return render(request, "trans/index.html", context)
