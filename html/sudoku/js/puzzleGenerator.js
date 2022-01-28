function initGamefield() {
    checkForDifficultyInput();

    gamefieldPlayingState();

    let gamefieldArray = initGamefieldArray();
    console.log(gamefieldArray);

    fillGamefield(gamefieldArray);
    //fillGamefieldRemasterd(gamefieldArray);
}

function initGamefieldArray() {
    let allQuadrantColumnRow = [];
    let quadrant = 0;
    let column = 0;
    let row = 0;

    //fill every cell in array
    while (quadrant < 9) {
        quadrant++;
        column = 0;

        while (column < 3) {
            column++;
            row = 0;

            while (row < 3) {
                row++;
                let quadrantColumnRow = quadrant + '' + row + '' + column;
                allQuadrantColumnRow.push(quadrantColumnRow);
            }
        }
    }

    return allQuadrantColumnRow;
}

function gamefieldPlayingState() {
    document.getElementById('start').style.display = 'none';
    document.getElementById('restart').style.display = 'block';
    document.getElementById('difficulty').firstChild.readOnly = true;
}

function checkForDifficultyInput() {
    let difficulty = document.getElementById('difficulty').firstChild.value;

    if (difficulty < 1 || difficulty > 10 || difficulty == '') {
        restartGame();
    }
}

function fillGamefield(gamefieldArray) {
    let randomIndex;
    let rows0 = [0, 1, 2];
    let rows1 = [27, 28, 29];
    let rows2 = [54, 55, 56];
    let col0 = [8, 9, 3, 2, 7, 6, 4, 5, 1];
    let col1 = [2, 7, 6, 4, 5, 1, 8, 9, 3];
    let col2 = [4, 5, 1, 8, 9, 3, 2, 7, 6];
    let col3 = [5, 1, 8, 9, 3, 2, 7, 6, 4];
    let col4 = [9, 3, 2, 7, 6, 4, 5, 1, 8];
    let col5 = [7, 6, 4, 5, 1, 8, 9, 3, 2];
    let col6 = [6, 4, 5, 1, 8, 9, 3, 2, 7];
    let col7 = [1, 8, 9, 3, 2, 7, 6, 4, 5];
    let col8 = [3, 2, 7, 6, 4, 5, 1, 8, 9];

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            //set random int for randomize row
            randomIndex = Math.floor(Math.random() * rows0.length) + 0;
        }

        //get first row (every 3rd in array)
        let quadrantColumnRowPos = row * 3 + rows0[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col0[row];
        quadrantColumnRow.classList.add(col0[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows0.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows0.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows0[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col1[row];
        quadrantColumnRow.classList.add(col1[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows0.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows0.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows0[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col2[row];
        quadrantColumnRow.classList.add(col2[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows0.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows1.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows1[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col3[row];
        quadrantColumnRow.classList.add(col3[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows1.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows1.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows1[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col4[row];
        quadrantColumnRow.classList.add(col4[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows1.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows1.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows1[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col5[row];
        quadrantColumnRow.classList.add(col5[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows1.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows2.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows2[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col6[row];
        quadrantColumnRow.classList.add(col6[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows2.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows2.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows2[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col7[row];
        quadrantColumnRow.classList.add(col7[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows2.splice(randomIndex, 1);

    for (let row = 0; row < 9; row++) {
        if (row === 0) {
            randomIndex = Math.floor(Math.random() * rows2.length) + 0;
        }

        let quadrantColumnRowPos = row * 3 + rows2[randomIndex];
        let quadrantColumnRow = document.getElementById(gamefieldArray[quadrantColumnRowPos]);
        quadrantColumnRow.innerHTML = col8[row];
        quadrantColumnRow.classList.add(col8[row]);
        changeStylePlayingState(quadrantColumnRow);
    }

    rows2.splice(randomIndex, 1);

    setDifficulty(gamefieldArray);
}

function setDifficulty(gamefieldArray) {
    let chosenDif = document.getElementById('difficulty').firstChild.value;

    for (let i = 0; i < gamefieldArray.length; i++) {
        //calculate range
        let factor = gamefieldArray.length / 2;
        let dif = Math.floor(Math.random() * (factor - chosenDif)) + 0;
        let quadrantColumnRow = document.getElementById(gamefieldArray[i + dif]);

        quadrantColumnRow.innerHTML = ' ';
        changeStyleForDifficulty(quadrantColumnRow);
    }
}

function fillGamefieldRemasterd() {
    let rows0 = [0, 1, 2];
    let rows1 = [27, 28, 29];
    let rows2 = [54, 55, 56];
    let col0 = [8, 9, 3, 2, 7, 6, 4, 5, 1];
    let col1 = [2, 7, 6, 4, 5, 1, 8, 9, 3];
    let col2 = [4, 5, 1, 8, 9, 3, 2, 7, 6];
    let col3 = [5, 1, 8, 9, 3, 2, 7, 6, 4];
    let col4 = [9, 3, 2, 7, 6, 4, 5, 1, 8];
    let col5 = [7, 6, 4, 5, 1, 8, 9, 3, 2];
    let col6 = [6, 4, 5, 1, 8, 9, 3, 2, 7];
    let col7 = [1, 8, 9, 3, 2, 7, 6, 4, 5];
    let col8 = [3, 2, 7, 6, 4, 5, 1, 8, 9];
    let allRows = [rows0, rows1, rows2];
    let allCol = [col0, col1, col2, col3, col4, col5, col6, col7, col8];

    let i = 0;

    for (let col = 0; col < 9; col++) {
        for (let row; row < 3; row++) {
            if (row === 0) {
                rndmIndex = Math.floor(Math.random() * allRows[row].length) + 0;
            }

            let quadrantColumnRowPos = row * 3 + allRows[row][rndmIndex];
            let quadrantColumnRow = document.getElementById(allQuadrantColumnRow[quadrantColumnRowPos]);
            quadrantColumnRow.innerHTML = allCol[col][row];
            quadrantColumnRow.classList.add(allCol[col][row]);
            quadrantColumnRow.style.color = '#999999';
            quadrantColumnRow.parentElement.style.pointerEvefnts = 'none';
        }

        if (col <= 6) {
            i = 1;
        } else if (col <= 9) {
            i = 2;
        } else if (col <= 12) {
            i = 3;
        }

        allRows[i].splice(rndmIndex, 1);
    }
}

//Styling starts here
function changeStylePlayingState(quadrantColumnRow) {
    quadrantColumnRow.style.color = '#999999';
    quadrantColumnRow.parentElement.style.pointerEvents = 'none';
}

function changeStyleForDifficulty(quadrantColumnRow) {
    quadrantColumnRow.parentElement.style.pointerEvents = 'auto';
    quadrantColumnRow.style.color = '#ffffff';
}
