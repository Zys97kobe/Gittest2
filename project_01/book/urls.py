from django.urls import path
from book.views import create_book
from book.views import shop

urlpatterns = {
    path('create/',create_book),
    path('<city_id>/<shop_id>',shop),
}