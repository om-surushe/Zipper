from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def decompressor(request,id):
    id = int(id)
    message = f"hello {id}"
    return HttpResponse(message)

def ecodetext(request):
    print("hello")
    if request.method == "POST":
        ecodedtxt = request.POST.get('eformtxt')
        print(ecodedtxt)
        success="ho gaya"
        print(success)
    else:
        success="nahi hua"
        print(success)
    return HttpResponse(success)