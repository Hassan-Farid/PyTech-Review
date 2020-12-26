/*
function addToQuery(num) {
    let query = document.querySelector("#query").value;
    document.querySelector('#query').value = query + num;
};
*/

document.querySelector('#one').onclick = function() {
    let query = document.querySelector("#query").value;
    document.querySelector('#query').value = query + '1';
};


document.querySelector('#two').onclick = function() {
    let query = document.querySelector("#query").value;
    document.querySelector('#query').value = query + '2';
};

document.querySelector('#three').onclick = function() {
    let query = document.querySelector("#query").value;
    document.querySelector('#query').value = query + '3';
};