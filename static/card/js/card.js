$(function () {
    $(".ischose").on("click",function () {
        var chose=$(this);
        var url="http://127.0.0.1:8000/app/changeselect";
        var cardid=$(this).attr("cardid");
        var isselect=$(this).attr("isselect");
        var data={
            "cardid":cardid,
            "isselect":isselect
        };
        // console.log("b");
        $.getJSON(url,data,function (data) {
            // console.log("a");
            if(data["msg"]=="ok"){
                chose.find("span").toggle();
            }
        })
    });

    $(".addShopping").on("click",function () {
        var adds=$(this);
        var url="http://127.0.0.1:8000/app/addcard";
        data={
            "cardid":adds.attr("cardid")
        };
        $.getJSON(url,data,function (data){
            adds.next("span").html(data["number"])
        })
    });

    $(".subShopping").on("click",function () {
        var sub=$(this);
        var url="http://127.0.0.1:8000/app/subcard";
        data={
            "cardid":sub.attr("cardid")
        };
        $.getJSON(url,data,function (data) {
            if(data["number"]=="0"){
                sub.parents("li").remove()
            }else{
                console.log(data["number"]);
                sub.next("span").html(data["number"])
            }
        })
    });
    $("#ok").on("click",function () {
        var cardids=[];
        $(".ischose").each(function () {
            var child=$(this).find("span");
            cardids.push()
        });
        var url="http://127.0.0.1:8000/app/makeorder";
        var data={
            "cardid":cardids.join("#")
        };
        $.getJSON(url,data,function (data) {
            alert("a")
        })
    });
});