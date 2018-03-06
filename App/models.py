from django.db import models

# Create your models here.
class Wheel(models.Model):
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=20)
    img=models.CharField(max_length=200)
    class Meta():
        db_table="axfWheel"

# axfNav(img,name,trackid)
class Nav(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=20)
    class Meta():
        db_table="axfNav"

# axfMustbuy(img,name,trackid)
class Mustbuy(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=20)
    class Meta():
        db_table="axfMustbuy"

# axfShop(img,name,trackid)
class Shop(models.Model):
    img=models.CharField(max_length=200)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=20)
    class Meta():
        db_table="axfShop"

# axfMainshow(trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3)
class Mainshow(models.Model):
    trackid=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=200)
    categoryid=models.CharField(max_length=20)
    brandname=models.CharField(max_length=100)

    img1=models.CharField(max_length=200)
    childcid1=models.CharField(max_length=20)
    productid1=models.CharField(max_length=100)
    longname1=models.CharField(max_length=100)
    price1=models.CharField(max_length=20)
    marketprice1=models.CharField(max_length=20)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=100)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=100)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)
    class Meta():
        db_table="axfMainshow"

#axfFoodtypes(typeid,typename,childtypenames,typesort)
class Foodtypes(models.Model):
    typeid=models.CharField(max_length=20)
    typename=models.CharField(max_length=20)
    childtypenames=models.CharField(max_length=200)
    typesort=models.IntegerField(default=1)
    class Meta():
        db_table="axfFoodtypes"

# insert into axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum)
#  闪送
class Goods(models.Model):
    productid=models.CharField(max_length=20)
    productimg=models.CharField(max_length=200)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=200)
    isxf=models.BooleanField(default=False)
    pmdesc=models.IntegerField(default=0)
    specifics=models.CharField(max_length=20)
    price=models.CharField(max_length=20)
    marketprice=models.CharField(max_length=20)
    categoryid=models.CharField(max_length=20)
    childcid=models.CharField(max_length=20)
    childcidname=models.CharField(max_length=100)
    dealerid=models.CharField(max_length=20)
    storenums=models.CharField(max_length=20)
    productnum=models.CharField(max_length=20)
    class Meta():
        db_table="axf_goods"

# 用户系统
class User(models.Model):
    u_name=models.CharField(max_length=16,unique=True)
    u_password=models.CharField(max_length=33)
    u_icon=models.ImageField(upload_to="uploadfiles")
    u_email=models.CharField(max_length=50)
    u_phone=models.CharField(max_length=20)
    class Meta():
        db_table="axf_user"


class Order(models.Model):
    o_user=models.ForeignKey(User)
    o_status=models.IntegerField(default=0)
    class Meta():
        db_table="axf_order"

class Card(models.Model):
    c_user=models.ForeignKey(User)
    c_good=models.ForeignKey(Goods)
    c_goodnumber=models.IntegerField(default=1)
    c_isselect=models.BooleanField(default=True)
    c_order=models.ForeignKey(Order,null=True,default=None)
    c_belong=models.BooleanField(default=False)
    class Meta():
        db_table="axf_card"
