from django.urls import path  

from . import views 

urlpatterns = [
	path('', views.places),
	path('newplace', views.newplace),
	path('<int:id>', views.placeshow),
	path('<int:id>/edit', views.editplace),
	path('<int:id>/comments/new', views.newcomment),
	path('<int:id>/comments', views.addcomment),
	path('<int:id>/comments/<int:cid>/edit', views.editcomment),
	path('<int:id>/comments/<int:cid>', views.deluptcomment),	
]
