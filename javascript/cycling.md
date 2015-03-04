# Cycling

To cycle through a list of objects; in this case, applying different classes at an interval

    var classList = ['class1', 'class2', 'class3'];
    var period = 4000;
    var index = 0;

    function cycleClasses() {
      index = (index + 1) % classList.length;
      document.getElementById('heroPrimaryWrap').className = ' ' + classList[index];
    }

    setInterval(cycleClasses, period);