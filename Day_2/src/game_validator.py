import os

from src.utils import parse_game, is_valid_game, get_minimum_viable_cubes, get_power

bag_contents = {"blue": 14, "red": 12, "green": 13}

if __name__ == "__main__":
    path = os.path.join("..", "resources", "input.txt")
    games = []
    with open(path, 'r') as infile:
        for line in infile:
            game_id, game_dict = parse_game(line)
            is_valid = is_valid_game(bag_contents, game_dict)
            games.append({"game_id": int(game_id.strip().split(' ')[-1]), "game": game_dict, "validity": is_valid})
    sum_total = 0
    for game in games:
        if game.get("validity"):
            sum_total += game.get("game_id")
    print(sum_total)

    total_power = 0
    for game in games:
        minimum_viable_cubes = get_minimum_viable_cubes(game["game"])
        total_power += get_power(minimum_viable_cubes)
    print(total_power)
