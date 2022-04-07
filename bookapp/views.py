from django.shortcuts import render
from .models import bookData

def bookview(request):
    bookdet=bookData.objects.all()
    return render(request,'book.html',{'bookdet':bookdet})
    
