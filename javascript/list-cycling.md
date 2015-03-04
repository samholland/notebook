# List cycling
Uses jquery. This could be a lot better.

    var i, j, k, delay, duration, interval;
    i = 0;
    j = 0;
    delay = 5000;
    duration = 500;
    $('.features-list li').hide().eq(0).addClass('active');
    listCycle = function(obj) {
      var listLength = $(obj + ' li').length - 1;
      $(obj + ' li:eq(' + i + ')')
        .delay(delay)
        .fadeIn(duration, function() {
          $(obj + ' li:eq(' + i + ')').delay(delay).removeClass('active');
          i == listLength ? i = 0 : i++;
          listCycle(obj);
        });
    }