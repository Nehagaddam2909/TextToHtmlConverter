
import markdown
from django.shortcuts import render
from django.http import HttpResponse
def getHome(request):
    return render(request,'main.html')


def result(request):
    if request.method=='POST':
        t=request.POST.get('text-area')
        #print(t)
        text = markdown.markdown(t)
        print(text)
        return render(request,'main.html',{"data":text,"input":t})
    else:
        return render(request,'main.html',{"data":None,"input":None})
