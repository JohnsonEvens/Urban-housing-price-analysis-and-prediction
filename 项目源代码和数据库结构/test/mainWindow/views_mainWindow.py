#作者：仲银炜 创建时间：2019.8.26 最后修改时间：2019.8.26
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404
from .models import *
from django import forms  # 导入表单
from django.template import RequestContext
from django.db import models
import django
import random

global city
# Create your views here.
def index1(request):
    if request.method == "POST":
        s = request.GET.get('search_Info')

        response = redirect("/indexnj/")
        return response

    return render_to_response('index1.html')

def indexnj(request):
    selectedHouse = House.objects.filter(city='南京')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 =0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '鼓楼' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '江宁'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '浦口'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '栖霞'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '雨花台'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '建邺'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '秦淮'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '玄武'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '六合'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '溧水'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '高淳'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)

    p1 = int(p1 / s1)
    p2 = int(p2 / s2)
    p3 = int(p3 / s3)
    p4 = int(p4 / s4)
    p5 = int(p5 / s5)
    p6 = int(p6 / s6)
    p7 = int(p7 / s7)
    p8 = int(p8 / s8)
    p9 = int(p9 / s9)
    p10 = int(p10 / s10)
    p11 = int(p11 / s11)

    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexnj.html', locals())

def indexbj(request):
    selectedHouse = House.objects.filter(city='北京')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 =0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '朝阳' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '海淀'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '门头沟'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '亦庄开发区'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '丰台'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '通州'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '石景山'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '昌平'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '大兴'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '顺义'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '房山'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexbj.html', locals())

def indextj(request):
    selectedHouse = House.objects.filter(city='天津')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 =0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '和平' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '河西'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '南开'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '河北'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '河东'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '西青'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '津南'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '武清'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '塘沽'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '北辰'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '东丽'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indextj.html', locals())

def indexsh(request):
    selectedHouse = House.objects.filter(city='上海')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 =0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '青浦' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '嘉定'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '奉贤'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '宝山'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '松江'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '浦东'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '普陀'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '闸北'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '金山'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '闵行'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '上海周边'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexsh.html', locals())

def indexhz(request):
    selectedHouse = House.objects.filter(city='杭州')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 =0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '江干' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '余杭'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '萧山'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '西湖'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '滨江'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '拱墅'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '下城'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '上城'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '富阳'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '桐庐'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '钱塘新区'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)
        if (single.district == '建德'and single.price!='价格待定'):
            s12 += 1
            p12 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    p12 = int(p12 / s12)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexhz.html', locals())

def indexcd(request):
    selectedHouse = House.objects.filter(city='成都')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 = 0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '双流' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '东坡区'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '大邑'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '天府新区'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '天府新区南区'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '成华'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '新都'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '青白江'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '高新'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '龙泉驿'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '锦江'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)
        if (single.district == '郫都'and single.price!='价格待定'):
            s12 += 1
            p12 += int(single.price)
        if (single.district == '都江堰'and single.price!='价格待定'):
            s13 += 1
            p13 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    p12 = int(p12 / s12)
    p13 = int(p13 / s13)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexcd.html', locals())

def indexcs(request):
    selectedHouse = House.objects.filter(city='长沙')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 = 0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '望城' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '宁乡'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '浏阳'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '长沙县'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '雨花'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '岳麓'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '天心'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '开福'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '芙蓉'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '雨湖区'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)

    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexcs.html', locals())

def indexsz(request):
    selectedHouse = House.objects.filter(city='深圳')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 = 0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '福田区' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '南山区'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '龙岗区'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '宝安区'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '罗湖区'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '龙华区'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '盐田区'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '光明区'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '坪山区'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '大鹏新区'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '惠城'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexsz.html', locals())

def indexty(request):
    selectedHouse = House.objects.filter(city='太原')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 = 0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0

    for single in selectedHouse:
        if(single.district== '杏花岭区' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '迎泽区'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '万柏林区'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '小店区'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '尖草坪区'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '晋源区'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '阳曲县'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '榆次区'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexty.html', locals())

def indexnc(request):
    selectedHouse = House.objects.filter(city='南昌')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 =0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0
    for single in selectedHouse:
        if(single.district== '青山湖区' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '东湖区'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '西湖区'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '青云谱区'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '进贤县'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '湾里区'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '安义县'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '南昌县'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '新建区'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '红谷滩'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '高新区'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)
        if (single.district == '经开区'and single.price!='价格待定'):
            s12 += 1
            p12 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    p12 = int(p12/s12)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexnc.html', locals())

def indexsu(request):
    selectedHouse = House.objects.filter(city='苏州')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 = 0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0

    for single in selectedHouse:
        if(single.district== '高新' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '姑苏'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '相城'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '吴江'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '常熟'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '昆山'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '吴中'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '工业园区'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexsu.html', locals())

def indexwx(request):
    selectedHouse = House.objects.filter(city='无锡')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 = 0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0

    for single in selectedHouse:
        if(single.district== '滨湖' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '惠山'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '梁溪'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '新吴'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '锡山'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '宜兴市'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '江阴市'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    price_list = [p1,p2,p3,p4,p5,p6,p7]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexwx.html', locals())

def indexwh(request):
    selectedHouse = House.objects.filter(city='武汉')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = s14 = s15 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = p14 = p15 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 =0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0

    for single in selectedHouse:
        if(single.district== '汉南' and single.price!='价格待定'):
            s1 += 1
            p1+=int(single.price)
        if (single.district == '蔡甸'and single.price!='价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '江夏'and single.price!='价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '黄陂'and single.price!='价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '新洲'and single.price!='价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '江岸'and single.price!='价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '江汉'and single.price!='价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '沌口开发区'and single.price!='价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '硚口'and single.price!='价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '东西湖'and single.price!='价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '武昌'and single.price!='价格待定'):
            s11 += 1
            p11 += int(single.price)
        if (single.district == '青山'and single.price!='价格待定'):
            s12 += 1
            p12 += int(single.price)
        if (single.district == '洪山'and single.price!='价格待定'):
            s13 += 1
            p13 += int(single.price)
        if (single.district == '汉阳'and single.price!='价格待定'):
            s14 += 1
            p14 += int(single.price)
        if (single.district == '东湖高新'and single.price!='价格待定'):
            s15 += 1
            p15 += int(single.price)

    p1 = int(p1/s1)
    p2 = int(p2/s2)
    p3 = int(p3/s3)
    p4 = int(p4/s4)
    p5 = int(p5/s5)
    p6 = int(p6/s6)
    p7 = int(p7/s7)
    p8 = int(p8/s8)
    p9 = int(p9/s9)
    p10 = int(p10/s10)
    p11 = int(p11/s11)
    p12 = int(p12 / s12)
    p13 = int(p13 / s13)
    p14 = int(p14 / s14)
    p15 = int(p15 / s15)
    price_list = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15]

    for single in selectedHouse:
        if(single.price!='价格待定'):
            s_price = int(single.price)
            if(s_price < 10000):
                pr1+=1
            if (s_price >= 10000 and s_price<15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1,pr2,pr3,pr4,pr5,pr6,pr7,pr8]


    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1+=1
    for select2 in single2:
        rs2+=1
    for select3 in single3:
        rs3+=1
    for select4 in single4:
        rs4+=1
    for select5 in single5:
        rs5+=1
    for select6 in single6:
        rs5+=1
    for select7 in single7:
        rs5+=1
    for select8 in single8:
        rs5+=1

    room_range = [rs1,rs2,rs3,rs4,rs5]

    return render(request, 'indexwh.html', locals())

def indexgz(request):
    selectedHouse = House.objects.filter(city='广州')
    s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = s11 = s12 = s13 = 0
    p1 = p2 = p3 = p4 = p5 = p6 = p7 = p8 = p9 = p10 = p11 = p12 = p13 = 0
    pr1 = pr2 = pr3 = pr4 = pr5 = pr6 = pr7 = pr8 = 0
    rs1 = rs2 = rs3 = rs4 = rs5 = 0

    for single in selectedHouse:
        if (single.district == '南沙' and single.price != '价格待定'):
            s1 += 1
            p1 += int(single.price)
        if (single.district == '荔湾' and single.price != '价格待定'):
            s2 += 1
            p2 += int(single.price)
        if (single.district == '越秀' and single.price != '价格待定'):
            s3 += 1
            p3 += int(single.price)
        if (single.district == '海珠' and single.price != '价格待定'):
            s4 += 1
            p4 += int(single.price)
        if (single.district == '天河' and single.price != '价格待定'):
            s5 += 1
            p5 += int(single.price)
        if (single.district == '白云' and single.price != '价格待定'):
            s6 += 1
            p6 += int(single.price)
        if (single.district == '黄埔' and single.price != '价格待定'):
            s7 += 1
            p7 += int(single.price)
        if (single.district == '番禺' and single.price != '价格待定'):
            s8 += 1
            p8 += int(single.price)
        if (single.district == '花都' and single.price != '价格待定'):
            s9 += 1
            p9 += int(single.price)
        if (single.district == '增城' and single.price != '价格待定'):
            s10 += 1
            p10 += int(single.price)
        if (single.district == '从化' and single.price != '价格待定'):
            s11 += 1
            p11 += int(single.price)
        if (single.district == '顺德' and single.price != '价格待定'):
            s12 += 1
            p12 += int(single.price)
        if (single.district == '南海' and single.price != '价格待定'):
            s13 += 1
            p13 += int(single.price)

    p1 = int(p1 / s1)
    p2 = int(p2 / s2)
    p3 = int(p3 / s3)
    p4 = int(p4 / s4)
    p5 = int(p5 / s5)
    p6 = int(p6 / s6)
    p7 = int(p7 / s7)
    p8 = int(p8 / s8)
    p9 = int(p9 / s9)
    p10 = int(p10 / s10)
    p11 = int(p11 / s11)
    p12 = int(p12 / s12)
    p13 = int(p13 / s13)
    price_list = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13]

    for single in selectedHouse:
        if (single.price != '价格待定'):
            s_price = int(single.price)
            if (s_price < 10000):
                pr1 += 1
            if (s_price >= 10000 and s_price < 15000):
                pr2 += 1
            if (s_price >= 15000 and s_price < 20000):
                pr3 += 1
            if (s_price >= 20000 and s_price < 25000):
                pr4 += 1
            if (s_price >= 25000 and s_price < 30000):
                pr5 += 1
            if (s_price >= 30000 and s_price < 40000):
                pr6 += 1
            if (s_price >= 40000 and s_price < 50000):
                pr7 += 1
            if (s_price >= 50000):
                pr8 += 1
    price_range = [pr1, pr2, pr3, pr4, pr5, pr6, pr7, pr8]

    single1 = selectedHouse.filter(layout__icontains='1室')
    single2 = selectedHouse.filter(layout__icontains='2室')
    single3 = selectedHouse.filter(layout__icontains='3室')
    single4 = selectedHouse.filter(layout__icontains='4室')
    single5 = selectedHouse.filter(layout__icontains='5室')
    single6 = selectedHouse.filter(layout__icontains='6室')
    single7 = selectedHouse.filter(layout__icontains='7室')
    single8 = selectedHouse.filter(layout__icontains='8室')
    for select1 in single1:
        rs1 += 1
    for select2 in single2:
        rs2 += 1
    for select3 in single3:
        rs3 += 1
    for select4 in single4:
        rs4 += 1
    for select5 in single5:
        rs5 += 1
    for select6 in single6:
        rs5 += 1
    for select7 in single7:
        rs5 += 1
    for select8 in single8:
        rs5 += 1

    room_range = [rs1, rs2, rs3, rs4, rs5]

    return render(request, 'indexgz.html', locals())

def result1(request):
    return render_to_response('result1.html')

def search(request):
    searchInfo = request.GET.get('search_Info')

    error_msg = ""

    if not searchInfo:
        error_msg = "您需要输入想要搜索的内容"
        return render(request, 'result1.html', locals())

    m_city = request.GET.get('searchCity')
    search_result = House.objects.filter(city=m_city)
    search_result = search_result.filter(properties=searchInfo)
    if not search_result:
        error_msg = "未能查找到你搜索的楼盘"
        return render(request, 'result1.html', locals())

    return render_to_response('result1.html', locals())



def houseSelect(request):
    s_region = request.GET.get('region')#区
    s_room = request.GET.get('room')#户型
    s_type = request.GET.get('type')
    s_city = request.GET.get('city')

    selectedHouse = House.objects.filter(city=s_city)

    if s_type == 'all':
        sel2=selectedHouse
        if s_region == 'all' and s_room != 'all':
            sel1 = sel2.filter(layout__icontains=s_room)
        elif s_region != 'all' and s_room == 'all':
            sel1 = sel2.filter(district=s_region)
        elif s_region != 'all' and s_room != 'all':
            sel1 = sel2.filter(district=s_region, layout__icontains=s_room)
        else:
            sel1 = sel2
    else:
        sel2=selectedHouse.filter(wkind=s_type)
        if s_region == 'all' and s_room != 'all':
            sel1 = sel2.filter(layout__icontains=s_room)
        elif s_region != 'all' and s_room == 'all':
            sel1 = sel2.filter(district=s_region)
        elif s_region != 'all' and s_room != 'all':
            sel1 = sel2.filter(district=s_region, layout__icontains=s_room)
        else:
            sel1 = sel2

    return render(request, 'result2.html', locals())

def predict(request):
    dict = {
        # 南京
        "句容": 92.266,
        "江宁": 2.178,
        "浦口": -18.213,
        "栖霞": 13.273,
        "雨花台": -2.58,
        "建邺": 123.664,
        "秦淮": 111.385,
        "鼓楼": 254.024,
        "玄武": 186.213,
        "六合": 50.206,
        "溧水": -32.86,
        "高淳": -33.969,
        # 北京
        "朝阳": -150.164,
        "海淀": -22.224,
        "门头沟": 30.287,
        "亦庄开发区": -106.57,
        "丰台": -99.427,
        "通州": 118.203,
        "石景山": -53.028,
        "昌平": -69.934,
        "大兴": -156.28,
        "顺义": 5.203,
        "房山": -12.364,
        # 天津
        "和平": -107.262,
        "河西": -73.196,
        "南开": -71.493,
        "河北": -145.629,
        "河东": -97.133,
        "西青": -118.577,
        "津南": -4.983,
        "武清": 13.678,
        "塘沽": 0,
        "北辰": -18.07,
        "东丽": -95.692,
        # 上海
        "青浦": -15.678,
        "嘉定": 151.895,
        "奉贤": -68.343,
        "宝山": -58.448,
        "松江": -35.832,
        "浦东": -53.577,
        "普陀": 74.252,
        "闸北": -58.346,
        "金山": -58.448,
        "闵行": 49.857,
        "上海周边": 49.857,
        # 杭州
        "江干": -69.762,
        "余杭": 62.892,
        "萧山": -77.189,
        "西湖": 19.451,
        "滨江": 37.056,
        "拱墅": -84.675,
        "下城": 5.85,
        "上城": -35.731,
        "富阳": -76.364,
        "桐庐": 306.909,
        "钱塘江新区": 0,
        "建德": 149.556,
        # 成都
        "双流": 48,
        "东坡区": -39.983,
        "大邑": -60.636,
        "天府新区": -7.057,
        "天府新区南区": -7.057,
        "成华": 0.944,
        "新都": -28.049,
        "青白江": -55.993,
        "高新": -9.269,
        "龙泉驿": -10.332,
        "锦江": 150.692,
        "郫都": 26.934,
        "都江堰": 0.899,
        # 长沙
        "望城": -0.273,
        "宁乡": -16.615,
        "浏阳": 21.647,
        "长沙县": -11.72,
        "雨花": -68.531,
        "岳麓": 17.213,
        "天心": -88042,
        "开福": -36.325,
        "芙蓉": -57.972,
        "雨湖区": -46.217,
        # 深圳
        "福田区": 78.084,
        "南山区": 390.668,
        "龙岗区": -15.371,
        "宝安区": 112.829,
        "罗湖区": 8.21,
        "龙华区": 108.906,
        "盐田区": -134.892,
        "光明区": 25.892,
        "坪山区": 365.825,
        "大鹏新区": 0,
        "惠城": -30.503,
        # 太原
        "杏花岭区": -1.832,
        "迎泽区": -10.563,
        "万柏林区": -13.434,
        "小店区": -25.07,
        "尖草坪区": -43.944,
        "晋源区": -14.832,
        "阳曲县": 4.916,
        "榆次区": 4.916,
        # 南昌
        "青山湖区": 54.059,
        "东湖区": 30.531,
        "西湖区": 6025,
        "青云谱区": 12.378,
        "进贤区": 13.717,
        "湾里区": 44.098,
        "安义县": 0,
        "南昌县": 43.308,
        "新建区": -1.979,
        "红谷滩": 0,
        "高新区": 27.273,
        "经开区": 15.93,
        # 苏州
        "姑苏": 286.476,
        "相城": 223.619,
        "吴江": 275.196,
        "常熟": -172.934,
        "昆山": 190.906,
        "吴中": 242.336,
        "工业园区": 0,
        # 无锡
        "滨湖": 23.986,
        "惠山": 50.406,
        "梁溪": 111.626,
        "新吴": 95.517,
        "锡山": 88.517,
        "宜兴市": 175.92,
        "江阴市": 36.416,
        # 武汉
        "汉南": 9.927,
        "蔡甸": 6.273,
        "江夏": -108.573,
        "黄陵": -58.252,
        "新洲": 36.175,
        "江岸": -91.36,
        "江汉": -60.126,
        "沌口开发区": 0,
        "硚口": -83.928,
        "东西湖": -76.304,
        "武昌": -58.794,
        "青山": -73.748,
        "洪山": -81.895,
        "汉阳": -46,
        "东湖高新": -231.406,
        # 广州
        "南沙": -128.696,
        "荔湾": -14.063,
        "越秀": -157.664,
        "海珠": -112.126,
        "天河": 98.521,
        "白云": 62.129,
        "黄埔": -0.399,
        "番禺": 57.993,
        "花都": -4.622,
        "增城": -97.727,
        "从化": 23.871,
        "顺德": 0,
        "南海": 196.741
    }
    gdpdict={
        "天津":12.02,
        "上海": 12.46,
        "苏州": 15.96,
        "广州": 15.31,
        "深圳": 20.45,
        "南京": 14.17,
        "北京": 12.9,
        "杭州": 13.66,
        "武汉": 12.44,
        "无锡": 16.1,
        "成都": 8.72,
        "南昌": 9.31,
        "长沙": 13.33,
        "太原": 7.41,
    }
    avgdict={
        "天津": -0.86,
        "上海": -0.42,
        "苏州": 3.08,
        "广州": 2.43,
        "深圳": 7.57,
        "南京": 1.29,
        "北京": 0.02,
        "杭州": 0.78,
        "武汉": -0.44,
        "无锡": 3.22,
        "成都": -4.16,
        "南昌": -3.57,
        "长沙": 0.45,
        "太原": -5.47,
    }
    searchInfo = request.GET.get('predictsc')

    search_result = House.objects.filter(properties=searchInfo)

    if searchInfo and not search_result:
        error_msg="未能查找到搜索的小区"
        return render(request,'predict.html',locals())

    for result in search_result:
        if (result.price != "价格待定" and result.unit!=" 万/套(总价)"):
            if (dict.get(result.district)):
                s = dict[result.district]  # 初始斜率
                sum = s  # 总斜率
                ss = abs(s)  # 初始斜率绝对值
                s1 = s2 = s3 = s4 = s5 = s6 = s7 = s8 = s9 = s10 = 0
                # 各个因素的值
                s1 = request.GET.get('radio1')
                s2 = request.GET.get('radio2')
                s3 = request.GET.get('radio3')
                s4 = request.GET.get('radio4')
                s5 = request.GET.get('radio5')
                s6 = request.GET.get('radio6')
                s7 = request.GET.get('radio7')
                s8 = request.GET.get('radio8')
                s9 = request.GET.get('radio9')
                s10 = request.GET.get('radio10')
                # 通过if条件语句求出总斜率
                if s1 == 1:
                    sum = sum + (0.8 * ss)
                else:
                    sum = sum
                if s2 == 1:
                    sum = sum + (0.6 * ss)
                else:
                    sum = sum
                if s3 == 1:
                    sum = sum + (0.5 * ss)
                else:
                    sum = sum
                if s4 == 1:
                    sum = sum + (0.4 * ss)
                else:
                    sum = sum
                if s5 == 1:
                    sum = sum + (0.2 * ss)
                else:
                    sum = sum
                if s6 == 1:
                    sum = sum - (0.4 * ss)
                else:
                    sum = sum
                if s7 == 1:
                    sum = sum - (0.3 * ss)
                else:
                    sum = sum
                if s8 == 1:
                    sum = sum - (0.8 * ss)
                else:
                    sum = sum
                if s9 == 1:
                    sum = sum - (0.8 * ss)
                else:
                    sum = sum
                if s10 == 1:
                    sum = sum - ss
                else:
                    sum = sum
                list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                sum = sum+avgdict[result.city] / gdpdict[result.city]
                list[0] = int(result.price)  # 小区当前价格
                i = 0
                while i < 23:
                    i = i + 1
                    a = 0
                    a = sum * i + float(result.price)  # 未来房价
                    r1 = int((-0.01) * a)
                    r2 = int(0.01 * a)
                    r = random.randint(r1, r2)
                    list[i] = int(a + r)
                minPrice = int(int(result.price) * 0.7)
                return render(request, 'predict.html', locals())
            else:
                error_msg = "未能查找到搜索小区的地区价格信息"
                return render(request, 'predict.html', locals())
        else:
            error_msg = "您搜索的小区价格待定"
            return render(request, 'predict.html', locals())

    return render(request, 'predict.html', locals())


