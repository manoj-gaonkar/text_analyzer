
function notfill(event){
    empt=document.forms['form1']['text'].value;
    var txtarea=document.getElementById('txtarea');
    var err = document.getElementById('error');
    if(empt=="")
    {
        document.getElementById('analyze').addEventListener('click',function(event){
            event.preventDefault();
        })
        err.style.visibility = 'visible';
        txtarea.style.borderColor="red";
        setInterval(function(){
            // err.classList.add("errbeg");
            // err.classList.toggle("errbeg");
            txtarea.style.borderColor="black";
            err.style.visibility='hidden';
        },1000);
        return false;
    }
    else{
        return true;
    }
}