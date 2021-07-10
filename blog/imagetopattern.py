from PIL import Image
import numpy
import random

def multiple_uniform():
    p=['!','@','#','$','%','^','&','*','(',')','-','+','=']#your pattern is filled with this
    for i in range(s+1):
        p.append(p[i])
    return p
def multiple_random():
    p=['!','@','#','$','%','^','&','*','(',')','-','+','=']#your pattern is filled with this
    for i in range(s):
        p.append(p[i])
    return random.choice(p)
def single_uniform():
    p=u'❤️'#your pattern is filled with this
    return p

def imgtoptn(imgpath,filepath):
    img=Image.open(imgpath)#your png image location
    s=16#output pattern's size
    r=img.resize((s,s)).convert('LA')
    a=numpy.asarray(r)
    with open(filepath,'w',encoding='utf-8') as f:
        for i in range(s):
             print('\n',file=f)
             for j in range(s):       
                if min(a[i][j])>10:
                    #f.write(single_uniform())
                    print(single_uniform(),end='    ',file=f)#call your desired function here
                else:
                    print('     ',end='',file=f)
                j+=1
#imgtoptn(r'C:\Users\Home\Pictures\heart.png',r'E:\djangoproject\blog\words.txt')
#imgtoptn(img,r'E:\djangoproject\blog\words.txt')
# if you call multiple_uniform(), use multiple_uniform()[j] for vertical orientation, and use multiple_uniform()[i] for horizotal orientation
#  u can use unicode to print pattern with emoji