# web-template
> Author: web-template

## PatchNotes

## Chall
### Description


### Solution
Oppgaven hinter til at man må sortere ut de i listen som har klasse, så gå sidelengs gjennom de, tar man en bokstav fra hver, bortover, så får man flagg

js:
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
