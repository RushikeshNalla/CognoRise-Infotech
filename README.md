# CognoRise-Infotech

**Task 1: Password Generator**

**Overview:**
This program generates a random password of a specified length. The password includes a mix of lowercase and uppercase letters, digits, and punctuation characters to ensure it is strong and secure.

**Code Explanation:**

1. **Function Definition:**

--Purpose: To generate a random password.
--Details:
           The function generate_password takes one argument, length, which specifies the desired password length.

2. **Length Check:**

--Purpose: To ensure the password is long enough.
--Details:
          The function raises an error if the password length is less than 4 to ensure it can include at least one of each character type: lowercase, uppercase, digit, and punctuation.

3. **Character Sets:**
   
--Purpose: To define possible characters for the password.
--Details:
          The function combines all letters, digits, and punctuation characters into a single string for random selection.

4.**Ensuring Character Variety:**

--Purpose: To include at least one of each character type.
--Details:
           The function ensures that the password includes one lowercase letter, one uppercase letter, one digit, and one punctuation mark.

5. **Filling the Password:**

--Purpose: To complete the password to the desired length.
--Details:
          The function randomly selects additional characters from the combined set until the desired length is reached.

6. **Randomizing Order:**

--Purpose: To ensure the password is randomized.
--Details:
           The password list is shuffled to randomize the order of characters.

7. **Returning the Password:**

--Purpose: To output the final password.
--Details:
          The list of characters is joined into a string and returned as the final password.

**Example Usage:**

Generates a password of length 12 and prints it.



**Task 2: Sudoku Solver**

**Overview:**
This program solves Sudoku puzzles by implementing an algorithm that fills in the missing numbers according to Sudoku rules. The program can handle any valid Sudoku grid and find the solution.

**Code Explanation:**

1. **find_empty_location Function:**

--Looks for an empty cell (represented by 0) in the grid.
--Returns the coordinates of the first empty cell found.

2. **is_valid_move Function:**

--Checks whether a number can be placed at a specific location according to Sudoku rules.
--Validates the number against the current row, column, and 3x3 subgrid.

3. **solve_sudoku Function:**

--Implements a backtracking algorithm to solve the puzzle.
--Attempts to fill empty cells one by one and backtracks if a conflict arises.

4. **print_grid Function:**

--Prints the Sudoku grid in a user-friendly format.

5. **main Function:**

--Initializes the grid with a partially filled Sudoku puzzle.
--Calls the solve_sudoku function to solve the puzzle.
--Prints the solution or informs the user if no solution exists.

**Example Usage:**
--Given a partially filled Sudoku grid, the program will solve it and display the complete grid. If the puzzle has no solution, the program will notify the user.



**Task 3: Countdown Timer**

**Overview:**
This program implements a countdown timer that counts down from a specified number of seconds. It displays the remaining time in a MM:SS format and updates every second until the time runs out.

**Code Explanation:**

1. **countdown_timer Function:**

--Purpose: This function is responsible for executing the countdown. It takes an input value in seconds and counts down to zero.

**Logic:**
--The divmod function is used to convert the total seconds into minutes and seconds.
--The time is formatted into MM:SS format using string formatting.
--The print function is used to display the remaining time, and end="\r" ensures that the time display updates on the same line.
--The time.sleep(1) function pauses the execution for one second before updating the countdown, simulating the passage of time.
--The countdown continues by decrementing the seconds by 1 until it reaches zero.
--When the countdown reaches zero: The message "Time's up!" is displayed to indicate the end of the countdown.

2. **Main Execution:**
   
--An example countdown time of 6 seconds (6 sec) is defined.
--The countdown_timer function is called with this value to start the countdown.

**Example Usage:**

--Input: countdown_time = 6 (for a 1-minute countdown).
--Output: The program will display the countdown in MM:SS format, updating every second until it reaches "00:00", after which it will display "Time's up!".
