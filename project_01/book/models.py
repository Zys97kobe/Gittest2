from django.db import models

# Create your models here.
'''
1、需要继承自models.Model，基类，增删改查等
2、系统自动添加主键ID
3、字段：
    字段名 = model.类型(选项)
    字段名不要用关键字，class def 等
    不要用连续的下划线
4、类型：
    CharField
    BooleanField
    AutoField
    DateField
5、限制条件：
    lenth
    是否唯一 unique
    是否为空 null  blank
6、修改表名称

'''


class Book(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    pub_date = models.DateField(null=True)
    readcount = models.BigIntegerField(default=0)
    commentcount = models.BigIntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'Bookinfo'
        verbose_name = '书籍管理'

    def __str__(self):
        # 显示书籍名字
        return self.name


class PeopleInfo(models.Model):
    GENDER_CHOICE = {
        (1, 'male'),
        (2, 'feamle'),
    }

    name = models.CharField(max_length=100, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键，系统自动添加 _id,
    # 外键的级联操作，主表和从表，1对多
    # 级联操作：当主表的数据被删除后，从表的外键该怎么处理：
    # SET_NULL(设置为空) , CASCADE(一起删除) , SET_DEFAULT(设为默认值) ,DO_NOTHING(不做处理) ,PROTECT(保护主表数据不被删除)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'PeopleInfo'

class Userinfo(models.Model):

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length = 18, null=False)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'userInfo'
