from django.shortcuts import render
from .models import Place, Comment
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.



def places(request):
	if(request.method=="POST"):
		name = request.POST.get('name')
		price = request.POST.get('price')
		image = request.POST.get('image')
		description = request.POST.get('description')
		author = request.user
		place = Place(name=name, price=price, image=image, description=description, author=author)
		place.save()
		messages.success(request, "Successfuly added Place!!!")
	return render(request, 'places/places.html', {'places': Place.objects.all()})

def newplace(request):
	if(request.user.is_authenticated):
		return render(request, 'places/new.html')
	else:
		messages.error(request, "Please login first!!!")
		return redirect('/login/')


def	placeshow(request, id):
	if(request.GET.get('method') == "DELETE"):
		Place.objects.filter(id=id).delete()
		messages.success(request, "Successfuly deleted Place!!!")
		return redirect('/')

	if(request.GET.get('method') == "PUT"):
		place = Place.objects.filter(id=id)[0]
		place.name = request.POST.get('name')
		place.price = request.POST.get('price')
		place.image = request.POST.get('image')
		place.description = request.POST.get('description')
		place.save()
		messages.success(request, "Successfuly updated Place!!!")
		return redirect('/' + str(id))

	place = Place.objects.filter(id=id)[0]
	return render(request, 'places/show.html', {'place': place})


def editplace(request, id):
	place = Place.objects.filter(id=id)[0]
	return render(request, 'places/edit.html', {'place': place})
	

def newcomment(request, id):
	if(request.user.is_authenticated):
		place = Place.objects.filter(id=id)[0]
		return render(request, 'comments/new.html', {'place': place})
	else:
		messages.error(request, "Please login first!!!")
		return redirect('/login/')


def editcomment(request, id, cid):
	comment = Comment.objects.filter(id=cid)[0]
	return render(request, 'comments/edit.html', {'comment':comment,'place_id':id})


def addcomment(request, id):
	place = Place.objects.filter(id=id)[0]
	text = request.POST.get('text')
	author = request.user
	comment = Comment(text=text, author=author)
	comment.save()
	place.comments.add(comment)
	place.save()
	messages.success(request, "Successfuly added comment!!!")
	return redirect('/' + str(id))


def deluptcomment(request, id, cid):
	comment = Comment.objects.filter(id=cid)[0]
	if(request.GET.get('method') == "PUT"):
		comment.text = request.POST.get('text')
		comment.save()
		messages.success(request, "Successfuly updated comment!!!")
	if(request.GET.get('method') == "DELETE"):
		comment.delete()
		messages.success(request, "Successfuly deleted comment!!!")
	return redirect('/' + str(id))


