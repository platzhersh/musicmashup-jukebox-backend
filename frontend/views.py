# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

def home(request):
  """
  Landing page

  :template:`chat.html`
  """
  return render(request, 'chat.html')