from django.shortcuts import render
from .models import *

# Create your views here.
def Index(request):
    return render(request,'index.html')
      
def Upload(request):
    if( request.method == "POST"):
        file = request.FILES['files']

        file = UploadFil.objects.create(file=file)
        msg = "File Successfully Uploaded"
        return render(request,'download.html',{'msg':msg})

def  download(request):
    filed = UploadFil.objects.all()
    return render(request,'download.html',{'filed':filed})
