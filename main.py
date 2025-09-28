import time
import random

def classic_mode():
    keys = ["W", "A", "S", "D", "Z", "X", "C"]
    score = 0
    misses = 0
    combo = 0
    max_misses = 3
    
    difficulty = {
        "easy": {"time_limit": 1.5, "score_multiplier": 1},
        "medium": {"time_limit": 1.0, "score_multiplier": 1.5},
        "hard": {"time_limit": 0.7, "score_multiplier": 2}
    }
    
    print("\nClassic Mode Selected!")
    print("Instructions: Press the displayed key as quickly as possible!")
    print("Choose difficulty: easy, medium, hard\n")
    level = input("Enter difficulty: ").lower()
    
    if level not in difficulty:
        print("Invalid choice. Defaulting to medium.")
        level = "medium"
    
    time_limit = difficulty[level]["time_limit"]
    score_multiplier = difficulty[level]["score_multiplier"]
    
    while misses < max_misses:
        target_key = random.choice(keys)  
        print(f"Press {target_key}!")
        
        start_time = time.time()
        user_input = input().upper()
        reaction_time = time.time() - start_time

        if user_input == target_key and reaction_time <= time_limit:
            combo += 1
            score += int(10 * combo * score_multiplier)
            print(f"Good! Combo: {combo} Score: {score}")
        else:
            combo = 0
            misses += 1
            print(f"Missed! You have {max_misses - misses} tries left.")
    
    print(f"Game Over! Final Score: {score}")

def timed_mode():
    keys = ["W", "A", "S", "D", "Z", "X", "C"]
    score = 0
    combo = 0
    
    difficulty = {
        "easy": {"time_limit": 1.5, "score_multiplier": 1},
        "medium": {"time_limit": 1.0, "score_multiplier": 1.5},
        "hard": {"time_limit": 0.7, "score_multiplier": 2}
    }
    
    print("\nTimed Mode Selected!")
    print("Instructions: Score as many points as you can in 30 seconds!")
    print("Choose difficulty: easy, medium, hard\n")
    level = input("Enter difficulty: ").lower()
    
    if level not in difficulty:
        print("Invalid choice. Defaulting to medium.")
        level = "medium"
    
    time_limit = difficulty[level]["time_limit"]
    score_multiplier = difficulty[level]["score_multiplier"]
    game_duration = 30
    start_time = time.time()
    
    while time.time() - start_time < game_duration:
        target_key = random.choice(keys)  
        print(f"Press {target_key}!")
        print(f"Time left: {int(game_duration - (time.time() - start_time))}s")
        
        start_time_input = time.time()
        user_input = input().upper()
        reaction_time = time.time() - start_time_input

        if user_input == target_key and reaction_time <= time_limit:
            combo += 1
            score += int(10 * combo * score_multiplier)
            print(f"Good! Combo: {combo} Score: {score}")
        else:
            combo = 0
            print("Missed! Keep going!")
    
    print(f"Time's up! Final Score: {score}")

def main():
    while True:
        print("\nSelect game mode:") 
        print("1. Classic Mode")
        print("2. Timed Mode")
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            classic_mode()
        elif choice == '2':
            timed_mode()
        else:
            print("Invalid choice. Please try again.")
        
        restart = input("\nPlay again? (y/n): ").lower()
        if restart != 'y':
            break

if __name__ == "__main__":
    main()
