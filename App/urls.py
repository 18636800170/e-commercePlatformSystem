from django.conf.urls import url

from App import views

urlpatterns = [
    url(r"^home/$", views.home, name="home"),

    url(r"^market/$", views.urlToMarket, name="urlToMarket"),
    url(r"^market/(\d+)/(\d+)/(\d+)/$", views.market, name="market"),

    url(r"^card/$", views.card, name="card"),
    url(r"^addcard/$",views.addCard,name="addcard"),
    url(r"^changeselect/$",views.changeSelect,name="changeselect"),
    url(r"^subcard/$",views.subCard,name="subcard"),
    url(r"^makeorder/$",views.makeorder,name="makeorder"),

    url(r"^mine/$", views.mine, name="mine"),
    url(r"^userinfo/(\d+)/$", views.userInfo, name="userinfo"),
    url(r"^doupdate/$", views.doUpdate, name="doupdate"),

    url(r"^login/$", views.login, name="login"),
    url(r"dologin/$", views.dologin, name="dologin"),

    url(r"^register/$", views.register, name="register"),
    url(r"^checkuser/$", views.checkUser, name="checkuser"),
    url(r"^doregister/$", views.doregister, name="doregister"),

    url(r"^quit/$", views.quit, name="quit"),
]
