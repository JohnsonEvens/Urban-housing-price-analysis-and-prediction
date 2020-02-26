#作者：王皓平 创建时间：2019.8.22 最后修改时间：2019.8.26
from django.db import models

# Create your models here.
class House(models.Model):
    properties= models.CharField(max_length=40)#楼盘
    city = models.CharField(max_length=20)#城市
    district = models.CharField(max_length=20)#区
    site1 = models.CharField(max_length=50)#地址1
    site2 = models.CharField(max_length=50)#地址2
    layout = models.CharField(max_length=30)#户型
    area = models.CharField(max_length=30)#面积
    price = models.CharField(max_length=30)#价格
    unit = models.CharField(max_length=30)#单位
    picture = models.CharField(max_length=110)#图片地址
    developer = models.CharField(max_length=80)#开发商
    park = models.CharField(max_length=70)#车位
    water = models.CharField(max_length=20)#供水
    kind = models.CharField(max_length=30)#建筑类型
    warm = models.CharField(max_length=20)#供暖
    ele = models.CharField(max_length=20)#供电
    fee = models.CharField(max_length=30)#物业费
    wkind = models.CharField(max_length=30)#物业类型

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.properties

class HouseInfo(models.Model):
    properties= models.CharField(max_length=20)#楼盘
    city = models.CharField(max_length=10)#城市
    district = models.CharField(max_length=10)#区
    site1 = models.CharField(max_length=30)#地址1
    site2 = models.CharField(max_length=30)#地址2
    layout = models.CharField(max_length=20)#户型
    area = models.CharField(max_length=20)#面积
    price = models.CharField(max_length=20)#价格
    unit = models.CharField(max_length=20)#单位
    picture = models.CharField(max_length=50)#图片地址
    developer = models.CharField(max_length=20)#开发商
    park = models.CharField(max_length=20)#车位
    water = models.CharField(max_length=10)#供水
    kind = models.CharField(max_length=20)#建筑类型
    warm = models.CharField(max_length=10)#供暖
    ele = models.CharField(max_length=10)#供电
    fee = models.CharField(max_length=20)#物业费
    wkind = models.CharField(max_length=10)#物业类型
