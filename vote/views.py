from django.shortcuts import render,redirect
from .models import Choice, Topic

# Create your views here.
def index(reqeust):
    t= Topic.objects.all()
    context = {
        'tset':t
    }
    
    return render(reqeust, 'vote/index.html',context)

def detail(request, tpk):
    t = Topic.objects.get(id=tpk)
    c = t.choice_set.all()
    context = {
        "t" : t,
        "cset" : c
    }
    return render(request, "vote/detail.html", context)


def vote(request, tpk):
    t = Topic.objects.get(id=tpk)
    if not request.user in t.voter.all():
        t.voter.add(request.user)
        cpk = request.POST.get("cho")
        c = Choice.objects.get(id=cpk)
        c.num += 1
        c.save()
    return redirect("vote:detail", tpk)


def create(request):
    if request.method == 'POST':
        s=request.POST.get('sub')
        c=request.POST.get('con')
        cho=request.POST.getlist('cho')
        pi=request.FILES.get('pic')
        t=Topic(subject=s, content=c, maker=request.user)
        t.save()
        for i in cho:
            Choice(top=t,name=i, pic=pi).save()
        return redirect('vote:index')
    return render(request, 'vote/create.html')




