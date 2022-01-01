from django.shortcuts import render
from compressor.models import Data

def home(request):
    axces=False
    return render(request,"index.html",{"axces":axces})

def decompressor(request,id):
    id = int(id)
    user_message = Data.objects.get(pk = id)
    secret = user_message.encoded_string
    return render(request,"decomp.html",{"secret":secret})

def ecodetext(request):
    if request.method == "POST":
        encodedtxt = request.POST.get('eformtxt')
        encodedratio = request.POST.get('eformratio')
        new_data = Data(encoded_string=encodedtxt)
        new_data.save()
        link = "http://127.0.0.1:8000/decompressor/" + str(new_data.pk)
        ratio = encodedratio
        axces=True
        return render(request,"index.html",{"axces":axces,"link":link,"ratio":ratio})