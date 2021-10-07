from django import forms
from django.http.response import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . import util
import encyclopedia
import random
import markdown2
from markdown2 import Markdown
markdowner = Markdown()
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def displayEntry(request, entry):
    return render(request, "encyclopedia/entry.html",{
        "wantedEntry": entry,
        "entryList": util.list_entries(),
        "content" : markdowner.convert(util.get_entry(entry))
    })


def searchResult(request):
    result = []
    
    wantedSite = request.POST["q"]
    print(wantedSite)
    for item in util.list_entries():
        if wantedSite == item:
            return render(request, "encyclopedia/entry.html",{
                "wantedEntry": item,
                "entryList": util.list_entries(),
                "content" : util.get_entry(item)
        })
        elif wantedSite in item:
            result.append(item)
        
        else:
            continue

    return render(request, "encyclopedia/searchResult.html", {
        "result": result,
        "numResult" :len(result)
    })

def createNewPage(request):
    return render(request, "encyclopedia/createNewPage.html")


def add(request):

    print("sup")
    siteTitle = request.POST["title"]
    siteContent = request.POST["content"]
    

    if siteTitle not in util.list_entries():
        util.save_entry(siteTitle, siteContent)
        return render(request, "encyclopedia/entry.html",{
            "wantedEntry": siteTitle,
            "entryList": util.list_entries(),
            "content" : util.get_entry(siteTitle)
    })
    else:
        return HttpResponse("This site already existed")

def edit(request):
    siteTitle = request.POST.get('editTitle', False)

    return render(request, "encyclopedia/editContent.html",{
        "siteTitle" : siteTitle,
        "siteContent": util.get_entry(siteTitle)
    })



def postEdit(request):
    editedContent = request.POST.get('editedContent', False)
    editedTitle = request.POST.get('editedTitle', False)

    util.save_entry(editedTitle, editedContent)
    return displayEntry(request, editedTitle)


def getRandom(request):
    entries = util.list_entries()
    randomTitle = str(random.choices(entries))
    randomTitle = (randomTitle[2:-2])

    return displayEntry(request, randomTitle)