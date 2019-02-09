
from django.http import HttpResponse

from django.shortcuts import render

import operator

def hello(request):
    return render(request,"homepage.html",{"vamsi":"Good Keep It Up.."})

def about(request):
    return render(request,"about.html")



def wordcount(request):
    inputword = request.GET['word']
    print(inputword)
    wordArray = inputword.split()
    print(wordArray)

    wordCountDictionary = {}

    for wd in wordArray:
        print(wd)
        if wd in wordCountDictionary:
            wordCountDictionary[wd] += 1
        else:
            wordCountDictionary[wd] = 1

    sortedList = sorted(wordCountDictionary.items(),key=operator.itemgetter(1),reverse=True)



    return render(request,"count.html",{"wc":len(wordArray),"words":sortedList})
