import random

def start_game():
    number_to_guess = random.randint(1, 100)
    attempts = 5  # CHANGED: Reduced attempts to 5
    
    print("\n🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while attempts > 0:
        try:
            guess = int(input(f"\nYou have {attempts} attempts left. Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("❌ Please guess a number between 1 and 100.")
                continue
            
            # Calculate the difference (how far off the guess is)
            # abs() ensures the number is always positive (e.g., abs(-3) becomes 3)
            difference = abs(number_to_guess - guess)

            if guess == number_to_guess:
                print(f"🎉 Congratulations! You guessed the number {number_to_guess}!")
                return
            
            # NEW: Proximity Logic
            if difference <= 3:
                print("🔥 Very close!")
            elif difference <= 5:
                print("⚠️ Close!")

            # Directional Logic (tells you to go Up or Down)
            if guess < number_to_guess:
                print("📉 Too low!")
            else:
                print("📈 Too high!")
            
            attempts -= 1
            
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

    if attempts == 0:
        print(f"💔 Out of attempts! The number was: {number_to_guess}")

def main():
    while True:
        start_game()
        again = input("\n🔄 Do you want to play again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()