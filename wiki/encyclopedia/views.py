from django.http.response import HttpResponse
from django.shortcuts import render 
from . import util
from markdown2 import Markdown, markdown
from django.http import Http404
from random import randint



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def search(request):
    query = request.GET['q']
    searchresult = util.get_entry(query) 
    #params= {"entries": searchresult}
    return render(request,"encyclopedia/search.html",{
        "title" : query , "entries" : Markdown().convert(searchresult)},
        )


def wiki(request,entry):
    if entry not in util.list_entries():
        raise Http404
    content = util.get_entry(entry)
    return render(request,"encyclopedia/wiki.html",{
    "title": entry, "content": Markdown().convert(content)},
    )

def random(request):
    entries = util.list_entries()
    entry = entries[randint(0, len(entries) - 1)]
    return render (request , "encyclopedia/random.html",{
        "entries": entry
    })
    
def newpage(request):
    return render (request ,"encyclopedia/newpage.html")
    

def savenewpage(request):
    title1 = request.GET.get("title")
    content1 = request.GET.get("content")
    util.save_entry(title1,content1)
    Markdown().convert(util.get_entry(title1))
    return render(request,"encyclopedia/wiki.html",{
        "title1" : title1 
    })

def edit(request,entryedit):
    text1 = entryedit
    return render (request,"encyclopedia/edit.html",{"text":util.get_entry(text1)})

def saveedit(request):
    title1  = request.GET.get("text1")
    content1  = request.GET.get("textchanged")
    util.save_entry(title1, content1)
    
    return HttpResponse(Markdown().convert(util.get_entry(title1)))