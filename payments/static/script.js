function sendNonce(nonce)
{
    console.log("foo")
}
function goo()
{
    console.log("foo")
}
var firstbuttonclicked=false
function buttor()
{
    firstbuttonclicked=true
    paymentval=document.getElementById("payment_val").value
}
function goobar(data)
{
    if(JSON.stringify(data)=='{"LOL":"YUH"}')
    {
        //console.log("mubugang");
        window.location="/success/";
    }
    else
    {
        alert("Error Transaction Has Not Went Through!")
        window.location="/error/"
    }

}
function foobar()
{
    paymentval=document.getElementById("payment_val").value
    
    $.ajax({
        type: "POST",
        url: "/",
        data: { payment_method_nonce: nonce,  'csrfmiddlewaretoken': csrf,'payment_amt':String(paymentval)},
        success:  function( data, textStatus, jQxhr ){
            goobar(data);
        },
    })
    

}
var nonce=""
var buttonclicked=false
var paymentval=0.23
var csrf=""

