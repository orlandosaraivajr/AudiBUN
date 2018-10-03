function change_click_categoria_distrito() {
    var distrito = document.getElementById("id_categoria_distrito").value;
    if (distrito == 0) {
        var link = document.getElementById('id_bairro');
        link.style.visibility = 'visible';
    } else {
        var link = document.getElementById('id_bairro');
        link.style.visibility = 'hidden';
        link.value = '';
    }
}

function change_distrito_click_bairro() {
    document.getElementById("id_categoria_distrito").value = 0;
}
