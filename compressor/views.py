from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import render
from compressor.models import Data

# Create your views here.
def home(request):
    axces=False
    return render(request,"index.html",{"axces":axces})

def decompressor(request,id):
    id = int(id)
    user_message = Data.objects.get(pk = id)
    message = user_message.encoded_string
    return HttpResponse(message)

def ecodetext(request):
    if request.method == "POST":
        encodedtxt = request.POST.get('eformtxt')
        encodedratio = request.POST.get('eformratio')
        new_data = Data(encoded_string=encodedtxt)
        new_data.save()
        # success= f"{new_data} <br> {encodedratio} <br> {encodedtxt}"
        link = "http://127.0.0.1:8000/decompressor/" + str(new_data.pk)
        ratio = encodedratio
        axces=True
        return render(request,"index.html",{"axces":axces,"link":link,"ratio":ratio})