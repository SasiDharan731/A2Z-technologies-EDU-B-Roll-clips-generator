var p=300;
var b=10;
var o=0;
var f=true;
function dd1()
{
    setInterval(dd,0.1);
    if (f)
    {
        rr();
    }
    f=False;
}

function keydown()
{
    var event = window.event ? window.event : e;
    if (event.keyCode==39 && p<800)
    {
        p+=5;
    }
    else if (event.keyCode==37 && p>300)
    {
        p-=5;
    }
}
function dd()
{
    document.getElementById("kla").style.left = p+"px"; 
    document.getElementById("fan").innerHTML =o; 
    if ((b<580 && b>500) && (p-r>-30 && p-r<90))
    {
        b=0;
        o-=10;
    }
    if (o<0)
    {
        alert("game over....");
        window.location.href = "index.html";
    }
}
function rr()
{
	r=Math.floor(Math.random()*600+300);
	document.getElementById("img1").style.left = r+"px";
    if (b==10)
    {
        setInterval(opp,10);
    }
}
function opp()
{
    document.getElementById("img1").style.top=b+"px";
    if (b<600)
    {
        b+=5;  
    }
    else
    {
        b=0;
        l();
        rr();
    }
}
function l()
{
    o+=1;
}