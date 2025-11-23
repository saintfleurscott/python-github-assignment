print ("Welcome to my Python Project!")
# --- Weekly Budget Planner ---
# This program calculates your daily spending limit based on a total weekly budget.

def main():
    print("--- Weekly Budget Planner ---")

    
    try:
        # Ask for input
        weekly_budget_input = input("Enter your total budget for the week (e.g., 250.00): ")

        # Convert input and calculate
        weekly_budget = float(weekly_budget_input)
        
        # Calculate daily limit
        daily_allowance = weekly_budget / 7

        #Display the Result Clearly
        print(f"To stay within your budget of ${weekly_budget:.2f},")
        print(f"you can spend approximately ${daily_allowance:.2f} per day.")

    except ValueError:
        # What appears after an input error
        print("Error: Invalid input. Please enter a numeric value for your budget.")

# Cleanup
# This makes sure the function works properly
if __name__ == "__main__":
    main()