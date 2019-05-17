#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageForm
from .models import Image
# Create your views here.

@login_required(login_url='/account/login/')
@csrf_exempt
@ require_POST
def upload_image(request):
	form = ImageForm(data=request.POST)
	print(1,form,form.is_valid())
	if form.is_valid():
		print(1.2)
		try:
			print(2)
			new_item = form.save(commit=False)
			print(3)
			new_item.user=request.user
			print(4)
			new_item.save()
			form.save_m2m()
			print(5)
			return JsonResponse({'status':"1"})
		except:
			return JsonResponse({'status':"0"})

@login_required(login_url='/account/login/')
def list_images(request):
	images=Image.objects.filter(user=request.user)
	return render(request, 'image/list_images.html', {"images":images})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_image(request):
	image_id = request.POST['image_id']
	try:
		image = Image.objects.get(id=image_id)
		image.delete()
		return JsonResponse({'status':"1"})
	except:
		return JsonResponse({'status':"2"})
