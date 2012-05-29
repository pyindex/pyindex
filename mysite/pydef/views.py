#!/usr/bin/env python
#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http    import HttpResponseRedirect

def funcs():
    res = ( {'cname':u'字符串类', 'fs':('def','def','def')}, 
            {'cname':u'时间类', 'fs':('def','def','def')},
        )
    return res
		
def intro(request): #
    return render_to_response('intro.html')
	
def index(request): #
    res = funcs()
    return render_to_response('index.html', locals())
		
def searchname(request, input):
    res = funcs()
    funcname = input
    if input == 'def': ##查询成功
        return render_to_response('showfunc.html', locals())
    else: ## 没有查询到， 寻找包含项
        if input == 'd': ## 寻找包含项
            return render_to_response('listfunc.html', locals())
        else: ## Nothing 
            return render_to_response('searcherror.html', locals())
			
def searchindex(request, input): #
    res = funcs()
    funcname = input
    return render_to_response('listindex.html', locals())
		
def edit_this_part(request): 
    res = funcs()
    return render_to_response('edit.html', locals())

def error(request): #
    res = funcs()
    return render_to_response('error.html', locals())
		
