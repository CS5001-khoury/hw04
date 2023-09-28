"""
Student: UPDATE
Semester: UPDATE

Plays a guessing game with the client, and also has an option for the
computer to play the game with itself.
"""
from random import randint  # use randint(a, b) to get a random number between a and b, inclusive

# variables like this are often used so that there is 
# a single place to change the prompt if needed
# these strings could come from a file in the future, which
# would allow things like localization (modifying the game
# for different languages) easier to handle. 

WELCOME_PROMPT = """Welcome to the guessing game!"""
END_PROMPT = """Thanks for playing!"""
ACTION_PROMPT = """What would you like to do? """
COMMAND_TXT_HELP = "help"
COMMAND_TXT_PLAY = "play"
COMMAND_TXT_QUIT = "quit"
COMMAND_TXT_SET_NUM = "set number"
COMMAND_TXT_SET_HIGH = "set high"
COMMAND_TXT_SET_LOW = "set low"
COMMAND_TXT_RESET = "reset"

SETTING_SET_NUM_TXT = "maximum number of attempts"
SETTING_SET_HIGH_TXT = "highest value"
SETTING_SET_LOW_TXT = "lowest value"

HELP_PROMPT = f"""Enter one of the following commands:
    {COMMAND_TXT_HELP} - prints this message
    {COMMAND_TXT_PLAY} - plays the game
    {COMMAND_TXT_QUIT} - exits the program
    {COMMAND_TXT_SET_NUM} - sets the {SETTING_SET_NUM_TXT}
    {COMMAND_TXT_SET_HIGH} - sets the {SETTING_SET_HIGH_TXT}
    {COMMAND_TXT_SET_LOW} - sets the {SETTING_SET_LOW_TXT}
    {COMMAND_TXT_RESET} - resets to the default values
"""

INVALID_COMMAND = "Invalid command. Type 'help' for a list of commands."
ENTRY_PROMPT = """Enter a number between {} and {}: """
ENTRY_NOT_NUMBER = "Invalid guess, please enter a whole number."
ENTRY_OUT_OF_RANGE = "Invalid guess, please enter a number between {} and {}."
CHANGE_SETTING_PROMPT = """Enter a new whole number value for {}: """

FEEDBACK_LOW = "Too low!"
FEEDBACK_HIGH = "Too high!"
FEEDBACK_CORRECT = "Correct!"
FEEDBACK_ATTEMPTS = "{} took {} attempts to guess the number {}."
FEEDBACK_ATTEMPTS_NONE = "{} failed to guess the number {} in {} attempts."

FEEDBACK_WINNER = "The winner is {} with {} attempts!"
FEEDBACK_WINNER_NONE = "No one won, both players failed to guess the number {} in {} attempts."

# sets the options that can be returned by get_command, notice they are all above 0.
OPTION_PLAY = 1
OPTION_QUIT = 2
OPTION_SET_NUM = 3
OPTION_SET_HIGH = 4
OPTION_SET_LOW = 5
OPTION_RESET = 6

# check OPTIONS
CHECK_LOW = -1
CHECK_CORRECT = 0
CHECK_HIGH = 1

# some defaults
DEFAULT_MIN = 1
DEFAULT_MAX = 100
DEFAULT_ATTEMPTS = 50

# player names
PLAYER1 = "Dave"
PLAYER2 = "HAL"


# functions below this line
def get_rnd_number(min: int, max: int) -> int:
    """Gets a random number between min and max, inclusive.

    Args:
        max (int): max number in range. 
        min (int): min number in range 

    Returns:
        int: a random number between min and max
    """
    return randint(min, max)


# we provided this one so you can see an example of how format is used
# with the various strings.
def play(min_val: int, max_val: int, max_attempts: int) -> None:
    """The main play sequence to be called by the
    main function when the client wants to play the game.

    Args:
        min_val (int): the lowest value the client can guess
        max_val (int): the highest value the client can guess
        max_attempts (int): the max attempts allowed
    """
    number = get_rnd_number(min_val, max_val)
    h_attempts = human_play(number, max_attempts, min_val, max_val)
    c_attempts = computer_play(number, max_attempts, min_val, max_val)
    if (h_attempts <= c_attempts and h_attempts > -1)  or (h_attempts > -1 and c_attempts < 0):
        print(FEEDBACK_WINNER.format(PLAYER1, h_attempts)) 
    elif c_attempts > -1:
        print(FEEDBACK_WINNER.format(PLAYER2, c_attempts))
    else:
        print(FEEDBACK_WINNER_NONE.format(number, max_attempts))


# do not modify above this line, but you can add functions below this line
# you are free to add additional functions beyond the required ones if that
# helps your design.
def check(guess: int, number: int) -> int:
    """Checks the number against the guess, and returns
    indicating if the guess was high, low, or correct

    Args:
        guess (int): the number the client is guessing
        number (int): the number the client is trying to guess

    Returns:
        int: -1 (CHECK_LOW) if the guess is low, 0 (CHECK_CORRECT) if they are equal, 
            and 1 (CHECK_HIGH) if the guess was high
    """
    pass


def get_number(setting: str) -> int:
    """Gets a whole number from the client, and returns it. Forces the client 
    to input a whole number using `.isnumeric()`.

    If the client enters a non-whole number, the client is prompted using ENTRY_NOT_NUMBER,
    before being asked to re-enter a number using the CHANGE_SETTING_PROMPT again.

    Args:
        setting (str): the setting to change (used by CHANGE_SETTING_PROMPT)

    Returns:
        int: a whole number
    """
    pass


def get_guess(min_val: int, max_val: int) -> int:
    """Prompts the user for a guess, and returns the guess. If the guess is not
    between min_val and max_val, inclusive, forces the user to enter a valid guess.

    The lowest number will always be 0 or greater, due to using `.isnumeric()` to
    check if the input is a number. 

    If the client enters a number that is not a whole number, the client is prompted
    using ENTRY_NOT_NUMBER, and then asked to re-enter a number.

    If a client enters a number not in the range, the client is prompted using
    ENTRY_OUT_OF_RANGE, and then asked to re-enter a number.

    Args:
        min_val (int): the lowest value they can guess
        max_val (int): the highest value they can guess

    Returns:
        int: a whole number greater than or equal to min_val, and less than or equal to max_val
    """
    pass 


def get_command() -> int:
    """Prompts the client for the command, and returns the corresponding option. If
    an invalid option is selected, prints INVALID_COMMAND and HELP_PROMPT, and continues to loop
    until a valid option is entered.

    For the client entry, spaces in the middle of the command matter, but are ignored if
    front or back. For example, "  play  " is valid, but "p lay" is not. Additionally, the
    command is not case sensitive, so "Play" is the same as "play".

    Hint: use .strip() and .casefold() to make the command easier to check.

    Returns:
        int: a number between 1 (OPTION_PLAY) and 6 (OPTION_RESET) corresponding to the option selected.
    """
    pass


def human_play(number: int, max_attempts: int, min_val: int, max_val: int) -> int:
    """
    Runs an interactive sequence of the client guessing numbers for the game.
    while the client has not guessed the number, and the number of attempts is
    less than max_attempts, the client is prompted for a guess. If the guess is
    too low, prints FEEDBACK_LOW, if the guess is too high, prints FEEDBACK_HIGH,
    and if the guess is correct, prints FEEDBACK_CORRECT, and then FEEDBACK_ATTEMPTS
    with the number of attempts and the number.

    If the client guesses the number, returns the number of attempts. If the client
    does not guess the number, returns -1 after printing FEEDBACK_ATTEMPTS_NONE with
    the number of attempts and the number.

    Hint:
    For printing with formatting, you will want to use something like the following two examples:

        print(FEEDBACK_ATTEMPTS.format(PLAYER1, attempts, number))

        print(FEEDBACK_ATTEMPTS_NONE.format(PLAYER2, number, max_attempts))

    Args:
        number (int): the correct number
        max_attempts (int): the max attempts allowed
        min_val (int): the lowest value the client can guess (used by get_guess)
        max_val (int): the highest value the client can guess (used by get_guess)

    Returns:
        int: number of attempts if the client guesses the number, -1 if the client failed
             to guess the number in max_attempts
    """
    pass


def computer_play(number: int, max_attempts: int, min_val: int, max_val: int) -> int:
    """
    Runs an automated sequence of the computer guessing numbers for the game.

    It is up to the programmer to determine if the computer should guess starting
    at 0 to max_val. Or if the computer should guess randomly, 
    or use a different strategy such as a binary search. 

    Returns the number of attempts if the computer guesses the number, or -1 if the
    computer failed to guess the number in max_attempts.

    Feedback only happens at the end with printing FEEDBACK_ATTEMPTS or FEEDBACK_ATTEMPTS_NONE
    depending on if the computer was able to find the number or not. 

    Args:
        number (int): the correct number
        max_attempts (int): the max attempts allowed
        min_val (int): the lowest value the client can guess
        max_val (int): the highest value the client can guess

    Returns:
        int: number of attempts if the computer guesses the number, -1 if the computer failed
    """
    pass

# this is completed correctly, and you do not have to modify it - use it as an example for loops. 
def main() -> None:
    """Main driver for the program.

    1.  sets the default values for min_val, max_val, and max_attempts
    2. prints WELCOME_PROMPT
    3. gets the command from the client
    4. while the command is not OPTION_QUIT, runs the corresponding option, and then gets the next command
    5. prints END_PROMPT

    """
    min_val = DEFAULT_MIN
    max_val = DEFAULT_MAX
    max_attempts = DEFAULT_ATTEMPTS

    print(WELCOME_PROMPT)
    option = get_command()
    while option != OPTION_QUIT:
        if option == OPTION_PLAY:
            play(min_val, max_val, max_attempts)
        elif option == OPTION_SET_NUM:
            max_attempts = get_number(SETTING_SET_NUM_TXT)
        elif option == OPTION_SET_HIGH:
            max_val = get_number(SETTING_SET_HIGH_TXT)
        elif option == OPTION_SET_LOW:
            min_val = get_number(SETTING_SET_LOW_TXT)
        elif option == OPTION_RESET:
            min_val = DEFAULT_MIN
            max_val = DEFAULT_MAX
            max_attempts = DEFAULT_ATTEMPTS
        option = get_command()

    print(END_PROMPT)


if __name__ == "__main__":
    main()
