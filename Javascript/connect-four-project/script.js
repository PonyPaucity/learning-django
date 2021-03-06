const playerOne = prompt("Please enter your name", "Player 1");
const player1Color = 'rgb(86, 151, 255)';

const playerTwo = prompt("Please enter your name", "Player 2");
const player2Color = 'rgb(237, 45, 73)';

const game_on = true;
const gameBoard = $('table tr');

function reportWin(rowNum, colNum) {
    console.log("You won starting at this row,col")
    console.log(rowNum);
    console.log(colNum);
}

function changeColor(rowIndex, colIndex, color) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color', color);
}

function returnColor(rowIndex, colIndex) {
    return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}

function checkBottom(colIndex) {
    let colorReport = returnColor(5, colIndex);
    for (let row = 5; row > -1; row--) {
        colorReport = returnColor(row, colIndex);
        if (colorReport === 'rgd(128, 128, 128)') {
            return row
        }
    }
}

function colorMatchCheck(one, two, three, four) {
    return (one === two && one === three && one === four && one != 'rgd(128, 128, 128)' && one !== undefined)
}

// Check for Horizontal Wins
function horizontalWinCheck() {
    for (let row = 0; row < 6; row++) {
        for (let col = 0; col < 4; col++) {
            if (colorMatchCheck(returnColor(row, col), returnColor(row, col + 1), returnColor(row, col + 2), returnColor(row, col + 3))) {
                console.log('horiz');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

// Check for Vertical Wins
function verticalWinCheck() {
    for (var col = 0; col < 7; col++) {
        for (var row = 0; row < 3; row++) {
            if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col), returnColor(row + 2, col), returnColor(row + 3, col))) {
                console.log('vertical');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

// Check for Diagonal Wins
function diagonalWinCheck() {
    for (var col = 0; col < 5; col++) {
        for (var row = 0; row < 7; row++) {
            if (colorMatchCheck(returnColor(row, col), returnColor(row + 1, col + 1), returnColor(row + 2, col + 2), returnColor(row + 3, col + 3))) {
                console.log('diag');
                reportWin(row, col);
                return true;
            } else if (colorMatchCheck(returnColor(row, col), returnColor(row - 1, col + 1), returnColor(row - 2, col + 2), returnColor(row - 3, col + 3))) {
                console.log('diag');
                reportWin(row, col);
                return true;
            } else {
                continue;
            }
        }
    }
}

$('h3').text(player1+" it is your turn")

$('.board buton').on('click', function() {
    let col= $(this).closest('td').index();
})