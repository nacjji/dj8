from multiprocessing import context
from django.shortcuts import render
from gtts import gTTS
# Create your views here.
def index(request):
    context={}
    if request.method == 'POST':
        st = request.POST.get('st')
        fn = request.POST.get('fname')
        la = request.POST.get('lang')
        tts = gTTS(st, lang=la)
        tts.save(f"media/tts/{fn}.mp3")
        context.update({
            'st':st,
            'fn':fn,
            'la':la
        })
        
    return render(request, 'tts/index.html', context)