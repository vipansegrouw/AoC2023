from typing import Tuple, List, Dict


def parse_game(game_string: str) -> Tuple[str, List[Dict[str, int]]]:
    game_id, turns_string = game_string.split(':')
    turns_list = turns_string.split(';')
    game = []
    for turn in turns_list:
        turn_dict = {"blue": 0, "red": 0, "green": 0}
        pulls = turn.split(',')
        for pull in pulls:
            num, col = pull.strip().split(' ')
            turn_dict[col] = int(num)
        game.append(turn_dict)
    return game_id, game


def is_valid_game(bag_contents: Dict[str, int], game: List[Dict[str, int]]) -> bool:
    for colour, bag_amount in bag_contents.items():
        for turn in game:
            if bag_amount < turn[colour]:
                return False
    return True
