from django.shortcuts import render
from .forms import*
# Create your views here.
def signup(request):
  form=myform()
  return render(request,'signup.html',{'form':form})
