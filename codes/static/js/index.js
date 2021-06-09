window.alert("ok");
var user = document.getElementById("user").value;
var title = document.getElementById("title").value;
var c = document.getElementById("code").value;
var discr = document.getElementById("discription").value;
if (user != null){
    create();
    window.alert("ok");
}
function create(){
    var contain = document.getElementById("bdy");
    var div = document.createElement("div");
    var cod = document.createTextNode(c);
    var code = document.createElement("code");
    code.appendChild(cod);
    div.appendChild(code);
    contain.appendChild(div);
}