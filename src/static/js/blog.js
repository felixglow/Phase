/**
 * Created by felix on 15/6/19.
 */

function gotoTop(min_height){
    //预定义返回顶部的html代码，它的css样式默认为不显示
    var gotoTop_html = '<div id="gotoTop"></div>';
    //将返回顶部的html代码插入页面上id为page的元素的末尾
    $("#page").append(gotoTop_html);
    $("#gotoTop").click(//定义返回顶部点击向上滚动的动画
        function(){$('html,body').animate({scrollTop:0},"normal");
    })
    //为窗口的scroll事件绑定处理函数
    $(window).scroll(function(){
        //获取窗口的滚动条的垂直位置
        var s = $(window).scrollTop();
        //当窗口的滚动条的垂直位置大于页面的最小高度时，让返回顶部元素渐现，否则渐隐
        if( s > min_height){
            $("#gotoTop").fadeIn(300);
        }else{
            $("#gotoTop").fadeOut(500);
        };
    });
};


$(document).ready(function(){
    function flush(){
        var nLeft = $(".left-content").get(0).scrollHeight;
        var nSide = $(".sidebar").get(0).scrollHeight;
        if(nLeft>nSide){
            $(".sidebar").css({"height":nLeft+"px"});
        }
    }
    flush();
    var timer = setInterval(function(){
        flush();
    },800);

    setTimeout(function(){
        clearInterval(timer);
    },12000);
    gotoTop(200);
});
