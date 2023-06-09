import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), round(((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2), 2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 122.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), round(((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2), 2)))

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidLessThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 118.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], float(quote['top_bid']['price']), float(quote['top_ask']['price']), round(((float(quote['top_bid']['price']) + float(quote['top_ask']['price'])) / 2), 2)))

  def test_getRatio_priceAGreaterThanPriceB(self):
    quotes = [
      {'top_ask': {'price': 123.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 122.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a = round(((float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price'])) / 2), 2)
    price_b = round(((float(quotes[1]['top_bid']['price']) + float(quotes[1]['top_ask']['price'])) / 2), 2)

    self.assertEqual(getRatio(price_a, price_b), round((price_a / price_b), 2))

  def test_getRatio_priceALessThanPriceB(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 118.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a = round(((float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price'])) / 2), 2)
    price_b = round(((float(quotes[1]['top_bid']['price']) + float(quotes[1]['top_ask']['price'])) / 2), 2)

    self.assertEqual(getRatio(price_a, price_b), round((price_a / price_b), 2))

  def test_getRatio_priceAEqualZero(self):
    quotes = [
      {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a = round(((float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price'])) / 2), 2)
    price_b = round(((float(quotes[1]['top_bid']['price']) + float(quotes[1]['top_ask']['price'])) / 2), 2)

    self.assertEqual(getRatio(price_a, price_b), 0)


  def test_getRatio_priceBEqualZero(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 118.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
       'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a = round(((float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price'])) / 2), 2)
    price_b = round(((float(quotes[1]['top_bid']['price']) + float(quotes[1]['top_ask']['price'])) / 2), 2)

    self.assertEqual(getRatio(price_a, price_b), None)



if __name__ == '__main__':
    unittest.main()
