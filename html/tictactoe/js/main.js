let roundNum = 0;

function drawStep(i) {
    let currentPlayer;
    let nextPlayer;
    roundNum++;

    if (roundNum % 2 == 0) {
        currentPlayer = "O";
        nextPlayer = "X";
    } else {
        currentPlayer = "X";
        nextPlayer = "O";
    }

    document.getElementById("d" + i).classList.add("notClickable");
    document.getElementById("p" + i).innerHTML = currentPlayer;
    document.getElementById("instruction").innerHTML = nextPlayer + " turn";

    if (roundNum > 2) {
        checkForWin(currentPlayer);
    }
}

function checkForWin(currentPlayer) {
    let p = ["p0", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"];

    for(let i = 0; i < 9; i++){
        p[i] = document.getElementById("p" + i).innerHTML;
    }

    if (areEqual(p[0], p[1], p[2]) || areEqual(p[3], p[4], p[5]) || areEqual(p[6], p[7], p[8]) ||
        areEqual(p[0], p[3], p[6]) || areEqual(p[1], p[4], p[7]) || areEqual(p[2], p[5], p[8]) ||
        areEqual(p[0], p[4], p[8]) || areEqual(p[2], p[4], p[6])) {
        document.getElementById("instruction").classList.add("playerWon");
        document.getElementById("instruction").innerHTML = currentPlayer + " won";

        let colClass = document.getElementsByClassName("col-md-4");

        for (let i = 0; i < colClass.length; i++) {
            colClass[i].classList.add("notClickable");
        }
    }else if(roundNum === 9){
        document.getElementById("instruction").classList.add("draw");
        document.getElementById("instruction").innerHTML = "Draw";
    }
}

function areEqual(p0, p1, p2) {
    if(p0 !== "" && p1 !== "" && p2 !== ""){
        if (p0 === p1 && p0 === p2 && p1 === p2) {
            return true;
        }
    }

    return false;
}

function restartGame(){
    location.reload();
}