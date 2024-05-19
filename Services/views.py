from django.shortcuts import render,redirect
from Services.models import Url
from django.contrib import messages
import random,string
from django.contrib.sites.shortcuts import get_current_site

def getAlias():
    return "".join([random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8)])

# Create your views here.
def dashboard(request):
    if request.method == "POST":
        URL = request.POST["URL"]
        alias = request.POST.get("alias",None)
        if not alias:
            alias = getAlias()
        try:
            Url.objects.create(user=request.user,target_url=URL,alias=alias).save()
            messages.success(request,"success")
            return redirect("dashboard")
        except:
            messages.error(request,"alias already under use")
            return render(request,"dashboard.html",{"url":URL,"alias":alias})
    
    site = get_current_site(request)
    return render(request,"dashboard.html",{"domain":site})


def redirect_to_target_page(request,alias):
    obj = Url.objects.get(alias=alias)
    URL = obj.target_url
    return redirect(URL)