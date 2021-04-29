from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Canditate,votedUser
from django.urls import reverse
from asgiref.sync import sync_to_async
import asyncio


#util functions
def check(tovote):
    v=votedUser.objects.all()
    votedlist = [i.voted for i in v]
    if tovote in votedlist:
        return False
    return True

@sync_to_async()
def addvote(votedid):
    temp=Canditate.objects.get(id=votedid)
    temp.Vote+=1
    temp.save()

@sync_to_async()
def addvoteduser(userid):
    votedUser.objects.update_or_create(voted=userid)
    

# Create your views here.
async def vote(request):
    current_user = request.user
    v=votedUser.objects.all()
    votedlist = [i.voted for i in v]
    if current_user.id in votedlist:
        flag=1
    else:
        flag=0
    if request.method == "POST":
        if flag==0:
            try:
                Votedid=int(request.POST['voted'])
                task1=asyncio.ensure_future(addvote(Votedid))
                task2=asyncio.ensure_future(addvoteduser(current_user.id))
                await asyncio.wait([task1,task2])
                return render(request,"voted.html")
            except:
                return render(request,"vote.html",{
                    "canditates":Canditate.objects.all(),
                    "flag":flag,
                    "flag1":1
                    })

    return render(request,"vote.html",{
        "canditates":Canditate.objects.all(),
        "flag":flag,
        "flag1":1
    })

def result(request):
    return render(request,"result.html",{
        "canditates":Canditate.objects.all()
    })

def addcanditate(request):
    if request.method == "POST":
        Canditate.objects.update_or_create(Name=request.POST['name'],Vote=0)
        return redirect(reverse('result'))
    return render(request, "addcanditate.html")


