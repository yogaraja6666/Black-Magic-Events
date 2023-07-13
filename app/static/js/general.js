function change(){
    let tn = document.getElementById("tnumber").value
    let tp = document.getElementById("total")
    let a = 500 * tn
    tp.innerHTML = "Total : Rs.  " + a
}