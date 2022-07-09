function notfill(){
    document.getElementById('error').innerHTML="Please enter any thing";

    console.log("ja na");
    empt=document.forms['text'].value;
    if(empt=="")
    {
        e.preventDefault();
        document.getElementById('error').innerHTML="Please enter any thing";
        return false;
    }
}