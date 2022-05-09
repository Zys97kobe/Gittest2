from django.urls import path
from book.views import create_book,delete_book,shop,school

urlpatterns = {
    path('create/',create_book),
    # <占位符> 可以是任意的数字和字符组合
    path('<prince_id>/<city_id>/<school_id>/',school),
    path('<city_id>/<shop_id>/',shop),
    path('delete/',delete_book),
}