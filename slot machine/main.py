import random

# Constants
MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = ["A", "B", "C", "D"]
symbol_weights = [2, 4, 6, 8]  # The probability of each symbol appearing
symbol_rewards = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def generate_random_reels(rows, cols, symbols, weights):
    """Generate a slot machine grid with random symbols."""
    reels = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            symbol = random.choices(symbols, weights)[0]
    #The [0] at the end of random.choices(symbols, weights)[0] is used to access the first (and only) element in the list.
    #This extracts the single selected symbol from the list, so get 'C' instead of ['C'].     
            row.append(symbol)
        reels.append(row)
    return reels


def calculate_winnings(reels, lines, bet_amount, reward_values):
    """Check the reels and calculate winnings based on matching rows."""
    total_winnings = 0
    winning_lines = []

    for line in range(lines):
        if all(reels[line][0] == symbol for symbol in reels[line]):
            total_winnings += reward_values[reels[line][0]] * bet_amount
            winning_lines.append(line + 1)

    return total_winnings, winning_lines

def display_reels(reels):
    """Print the slot machine's reels."""
    for row in reels:
        print(" | ".join(row))

def get_deposit():
    while True:
        deposit_amount = input("What would you like to deposit? $")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount > 0:
                return deposit_amount
            else:
                print("Deposit amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

def get_lines_to_bet_on():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")

def get_bet_amount():
    while True:
        bet_amount = input("What would you like to bet on each line? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                return bet_amount
            else:
                print(f"Bet amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

def play_spin(balance):
    lines = get_lines_to_bet_on()

    while True:
        bet = get_bet_amount()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds. Your current balance is: ${balance}")
        else:
            break

    print(f"Betting ${bet} on {lines} lines. Total bet: ${total_bet}")

    reels = generate_random_reels(ROWS, COLS, symbols, symbol_weights)
    display_reels(reels)

    winnings, winning_lines = calculate_winnings(reels, lines, bet, symbol_rewards)
    print(f"You won ${winnings}.")
    print("Winning lines:", *winning_lines)

    return winnings - total_bet

def main():
    balance = get_deposit()

    while True:
        print(f"Current balance: ${balance}")
        play_or_quit = input("Press enter to play (or 'q' to quit): ")
        if play_or_quit.lower() == "q":
            break
        balance += play_spin(balance)

    print(f"You're leaving with ${balance}")

if __name__ == "__main__":
    main()
