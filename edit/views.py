from django.shortcuts import render
from .models import Edit
from PIL import Image
# Create your views here.
def index(request):
    context={}
    if request.method=="POST":
        im=request.FILES.get('im')
        Edit(img=im).save()
        imag= Image.open(f"media/media/{im}")
        print(imag.getpixel((0,0)))
        w,h=imag.size
        for i in range(w):
            for j in range(h):
                r,g,b=imag.getpixel((i,j))
                a=(r+g+b)//3
                imag.putpixel((i,j),(a,a,a))
        print(imag.save(f"media/media/{im}"))

        context.update({
            'imag':imag,
            'im':im
        })
    return render(request,'edit/index.html',context)