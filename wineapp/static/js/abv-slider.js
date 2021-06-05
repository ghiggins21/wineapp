$( function() {
        $(".abv-numeric-slider-range").slider({
          range: true,
          animate: true,
          step:.5,
          orientation: 'vertical',
          slide: function( event, ui ) {
            $("#" + $(this).parent().attr("id") + "_min").val(ui.values[ 0 ]);
            $("#" + $(this).parent().attr("id") + "_max").val(ui.values[ 1 ]);
            $("#" + $(this).parent().attr("id") + "_text").text(ui.values[ 0 ] + '%' + ' - ' + ui.values[ 1 ] + '%');
          },
          create: function( event, ui ) {
            $(this).slider("option",'values',[$(this).parent().data("cur_min"), $(this).parent().data("cur_max")]);
            $(this).slider("option",'max',$(this).parent().data("range_max"));
            $(this).slider("option",'values',[$(this).parent().data("cur_min"), $(this).parent().data("cur_max")]);
            },
        });
  });
