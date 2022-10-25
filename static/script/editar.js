const ipt_foto_usuario = document.getElementById("foto_usuario");
const foto = document.getElementById("foto");



ipt_foto_usuario.onchange = function() {
    let foto_usuario = ipt_foto_usuario.files[0];
    let url = URL.createObjectURL(foto_usuario)
    console.log(url);

    foto.src = url;
}