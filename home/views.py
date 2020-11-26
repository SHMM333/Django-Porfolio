from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
import os
from proj1 import settings

# Create your views here.
def index(request):
    context = {
        "variable1":"mai variable1 sent",
        "variable2":"maii variable2 sent"
    }
    return render (request, 'index.html',context)
    #return HttpResponse("THIS IS HOME PAGE")

def mywork(request):
    return render (request, 'mywork.html')
    # return HttpResponse("this is mywork link page")

def downloadResume(request,fileName):
    filePath=os.path.join(settings.MEDIA_URL,fileName)
    print(filePath)
    response = HttpResponse(open(filePath, 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=1.docx'
    return response


def aboutme(request):
    return render (request, 'aboutme.html')
    # return HttpResponse("this is about me page")

def myskillset(request):
    return render (request, 'myskillset.html')
    # return HttpResponse("this is my skill set page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        messages.success(request, 'Sent Successfully!')

    return render (request, 'contact.html')
    #return HttpResponse("this is my contact page")
    
