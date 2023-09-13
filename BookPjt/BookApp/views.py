from django.shortcuts import render, redirect
from .models import Book_List
from .forms import BookForms

from django.http import HttpResponse

# Create your views here.
def index(request):
    Book = Book_List.objects.all()
    context = {'Book_lst': Book}
    return render(request, "index.html",context)


def detail(request,Bid):
    book=Book_List.objects.get(id=Bid)
    return render(request,"detail.html",{'book':book})
def add_book(request):
    if request.method=="POST":
        name = request.POST.get('name',)
        desc = request.POST.get('desc',)
        year = request.POST.get('year',)
        img = request.FILES['img']
        book=Book_List(name=name,desc=desc,year=year,img=img)
        book.save()
    return render(request,"add.html")
def update_book(request,id):
    book=Book_List.objects.get(id=id)
    form=BookForms(request.POST or None,request.FILES,instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'book':book})


def delete_book(request,id):
    if request.method == "POST":
        book=Book_List.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request,'delete.html')

