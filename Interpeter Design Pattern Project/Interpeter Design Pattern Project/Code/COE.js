var COEtutors = new Map([
    ['Joanne Rizkallah', 'JR_01'],
    ['Wajih El Tayyar', 'WE_01'],
    ['Dany Chaddad', 'DC_01']
]);
var n1 = COEtutors.get('Joanne Rizkallah');
var n2 = COEtutors.get('Wajih El Tayyar');
var n3 = COEtutors.get('Dany Chaddad');
document.getElementById("n1").innerHTML = n1;
document.getElementById("n2").innerHTML = n2;
document.getElementById("n3").innerHTML = n3;