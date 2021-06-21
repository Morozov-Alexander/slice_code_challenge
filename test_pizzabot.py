import unittest
import pizzabot
from parser import Parser


class TestPizzabot(unittest.TestCase):
    # --------------------- parser.py----------------------------------------

    def setUp(self) -> None:
        self.parser = Parser("5x5 (0,0) (1,3) (4,4) (4,2) (4,2) (0,1) (3,2) (2,3) (4,1)")

    def test_parse_key_points_function(self):
        self.assertEqual(self.parser.parse_key_points(),
                         [('0', '0'), ('1', '3'), ('4', '4'), ('4', '2'), ('4', '2'), ('0', '1'),
                          ('3', '2'), ('2', '3'), ('4', '1')])

    def test_convert_params_to_int(self):
        self.assertEqual(self.parser.parse_field_size(), ('5', '5'))

    def test_parse_params(self):
        self.parser.parse_params()
        self.assertEqual(self.parser.get_key_points,
                         [[0, 0], [1, 3], [4, 4], [4, 2], [4, 2], [0, 1], [3, 2], [2, 3], [4, 1]])

    # --------------------- pizzabot.py----------------------------------------
    def test_sort_function(self):
        self.assertEqual(pizzabot.sort_function([1, 2]), 3)
        self.assertEqual(pizzabot.sort_function([-1, -2]), -3)
        self.assertEqual(pizzabot.sort_function([1, -1]), 0)
        self.assertEqual(pizzabot.sort_function([0, 0]), 0)

    def test_path_building(self):
        self.assertEqual(pizzabot.path_building(2, 0), "EE")
        self.assertEqual(pizzabot.path_building(0, 2), "NN")
        self.assertEqual(pizzabot.path_building(0, 0), "")
        self.assertEqual(pizzabot.path_building(2, 2), "EENN")
        self.assertEqual(pizzabot.path_building(-3, -2), "WWWSS")
        self.assertEqual(pizzabot.path_building(0, -5), "SSSSS")

    def test_find_shortest_path(self):
        self.assertEqual(pizzabot.find_shortest_path([[1, 1]]), "END")
        self.assertEqual(pizzabot.find_shortest_path([[1, 3], [0, 1], [2, 5]]), "NDENNDENND")
        self.assertEqual(pizzabot.find_shortest_path([[2, 3], [1, 1], [1, 3], [2, 2]]), "ENDNNDESDND")
        self.assertEqual(pizzabot.find_shortest_path([]), "")
        self.assertEqual(pizzabot.find_shortest_path([[0, 0]]), "D")


if __name__ == '__main__':
    unittest.main()
