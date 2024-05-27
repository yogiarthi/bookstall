from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def dummy_view(request):
    data = {"message": "This is a dummy response from Django."}
    return JsonResponse(data)

def Home(request):
    # return HttpResponse("<h1>welcome</h1>")
     return render(request,"booksale.html")

def Book(request):
    return render(request,"booksale.html")

