import unittest

from parameterized import parameterized

from src.utils import parse_game


class GamePossibilityValidator(unittest.TestCase):

    @parameterized.expand([
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
         ("Game 1", [
             {"blue": 3, "red": 4, "green": 0},
             {"blue": 6, "red": 1, "green": 2},
             {"blue": 0, "red": 0, "green": 2},
         ])
         ),
        ("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
         ("Game 2", [
             {"blue": 1, "red": 0, "green": 2},
             {"blue": 4, "red": 1, "green": 3},
             {"blue": 1, "red": 0, "green": 1},
         ])
         ),
        ("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
         ("Game 3", [
             {"blue": 6, "red": 20, "green": 8},
             {"blue": 5, "red": 4, "green": 13},
             {"blue": 0, "red": 1, "green": 5},
         ])
         )
    ])
    def test_parse_game(self, game_string: str, expected_game: dict):
        actual_game = parse_game(game_string)
        self.assertEqual(actual_game, expected_game)


if __name__ == '__main__':
    unittest.main()
