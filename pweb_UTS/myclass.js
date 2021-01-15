
console.log("terhubung");
var Apakah = document.querySelector(".delete");
function inputData(){
    var hari = document.forms['inputan']['hari'].value;
    var matakuliah = document.forms['inputan']['mataKuliah'].value;
    var jam = document.forms['inputan']['jam'].value;

    if(hari == 'Monday') {
        var tabelMonday = document.querySelector('.Monday')
        var row = tabelMonday.insertRow(1);
        var cel1 = row.insertCell(0);
        var cel2 = row.insertCell(1);
        var cell3 = row.insertCell(2);
    
        cel1.innerHTML = matakuliah;
        cel2.innerHTML = jam;
        cell3.innerHTML = '<button onclick="deleteData()" class="delete">Delete</button>'
    }

    if (hari == 'Tuesday') {
        var tabelTuesday = document.querySelector('.Tuesday')
        var row = tabelTuesday.insertRow(1);
        var Tuesday1 = row.insertCell(0);
        var Tuesday2 = row.insertCell(1);
        var Tuesday3 = row.insertCell(2);

        Tuesday1.innerHTML = matakuliah;
        Tuesday2.innerHTML = jam;
        Tuesday3.innerHTML = '<button onclick="deleteData1()" class="delete">Delete</button>'  
    } 

    if (hari == 'Wednesday') {
        var tabelWednesday = document.querySelector('.Wednesday')
        var row = tabelWednesday.insertRow(1);
        var w1 = row.insertCell(0);
        var w2 = row.insertCell(1);
        var w3 = row.insertCell(2);

        w1.innerHTML = matakuliah;
        w2.innerHTML = jam;
        w3.innerHTML = '<button onclick="deleteData2()" class="delete">Delete</button>'  
    } 
  
    if (hari == 'Thursday') {
        var tabelThurday = document.querySelector('.Thursday')
        var row = tabelThurday.insertRow(1);
        var Thurday1 = row.insertCell(0);
        var Thurday2 = row.insertCell(1);
        var Thurday3 = row.insertCell(2);

        Thurday1.innerHTML = matakuliah;
        Thurday2.innerHTML = jam;
        Thurday3.innerHTML = '<button onclick="deleteData3()" class="delete">Delete</button>'  
    } 

    if (hari == 'Friday') {
        var tabelFriday= document.querySelector('.Friday')
        var row = tabelFriday.insertRow(1);
        var Friday1 = row.insertCell(0);
        var Friday2 = row.insertCell(1);
        var Friday3 = row.insertCell(2);

        Friday1.innerHTML = matakuliah;
        Friday2.innerHTML = jam;
        Friday3.innerHTML = '<button onclick="deleteData4()" class="delete">Delete</button>'  
    } 
}

function deleteData(){
    confirm("Apakah anda yakin akan menghapus daftar ini") 
        document.querySelector('.Monday').deleteRow(1);
}

function deleteData1(){
    confirm("Apakah anda yakin akan menghapus daftar ini") 
        document.querySelector('.Tuesday').deleteRow(1);
}
    
function deleteData2(){
    confirm("Apakah anda yakin akan menghapus daftar ini") 
        document.querySelector('.Wednesday').deleteRow(1);
}
    
function deleteData3(){
    confirm("Apakah anda yakin akan menghapus daftar ini") 
        document.querySelector('.Thursday').deleteRow(1);
}
    
function deleteData4(){
    confirm("Apakah anda yakin akan menghapus daftar ini") 
        document.querySelector('.Friday').deleteRow(1);
}




