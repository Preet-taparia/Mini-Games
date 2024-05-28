#include <stdio.h>
#include <unistd.h>

char board[3][3];  // The Tic-Tac-Toe board
char player_name[2][20];  // Array to store the names of the players

// Function to initialize the board with empty spaces
void initialize_board() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            board[i][j] = ' ';
        }
    }
}

// Function to print the current state of the board
void print_board() {
    printf("\033[2J\033[H");  // Clear the screen using escape sequences
    printf("   Tic-Tac-Toe\n");
    printf("---------------\n");
    printf("   1   2   3\n");  // Modified row labels
    printf(" -------------\n");
    
    for (int i = 0; i < 3; i++) {
        printf("%d", i + 1);  // Modified column labels
        
        for (int j = 0; j < 3; j++) {
            printf(" | %c ", board[i][j]);
        }
        
        printf("|\n");
        printf(" -------------\n");
    }
}

// Function to check if a player has won
char check_win(char board[3][3]) {
    // Check rows
    for (int i = 0; i < 3; i++) {
        if (board[i][0] != ' ' && board[i][0] == board[i][1] && board[i][1] == board[i][2]) {
            return board[i][0];  // Player wins
        }
    }

    // Check columns
    for (int j = 0; j < 3; j++) {
        if (board[0][j] != ' ' && board[0][j] == board[1][j] && board[1][j] == board[2][j]) {
            return board[0][j];  // Player wins
        }
    }

    // Check diagonals
    if (board[0][0] != ' ' && board[0][0] == board[1][1] && board[1][1] == board[2][2]) {
        return board[0][0];  // Player wins
    }
    
    if (board[0][2] != ' ' && board[0][2] == board[1][1] && board[1][1] == board[2][0]) {
        return board[0][2];  // Player wins
    }

    return ' ';  // No winner
}

// Function to check if the board is full
int is_board_full() {
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[i][j] == ' ') {
                return 0;  // Board is not full
            }
        }
    }
    return 1;  // Board is full
}

// Function to play the game
void play_game() {
    int row, col;
    char player = 'X';  // Player X starts the game

    initialize_board();

    // Get player names
    printf("Enter Player X's name: ");
    scanf("%s", player_name[0]);
    printf("Enter Player O's name: ");
    scanf("%s", player_name[1]);

    while (1) {
        // Print the board
        print_board();

        // Get the player's move
        printf("Player %c (%s)'s turn.\n", player, (player == 'X') ? player_name[0] : player_name[1]);  // Modified prompt
        printf("Enter row (1-3): ");
        
        if (scanf("%d", &row) != 1) {
            printf("Invalid input. Please enter a number.\n");
            sleep(1);  // Delay for one second
            fflush(stdin);  // Clear input buffer
            continue;
        }
        
        printf("Enter column (1-3): ");  // Modified prompt
        
        if (scanf("%d", &col) != 1) {
            printf("Invalid input. Please enter a number.\n");
            sleep(1);  // Delay for one second
            fflush(stdin);  // Clear input buffer
            continue;
        }

        // Adjust the row and column to match the array indices
        row--;
        col--;

        // Check if the move is valid
        if (row < 0 || row >= 3 || col < 0 || col >= 3 || board[row][col] != ' ') {
            printf("Invalid move. Try again.\n");
            sleep(1);  // Delay for one second
            continue;
        }

        // Make the move
        board[row][col] = player;

        // Check if the player has won
        char winner = check_win(board);
        if (winner != ' ') {
            print_board();
            printf("Player %c (%s) wins!\n", winner, (winner == 'X') ? player_name[0] : player_name[1]);
            break;
        }

        // Check if the game is a draw
        if (is_board_full()) {
            print_board();
            printf("It's a draw!\n");
            break;
        }

        // Switch to the other player
        player = (player == 'X') ? 'O' : 'X';
    }
}

int main() {
    printf("Tic-Tac-Toe Game\n");
    printf("----------------\n");
    play_game();
    return 0;
}