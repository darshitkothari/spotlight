function display_ct()
{
    var x = new Date()
    var day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    var x1 = x.getMonth() + 1+ "/" + x.getDate() + "/" + x.getYear();
    var hours = x.getHours()
    var minutes = x.getMinutes()
    var seconds = x.getSeconds()
    if (hours < 10)
        {hours = '0' + x.getHours()}
    if (minutes < 10)
        {minutes = '0' + x.getMinutes()}
    if (seconds < 10)
        {seconds = '0' + x.getSeconds()}
    x1 = hours + ":" +  minutes + ":" + seconds;
    x2 = day[x.getDay()] + ", " + month[x.getMonth()] + " " + x.getDate()
    document.getElementById('ct').innerHTML = x1;
    document.getElementById('dy').innerHTML = x2;
    display_c();
}