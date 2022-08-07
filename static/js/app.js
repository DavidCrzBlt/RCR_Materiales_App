var productos = document.getElementById("productos");
var fragment = document.createDocumentFragment();

for (let i = 0; i < myproducts.length; i++) {
    var div1 = document.createElement('div');
    var div2 = document.createElement('div');
    var img = document.createElement('img');
    var div3 = document.createElement('div');
    var h5 = document.createElement('h5');
    var p = document.createElement('p');
    
    div1.className = "col";
    div2.className = "card";
    div3.className = "card-body"
    h5.className = "card-title text-center text-capitalize"
    p.className = "card-text"
    img.className = "card-img-top"

    var cardTitle = document.createTextNode(myproducts[i]);
    var cardText = document.createTextNode(myprices[i]);
    img_src_start = "http://localhost:5000/static/db_images/";
    fileType = ".png";
    img_src = img_src_start.concat(myids[i].toString(),fileType);
    img.src = img_src;

    div1.appendChild(div2);
    div2.appendChild(img);
    div2.appendChild(div3);
    div3.appendChild(h5);
    div3.appendChild(p);
    h5.appendChild(cardTitle);
    p.appendChild(cardText);
    fragment.appendChild(div1);
}
productos.appendChild(fragment);
