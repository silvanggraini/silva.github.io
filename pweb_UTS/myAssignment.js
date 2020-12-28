console.log("terhubung");
var del = document.querySelector(".delete");
function inputData(){
    var tanggal = document.forms['inputan']['tanggal'].value;
    var matkul = document.forms['inputan']['matkul'].value;
    var dl = document.forms['inputan']['dl'].value;
    var ket = document.forms['inputan']['ket'].value;

    var tabelInputan = document.getElementById('TabelInputan');
    var row = tabelInputan.insertRow(1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);

    cell1.innerHTML = tanggal;
    cell2.innerHTML  = matkul;
    cell3.innerHTML  = dl;
    cell4.innerHTML  = ket;
    cell5.innerHTML  = `<input type="button" value="Delete" onclick="deleteData()" class="delete">`
}

function deleteData(){
    confirm("Apakah anda yakin akan menghapus daftar ini") 
        document.querySelector('#TabelInputan').deleteRow(1);
}
