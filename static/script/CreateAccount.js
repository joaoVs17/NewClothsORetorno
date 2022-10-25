let senha = document.getElementById("senha");
let senhaConfirmar = document.getElementById("senhaConfirmar");

let email = document.getElementById("email");
let emailConfirmar = document.getElementById("emailConfirmar")

let submit = document.getElementById("submit");


//Verifica se as senhas estão iguais
senha.onkeyup = function() {
    if (senha.value != senhaConfirmar.value) {
        submit.disabled = true;
        senha.setAttribute('style', 'border-color: red !important');
        senhaConfirmar.setAttribute('style', 'border-color: red !important');
    } 
    if (senha.value == senhaConfirmar.value) {
        submit.disabled = false;  
        senha.setAttribute('style', 'border-color: #FF6B18 !important');
        senhaConfirmar.setAttribute('style', 'border-color: #FF6B18 !important');
    }
}

senhaConfirmar.onkeyup = function() {
    if (senha.value != senhaConfirmar.value) {
        submit.disabled = true;
        senha.setAttribute('style', 'border-color: red !important');
        senhaConfirmar.setAttribute('style', 'border-color: red !important');
    } 
    if (senha.value == senhaConfirmar.value) {
        submit.disabled = false;
        senha.setAttribute('style', 'border-color: #FF6B18 !important');
        senhaConfirmar.setAttribute('style', 'border-color: #FF6B18 !important');
    }
}

//verifica se os emails estão iguais

email.onkeyup = function() {
    if (email.value != emailConfirmar.value) {
        submit.disabled = true;
        email.setAttribute('style', 'border-color: red !important');
        emailConfirmar.setAttribute('style', 'border-color: red !important');
    } 
    if (email.value == emailConfirmar.value) {
        submit.disabled = false;  
        email.setAttribute('style', 'border-color: #FF6B18 !important');
        emailConfirmar.setAttribute('style', 'border-color: #FF6B18 !important');
    }
}

emailConfirmar.onkeyup = function() {
    if (email.value != emailConfirmar.value) {
        submit.disabled = true;
        email.setAttribute('style', 'border-color: red !important');
        emailConfirmar.setAttribute('style', 'border-color: red !important');
    } 
    if (email.value == emailConfirmar.value) {
        submit.disabled = false;
        email.setAttribute('style', 'border-color: #FF6B18 !important');
        emailConfirmar.setAttribute('style', 'border-color: #FF6B18 !important');
    }
}