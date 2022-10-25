const img1 = document.getElementById("img1");
const img2 = document.getElementById("img2");
const ipt1 = document.getElementById("ipt1");
const ipt2 = document.getElementById("ipt2");



ipt1.onchange = function() {
    let foto_usuario = ipt1.files[0];
    let url = URL.createObjectURL(foto_usuario)
    console.log(url);

    img1.src = url;
}

ipt2.onchange = function() {
    let foto_usuario = ipt2.files[0];
    let url = URL.createObjectURL(foto_usuario)
    console.log(url);

    img2.src = url;
}