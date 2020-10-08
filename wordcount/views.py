from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    input_text = request.GET['inputtext']
    itext_list = input_text.split()
    return render(request, 'count.html', {'itext':input_text, 'wc':len(itext_list)})