from django.shortcuts import render
from .forms import ImageForm,CreateNewList
import os
from blog import imagetopattern as imtp
from django.core.files.storage import FileSystemStorage

def getpath(files):
	return os.path.join(os.path.dirname(os.path.realpath(__file__)), files)
filepath=getpath('words.txt')

data=[{'name':'vignesh',
		'age':19,
		'message':'hello guys'},
		{'name':'ramesh',
		'age':24,
		'message':'i am rames'}]
# Create your views here.
def home(request):
	context={'data':data}
	return render(request,'blog/home.html',context)

def imagetopattern(request):
	if request.method == 'POST':
		imageform = ImageForm(request.POST, request.FILES)
		if imageform.is_valid():
			imageform.save()
			# Get the current instance object to display in the template
			img_obj = form.instance

			imtp.imgtoptn(getpath(img_obj.image.url),filepath)
			os.remove(getpath(img_obj.image.url))
			with open(filepath,'r',encoding='utf-8') as w: 
				return render(request, 'blog/imagetopattern.html', {'imageform': imageform,'location':getpath(img_obj.image.url), 'img_obj': img_obj,'lines':w.readlines()})
	else:
		imageform = ImageForm()
	    
	return render(request,'blog/imagetopattern.html',{'title':'imagetopattern','imageform':imageform})

