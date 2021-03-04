from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.contrib.auth import logout
from django import template
from django.views.generic.base import TemplateView
import fitz
import qrcode
from app.models import Labreport
from .settings import BASE_DIR
from .forms import DocumentForm

def home(request):
    return render(request, 'err.html')

@login_required(login_url='login/')
def upload(request):
    try:
        if request.method == 'POST':
            print(request.POST)
            form = DocumentForm(request.POST,request.FILES)
            print(form)
            if form.is_valid():
                form.save()
                return redirect(index)
            else:
                form = DocumentForm()
                print(form)
                
        else:
            form = DocumentForm()

        
        return index(request)
    except Exception as e:
        print('Error',e)
    # else:
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login/')
def index(request):
    context = {}
    context['segment'] = 'index'
    context['reports'] = list(Labreport.objects.all())
    html_template = loader.get_template( 'index2.html')
    return HttpResponse(html_template.render(context,request))

    
    #return HttpResponse("<html><head><title>Lab Report Portal</title></head><body><h1>Lab Report Portal</h1></body></html>")
def get_report(request,id):
    try:
        mediadir = str(BASE_DIR)+"/LabReport/media/"
        print(mediadir)
        input_file = mediadir+str(id)+".pdf"
        output_file = mediadir+str(id)+"_qr.pdf"
        barcode_file = mediadir+"barcode.png"
        data = "http://167.71.228.127:8004/report/"+str(id)
        qroutfile = barcode_file
        img = qrcode.make(data)
        img.save(qroutfile)
        image_rectangle = fitz.Rect(450,20,550,120)
        file_handle = fitz.open(input_file)
        first_page = file_handle[0]
        pix = fitz.Pixmap(barcode_file)        # any supported image file
        first_page.insertImage(image_rectangle, pixmap=pix, overlay=True) 
        file_handle.save(output_file)
        fs = FileSystemStorage()
        filename = output_file
        if fs.exists(filename):
            with fs.open(filename) as pdf:
                response = HttpResponse (pdf,content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename='+filename
                return response
        else:
            return render(request, 'err.html')
  
    except :
        return render(request, 'err.html')
    

