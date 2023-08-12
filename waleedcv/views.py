from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Detail


# for programmer cv
def index (request):
    return render (request, 'index.html')



#for fuckin contact table

def Get_detail (request):
    #form = Detail()
    #context = {'form' : form}
    if request.method == 'POST':
        form = Detail(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Success')
    else:
        form = Detail()
    return render (request,'index.html', {'form' : form})

#def success(request):
    return HttpResponse('Success!!!')

#for petroluem cv
def home (request):
    return render (request,'srt-resume.html')