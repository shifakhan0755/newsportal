from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404,HttpResponse
from django.template.defaultfilters import slugify

from .models import EntertainmentModel,IPLModel,StateModel,CoronaModel,CareerModel,WorldModel,ContactModel,News
from adminpannel.models import Main
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
import requests
from .forms import SignupForm,LoginForm,tagForm,tagstateForm,tagcoronaForm,tagcareerForm,tagiplForm,tagworldForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group
import calendar
from calendar import HTMLCalendar
from taggit.models import Tag

# Create your views here.
def home(request):
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    b1 =EntertainmentModel.objects.all().filter(Q(title='b1'))
    b2 =EntertainmentModel.objects.all().filter(Q(title='b2'))
    t2 =EntertainmentModel.objects.all().filter(Q(title='t2'))
    b3 =EntertainmentModel.objects.all().filter(Q(title='b3'))
    h2 =EntertainmentModel.objects.all().filter(Q(title='h2'))
    television = EntertainmentModel.objects.filter(Q(title='t1'))
    t3 = EntertainmentModel.objects.filter(Q(title='t3'))
    h1 = EntertainmentModel.objects.filter(Q(title='h1'))
    uttarpradesh = StateModel.objects.all().filter(Q(title='hello'))
    ut = StateModel.objects.all().filter(Q(title='pm'))
    vaccine = CoronaModel.objects.all().filter(Q(title='shifa'))
    vacc = CoronaModel.objects.all().filter(Q(title='anas'))
    va1 = CoronaModel.objects.all().filter(Q(title='va1'))
    recovery = CoronaModel.objects.all().filter(Q(title='re1'))
    re1 = CoronaModel.objects.all().filter(Q(title='re2'))
    re3 = CoronaModel.objects.all().filter(Q(title='re3'))
    death1 = CoronaModel.objects.all().filter(title='death1')
    death2 = CoronaModel.objects.all().filter(title='death2')
    death3 = CoronaModel.objects.all().filter(title='death3')
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m1'))
    m2 = StateModel.objects.all().filter(Q(title='m2'))
    up1 = StateModel.objects.all().filter(Q(title='up1'))
    j2 = StateModel.objects.all().filter(Q(title='j2'))
    j1 = StateModel.objects.all().filter(Q(title='j1'))
    mp4 = StateModel.objects.all().filter(Q(title='mp4'))
    mp3 = StateModel.objects.all().filter(Q(title='mp3'))
    ncr3 = StateModel.objects.all().filter(Q(title='ncr3'))
    ncr4 = StateModel.objects.all().filter(Q(title='ncr4'))
    mp1 = StateModel.objects.all().filter(Q(title='mp1'))
    mp2 = StateModel.objects.all().filter(Q(title='mp2'))
    m3 = StateModel.objects.all().filter(Q(title='m3'))
    ch1 = StateModel.objects.all().filter(Q(title='ch1'))
    ch2 = StateModel.objects.all().filter(Q(title='ch2'))
    bihar1 = StateModel.objects.all().filter(Q(title='bihar1'))
    bihar2 = StateModel.objects.all().filter(Q(title='bihar2'))
    ipl1 = IPLModel.objects.all().filter(Q(title='ipl1'))
    ipl2 = IPLModel.objects.all().filter(Q(title='ipl2'))
    ipl3 = IPLModel.objects.all().filter(Q(title='ipl3'))
    ipl4 = IPLModel.objects.all().filter(Q(title='ipl4'))
    ipl5 = IPLModel.objects.all().filter(Q(title='ipl5'))
    education1 = CareerModel.objects.all().filter(Q(title='education1'))
    w1 = WorldModel.objects.all().filter(Q(title='w1'))
    w2 = WorldModel.objects.all().filter(Q(title='w2'))
    w3 = WorldModel.objects.all().filter(Q(title='w3'))
    w4 = WorldModel.objects.all().filter(Q(title='w4'))
    w5 = WorldModel.objects.all().filter(Q(title='w5'))
    stu = ContactModel.objects.last()
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b=Main.objects.all()
    a = Main.objects.exists()
    return render(request,'home.html',{'b':b1,'b2':b2,'t':television,'up':uttarpradesh,'v':vaccine,'r':recovery,'vacc':vacc,'da':death1,'da1':death2,'el':el,'ut':ut,'ncr1':ncr1,'ncr2':ncr2,'m1':m1,'ncr3':ncr3,'mp1':mp1,'mp2':mp2,'re1':re1,'va1':va1,'death3':death3,'t2':t2,'h1':h1,'t3':t3,'re3':re3,'ncr4':ncr4,'m2':m2,'up1':up1,'ch1':ch1,'ch2':ch2,'m3':m3,'bihar1':bihar1,'ipl1':ipl1,'bihar2':bihar2,'education1':education1,'w1':w1,'w2':w2,'w3':w3,'w4':w4,'w5':w5,'b3':b3,'h2':h2,'ipl2':ipl2,'ipl3':ipl3,'ipl4':ipl4,'ipl5':ipl5,'j1':j1,'j2':j2,'mp3':mp3,'mp4':mp4,'cc':newcount,'st':stu,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def contact(request):
    if request.method == 'POST':
        un = request.POST['name']
        en = request.POST['email']
        s = request.POST['subject']
        com = request.POST['comment']
        x = ContactModel.objects.create(name=un,email=en,subject=s,comment=com)
        messages.success(request, 'Congratulations!! You have send Successfully ')
        x.save()
    h1 = StateModel.objects.all().filter(Q(title='j1'))
    h2 = StateModel.objects.all().filter(Q(title='j2'))
    h3 = StateModel.objects.all().filter(Q(title='j3'))
    h4 = StateModel.objects.filter(Q(title='j4'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'contact.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def NewsEntertainment(request):
  stu = ContactModel.objects.last()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  b1 = EntertainmentModel.objects.all().filter(Q(title='b1'))
  b2 = EntertainmentModel.objects.all().filter(Q(title='b2'))
  t2 = EntertainmentModel.objects.all().filter(Q(title='t2'))
  b3 = EntertainmentModel.objects.all().filter(Q(title='b3'))
  h2 = EntertainmentModel.objects.all().filter(Q(title='h2'))
  t1 = EntertainmentModel.objects.filter(Q(title='t1'))
  t3 = EntertainmentModel.objects.filter(Q(title='t3'))
  h1 = EntertainmentModel.objects.filter(Q(title='h1'))
  h3 = EntertainmentModel.objects.filter(Q(title='h3'))
  t4 = EntertainmentModel.objects.filter(Q(title='t4'))
  b4 = EntertainmentModel.objects.filter(Q(title='b4'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  s = EntertainmentModel.objects.all().order_by('title')
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  p = Paginator(s,8)
  page_num = request.GET.get('page', 1)
  try:
      page = p.page(page_num)
  except PageNotAnInteger:
      page =p.page(1)
  except EmptyPage:
      page = p.page(p.num_pages)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'entertainment.html',{'bollywood':b1,'hollywood':b2,'t':t2,'up':b3,'v':h2,'r':t1,'da':t3,'h1':h1,'h3':h3,'t4':t4,'b4':b4,'items':page,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})


def NewsDetailEntertainment(request,slug):
  product = EntertainmentModel.objects.filter(slug=slug)
  if product.exists():
      product = product.first()
  else:
      return render(request,'404.html')
  common_tags = EntertainmentModel.tags.most_common()[:4]
  form = tagForm(request.POST)
  if form.is_valid():
      newspost = form.save(commit=False)
      newspost.a = slugify(newspost.title)
      newspost.save()
      form._save_m2m()

  nextpost =EntertainmentModel.objects.filter(slug__gt=product.slug).order_by('slug').first()
  prevpost =EntertainmentModel.objects.filter(slug__lt=product.slug).order_by('slug').last()
  stu = ContactModel.objects.last()
  if request.method == 'POST':
        un = request.POST['name']
        en = request.POST['email']
        s = request.POST['subject']
        com = request.POST['comment']
        x = ContactModel.objects.create(name=un, email=en, subject=s, comment=com)
        messages.success(request, 'Congratulations!! You have send Comment Successfully ')
        x.save()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  t1 = EntertainmentModel.objects.filter(Q(title='t1'))
  t3 = StateModel.objects.all().filter(Q(title='hello'))
  h1 = CoronaModel.objects.all().filter(Q(title='va1'))
  h3 = IPLModel.objects.all().filter(Q(title='ipl4'))
  h4 = WorldModel.objects.all().filter(Q(title='w1'))
  h5 = CareerModel.objects.all().filter(Q(title='education1'))
  h6 = StateModel.objects.all().filter(Q(title='ncr1'))
  h2 = StateModel.objects.all().filter(Q(title='ncr2'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'entertainmentdetail.html',{'product':product,'nextpost':nextpost,'prevpost':prevpost,'t1':t1,'t2':t3,'t3':h1,'t4':h3,'t5':h4,'t6':h5,'t7':h6,'t8':h2,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b,'common_tags':common_tags,'form':form})



def tagged(request,slug):
    tag = get_object_or_404(Tag,slug=slug)
    posts = EntertainmentModel.objects.filter(tags=tag)
    product = EntertainmentModel.objects.all()
    stu = ContactModel.objects.last()
    if request.method == 'POST':
        un = request.POST['name']
        en = request.POST['email']
        s = request.POST['subject']
        com = request.POST['comment']
        x = ContactModel.objects.create(name=un, email=en, subject=s, comment=com)
        messages.success(request, 'Congratulations!! You have send Comment Successfully ')
        x.save()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    t1 = EntertainmentModel.objects.filter(Q(title='t1'))
    t3 = StateModel.objects.all().filter(Q(title='hello'))
    h1 = CoronaModel.objects.all().filter(Q(title='va1'))
    h3 = IPLModel.objects.all().filter(Q(title='ipl4'))
    h4 = WorldModel.objects.all().filter(Q(title='w1'))
    h5 = CareerModel.objects.all().filter(Q(title='education1'))
    h6 = StateModel.objects.all().filter(Q(title='ncr1'))
    h2 = StateModel.objects.all().filter(Q(title='ncr2'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year = 2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year, month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'entertainmentdetail.html',{'product':product,'t1':t1,'t2':t3,'t3':h1,'t4':h3,'t5':h4,'t6':h5,'t7':h6,'t8':h2,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b,'tag':tag,'posts':posts})


def StateDetail(request,slug):
  product = StateModel.objects.filter(slug=slug)
  if product.exists():
      product = product.first()
  else:
      return render(request,'404.html')
  common_tags = StateModel.tags.most_common()[:4]
  form =tagstateForm(request.POST)
  if form.is_valid():
      newspost = form.save(commit=False)
      newspost.a = slugify(newspost.title)
      newspost.save()
      form._save_m2m()

  nextpost =StateModel.objects.filter(slug__gt=product.slug).order_by('slug').first()
  prevpost =StateModel.objects.filter(slug__lt=product.slug).order_by('slug').last()
  stu = ContactModel.objects.last()
  if request.method == 'POST':
        un = request.POST['name']
        en = request.POST['email']
        s = request.POST['subject']
        com = request.POST['comment']
        x = ContactModel.objects.create(name=un, email=en, subject=s, comment=com)
        messages.success(request, 'Congratulations!! You have send Comment Successfully ')
        x.save()
  ct = request.session.get('count',0)
  newcount = ct + 1
  request.session['count'] = newcount
  t1 = EntertainmentModel.objects.filter(Q(title='t1'))
  t3 = StateModel.objects.all().filter(Q(title='hello'))
  h1 = CoronaModel.objects.all().filter(Q(title='va1'))
  h3 = IPLModel.objects.all().filter(Q(title='ipl4'))
  h4 = WorldModel.objects.all().filter(Q(title='w1'))
  h5 = CareerModel.objects.all().filter(Q(title='education1'))
  h6 = StateModel.objects.all().filter(Q(title='ncr1'))
  h2 = StateModel.objects.all().filter(Q(title='ncr2'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'statedetail.html',{'nextpost':nextpost,'prevpost':prevpost,'product':product,'t1':t1,'t2':t3,'t3':h1,'t4':h3,'t5':h4,'t6':h5,'t7':h6,'t8':h2,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b,'common_tags':common_tags,'form':form})


def CoronaDetail(request,slug):
  product = CoronaModel.objects.filter(slug=slug)
  if product.exists():
      product = product.first()
  else:
      return render(request,'404.html')
  common_tags = CoronaModel.tags.most_common()[:4]
  form =tagcoronaForm(request.POST)
  if form.is_valid():
      newspost = form.save(commit=False)
      newspost.a = slugify(newspost.title)
      newspost.save()
      form._save_m2m()

  nextpost =CoronaModel.objects.filter(slug__gt=product.slug).order_by('slug').first()
  prevpost = CoronaModel.objects.filter(slug__lt=product.slug).order_by('slug').last()
  stu = ContactModel.objects.last()
  if request.method == 'POST':
      un = request.POST['name']
      en = request.POST['email']
      s = request.POST['subject']
      com = request.POST['comment']
      x = ContactModel.objects.create(name=un, email=en, subject=s, comment=com)
      messages.success(request, 'Congratulations!! You have send Successfully ')
      x.save()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  t1 = EntertainmentModel.objects.filter(Q(title='t1'))
  t3 = StateModel.objects.all().filter(Q(title='hello'))
  h1 = CoronaModel.objects.all().filter(Q(title='va1'))
  h3 = IPLModel.objects.all().filter(Q(title='ipl4'))
  h4 = WorldModel.objects.all().filter(Q(title='w1'))
  h5 = CareerModel.objects.all().filter(Q(title='education1'))
  h6 = StateModel.objects.all().filter(Q(title='ncr1'))
  h2 = StateModel.objects.all().filter(Q(title='ncr2'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'Coronadetail.html',{'nextpost':nextpost,'prevpost':prevpost,'product':product,'t1':t1,'t2':t3,'t3':h1,'t4':h3,'t5':h4,'t6':h5,'t7':h6,'t8':h2,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b,'common_tags':common_tags,'form':form})

def IPLDetail(request,slug):
  product = IPLModel.objects.filter(slug=slug)
  if product.exists():
      product = product.first()
  else:
      return render(request,'404.html')
  common_tags = IPLModel.tags.most_common()[:4]
  form = tagiplForm(request.POST)
  if form.is_valid():
      newspost = form.save(commit=False)
      newspost.a = slugify(newspost.title)
      newspost.save()
      form._save_m2m()

  nextpost =IPLModel.objects.filter(slug__gt=product.slug).order_by('slug').first()
  prevpost =IPLModel.objects.filter(slug__lt=product.slug).order_by('slug').last()
  stu = ContactModel.objects.last()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  t1 = EntertainmentModel.objects.filter(Q(title='t1'))
  t3 = StateModel.objects.all().filter(Q(title='hello'))
  h1 = CoronaModel.objects.all().filter(Q(title='va1'))
  h3 = IPLModel.objects.all().filter(Q(title='ipl4'))
  h4 = WorldModel.objects.all().filter(Q(title='w1'))
  h5 = CareerModel.objects.all().filter(Q(title='education1'))
  h6 = StateModel.objects.all().filter(Q(title='ncr1'))
  h2 = StateModel.objects.all().filter(Q(title='ncr2'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'ipldetail.html',{'nextpost':nextpost,'prevpost':prevpost,'product':product,'form':form,'t1':t1,'t2':t3,'t3':h1,'t4':h3,'t5':h4,'t6':h5,'t7':h6,'t8':h2,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def CareerDetail(request,slug):
  product = CareerModel.objects.filter(slug=slug)
  if product.exists():
      product = product.first()
  else:
      return render(request,'404.html')
  common_tags = CareerModel.tags.most_common()[:4]
  form = tagcareerForm(request.POST)
  if form.is_valid():
      newspost = form.save(commit=False)
      newspost.a = slugify(newspost.title)
      newspost.save()
      form._save_m2m()

  nextpost =CareerModel.objects.filter(slug__gt=product.slug).order_by('slug').first()
  prevpost =CareerModel.objects.filter(slug__lt=product.slug).order_by('slug').last()
  stu = ContactModel.objects.last()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  t1 = EntertainmentModel.objects.filter(Q(title='t1'))
  t3 = StateModel.objects.all().filter(Q(title='hello'))
  h1 = CoronaModel.objects.all().filter(Q(title='va1'))
  h3 = IPLModel.objects.all().filter(Q(title='ipl4'))
  h4 = WorldModel.objects.all().filter(Q(title='w1'))
  h5 = CareerModel.objects.all().filter(Q(title='education1'))
  h6 = StateModel.objects.all().filter(Q(title='ncr1'))
  h2 = StateModel.objects.all().filter(Q(title='ncr2'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'careerdetail.html',{'nextpost':nextpost,'prevpost':prevpost,'product':product,'t1':t1,'t2':t3,'t3':h1,'t4':h3,'t5':h4,'t6':h5,'t7':h6,'t8':h2,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b,'form':form})

def WorldDetail(request,slug):
  product = WorldModel.objects.filter(slug=slug)
  if product.exists():
      product = product.first()
  else:
      return render(request,'404.html')
  common_tags = WorldModel.tags.most_common()[:4]
  form = tagworldForm(request.POST)
  if form.is_valid():
      newspost = form.save(commit=False)
      newspost.a = slugify(newspost.title)
      newspost.save()
      form._save_m2m()

  nextpost =WorldModel.objects.filter(slug__gt=product.slug).order_by('slug').first()
  prevpost =WorldModel.objects.filter(slug__lt=product.slug).order_by('slug').last()
  stu = ContactModel.objects.last()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  t1 = EntertainmentModel.objects.filter(Q(title='t1'))
  t3 = StateModel.objects.all().filter(Q(title='hello'))
  h1 = CoronaModel.objects.all().filter(Q(title='va1'))
  h3 = IPLModel.objects.all().filter(Q(title='ipl4'))
  h4 = WorldModel.objects.all().filter(Q(title='w1'))
  h5 = CareerModel.objects.all().filter(Q(title='education1'))
  h6 = StateModel.objects.all().filter(Q(title='ncr1'))
  h2 = StateModel.objects.all().filter(Q(title='ncr2'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'worlddetail.html',{'form':form,'nextpost':nextpost,'prevpost':prevpost,'product':product,'t1':t1,'t2':t3,'t3':h1,'t4':h3,'t5':h4,'t6':h5,'t7':h6,'t8':h2,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def bollywood(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    b1 = EntertainmentModel.objects.all().filter(Q(title='b1'))
    b2 = EntertainmentModel.objects.all().filter(Q(title='b2'))
    b3 = EntertainmentModel.objects.all().filter(Q(title='b3'))
    b4 = EntertainmentModel.objects.filter(Q(title='b4'))
    b5= EntertainmentModel.objects.all().filter(Q(title='b5'))
    b6 = EntertainmentModel.objects.filter(Q(title='h3'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'bollywood.html',{'b1':b1,'b2':b2,'b3':b3,'b4':b4,'b5':b5,'b6':b6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def hollywood(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = EntertainmentModel.objects.all().filter(Q(title='h1'))
    h2 = EntertainmentModel.objects.all().filter(Q(title='h2'))
    h3 = EntertainmentModel.objects.all().filter(Q(title='h3'))
    h4 = EntertainmentModel.objects.filter(Q(title='h4'))
    h5= EntertainmentModel.objects.all().filter(Q(title='h5'))
    h6 = EntertainmentModel.objects.filter(Q(title='h6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'hollywood.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def television(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = EntertainmentModel.objects.all().filter(Q(title='t1'))
    h2 = EntertainmentModel.objects.all().filter(Q(title='t2'))
    h3 = EntertainmentModel.objects.all().filter(Q(title='t3'))
    h4 = EntertainmentModel.objects.filter(Q(title='t4'))
    h5= EntertainmentModel.objects.all().filter(Q(title='t5'))
    h6 = EntertainmentModel.objects.filter(Q(title='t6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'television.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def State(request):
  stu = ContactModel.objects.last()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  b1 = StateModel.objects.all().filter(Q(title='hello'))
  b2 = StateModel.objects.all().filter(Q(title='election'))
  t2 = StateModel.objects.all().filter(Q(title='pm'))
  b3 = StateModel.objects.all().filter(Q(title='ncr1'))
  h2 = StateModel.objects.all().filter(Q(title='ncr2'))
  t1 = StateModel.objects.all().filter(Q(title='m1'))
  t3 = StateModel.objects.all().filter(Q(title='ncr3'))
  h1 = StateModel.objects.all().filter(Q(title='mp1'))
  h3 = StateModel.objects.all().filter(Q(title='mp2'))
  t4 = StateModel.objects.all().filter(Q(title='ncr4'))
  b4 = StateModel.objects.all().filter(Q(title='j1'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  s = StateModel.objects.all().order_by('title')
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  p = Paginator(s,8)
  page_num = request.GET.get('page', 1)
  try:
      page = p.page(page_num)
  except PageNotAnInteger:
      page =p.page(1)
  except EmptyPage:
      page = p.page(p.num_pages)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'state.html',{'b1':b1,'h':b2,'t':t2,'up':b3,'v':h2,'r':t1,'da':t3,'h1':h1,'h3':h3,'t4':t4,'b4':b4,'items':page,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})



def ncr(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='ncr1'))
    h2 = StateModel.objects.all().filter(Q(title='ncr2'))
    h3 = StateModel.objects.all().filter(Q(title='ncr3'))
    h4 = StateModel.objects.all().filter(Q(title='ncr4'))
    h5 = StateModel.objects.all().filter(Q(title='ncr5'))
    h6 = StateModel.objects.all().filter(Q(title='ncr6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'ncr.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})


def uttarpradesh(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='hello'))
    h2 = StateModel.objects.all().filter(Q(title='election'))
    h3 = StateModel.objects.all().filter(Q(title='pm'))
    h4 = StateModel.objects.filter(Q(title='up1'))
    h5= StateModel.objects.all().filter(Q(title='up2'))
    h6 = StateModel.objects.filter(Q(title='up3'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'uttarpradesh.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def bihar(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='hello'))
    h2 = StateModel.objects.all().filter(Q(title='bihar2'))
    h3 = StateModel.objects.all().filter(Q(title='bihar3'))
    h4 = StateModel.objects.filter(Q(title='bihar4'))
    h5= StateModel.objects.all().filter(Q(title='bihar5'))
    h6 = StateModel.objects.filter(Q(title='bihar6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'bihar.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def uttarakhand(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='ut1'))
    h2 = StateModel.objects.all().filter(Q(title='ut3'))
    h3 = StateModel.objects.all().filter(Q(title='ut2'))
    h4 = StateModel.objects.filter(Q(title='ut4'))
    h5= StateModel.objects.all().filter(Q(title='ncr5'))
    h6 = StateModel.objects.filter(Q(title='bihar6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'uttarakhand.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def jharkhand(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='j1'))
    h2 = StateModel.objects.all().filter(Q(title='j2'))
    h3 = StateModel.objects.all().filter(Q(title='j3'))
    h4 = StateModel.objects.filter(Q(title='j4'))
    h5= StateModel.objects.all().filter(Q(title='j5'))
    h6 = StateModel.objects.filter(Q(title='ut4'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'jharkhand.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def rajasthan(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='r1'))
    h2 = StateModel.objects.all().filter(Q(title='r2'))
    h3 = StateModel.objects.all().filter(Q(title='r3'))
    h4 = StateModel.objects.filter(Q(title='r4'))
    h5= StateModel.objects.all().filter(Q(title='ncr5'))
    h6 = StateModel.objects.filter(Q(title='ncr6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'rajasthan.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def madhyapradesh(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='mp1'))
    h2 = StateModel.objects.all().filter(Q(title='mp2'))
    h3 = StateModel.objects.all().filter(Q(title='mp3'))
    h4 = StateModel.objects.filter(Q(title='mp4'))
    h5= StateModel.objects.all().filter(Q(title='mp5'))
    h6 = StateModel.objects.filter(Q(title='mp6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'madhyapradesh.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def maharashtra(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='m1'))
    h2 = StateModel.objects.all().filter(Q(title='hello'))
    h3 = StateModel.objects.all().filter(Q(title='m3'))
    h4 = StateModel.objects.filter(Q(title='up1'))
    h5= StateModel.objects.all().filter(Q(title='ncr5'))
    h6 = StateModel.objects.filter(Q(title='mp4'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'maharashtra.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def haryana(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='h1'))
    h2 = StateModel.objects.all().filter(Q(title='h2'))
    h3 = StateModel.objects.all().filter(Q(title='h3'))
    h4 = StateModel.objects.filter(Q(title='h4'))
    h5= StateModel.objects.all().filter(Q(title='ncr5'))
    h6 = StateModel.objects.filter(Q(title='ncr6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'haryana.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def chhattisgrah(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='ch1'))
    h2 = StateModel.objects.all().filter(Q(title='ch2'))
    h3 = StateModel.objects.all().filter(Q(title='pm'))
    h4 = StateModel.objects.filter(Q(title='up1'))
    h5= StateModel.objects.all().filter(Q(title='ncr5'))
    h6 = StateModel.objects.filter(Q(title='ncr6'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'chhattisgrah.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})

def himachalpradesh(request):
    stu = ContactModel.objects.last()
    ct = request.session.get('count', 0)
    newcount = ct + 1
    request.session['count'] = newcount
    h1 = StateModel.objects.all().filter(Q(title='m3'))
    h2 = StateModel.objects.all().filter(Q(title='ut4'))
    h3 = StateModel.objects.all().filter(Q(title='ncr2'))
    h4 = StateModel.objects.filter(Q(title='up1'))
    h5= StateModel.objects.all().filter(Q(title='r3'))
    h6 = StateModel.objects.filter(Q(title='j1'))
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'himachalpradesh.html',{'b1':h1,'b2':h2,'b3':h3,'b4':h4,'b5':h5,'b6':h6,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})


def country(request):
  stu = ContactModel.objects.last()
  ct = request.session.get('count',0)
  newcount = ct + 1
  request.session['count'] = newcount
  b1 = EntertainmentModel.objects.all().filter(Q(title='t3'))
  b2 = StateModel.objects.all().filter(Q(title='ch2'))
  t2 = StateModel.objects.all().filter(Q(title='h3'))
  b3 = StateModel.objects.all().filter(Q(title='ncr3'))
  h2 = StateModel.objects.all().filter(Q(title='h2'))
  t1 = StateModel.objects.filter(Q(title='mp2'))
  t3 = StateModel.objects.filter(Q(title='ncr3'))
  h1 = StateModel.objects.filter(Q(title='h1'))
  h3 = StateModel.objects.filter(Q(title='h3'))
  t4 = StateModel.objects.filter(Q(title='ncr4'))
  b4 = StateModel.objects.filter(Q(title='ut2'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  s = StateModel.objects.all().order_by('id')
  p = Paginator(s,8)
  page_num = request.GET.get('page', 1)
  try:
      page = p.page(page_num)
  except PageNotAnInteger:
      page =p.page(1)
  except EmptyPage:
      page = p.page(p.num_pages)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'country.html',{'bollywood':b1,'t':b2,'hollywood':t2,'up':b3,'v':h2,'r':t1,'da':t3,'h1':h1,'h3':h3,'t4':t4,'b4':b4,'items':page,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})




def ipl(request):
  stu = ContactModel.objects.last()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  b1 = IPLModel.objects.all().filter(Q(title='ipl1'))
  b2 = IPLModel.objects.all().filter(Q(title='ipl2'))
  t2 = IPLModel.objects.all().filter(Q(title='ipl3'))
  b3 = IPLModel.objects.all().filter(Q(title='ipl4'))
  h2 = IPLModel.objects.all().filter(Q(title='ipl5'))
  t1 = IPLModel.objects.filter(Q(title='ipl6'))
  t3 = IPLModel.objects.filter(Q(title='ipl7'))
  h1 = IPLModel.objects.filter(Q(title='ipl8'))
  h3 = IPLModel.objects.filter(Q(title='ipl9'))
  t4 = IPLModel.objects.filter(Q(title='ipl10'))
  b4 = IPLModel.objects.filter(Q(title='ipl11'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  s = IPLModel.objects.all().order_by('id')
  p = Paginator(s,8)
  page_num = request.GET.get('page', 1)
  try:
      page = p.page(page_num)
  except PageNotAnInteger:
      page =p.page(1)
  except EmptyPage:
      page = p.page(p.num_pages)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'ipl.html',{'bollywood':b1,'t':b2,'hollywood':t2,'up':b3,'v':h2,'r':t1,'da':t3,'h1':h1,'h3':h3,'t4':t4,'b4':b4,'items':page,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})


def corona(request):
  data = True
  gl = None
  country = None
  while (data):
        try:
            result = requests.get('https://api.covid19api.com/summary')
            gl = result.json()['Global']
            country = result.json()['Countries']
            data = False
        except:
            data = True
  stu = ContactModel.objects.last()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  b1 = CoronaModel.objects.all().filter(Q(title='shifa'))
  b2 = CoronaModel.objects.all().filter(Q(title='re1'))
  t2 = CoronaModel.objects.all().filter(Q(title='anas'))
  b3 = CoronaModel.objects.all().filter(Q(title='death1'))
  h2 = CoronaModel.objects.all().filter(Q(title='death2'))
  t1 = CoronaModel.objects.all().filter(Q(title='re2'))
  t3 = CoronaModel.objects.all().filter(Q(title='va1'))
  h1 = CoronaModel.objects.all().filter(Q(title='death3'))
  h3 = CoronaModel.objects.all().filter(Q(title='re3'))
  t4 = CoronaModel.objects.all().filter(Q(title='t4'))
  b4 = StateModel.objects.all().filter(Q(title='h3'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  s = CoronaModel.objects.all().order_by('title')
  p = Paginator(s,6)
  page_num = request.GET.get('page', 1)
  try:
      page = p.page(page_num)
  except PageNotAnInteger:
      page =p.page(1)
  except EmptyPage:
      page = p.page(p.num_pages)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'corona.html',{'bollywood':b1,'hollywood':b2,'t':t2,'up':b3,'v':h2,'r':t1,'da':t3,'h1':h1,'h3':h3,'t4':t4,'b4':b4,'items':page,'cc':newcount,'st':stu,'gl':gl,'country':country,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})



def career(request):
  stu = ContactModel.objects.last()
  if request.method == 'POST':
        un = request.POST['name']
        en = request.POST['email']
        s = request.POST['subject']
        com = request.POST['comment']
        x = ContactModel.objects.create(name=un, email=en, subject=s, comment=com)
        messages.success(request, 'Congratulations!! You have send Successfully ')
        x.save()
  ct = request.session.get('count', 0)
  newcount = ct + 1
  request.session['count'] = newcount
  b1 = CareerModel.objects.all().filter(Q(title='education1'))
  b2 = CareerModel.objects.all().filter(Q(title='e2'))
  t2 = CareerModel.objects.all().filter(Q(title='e3'))
  b3 = CareerModel.objects.all().filter(Q(title='e4'))
  h2 = CareerModel.objects.all().filter(Q(title='e5'))
  t1 = CareerModel.objects.filter(Q(title='e6'))
  t3 = CareerModel.objects.filter(Q(title='e7'))
  h1 = CareerModel.objects.filter(Q(title='e8'))
  h3 = CareerModel.objects.filter(Q(title='e9'))
  t4 = CareerModel.objects.filter(Q(title='e10'))
  b4 = CareerModel.objects.filter(Q(title='e11'))
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
  vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
  vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  s =CareerModel.objects.all().order_by('id')
  p = Paginator(s,4)
  page_num = request.GET.get('page', 1)
  try:
      page = p.page(page_num)
  except PageNotAnInteger:
      page =p.page(1)
  except EmptyPage:
      page = p.page(p.num_pages)
  b = Main.objects.all()
  a = Main.objects.exists()
  return render(request,'career.html',{'bollywood':b1,'hollywood':b2,'t':t2,'up':b3,'v':h2,'r':t1,'da':t3,'h1':h1,'h3':h3,'t4':t4,'b4':b4,'items':page,'cc':newcount,'st':stu,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})


def about(request):
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'may'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    b = Main.objects.all()
    a = Main.objects.exists()
    return render(request,'about.html',{'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})



#Logout Page
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

#Login Page
def user_login(request):
  b = Main.objects.all()
  a = Main.objects.exists()
  month = 'may'.capitalize()
  year = 2021
  month_numbers = list(calendar.month_name).index(month)
  month_numbers = int(month_numbers)
  cal = HTMLCalendar().formatmonth(year, month_numbers)
  el = StateModel.objects.all().filter(Q(title='election'))
  ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
  ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
  m1 = StateModel.objects.all().filter(Q(title='m3'))
  m2 = StateModel.objects.all().filter(Q(title='m1'))
  if not request.user.is_authenticated:
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user=authenticate(username=uname,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in Successfully !!')
                return HttpResponseRedirect('/')
    else:
      form=LoginForm()
    return render(request,'login.html',{'form':form,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})
  else:
      return HttpResponseRedirect('/')

#Signup Page
def user_signup(request):
  if request.user.is_authenticated:
    b = Main.objects.all()
    a = Main.objects.exists()
    month = 'May'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
           messages.success(request,'Congratulations!! You have Signin Successfully. ')
           user = form.save()
           group = Group.objects.get(name='author')
           user.groups.add(group)

    else:
          form = SignupForm()
    return render(request,'signin.html',{'form':form,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'month_numbers':month_numbers,'cal':cal,'a':a,'add':b})
  else:
      return HttpResponseRedirect('/login/')

def search(request):
    vaccine1 = CoronaModel.objects.all().filter(Q(title='vaccine1'))
    vaccine2 = CoronaModel.objects.all().filter(Q(title='vaccine2'))
    vaccine3 = CoronaModel.objects.all().filter(Q(title='vaccine3'))
    month = 'May'.capitalize()
    year=2021
    month_numbers = list(calendar.month_name).index(month)
    month_numbers = int(month_numbers)
    cal = HTMLCalendar().formatmonth(year,month_numbers)
    el = StateModel.objects.all().filter(Q(title='election'))
    ncr1 = StateModel.objects.all().filter(Q(title='ncr1'))
    ncr2 = StateModel.objects.all().filter(Q(title='ncr2'))
    m1 = StateModel.objects.all().filter(Q(title='m3'))
    m2 = StateModel.objects.all().filter(Q(title='m1'))
    b = Main.objects.all()
    a = Main.objects.exists()
    query=request.GET['query']
    if len(query) > 78:
        allpost = CoronaModel.objects.none()
    else:
       allpostcaption = CoronaModel.objects.filter(caption__icontains=query)
       allpostdiscription = CoronaModel.objects.filter(description__icontains=query)
       allpost = allpostcaption.union(allpostdiscription)
    if allpost.count() == 0:
        messages.warning(request,"No search result found. PLease refine your query")
    params = {'allpost':allpost,'query':query,'vaccine1':vaccine1,'vaccine2':vaccine2,'vaccine3':vaccine3,'month_numbers':month_numbers,'cal':cal,'re1':el,'m1':ncr1,'mp1':ncr2,'j1':m1,'ch1':m2,'a':a,'add':b}
    return render(request,'search.html',params)
