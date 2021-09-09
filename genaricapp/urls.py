from django.urls import path 
from genaricapp import views 
urlpatterns = [
    path('two/',views.ProductListView.as_view()),
    path('two/<int:pk>/',views.ProductDetailesView.as_view())
]