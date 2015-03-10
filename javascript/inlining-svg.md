# Inlining SVG

With modernizr, inlines svg with class 'svg_inline' so it can be animated; replaces with png if the browser doesn't support svg.

    if ($("html").hasClass("inlinesvg")) {
      return $(".svg_inline").each(function() {
        var $img, imgClass, imgID, imgURL;
        $img = $(this);
        imgID = $img.attr("id");
        imgClass = $img.attr("class");
        imgURL = $img.attr("src");
        return jQuery.get(imgURL, (function(data) {
          var $svg;
          $svg = $(data).find("svg");
          if (typeof imgID !== "undefined") {
            $svg = $svg.attr("id", imgID);
          }
          if (typeof imgClass !== "undefined") {
            $svg = $svg.attr("class", imgClass + " replaced-svg");
          }
          $svg = $svg.removeAttr("xmlns:a");
          return $img.replaceWith($svg);
        }), "xml");
    });
    } else {
      return $(".svg_inline").each(function() {
        var $img, imgPNG, imgURL;
        $img = $(this);
        imgURL = $img.attr("src").split(".");
        imgPNG = imgURL[0] + ".png";
        $img.attr("src", imgPNG);
      });
    }