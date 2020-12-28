
function tambahForm() {
    const hari = document.getElementById('hari').value;
    const jam = document.getElementById('jam').value;
    const mataKuliah = document.getElementById('mataKuliah').value;
    const kelas = document.getElementById('kelas').value;

    var tabel = document.getElementById("daftarKelas").getElementsByTagName('tbody')[0];
    var newRow = tabel.insertRow(tabel.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = hari;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = jam;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = mataKuliah;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = kelas;
    cell5 = newRow.insertCell(4);
    cell5.innerHTML = `<a onClick="onEdit(this)">Edit</a>
                       <a onClick="onDelete(this)">Delete</a>`;

}