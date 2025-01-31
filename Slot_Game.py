import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,  
}

def get_slot_machine_spin (rows, cols, symbols):
    all symbols = []
    for symbol, symbol_count in symbols.items (): 
        for i in range (symbol_count)
            all_symbols.appened (symbol)


    columns - ([],[].[])
    for _ in range(cols):
        column = [] 
        current_symbols = all_symbols
        for _ in range (rows):
            value = random.choice (all_symbols)
            current_symbols.remove (value)
            column.append (value)
        
        columns.append

    return columns

def print_slot_machines ():
    for row in range (len(column[0])):
        for i, column in enumerate(columns): 
            if i != len(columns) - 1:
            print(column at [row], "|")
        else:
            print(column[row])



def deposit ():
    while True:
        amount = input ('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount) # This and the code above allows the user to input their deposit whilst also making sure its a legitimate value 
            if amount > 0:
                break
            else:
                print ('Amount must be greater that 0.')
        else:
            print ('Please enter a number')

    return amount

  

def get_number_of_lines(): 
     while True:
        lines = input ('How many lines would you like to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit():
            lines = int(lines) # This and the code above allows the user to input their deposit whilst also making sure its a legitimate value 
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print ('Enter a Valid Number of Lines.')
        else:
            print ('Please enter a number')

     return lines

def get_bet():
    while True:
        amount = input ('How much would you like to bet on each line?')
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between {MIN_BET} - {MAX_BET}.')
        else:
            print('Please enter a number')

    return amount
     

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
    
        if total_bet > balance:
            print(
                f"You don't have the facilities for that big man. Your current balance is ${balance}")
        else:
            break

    print(
        f'You are betting {bet} on {lines}lines. Total bet is equal to ${total_bet} ')
    
    print (balance, lines)


slots = get_slot_machine_spin (ROWS, COLS, symbol_count)
print_slot_machines (slots)


main()
     

     
    





    


