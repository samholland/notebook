# Waypoints scrolling highlight

Highlights sections using waypoints.js

    var containers = $('.container-class-name');
      function isScrolledIntoView(elem) {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();

        var elemTop = $(elem).offset().top + $(elem).height();
        if ($(window).width() <= 480) {
          // disable for small screens
          var elemTop = $(elem).offset().top + ($(elem).height() * 2);
        }
        var elemBottom = elemTop + $(elem).height();
        return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
      }

      window.onscroll = function (event) {
        // attaches to scroll event... not great
        for (var i = 0; i < containers.length; i++) {
          var container = containers[i];
          if (isScrolledIntoView(container)) {
              if ($(window).width() >= 480) {
                // animate as needed here
                for (i = 0; i < containers.length; i++) {
                  //adds class 'active'
                  $(containers[i]).removeClass('active');
                }
                $(container).addClass('active');
              } else {
                $(container).addClass('active');
              }
            }
          }
      };