from django.shortcuts import render,redirect
from django.contrib import messages
from record.forms import addrecord
from record.models import Record



def home(request):
    record = Record.objects.all()
    
    return render(request,'index.html',{'record':record})


def add_record(request):
    forms = addrecord()
    if request.method =='POST':
            form = addrecord(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Record add successfully!')     
                return redirect('home')    
        
    return render(request,"add_record.html",{'forms':forms})

def delete_record(request,pk):
    delete_record=Record.objects.get(id=pk)
    delete_record.delete()
    messages.success(request,'Record deleted successfully')
    return redirect('home')


def update_record(request,pk):    
    current_record=Record.objects.get(id=pk)
    form = addrecord(request.POST or None,request.FILES or None,instance=current_record)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated successfully!')
        return redirect('home')
    return render(request,'update.html',{'form':form})
            