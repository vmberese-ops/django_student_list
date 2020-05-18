from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, EditForm
# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def listings(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
		all_items = List.objects.all()
		context = {'all_items' : all_items}
		return render(request, 'listings.html', context)
	else:
		all_items = List.objects.all()
		context = {'all_items': all_items}
		return render(request, 'listings.html', context)

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	return redirect('listings')

def edit(request, list_id):
	if request.method == 'POST':
		list_item = List.objects.get(pk=list_id)
		form = EditForm(request.POST or None)
		if form.is_valid():
			list_item.lastname = form.cleaned_data.get("lastname")
			list_item.firstname = form.cleaned_data.get("firstname")
			list_item.course = form.cleaned_data.get("course")
			list_item.gender = form.cleaned_data.get("gender")
			list_item.yearlevel = form.cleaned_data.get("yearlevel")
			list_item.save()
		return redirect('listings')
	else:
		list_item = List.objects.get(pk=list_id)
		context = {"list_id": list_id, "list_item": list_item }
		return render(request, 'edit.html', context)