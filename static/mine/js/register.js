$(function () {
    $("#username").on("blur", function () {
        var username = $(this).val();
        console.log("a");
        $.getJSON(
            "http://127.0.0.1:8000/app/checkuser/",
            {
                "username": username
            },
            function (data) {
                if (data["state"] == 200) {
                    console.log(data);
                    $("#username").next().innerHTML(data["msg"])
                } else if (data["state"] == 201) {
                    $("#username").next().innerHTML(data["msg"])
                    console.log(data)
                }

            }
        )
    })
});

function check() {

    var pasd = $("#password").val();


    var pasdvi = $("#passtwo").val();
    console.log("a");
    if (pasd == pasdvi) {
        console.log("b");
        $("#passtwo").next().innerHTML("可用");
    } else {
        console.log("c");
        $("#passtwo").next().innerHTML("不可用");
        return false;
    }
    var newpwd=md5(pwd);
    $("#password").val(newpwd);
    return true
}
