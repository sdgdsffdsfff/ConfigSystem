function showModel(obj){
    //令当前显示的模块消失
    $(".jumbotron:visible").css("display", "none");
    //显示本模块
    $("#" + obj.name).css("display", "block");
    //当前li非active
    $(".nav .active").removeClass("active");

    //active本li
    $(obj).parent().addClass("active");
}

$(function(){
    $("#web-gather-check-btn").click(function(){
        //查询网站同名、包含host的网站，列出到本行下供选择。并隐藏掉check按钮，显示出add按钮
        $("#web-gather-check-btn").css("display", "none")

        //若点击某个提示，则把对应的网站更新。如果相同项目，则只更新录入时间。如果项目不同，则重新创建网站

        //显示add按钮
        $("#web-gather-add-btn").css("display", "inline-block")
    })

    $("#web-gather-add-btn").click(function(){
        //1.发请求添加信息到本周新增
        $.post('/addGatherIssue',function(){
            alert("----add ok----")
        })

        //2.请求返回后，若添加成功，刷新本周新增区域。否则提示错误

        //3.隐藏add按钮，重新显示check按钮。同时清空网站名、网站地址输入框
        $("#web-gather-add-btn").css("display", "none")
        $("#web-gather-net_name").val("")
        $("#web-gather-net_add").val("")
        $("#web-gather-check-btn").css("display", "inline-block")
    })
})