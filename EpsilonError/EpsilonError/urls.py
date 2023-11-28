from django.contrib import admin
from django.urls import path
import stockVisualizer.views
import playground.views
import news.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", stockVisualizer.views.home, name='home'),
    path('get_stock_data/', stockVisualizer.views.get_stock_data),
    path('playground/', playground.views.playground),
    path('news/', news.views.index, name='index')
]