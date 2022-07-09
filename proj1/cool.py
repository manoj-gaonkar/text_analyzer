from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    content={}
    return render(request, "textutils_1.html",content)

def home(Request):
    return HttpResponse('''<h1>New header in the background</h1>
<ul>
    <li>ok</li>
    <li>jana bhai</li>
</ul> ''')

def about(request):
    content ={
        "class":"5th sem",
        "hobbies":"video editing, learning new things"
    }
    return render(request,"about.html",content)


def removepunctuations(request):
    inputtext = request.GET.get("text","default")
    removepunctuations = request.GET.get("removepunctuations","off")
    spaceremover = request.GET.get("spaceremover","off")
    capitalize = request.GET.get("capitalize","off")
    lexanalyzer = request.GET.get("lexanalyzer","off")
    

    
    if(removepunctuations=="on"):
        result=""
        punctutations= ' ' ' !@#$%^&*()_/.,?><;:\ ' ' '
        analyzed=""
        for i in inputtext:
            if(i==" "):
                    analyzed=analyzed+" "
            if i not in punctutations:
                analyzed=analyzed+i
        result="Removed Punctuations result"
    elif(spaceremover=="on"):
        analyzed=""
        result=""
        for i in inputtext:
            if( i ==" "):
                pass
            else:
                analyzed=analyzed+i
        result="Space Removed result"
    elif(capitalize=="on"):
        result=""
        analyzed=""
        for i in inputtext:
            analyzed=analyzed+i.upper()
        result="Capitalized result"
    elif(lexanalyzer=="on"):
        result=""
        alpha,space,num,sentences=0,0,0,0
        analyzed=""
        words=len(inputtext.split())
        sentences=len(inputtext.split('.'))
        for i in inputtext:
            if(i.isalpha()):
                alpha+=1
            if(i==" "):
                space+=1
                continue
            if(i.isnumeric()):
                num+=1
    else:
        return HttpResponse("Your text has not been analyzed")
    result = { "Task": result , 
    "analyzedresult": analyzed ,
    "alpha":alpha,
    "words":words,
    "sentences":sentences-1,
    "spaces":space,
    "num":num,
    "totalwithspaces":alpha+space,
    "totalwithoutspaces":alpha
     }
    return render( request , "lexanalyzed.html" , result )