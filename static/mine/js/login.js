function check() {
    var pwd=$("#password").val();
    var newpwd=md5(pwd)
    $("#password").val(newpwd);
    return true
}