from django.http import HttpResponse
from django.shortcuts import render
def homepage(request) :
    return render(request,'homepage.html')
def removepunc(request):
    text = request.GET.get('text','default')
    removepunc = request.GET.get('removepunctutations','off')
    capitalize = request.GET.get('capitalize','off')
    counting = request.GET.get('charcount', 0)
    params={}
    params['analyzed'] = ""
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed= ""
        for char in text :
            if char not in punctuations:
                analyzed += char
                params['analyzed'] = analyzed
        text = analyzed

    params['caps'] = ""
    params['count'] = 0
    if counting == "on":
        params['count'] = len(text)
    if(capitalize == "on"):
        params['caps'] = text.upper()
    return render(request,'analyzetext.html',params)