$( function() {
    // $( ".numeric-slider-range" ).each(function() {
        $(".numeric-slider-range").slider({
          range: true,
          animate: true,
          step:.5,
          orientation: 'horizontal',
          slide: function( event, ui ) {
            $("#" + $(this).parent().attr("id") + "_min").val(ui.values[ 0 ]);
            $("#" + $(this).parent().attr("id") + "_max").val(ui.values[ 1 ]);
            $("#" + $(this).parent().attr("id") + "_text").text("£" + ui.values[ 0 ] + ' - ' + "£" + ui.values[ 1 ]);
          },
          create: function( event, ui ) {
            $(this).slider("option",'values',[$(this).parent().data("cur_min"), $(this).parent().data("cur_max")]);
            $(this).slider("option",'max',$(this).parent().data("range_max"));
            $(this).slider("option",'values',[$(this).parent().data("cur_min"), $(this).parent().data("cur_max")]);
            },
      });
          $("#" + $(".numeric-slider").attr("id") + "_min").val( $(".numeric-slider").data("cur_min") );
          $("#" + $(".numeric-slider").attr("id") + "_max").val( $(".numeric-slider").data("cur_max") );
          //$("#" + $(".numeric-slider").attr("id") + "_text").text(ui.values[ 0 ] + ' - ' + ui.values[ 1 ]);

          $(".abv-numeric-slider-range").slider({
            range: true,
            animate: true,
            step:.5,
            orientation: 'horizontal',
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
              $("#" + $(".abv-numeric-slider").attr("id") + "_min").val( $(".abv-numeric-slider").data("cur_min") );
              $("#" + $(".abv-numeric-slider").attr("id") + "_max").val( $(".abv-numeric-slider").data("cur_max") );
              //$("#" + $(".numeric-slider").attr("id") + "_text").text(ui.values[ 0 ] + ' - ' + ui.values[ 1 ]);

          $(".rating-numeric-slider-range").slider({
            range: true,
            animate: true,
            step:.5,
            orientation: 'horizontal',
            slide: function( event, ui ) {
              $("#" + $(this).parent().attr("id") + "_min").val(ui.values[ 0 ]);
              $("#" + $(this).parent().attr("id") + "_max").val(ui.values[ 1 ]);
              $("#" + $(this).parent().attr("id") + "_text").text("stars " + ui.values[ 0 ] + ' - ' + "stars " + ui.values[ 1 ]);
            },
            create: function( event, ui ) {
              $(this).slider("option",'values',[$(this).parent().data("cur_min"), $(this).parent().data("cur_max")]);
              $(this).slider("option",'max',$(this).parent().data("range_max"));
              $(this).slider("option",'values',[$(this).parent().data("cur_min"), $(this).parent().data("cur_max")]);
              },
        });
            $("#" + $(".rating-numeric-slider").attr("id") + "_min").val( $(".rating-numeric-slider").data("cur_min") );
            $("#" + $(".rating-numeric-slider").attr("id") + "_max").val( $(".rating-numeric-slider").data("cur_max") );
            //$("#" + $(".numeric-slider").attr("id") + "_text").text(ui.values[ 0 ] + ' - ' + ui.values[ 1 ]);
  // });
});
