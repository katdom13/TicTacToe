class Player {
    constructor(name, mark) {
        this.name = name;
        this.mark = mark;
    }
}

var p1Name = prompt("Enter player 1 name");
var p2Name = prompt("Enter player 2 name");

var p1 = new Player(p1Name, "X");
var p2 = new Player(p2Name, "O");

var board = ["", "", "", "", "", "", "", "", ""];
var isWon = false;
var currentPlayer = p1;

var message = document.querySelector(".message");
message.innerHTML = currentPlayer.name +"'s Turn";

var playerDict = new Object();
playerDict[p1.name] = 0;
playerDict[p2.name] = 0;

var place = document.querySelector("#placemark");
var cellIdx = document.querySelector("#cell");

place.onclick = function() {
    var index = parseInt(cellIdx.value);
    if(!isNaN(index) && index <= 9 && index >= 1) {
        if(board[index - 1] === "") {
            board[index - 1] = currentPlayer.mark;
            var cell = document.querySelector("#cell-" +index);
            cell.innerHTML = currentPlayer.mark;

            isWon = validateBoard();

            if(isWon || !board.includes("")) {
                if(isWon) {
                    message.innerHTML = "Player " +currentPlayer.name +" wins";
                    playerDict[currentPlayer.name] = 1
                }else {
                    message.innerHTML = "Game ended in draw";
                    playerDict[p1.name] = 1;
                    playerDict[p2.name] = 1;
                }
                
                var playerAction = document.querySelector("#player-action");
                playerAction.style.display = "none";
                $("#record").toggle();
                return;
            }

            currentPlayer = (currentPlayer === p1) ? p2 : p1;
            message.innerHTML = currentPlayer.name +"'s Turn";
        }
    }
    document.getElementById("cell").value = "";
};

var record = document.querySelector("#record");
record.onclick = function() {
    var form = document.querySelector("#record-form");
    var data = document.createElement("input");
    data.type = "hidden";
    data.name = "data";
    data.value = JSON.stringify(playerDict);
    form.appendChild(data);
    form.submit();
}

function validateBoard() {
    const winIdx = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    for(var i = 0; i < 8; i++) {
        var win = winIdx[i];
        if(board[win[0]] !== "" && board[win[1]] !== "" && board[win[2]] !== ""){
            if(board[win[0]] === board[win[1]] && board[win[1]] === this.board[win[2]]) {
                return true;
            }    
        }
    }

    return false;
}