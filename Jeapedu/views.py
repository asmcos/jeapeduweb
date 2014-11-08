# -*- coding:UTF-8 -*-
from django.shortcuts import render_to_response
from Jeapedu.models import *
from django.template import RequestContext
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

def index(request):
	news     = News.objects.all()
	teachers = Teachers.objects.filter(order__lt=7).filter(kw="open").order_by("order")
	students = Students.objects.filter(order__lt=4).filter(kw="open").order_by("order")
	course   = Course.objects.filter(kw="open").order_by("order")
	d        = {'news':news,'teachers':teachers,'students':students,'course':course}
	return render_to_response('index_tag.html', d, context_instance=RequestContext(request))
	
def course(request):
	courses     = Course.objects.all()
	courses_num = Course.objects.all().count()
	d           = {'courses':courses,'courses_num':courses_num}
	return render_to_response('course.html', d, context_instance=RequestContext(request))
	
def teachers(request):
	teachers     = Teachers.objects.all()
	teachers_num = Teachers.objects.all().count()
	d            = {'teachers':teachers,'teachers_num':teachers_num}
	return render_to_response('teachers.html', d, context_instance=RequestContext(request))
	
def courseshow(request,id):
	course = Course.objects.get(id=int(id))
	d      = {'course':course}
	return render_to_response('courseshow.html', d, context_instance=RequestContext(request))

def paginator(request,id):
    courses  = Course.objects.order_by('-id')
    p        = Paginator(courses,5)
    try:
        p1 = p.page(id)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        p1 = p.page(1)

    after_range_num = 5
    before_range_num = 6

    if id >= after_range_num:
        page_range = p.page_range[int(id)-after_range_num:int(id)+before_range_num]
    else:
        page_range = p.page_range[0:int(id)+before_range_num]


    d        = {'courses':courses,'p':p,'count':p.count,'pages':p.num_pages,'p_list':page_range,
                'p1':p1,'has_previous':p1.has_previous(),'has_next':p1.has_next()}
    return render_to_response('course.html',d,context_instance=RequestContext(request))

def paginator_teachers(request,id):
    teacherss  = Teachers.objects.order_by('-id')
    p        = Paginator(teacherss,5)
    try:
        p1 = p.page(id)
    except(EmptyPage,InvalidPage,PageNotAnInteger):
        p1 = p.page(1)

    after_range_num = 5
    before_range_num = 6

    if id >= after_range_num:
        page_range = p.page_range[int(id)-after_range_num:int(id)+before_range_num]
    else:
        page_range = p.page_range[0:int(id)+before_range_num]


    d        = {'teacherss':teacherss,'p':p,'count':p.count,'pages':p.num_pages,'p_list':page_range,
                'p1':p1,'has_previous':p1.has_previous(),'has_next':p1.has_next()}
    return render_to_response('teachers.html',d,context_instance=RequestContext(request))

