var Common = Common || {};

(function($){
    //init
    Common.init = function(){
        Common.navi();
    }; //init

    Common.navi = function(){
        var _self = {};
        _self = this.navi;

        var param = _self.param = {
            $target: $('#Header').find('.drawer-toggle'),
            $header: $('#Header').find('.drawer-nav'),
            $loading: $('#Loading'),
            activeClass: 'active',
            flag: false
        };

        var func = _self.func = {
            init: function(){
                func.eventSetting();
            },

            //eventSetting
            eventSetting: function(){
                $('html').imagesLoaded( function() {
                    param.$loading.fadeOut(1000);
                });
                func.drawerDirection();
                $(window).resize(function() {
                    func.drawerDirection();
                });
                $('a[href^="#"]').on('click', func.smoothScroll.bind(this));
            }, //eventSetting

            //drawerDirection
            drawerDirection: function(){
                var wW = $(window).width();
                var Hh = $('html').height();
                if(wW <= 720){
                    $('body').removeClass('drawer--right');
                    $('body').addClass('drawer--top');
                    param.$header.height('100vh');
                }else{
                    $('body').removeClass('drawer--top');
                    $('body').addClass('drawer--right');
                    param.$header.height(Hh);
                }
            }, //drawerDirection

            //smoothScroll
            smoothScroll: function(e){
                var speed = 400;
                var href= $(e.currentTarget).attr("href");
                var target = $(href && (href !== "#")? href : 'html');
                var position = target.offset().top;
                $('body,html').animate({scrollTop:position}, speed, 'swing');
                return false;
            }, //smoothScroll

        };
        return func.init();
    };

    //DOM READY
    jQuery(function($){
        Common.navi();
        $(".drawer").drawer();
        });

}(jQuery));
