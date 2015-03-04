# Oscillator

    var frequency = 8; 
    var maxValue = 100; 
    var position = 0;
    var numX = 0;

    function updateNumber() {
         position++;
         numX = Math.sin(position * 2 * Math.PI/frequency) * (maxValue/2 + maxValue/2);
    }