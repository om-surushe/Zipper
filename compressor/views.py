from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from compressor.models import Data

# Create your views here.
def home(request):
    return render(request,"index.html")

def decompressor(request,id):
    id = int(id)
    user_message = Data.objects.get(pk = id)
    message = user_message.encoded_string
    return HttpResponse(message)

def ecodetext(request):
    if request.method == "POST":
        encodedtxt = request.POST.get('eformtxt')
        new_data = Data(encoded_string=encodedtxt)
        new_data.save()
        success= new_data.pk
    else:
        success="nahi hua"
        print(success)
    return HttpResponse(success)