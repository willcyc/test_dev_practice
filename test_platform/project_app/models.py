from django.db import models

# Create your models here.
class Project(models.Model):
    """项目表"""
    name = models.CharField("名称",max_length=100,blank=False,default="") #https://www.cnblogs.com/linxiyue/p/3662535.html
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=True)
    create_time = models.DateTimeField("创建时间",auto_now=True)  #https://blog.csdn.net/davidsu33/article/details/49893055

    def __str__(self):
        return self.name

class Module(models.Model):
    """模块表"""
    project = models.ForeignKey(Project,on_delete=models.CASCADE) #https://blog.csdn.net/hpu_yly_bj/article/details/78927121
    name = models.CharField("名称", max_length=100, blank=False, default="")
    describe = models.TextField("描述", default="")
    create_time = models.DateTimeField("创建时间", auto_now=True)

    def __str__(self):
        return self.name