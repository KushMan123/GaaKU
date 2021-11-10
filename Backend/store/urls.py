from django.urls import path
from . import views


urlpatterns = [
    path('', views.pmainpage, name='pmainpage'),
    path('pdescription/<int:pk>/', views.pdescription, name='pdescription'),
    path('Landing/', views.Landingpage, name='Landingpage'),
    path('notify/me', views.lookingfor, name='lookingfor'),
    path('<category>', views.category, name='category'),
    path('<category1>/<category2>', views.subcategory1, name='subcategory1'),
    path('<category1>/<category2>/<category3>',
         views.subcategory2, name="subcategory2"),
    path('search/', views.search, name='search'),
    path('add_to_whishlist/<int:pk>/',
         views.add_to_whishlist, name='add_to_whishlist'),
    path('comment/show', views.commentview, name='comment'),
]
