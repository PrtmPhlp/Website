var ReleaseDate = new Date("May 14, 2021 20:00:00").getTime();
var TimerFunction = setInterval(function () {
    var DatumHeute = new Date().getTime();
    var Differenz = ReleaseDate - DatumHeute;

//    var d = Math.floor(Differenz / (1000 * 60 * 60 * 24));
    var h = Math.floor((Differenz % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var m = Math.floor((Differenz % (1000 * 60 * 60)) / (1000 * 60));
    var s = Math.floor((Differenz % (1000 * 60)) / 1000);

    document.getElementById("timer").innerHTML =
        "<span>" +
//        d +
//        "<br><i>Tage</i></span><span>" +
        h +
        "<br><i>Stunden</i></span><span>" +
        m +
        "<br><i>Minuten</i></span><span>" +
        s +
        "<br><i>Sekunden</i></span>";

    if (Differenz < 0) {
        clearInterval(TimerFunction);
        document.getElementById("timer").innerHTML = "Abgelaufen";
    }
}, 1);

//Timer 2
var ReleaseDate1 = new Date("May 06, 2021 8:00:00").getTime();
var TimerFunction = setInterval(function () {
    var DatumHeute = new Date().getTime();
    var Differenz = ReleaseDate1 - DatumHeute;

    var h = Math.floor((Differenz % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var m = Math.floor((Differenz % (1000 * 60 * 60)) / (1000 * 60));
    var s = Math.floor((Differenz % (1000 * 60)) / 1000);

    document.getElementById("timer2").innerHTML =
        "<span>" +
        h +
        "<br><i>Stunden</i></span><span>" +
        m +
        "<br><i>Minuten</i></span><span>" +
        s +
        "<br><i>Sekunden</i></span>";

    if (Differenz < 0) {
        clearInterval(TimerFunction);
        document.getElementById("timer2").innerHTML = "Abgelaufen";
    }
}, 1);
alert('Diese Website ist für Querformat optimiert. Benutze dies, für eine besseres Benutzererlebnis :) ')
//Timer3
var ReleaseDate2 = new Date("May 06, 2021 13:05:00").getTime();
var TimerFunction = setInterval(function () {
    var DatumHeute = new Date().getTime();
    var Differenz = ReleaseDate2 - DatumHeute;

    var h = Math.floor((Differenz % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var m = Math.floor((Differenz % (1000 * 60 * 60)) / (1000 * 60));
    var s = Math.floor((Differenz % (1000 * 60)) / 1000);

    document.getElementById("timer3").innerHTML =
        "<span>" +
        h +
        "<br><i>Stunden</i></span><span>" +
        m +
        "<br><i>Minuten</i></span><span>" +
        s +
        "<br><i>Sekunden</i></span>";

    if (Differenz < 0) {
        clearInterval(TimerFunction);
        document.getElementById("timer2").innerHTML = "Abgelaufen";
    }
}, 1);
