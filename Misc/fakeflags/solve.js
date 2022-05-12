lists = document.querySelector("body > ul").children;
j = 0;
tot = "";
for (var i = 0; i < lists.length; i++) {
    if (lists[i].className == 'T') {
        tot = tot + lists[i].innerText["TG22{".length+j];
        j++;
    }
}
console.log("TG22{" + tot + "}");