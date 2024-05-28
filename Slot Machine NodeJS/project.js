const prompt = require("prompt-sync")();


const ROWS = 3;
const COLS = 3;
const Symbols_COUNT = {
    A: 3,
    B: 9,
    C: 27,
    D: 81,

}

const Symblos_VALUE = {
    A: 8,
    B: 4,
    C: 2,
    D: 1,
}


const getDeposit = () => {
    while (true) {
        const depositAmount = parseFloat(prompt("Enter a deposit amount: "));
        if (isNaN(depositAmount) || depositAmount <= 0) {
            console.log("Invalid number, Please Try again!");
        }
        else {
            return depositAmount
        }
    }
};

const getNumberOfLines = () => {
    while (true) {
        const NumberOfLines = parseFloat(prompt("Enter the number of line(s) to bet on (1-3): "));
        if (isNaN(NumberOfLines) || NumberOfLines <= 0 || NumberOfLines > 3) {
            console.log("Invalid number of Lines, Please Try again!");
        }
        else {
            return NumberOfLines
        }
    }
};

const getBet = (balance, lines) => {
    while (true) {
        const NumberOfBet = parseFloat(prompt("Enter the bet per line: "));
        if (isNaN(NumberOfBet) || NumberOfBet <= 0 || NumberOfBet > balance / lines) {
            console.log("Invalid Bet, Please Try again!");
        }
        else {
            return NumberOfBet
        }
    }
};

const spin = () => {
    const symbols = [];
    for (const [symbol, count] of Object.entries(Symbols_COUNT)) {
        for (let i = 0; i < count; i++) {
            symbols.push(symbol);
        };
    };
    const reels = [];
    for (let i = 0; i < COLS; i++) {
        reels.push([]);
        const reelSymbol = [...symbols];
        for (let j = 0; j < ROWS; j++) {
            const randomIndex = Math.floor(Math.random() * reelSymbol.length);
            const selectedSymbol = reelSymbol[randomIndex];
            reels[i].push(selectedSymbol);
            reelSymbol.splice(randomIndex, 1);
        };
    };
    return reels
};

const transpose = (reels) => {
    const rows = [];
    for (let i = 0; i < ROWS; i++) {
        rows.push([]);
        for (let j = 0; j < COLS; j++) {
            rows[i].push(reels[j][i]);
        }
    }
    return rows;
};

const printRows = (rows) => {
    for (const row of rows) {
        let rowString = "";
        for (const [i, symbol] of row.entries()) {
            rowString += symbol;
            if (i != row.length - 1) {
                rowString += " | "
            };
        };
        console.log(rowString);
    };
};


const getWinings = (rows, bet, lines) => {
    let winnings = 0;
    for (let i = 0; i < lines; i++) {
        const symbols = rows[i];
        let allSame = true;

        for (const symbol of symbols) {
            if (symbol != symbols[0]) {
                allSame = false;
                break;
            };
        };

        if (allSame) {
            winnings += bet * Symblos_VALUE[symbols[0]];
        }
    };
    return winnings;
};

const game = () => {

    let balance = getDeposit();

    while (true) {
        console.log("You have balance of: " + balance.toString());
        const NumberOfLines = getNumberOfLines()
        const bet = getBet(balance, NumberOfLines)
        balance -= bet * NumberOfLines;
        const reels = spin();
        const rows = transpose(reels);
        printRows(rows);
        const winnings = getWinings(rows, bet, NumberOfLines);
        balance += winnings
        console.log("You have won: " + winnings.toString());

        if (balance <= 0) {
            console.log("You Ran Out of Money!");
            break;
        }
        const playAgain = prompt("Do you want to play again? (y/n): ")
        if (playAgain != "y") {
            break
        };
    }
};

game(); 