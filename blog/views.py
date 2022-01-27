from django.shortcuts import render
from .forms import ImageForm
import os,shutil
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
					'description':'Interactive bubbles '},
					{'author':'vignesh',
					'date':'28/08/2022',
					'title':'Data Visualization',
					'filename':jspath('datavis'),
					'thumbnail':jsppath+'datavis.gif',
					'description':'Interactive bubbles '}
					]
def getpage(folder,file):
	return f'blogcontent/{folder}/{file}.html'
folder='programming'
blogcontent=[{'author':'vignesh',
					'date':'24/07/2021',
					'title':'Image Encryption with python',
					'filename':getpage(folder,'imageencryption'),
					'thumbnail':bpath+'imgencryption.jpeg',
					'description':'I am going to show you how you can encrypt/decrypt images by moving the pixel positions'},
					{'author':'vignesh',
					'date':'24/07/2021',
					'title':'Image processing with python - Part 2',
					'filename':getpage(folder,'imageprocessing2'),
					'thumbnail':bpath+'imageprocessing2.jpeg',
					'description':'Second part of the blog Image Processing with python'},
					{'author':'vignesh',
					'date':'22/07/2021',
					'title':'Image processing with python - Part 1',
					'filename':getpage(folder,'imageprocessing'),
					'thumbnail':bpath+'imageprocessing.jpeg',
					'description':'In this blog i am going to discuss about Image Processing with python'},
					{'author':'vignesh',
					'date':'22/07/2021',
					'title':'Pattern programming with python',
					'filename':'blogcontent/patternprogramming.html',
					'thumbnail':bpath+'patternprogramming.JPG',
					'description':'Pattern programming will be very useful for beginners to understand about conditions(if,elseif,else) and loops(for ,while)'}
					]
tpath='photography/'
folder='photography'
photoblogcontent=[{'author':'Santhosh',
					'date':'26/07/2021',
					'title':'Eye',
					'filename':getpage(folder,'eyeimage1'),
					'thumbnail':tpath+'pic10.jpg',
					'description':'Camera of our body is eye'},
{'author':'Santhosh',
					'date':'27/07/2021',
					'title':'Hand',
					'filename':getpage(folder,'handimage'),
					'thumbnail':tpath+'pic1.jpg',
					'description':'This image is made by stacking 2 to 3 images and processing it'},

{'author':'Santhosh',
					'date':'28/07/2021',
					'title':'Spider',
					'filename':getpage(folder,'spiderimage'),
					'thumbnail':tpath+'pic11.jpg',
					'description':'Learn how to work hard from our spidy friend'},

{'author':'Santhosh',
					'date':'29/07/2021',
					'title':'Rose',
					'filename':'roseimage',
					'thumbnail':tpath+'pic12.jpg',
					'description':'Tiatnic rose may leave you, but this rose will never'},

{'author':'Santhosh',
					'date':'30/07/2021',
					'title':'Love birds',
					'filename':'birdimage',
					'thumbnail':tpath+'pic2.jpg',
					'description':'Nature is full of love. Just take a look at it'},

{'author':'Santhosh',
					'date':'31/07/2021',
					'title':'Eye',
					'filename':'eyeimage2',
					'thumbnail':tpath+'pic3.jpg',
					'description':'Never underestimate the power of your vision'},

{'author':'Santhosh',
					'date':'01/08/2021',
					'title':'Cat',
					'filename':'catimage',
					'thumbnail':tpath+'pic4.jpg',
					'description':'Pussy cat '},

{'author':'Santhosh',
					'date':'02/08/2021',
					'title':'Myna',
					'filename':'mynaimage',
					'thumbnail':tpath+'pic5.jpg',
					'description':"If nature is a sony, then Myna's are the Rockstars"},
{'author':'Santhosh',
					'date':'03/08/2021',
					'title':'Raindrop',
					'filename':'rainimage',
					'thumbnail':tpath+'pic6.jpg',
					'description':'Raindrops '},

{'author':'Santhosh',
					'date':'04/08/2021',
					'title':'Star Trials',
					'filename':'starimage',
					'thumbnail':tpath+'pic7.jpg',
					'description':'If you this you are useless, just look t the sky. It will teach you many lessons'},

{'author':'Santhosh',
					'date':'05/08/2021',
					'title':'Sun',
					'filename':'sunimage',
					'thumbnail':tpath+'pic8.jpg',
					'description':'A nice composition is like a extra life for an image'},

{'author':'Santhosh',
					'date':'06/08/2021',
					'title':'Butterfly',
					'filename':'butterflyimage',
					'thumbnail':tpath+'pic9.jpg',
					'description':'Just when the caterpillar thought the life was over, she began to fly. '}]


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
	blogcontent1=blogcontent.copy()
	blogcontent1.extend(photoblogcontent)
	context={'title':'blog','blogcontent':blogcontent1}
	
	
	if request.method == 'GET':
		if 'all' in request.GET:
			return render(request,'blog/blog.html',context)
			
		elif 'programming' in request.GET:
			context['blogcontent']=blogcontent
		elif 'photography' in request.GET:
			context['blogcontent']=photoblogcontent
		elif 'btn' in request.GET:
			a=request.GET.get('btn')
			print('sdsdad',a)
			if a==None:
				return render(request,'blog/blog.html',context)
			
			context={'title':a}
			#f'blogcontent/{a}.html'
			print(f'blogcontent/{a}.html')
			return render(request,a,context)
		return render(request,'blog/blog.html',context)	
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
		if request.POST.get('upload') == 'upload':
			imgpath=getpathmain(r'media\images')
			destpath=getpathmain(r'static\projectcontent\images\temp')
			files = [f for f in os.listdir(imgpath)]
			os.chdir(imgpath)
			for i in files:
				if not i == "heart.png":
					#os.remove(i)
					shutil.move(i,destpath)
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

