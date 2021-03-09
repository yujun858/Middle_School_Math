# 单表查询
## ORM 关系数据库(第一课)
```
from django.db import connection
def showsql()
    print(connection.queries[-1]['sql'])
```
### 查询单个对象
Movie 继承 Model类
```
Movie.objects.get(mid='147')
```
```
改变对象输出 models中
def __str__(self):
    return u"Movie:%s"%self.mid
```
```
Movie.objects.filter(mid='147')
QuerySet
输入mid不存在：get返回异常, filter返回null
```
```
获取第一个 first()
获取最后一个 last()
获取个数 count()
```
### 查询多个对象
```
切片
Movie.objects.all()[0:20]
```
```
模糊查询
Movie.objects.filter(mname__endswith='爱情')
Movie.objects.filter(name__startdswith='爱情'）
Movie.objects.filter(name__contains='爱情')
Movie.object.filter(name_exact='爱情')完全相等
```
### 部分字段查询
```
Movie.objects.values('mid','mane').filter(mid=44474)
```
### 除外
```
Movie.objects.filter(mname__icontains='H').exclude(mid=4443)
```
## ORM（第二课程)
```
升序： Movie.objects.order_by('mid')
降序: Movie.objecgts.oreder_by('-mid')
日期查询大于某个日期: Movie.objects.filter(created__gt='2017-10-20')
Movie.objects.filter(created_in='10,20,30')
Movie.objects.filter(created_range=’1,2,3)
```
## ORM (增删改)
```
Movie.objects.create(mid=10002,)
Move.objects.filter(name_startswith='h').delete()
Post.objects.filter(id=26).update(title='又更新了'）
post.save()持久化
```
# 多表查询

