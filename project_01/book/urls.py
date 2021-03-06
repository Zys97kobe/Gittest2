from django.urls import path
from book.views import create_book,delete_book,shop,school,register,method,\
    response,jsresponse,Redirect,set_Cookie,get_Cookie,del_Cookie,set_Session,get_Session,del_Session
from book.views import postAndget
from book.views import Class_view,Order


"""自定义转化器"""
class SchoolConverter:
    regex = '2[0-9]\d{5}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
"""注册转换器"""
from django.urls.converters import register_converter
register_converter(SchoolConverter,'school')

urlpatterns = [
    path('create/',create_book),
    # <占位符> 可以是任意的数字和字符组合,实际情况下通常字符串不能作为编号，要进行数据验证
    # <转换器：变量名> 转换器会对变量数据进行正则验证
    path('<int:prince_id>/<int:city_id>/<school:school_id>/',school),
    path('<int:city_id>/<int:shop_id>/',shop),
    path('delete/',delete_book),
    path('register/',register),
    path('method/',method),
    path('response/',response),
    path('jsresponse/',jsresponse),
    path('res/',Redirect),
    path('set_Cookie/',set_Cookie),
    path('get_Cookie/',get_Cookie),
    path('del_Cookie/',del_Cookie),
    path('set_Session/',set_Session),
    path('get_Session/',get_Session),
    path('del_Session/',del_Session),
    path('postAndget/',postAndget),
    ########类试图路由######
    path('classview/',Class_view.as_view()),

    ########多继承#########
    path('order/',Order.as_view())
]