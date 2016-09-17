# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, get_object_or_404
from jukebox.models import Room

def home(request):
	"""
	Landing page

	:template:`index.html`
	"""
	return render(request, 'index.html')


def rooms(request):
	"""
	Landing page

	:template:`room.html`
	"""
	return render(request, 'rooms.html')


def room(request, pk):
	"""
	Landing page

	:template:`room.html`
	"""
	room = get_object_or_404(Room, pk=pk)
	return render(request, 'room.html', context={ 'room' : room	})