from django.shortcuts import render

def home_page(request):
    return render(request,'index.html')

def author_create(request):
    return render(request,'author/form.html')


def author_list(request):
    return render(request,'author/list.html')