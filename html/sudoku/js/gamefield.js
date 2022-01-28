let currentNum;

function printNum(qcr) {
    if (currentNum >= 0 && currentNum <= 9) {
        document.getElementById(qcr).innerHTML = currentNum;

        //check for correct input
        if (currentNum != document.getElementById(qcr).className) {
            playerLose();
        }
    }
}

function playerLose() {
    let status = document.getElementById('status');
    status.style.color = 'red';
    status.innerHTML = 'You lose';
    status.style.display = 'block';

    for (let i = 0; i <= allQcr.length; i++) {
        document.getElementById(allQcr[i]).style.color = 'gray';
        document.getElementById(allQcr[i]).parentElement.style.pointerEvents = 'none';
    }
}

function changeBackgroundOfNum(num) {
    for (let i = 1; i <= 9; i++) {
        let allId = 'c' + i;
        document.getElementById(allId).style.backgroundColor = '#525252';
    }

    let id = 'c' + num;
    document.getElementById(id).style.backgroundColor = '#606060';
    currentNum = num;
}

function restartGame() {
    location.reload();
}
