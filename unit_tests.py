from receipt import Receipt
import unittest


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")


    def setUp(self):
        print("setUp")
        receipt_from_api = {
            "title": "Итальянская пицца",
            "ingredients_list": [
                ('Мука', 600, 400, 200),
                ('Томатный соус', 110, 70, 300),
                ('Сыр моцарелла ', 100, 90, 250),
                ('Шампиньоны', 70, 60, 100),
                ('Ветчина', 70, 60, 150),
            ],
        }

        self._receipt = Receipt(receipt_from_api['title'], receipt_from_api['ingredients_list'])

    
    def tearDown(self):
        print("tearDown")
        del self._receipt


    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


    def test_first(self):
        self.assertEqual(self._receipt.calc_cost(), 1000)


    def test_second(self):
        self.assertEqual(self._receipt.calc_cost(2), 2000)


    def test_third(self):
        self.assertEqual(self._receipt.calc_weight(3), 2850)


    def test_fourth(self):
        self.assertEqual(self._receipt.calc_weight(raw=False), 680)


if __name__ == '__main__':
    unittest.main()