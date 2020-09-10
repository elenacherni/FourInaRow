
const input = document.getElementById("colNumInput");
const submit = document.getElementById("submit");
function fill_input(col){
    input.setAttribute('value',col);
    submit.click();
}

