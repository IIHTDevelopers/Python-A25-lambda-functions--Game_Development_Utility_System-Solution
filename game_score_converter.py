# game_score_converter.py

"""
Required Variable Names:
- mining_score (string input like "100")
- mining_points (converted to integer)
- combat_score (decimal like 98.7)
- combat_points (converted to integer)
- achievement_hex (hex string like "1F")
- achievement_bonus (converted to integer)
- total_score (sum of all points)
- score_display (total score as string)
- player_stats (list with name and score)
"""

def convert_string_to_int(mining_score):
    """Convert string mining score to integer"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(mining_score, str) or not mining_score.isdigit():
        raise ValueError("Score must be a string containing only digits")
    
    # ACTUAL IMPLEMENTATION (replace the 'return None')
    return int(mining_score)

def convert_float_to_int(combat_score):
    """Convert float combat score to integer"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(combat_score, float):
        raise ValueError("Score must be a float")
    if combat_score < 0:
        raise ValueError("Score must be non-negative")
    
    # ACTUAL IMPLEMENTATION (replace the 'return None')
    return int(combat_score)

def convert_hex_to_int(achievement_hex):
    """Convert hexadecimal achievement score to integer"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(achievement_hex, str) or not all(c in '0123456789ABCDEFabcdef' for c in achievement_hex):
        raise ValueError("Input must be a valid hexadecimal string")
    
    # ACTUAL IMPLEMENTATION (replace the 'return None')
    return int(achievement_hex, 16)

def convert_score_to_string(total_score):
    """Convert total score to string for display"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(total_score, (int, float)):
        raise ValueError("Score must be a number")
    
    # ACTUAL IMPLEMENTATION (replace the 'return None')
    return str(total_score)

def create_player_list(player_name, total_score):
    """Create a list containing player name and score"""
    # Input validation (DON'T CHANGE THIS)
    if not isinstance(player_name, str) or not player_name:
        raise ValueError("Player name must be a non-empty string")
    
    # ACTUAL IMPLEMENTATION (replace the 'return None')
    return [player_name, total_score]

if __name__ == "__main__":
    print("Minecraft Score Calculator")
    print("=" * 30)
    print("Welcome to the new Minecraft scoring system!")
    print("-" * 30)
    
    # ACTUAL IMPLEMENTATION (replace the TODO comments)
    
    # 1. Ask user for mining_score and convert to mining_points
    mining_score = input("Enter your mining points: ")
    mining_points = convert_string_to_int(mining_score)
    
    # 2. Ask user for combat_score and convert to combat_points
    combat_input = input("Enter your combat score: ")
    combat_score = float(combat_input)
    combat_points = convert_float_to_int(combat_score)
    
    # 3. Ask user for achievement_hex and convert to achievement_bonus
    achievement_hex = input("Enter your achievement hex: ")
    achievement_bonus = convert_hex_to_int(achievement_hex)
    
    # 4. Calculate total_score (add all points together)
    total_score = mining_points + combat_points + achievement_bonus
    
    # 5. Convert total_score to score_display
    score_display = convert_score_to_string(total_score)
    
    # 6. Get player_name and create player_stats list
    player_name = input("Enter your player name: ")
    player_stats = create_player_list(player_name, total_score)
    
    # 7. Display all results nicely formatted
    print(f"Mining Points: {mining_points}")
    print(f"Combat Points: {combat_points}")
    print(f"Achievement Bonus: {achievement_bonus}")
    print(f"Total Score: {score_display}")
    print(f"Player Stats: {player_stats}")