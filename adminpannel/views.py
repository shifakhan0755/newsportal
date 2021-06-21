from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.utils import timezone
from django.contrib.auth.models import User
from home.models import CareerModel,EntertainmentModel, CoronaModel,StateModel,IPLModel,ContactModel,WorldModel
from .forms import EditAdminProfileForm,MainForm,EditUserProfileForm,UserForm,EntertainmentForm,CareerForm,CoronaForm,WorldForm,IPLForm,StateForm
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.files.storage import FileSystemStorage  # for upload image
from .models import Main

# Create your views here.
def careerModel(request):
    if request.method == 'POST':
        form = CareerForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! You have add Successfully ')
    else:
        form = CareerForm()
    posts =CareerModel.objects.all()
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request,'datatable.html',{'posts':posts,'st':stu,'message':ms,'form':form})

#delete post
def delete_post(request,id):
        if request.method == 'POST':
            pi=CareerModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/adminpannel11/')


def updatenews(request,id):
 if request.method == "POST":
    updatevar = CareerModel.objects.get(id=id)
    updatevar.title = request.POST['title']
    updatevar.caption = request.POST['caption']
    updatevar.description =  request.POST['description']
    updatevar.detail_description= request.POST['detail_description']
    updatevar.category = request.POST['category']
    updatevar.s_image = request.POST['image']
    updatevar.save()
    return redirect('/adminpannel11/')
    #messages.success(request, 'Record Update Successfully ')
 else:
     pi = CareerModel.objects.get(id=id)
     return render(request, 'updatepost.html', {'fm': pi})


def contactModel(request):
    posts = ContactModel.objects.all()
    stu = ContactModel.objects.last()
    return render(request,'contactmodel.html',{'posts':posts,'st':stu})

#delete post
def delete_contact(request,id):
        if request.method == 'POST':
            pi = ContactModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/contactmodel/')

def coronavirusModel(request):
    if request.method == 'POST':
        form = CoronaForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! You have add Successfully ')
    else:
        form = CoronaForm()
    posts = CoronaModel.objects.all()
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request,'coronavirusmodel.html',{'posts':posts,'st':stu,'message':ms,'form':form})

#delete post
def delete_coronavirus(request,id):
        if request.method == 'POST':
            pi = CoronaModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/adminpannel11/coronavirusmodel/')

def updatecorona(request,id):
 if request.method == "POST":
    updatevar = CoronaModel.objects.get(id=id)
    updatevar.title = request.POST['title']
    updatevar.caption = request.POST['caption']
    updatevar.description =  request.POST['description']
    updatevar.d_description= request.POST['detail_description']
    updatevar.s_image = request.POST['image']
    updatevar.save()
    return redirect('/adminpannel11/coronavirusmodel/')
    #messages.success(request, 'Record Update Successfully ')
 else:
     pi = CoronaModel.objects.get(id=id)
     return render(request, 'updatecorona.html', {'fm': pi})

def entertainmentModel(request):
    posts = EntertainmentModel.objects.all()
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    if request.method == 'POST':
        form = EntertainmentForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! You have add Successfully ')
    else:
        form = EntertainmentForm()
    return render(request,'entertainmentmodel.html',{'posts':posts,'st':stu,'message':ms,'form':form})


#delete post
def entertaindel(request,id):
        if request.method == 'POST':
            pi = EntertainmentModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/entertainmentmodel/')
        return HttpResponse('no delete')

def updateentertainment(request,id):
 if request.method == "POST":
    updatevar = EntertainmentModel.objects.get(id=id)
    updatevar.title = request.POST['title']
    updatevar.caption = request.POST['caption']
    updatevar.description =  request.POST['description']
    updatevar.d_description= request.POST['detail_description']
    updatevar.category = request.POST['category']
    updatevar.s_image = request.POST['image']
    updatevar.tags = request.POST['tags']
    updatevar.save()
    return redirect('/adminpannel11/entertainmentmodel/')
    #messages.success(request, 'Record Update Successfully ')
 else:
     pi = EntertainmentModel.objects.get(id=id)
     return render(request, 'updateentertainment.html', {'fm': pi})

def iplModel(request):
    if request.method == 'POST':
        form = IPLForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! You have add Successfully ')
    else:
        form = IPLForm()
    posts = IPLModel.objects.all()
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request,'iplmodel.html',{'posts':posts,'st':stu,'message':ms,'form':form})

#delete post
def ipldel(request,id):
        if request.method == 'POST':
            pi = IPLModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/adminpannel11/iplmodel/')
        return HttpResponse('no delete')

def updateipl(request,id):
 if request.method == "POST":
    updatevar = IPLModel.objects.get(id=id)
    updatevar.title = request.POST['title']
    updatevar.caption = request.POST['caption']
    updatevar.description =  request.POST['description']
    updatevar.d_description= request.POST['detail_description']
    updatevar.s_image = request.POST['image']
    updatevar.save()
    return redirect('/adminpannel11/iplmodel/')
    #messages.success(request, 'Record Update Successfully ')
 else:
     pi = IPLModel.objects.get(id=id)
     return render(request, 'updateipl.html', {'fm': pi})

def worldModel(request):
    if request.method == 'POST':
        form = WorldForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! You have add Successfully ')
    else:
        form = WorldForm()
    posts = WorldModel.objects.all()
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request,'worldmodel.html',{'posts':posts,'st':stu,'message':ms,'form':form})

#delete post
def worlddel(request,id):
        if request.method == 'POST':
            pi = WorldModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/adminpannel11/worldmodel/')
        return HttpResponse('no delete')

def updateworld(request,id):
 if request.method == "POST":
    updatevar = WorldModel.objects.get(id=id)
    updatevar.title = request.POST['title']
    updatevar.caption = request.POST['caption']
    updatevar.description =  request.POST['description']
    updatevar.detail_description= request.POST['detail_description']
    updatevar.s_image = request.POST['image']
    updatevar.save()
    return redirect('/adminpannel11/worldmodel/')
    #messages.success(request, 'Record Update Successfully ')
 else:
     pi = WorldModel.objects.get(id=id)
     return render(request, 'updatestate.html', {'fm': pi})



def stateModel(request):
    if request.method == 'POST':
        form = StateForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations!! You have add Successfully ')
    else:
        form = StateForm()
    posts = StateModel.objects.all()
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    s = StateModel.objects.all().order_by('id')
    p = Paginator(s, 5)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except PageNotAnInteger:
        page = p.page(1)
    except EmptyPage:
        page = p.page(p.num_pages)
    return render(request,'statemodel.html',{'posts':posts,'st':stu,'message':ms,'items':page,'form':form})


#delete post
def statedel(request,id):
        if request.method == 'POST':
            pi = StateModel.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/adminpannel11/statemodel/')
        return HttpResponse('no delete')

def updatestate(request,id):
 if request.method == "POST":
    updatevar = StateModel.objects.get(id=id)
    updatevar.title = request.POST['title']
    updatevar.caption = request.POST['caption']
    updatevar.description =  request.POST['description']
    updatevar.d_description= request.POST['detail_description']
    updatevar.s_image = request.POST['image']
    updatevar.save()
    return redirect('/adminpannel11/statemodel/')
    #messages.success(request, 'Record Update Successfully ')
 else:
     pi = StateModel.objects.get(id=id)
     return render(request, 'updatestate.html', {'fm': pi})


def careerdetailmodel(request,pk):
    product = CareerModel.objects.get(pk=pk)
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request, 'careermodeldetail.html', {'product': product,'st':stu,'message':ms})

def coronavirusdetailmodel(request,pk):
    product = CoronaModel.objects.get(pk=pk)
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request, 'careermodeldetail.html', {'product': product,'st':stu,'message':ms})

def statedetailmodel(request,pk):
    product = StateModel.objects.get(pk=pk)
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request, 'statedetailmodel.html', {'product': product,'st':stu,'message':ms})

def worlddetailmodel(request,pk):
    product = WorldModel.objects.get(pk=pk)
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request, 'careermodeldetail.html', {'product': product,'st':stu,'message':ms})

def ipldetailmodel(request,pk):
    product = IPLModel.objects.get(pk=pk)
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request, 'careermodeldetail.html', {'product': product,'st':stu,'message':ms})

def entertainmentdetailmodel(request,pk):
    product = EntertainmentModel.objects.get(pk=pk)
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request, 'careermodeldetail.html', {'product': product,'st':stu,'message':ms})

def Edit_profile(request):
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    users = User.objects.all()
    return render(request,'editprofile.html',{'st':stu,'message':ms,'users':users})

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST,instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST,instance=request.user)
                users = None
                if fm.is_valid():
                    fm.save()
        else:
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance=request.user)
                users = None
        stu = ContactModel.objects.last()
        ms = ContactModel.objects.all()
        return render(request,'profile.html',{'name':request.user,'form':fm,'users':users,'st':stu,'message':ms})
    else:
        return HttpResponseRedirect('/login/')


def site_setting(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('/login/')  # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    if request.method == 'POST':
        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        link = request.POST.get('link')
        txt = request.POST.get('txt')
        addre = request.POST.get('address')
        email = request.POST.get('email')
        x = Main.objects.create(name=name,address=addre, tell=tell, fb=fb, tw=tw,yt=yt,lin=link,about=txt,email=email)
        messages.success(request, 'Congratulations!! You have send Successfully ')
        x.save()
        ## Values saved end

        ## To control social media Start
        if fb == "": fb = "#"  # hashtag would be automatically set inside it
        if tw == "": tw = "#"
        if yt == "": yt = "#"
        if link == "": link = "#"
        ## To control social media End
    stu = ContactModel.objects.last()
    ms = ContactModel.objects.all()
    return render(request, 'setting.html',{'st':stu,'message':ms})
##--#--## Site Settings (Topbar, fb/yt/tw link, logo etc) Function For Back (Admin Panel - Backend) End ##--#--##

def user_detail(request,id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditAdminProfileForm(instance=pi)
        stu = ContactModel.objects.last()
        ms = ContactModel.objects.all()
        return render(request,'userdetail.html',{'form':fm,'st':stu,'message':ms})
    else:
        return HttpResponseRedirect('/login/')

def user_create(request):
  if request.user.is_authenticated:
     stu = ContactModel.objects.last()
     ms = ContactModel.objects.all()
     if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have Add Successfully. ')
            form.save()

     else:
        form = UserForm()
     return render(request, 'adduser.html', {'form': form,'st':stu,'message':ms})
  else:
     return HttpResponseRedirect('/login/')

