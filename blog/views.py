from django.shortcuts import render
from .forms import ImageForm
import os
from blog import imagetopattern as imtp
from django.core.files.storage import FileSystemStorage

def getpathmain(files):#path of files from main directory
	settings_dir = os.path.dirname(__file__)
	PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
	path = os.path.join(PROJECT_ROOT, files)
	return path
def getpathcwd(files):#path of files in current working directory
	return os.path.join(os.path.dirname(os.path.realpath(__file__)), files)
filepath=getpathcwd('words.txt')
# Create your views here.


def home(request):
	context={'title':'home','blogcontent':blogcontent[:2],'range':[pic(1,3),pic(3,5),pic(5,9)]}
	return render(request,'blog/home1.html',context)
bpath=r'blogcontent/images/'
ppath=r'projectcontent/images/'
jsppath=r'projectcontent/images/javascript/'
projectcontent=[{'author':'vignesh',
					'date':'24/07/2021',
					'title':'Javascript Projects',
					'filename':'javascriptprojects',
					'thumbnail':ppath+'javascript.png',
					'description':'This section contains my interactable javascript projects '},
					]
def jspath(a):
	return f'projectcontent/p5/{a}/index.html'
javascriptprojectcontent=[{'author':'vignesh',
					'date':'24/07/2021',
					'title':'Bouncing Ball',
					'filename':jspath('bouncingball'),
					'thumbnail':jsppath+'bouncingball.gif',
					'description':'Interactive Bouncing Ball '},
					{'author':'vignesh',
					'date':'24/07/2021',
					'title':'Bubbles',
					'filename':jspath('bubbles'),
					'thumbnail':jsppath+'bubbles.gif',
					'description':'Interactive bubbles '}
					]
blogcontent=[{'author':'vignesh',
					'date':'24/07/2021',
					'title':'Image Encryption with python',
					'filename':'imageencryption',
					'thumbnail':bpath+'imgencryption.jpeg',
					'description':'I am going to show you how you can encrypt/decrypt images by moving the pixel positions'},
					{'author':'vignesh',
					'date':'24/07/2021',
					'title':'Image processing with python - Part 2',
					'filename':'imageprocessing2',
					'thumbnail':bpath+'imageprocessing2.jpeg',
					'description':'Second part of the blog Image Processing with python'},
					{'author':'vignesh',
					'date':'22/07/2021',
					'title':'Image processing with python',
					'filename':'imageprocessing',
					'thumbnail':bpath+'imageprocessing.jpeg',
					'description':'In this blog i am going to discuss about Image Processing with python'},
					{'author':'vignesh',
					'date':'22/07/2021',
					'title':'Pattern programming with python',
					'filename':'patternprogramming',
					'thumbnail':bpath+'patternprogramming.JPG',
					'description':'Pattern programming will be very useful for beginners to understand about conditions(if,elseif,else) and loops(for ,while)'}
					]
def about(request):
	context={'title':'about'}
	return render(request,'blog/about.html',context)
def pic(a,b):
	return [f'photography/pic{i}.jpg' for i in range(a,b)]

def photography(request):
	
	context={'title':'photography','range':[pic(1,4),pic(4,7),pic(7,10),pic(10,12)]}
	print(context['range'])
	return render(request,'blog/photography.html',context)

def myblog(request):
	context={'title':'blog','blogcontent':blogcontent}
	
	
	if request.method == 'GET':
		a=request.GET.get('btn')
		
		if a==None:
			return render(request,'blog/blog.html',context)
		
		context={'title':a}
		#f'blogcontent/{a}.html'
		print(f'blogcontent/{a}.html')
		return render(request,f'blogcontent/{a}.html',context)	
	return render(request,'blog/myblog.html',context)



def projects(request):
	context={'title':'blog','blogcontent':projectcontent}
	
	
	if request.method == 'GET':
		a=request.GET.get('btn')
		
		if a==None:
			return render(request,'blog/project.html',context)
		
		context={'title':a}
		#f'blogcontent/{a}.html'
		print(a)
		print(f'project/{a}.html')
		return render(request,f'project/{a}.html',context)	
	return render(request,'blog/myblog.html',context)

def javascriptprojects(request):
	context={'title':'javascriptprojects','blogcontent':javascriptprojectcontent}
	
	
	if request.method == 'GET':
		a=request.GET.get('btn')
		
		if a==None:
			return render(request,'project/javascriptprojects.html',context)
		
		context={'title':a}
		#f'blogcontent/{a}.html'
		print(a)
		print(f'project/{a}.html')
		return render(request,f'project/{a}.html',context)	
	return render(request,'blog/myblog.html',context)


def imagetopattern(request):

	if request.method == 'POST':
		imageform = ImageForm(request.POST, request.FILES)
		context={'title':'imagetopattern','imageform':imageform,'lct':'40','uct':'200','resolution':'10','yourimage':'your image'}
		context['resolution']=request.POST.get('resolution')
		lcolour=request.POST.get('lct')
		context['lct']=lcolour
		ucolour=request.POST.get('uct')
		context['uct']=ucolour
		#print('clr',lcolour,ucolour)
		if request.POST.get('button') == 'pressed':
			imgpath=getpathmain(r'media\images')
			files = [f for f in os.listdir(imgpath)]
			os.chdir(imgpath)
			for i in files:
				if not i == "heart.png":
					os.remove(i)
			return render(request,'blog/imagetopattern.html',context)
		
		elif imageform.is_valid():
			imgfunction=context['imageform'].cleaned_data['imgfunction']
			character=context['imageform'].cleaned_data['name']
			if character=="":
				character='-'
			resolution=request.POST.get('resolution')
			imageform.save()
			# Get the current instance object to display in the template
			img_obj = imageform.instance
			imgpath=getpathcwd(img_obj.image.url)
			if imgpath[len(imgpath)-9:]=='heart.png':
				context['yourimage']='default image - heart.png'
			imtp.imgtoptn(imgpath,filepath,imgfunction,resolution,c=character,l=lcolour,u=ucolour)
			with open(filepath,'r',encoding='utf-8') as w:
				#debugcontext={'post':imageform.cleaned_data}
				newcontext={'mytext':w.read(), 'img_obj': img_obj,'lines':w.readlines()}
				context.update(newcontext)
				return render(request, 'blog/imagetopattern.html',context )
	else:
		imageform = ImageForm()
		context={'title':'imagetopattern','imageform':imageform}
		return render(request,'blog/imagetopattern.html',context)

