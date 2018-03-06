import hashlib

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse

from App.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User, Card, Order


# 首页


def home(request):
    wheel = Wheel.objects.all()
    nav = Nav.objects.all()
    mustbuy = Mustbuy.objects.all()
    shop = Shop.objects.all()
    shopOne = shop[0]
    shopTwo = shop[1:3]
    shopThree = shop[3:7]
    shopFour = shop[7:11]
    mainshow = Mainshow.objects.all()
    data = {
        "wheel": wheel,
        "nav": nav,
        "mustbuy": mustbuy,
        "shopOne": shopOne,
        "shopTwo": shopTwo,
        "shopThree": shopThree,
        "shopFour": shopFour,
        "mainShow": mainshow,
    }
    return render(request, "home/home.html", context=data)


# 超市
def market(request, typeid, childid, sortid):
    title = "闪送超市"

    foodtypes = Foodtypes.objects.all()

    if childid == "0":
        goodsList = Goods.objects.filter(categoryid=typeid)
    else:
        goodsList = Goods.objects.filter(categoryid=typeid).filter(childcid=childid)

    foodtypeChild = Foodtypes.objects.filter(typeid=typeid)

    foodtypenames = "全部分类：0"
    if len(foodtypeChild) > 0:
        foodtypenames = foodtypeChild.first().childtypenames
    namelist = foodtypenames.split("#")

    transfo = []
    for item in namelist:
        itemtran = item.split(":")
        transfo.append(itemtran)

    if sortid == "1":
        goodsList = goodsList.order_by("productnum")
    elif sortid == "2":
        goodsList = goodsList.order_by("-productnum")
    elif sortid == "3":
        goodsList = goodsList.order_by("-price")
    elif sortid == "4":
        goodsList = goodsList.order_by("price")
    else:
        pass

    sortRuleList = [["综合排序", "0"], ["销量升序", '1'], ["销量降序", "2"], ["价格最低", "3"], ["价格最高", "4"]]

    data = {
        "title": title,
        "foodtypes": foodtypes,
        "goodslist": goodsList[:20],
        "transfo": transfo,
        "typeid": typeid,
        "childtype": childid,
        "sortRule": sortRuleList,
    }
    return render(request, "market/market.html", context=data)


# 定向超市
def urlToMarket(request):
    return redirect(reverse("app:market", args=["104749", "0", "0"]))


# 购物车
def card(request):
    username=request.session.get("username")
    if username == None:
        return redirect(reverse("app:mine"))
    user=User.objects.filter(u_name=username).last()
    cards=Card.objects.filter(c_user=user).filter(c_belong=False)
    print(cards)
    data={
        "card":cards,
    }
    return render(request, "card/card.html", context=data)


# 我的
def mine(request):
    title = "我的"
    username = request.session.get("username")
    usericon = ""
    if username == None:
        username = "未登录"
        is_login = False

        data = {
            "title": title,
            "username": username,
            "is_login": is_login,
            "usericon": usericon,
        }
    else:
        is_login = True
        user = User.objects.get(u_name=username)
        userId = user.id
        usericon = "http://127.0.0.1:8000/static/uploadfiles/" + user.u_icon.url

        data = {
            "title": title,
            "username": username,
            "is_login": is_login,
            "usericon": usericon,
            "userid": user.id,
        }
    return render(request, "mine/mine.html", context=data)


# 登录
def login(request):
    return render(request, "mine/login.html")


# 登录操作
def dologin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = User.objects.filter(u_name=username)
    if len(user) > 0:
        md5 = hashlib.md5()
        md5.update(password.encode("utf-8"))
        newpwd = md5.hexdigest()
        if newpwd == user.first().u_password:
            request.session["username"] = username
            return redirect(reverse("app:mine"))
        else:
            return redirect(reverse("app:login"))

    elif len(user) <= 0:
        return redirect(reverse("app:login"))

    return None


# 注册
def register(request):
    return render(request, "mine/register.html")


# 注册操作
def doregister(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    icon = request.FILES.get("icon")
    # print(username,password,email,phone,icon)
    md5 = hashlib.md5()
    # 进行摘要算法
    md5.update(password.encode("utf-8"))
    # 获取十六进制的输出
    # digest()获取二进制输出
    password = md5.hexdigest()

    try:
        user = User()
        user.u_name = username
        user.u_password = password
        user.u_email = email
        user.u_phone = phone
        user.u_icon = icon
        user.save()
        request.session["username"] = username
        return redirect(reverse("app:mine"))
    except Exception as e:
        print(e)
        return HttpResponse("注册失败")


# 推出
def quit(request):
    del request.session["username"]
    return redirect(reverse("app:mine"))


def checkUser(request):
    username = request.GET.get("username")
    users = User.objects.filter(u_name=username)

    if len(users) > 0:
        msg = '用户已存在'
        state = 201
    else:
        msg = "可用"
        state = 200
    data = {
        "msg": msg,
        "state": state,
    }
    return JsonResponse(data)


def userInfo(request,userId):
    users=User.objects.filter(id=userId).last()
    usericon="http://127.0.0.1:8000/static/uploadfiles/"+users.u_icon.url
    data={
        "user":users,
        "usericon":usericon,
    }
    return render(request, "mine/userinfo.html",context=data)


def doUpdate(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    email=request.POST.get("email")
    phone=request.POST.get("phone")
    icon=request.FILES.get("icon")
    print(username, password, phone, email, icon)
    if icon==None:
        try:
            user=User.objects.filter(u_name=username).last()
            user.u_phone=phone
            user.u_email=email
            user.save()
            request.session["username"]=username
            return redirect(reverse("app:mine"))
        except Exception as e:
            print(e)
            return HttpResponse("false")
    else:
        try:
            user = User.objects.filter(u_name=username).last()
            user.u_phone = phone
            user.u_email = email
            user.u_icon=icon
            user.save()
            request.session["username"] = username
            return redirect(reverse("app:mine"))
        except Exception as e:
            print(e)
            return HttpResponse("false")


def addCard(request):
    username=request.session.get("username")
    if username==None:
        return redirect(reverse("app:mine"))
    user = User.objects.filter(u_name=username).last()
    goodsid=request.GET.get("goodsid")
    # print(goodsid)
    goods=Goods.objects.filter(productid=goodsid).last()
    # print(goods)
    c=Card.objects.filter(c_good=goods)
    if len(c):
        addcard=c.last()
    else:
        addcard=Card()
    addcard.c_user=user
    addcard.c_good=goods
    addcard.c_goodnumber+=1
    addcard.save()
    data={
        "msg":"succeful",
        "number":addcard.c_goodnumber,
    }
    return JsonResponse(data)


def changeSelect(request):
    cardid=request.GET.get("cardid")
    isselect=request.GET.get("isselect")
    print(isselect)
    # print(cardid,isselect)
    cards=Card.objects.filter(pk=cardid).last()
    if isselect=="True":
        cards.c_isselect = False
    elif isselect=="False":
        cards.c_isselect=True
    cards.save()
    data={
        "msg":"ok",

    }
    return JsonResponse(data)


def subCard(request):
    cardid=request.GET.get("cardid")
    cards=Card.objects.filter(pk=cardid).last()
    cardGoodNumber=cards.c_goodnumber
    if cardGoodNumber==1:
        cards.delete()
        data={
            "number":"0",
        }
    else:
        cards.c_goodnumber=cardGoodNumber-1
        cards.save()
        data={
            "number":cardGoodNumber-1,
        }
    return JsonResponse(data)


def makeorder(request):
    username=request.session.get("username")
    user=User.objects.filter(u_name=username).last()
    cardids=request.GET.get("cardids")
    # print(cardids)
    cardList=cardids.split("#")

    order=Order()
    order.o_user=user
    order.save()
    for cards in cardids:
        c=Card.objects.filter(pk=cards).last()
        c.c_order=order
        c.c_belong=True
        c.save()
    data={
        "msg":"succeful",
    }
    return JsonResponse(data)