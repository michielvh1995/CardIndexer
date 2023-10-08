import unittest

from tmp.models import Card, CardVersion

werefoxDict : dict = {
    "name": "Werefox Bodyguard",
    "versions": [{
        "card_count": 1,
        "set_code": "woe",
        "number": "39",
        "foil" : False
    },
    {
        "card_count": 1,
        "set_code": "woe",
        "number": "39",
        "foil": True
    }]
}


class TestCardModelMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.cardOne = Card (
            name="Werefox Bodyguard",
            versions=[CardVersion(card_count=1, set_code="woe", number=39), 
                    CardVersion(card_count=1, set_code="woe", number=39, foil=True)])
        self.cardTwo = Card (
            name="Restless Fortress",
            versions=[CardVersion(card_count=1, foil=True, set_code="woe", number=305)])
        
    def compareCards(self, cardOne : Card, cardTwo : Card):
        """ Helper function to assert that two cards are exactly the same.
        """
        self.assertEqual(cardOne, cardTwo)
        self.assertEqual(len(cardOne.versions), len(cardTwo.versions))

        for verOne in cardOne.versions:
            self.assertIn(verOne, cardTwo.versions)

        for verTwo in cardTwo.versions:
            self.assertIn(verTwo, cardOne.versions)

        
    def test_initalization(self):        
        self.assertIsInstance(self.cardOne, Card, msg="After initialization self.a card should be of Card type")
        self.assertIsInstance(self.cardTwo, Card, msg="After initialization self.a card should be of Card type")
        
        for version in self.cardOne.versions:
            self.assertIsInstance(version, CardVersion, msg="Each item in versions should be self.a CardVersion")

        for version in self.cardTwo.versions:
            self.assertIsInstance(version, CardVersion, msg="Each item in versions should be self.a CardVersion")

        # Assert that the initialization went successfully
        self.assertEqual(self.cardOne.name, "Werefox Bodyguard")
        self.assertEqual(len(self.cardOne.versions), 2)

        # Here we do it by hand, as self.cardOne needs to be the ground truth
        self.assertEqual(self.cardOne.versions[0].card_count, 1)
        self.assertEqual(self.cardOne.versions[0].set_code, "woe")
        self.assertEqual(self.cardOne.versions[0].number, "39")
        self.assertFalse(self.cardOne.versions[0].foil)

        self.assertEqual(self.cardOne.versions[1].card_count, 1)
        self.assertEqual(self.cardOne.versions[1].set_code, "woe")
        self.assertEqual(self.cardOne.versions[1].number, "39")
        self.assertTrue(self.cardOne.versions[1].foil)

        # Assert each one is unique
        self.assertEqual(self.cardOne.versions.count(self.cardOne.versions[0]), 1)
        self.assertEqual(self.cardOne.versions.count(self.cardOne.versions[1]), 1)

    def test_from_dict(self):
        card = Card.from_dict(werefoxDict)

        self.assertIsInstance(card, Card, msg ="from_dict should return self.a card")
        for version in card.versions:
            self.assertIsInstance(version, CardVersion, msg="Each item in versions should be self.a CardVersion")
        
        # Ensure uniqueness of each cardversion
        for ver in card.versions:
            self.assertEqual(card.versions.count(ver), 1)

        self.compareCards(card, self.cardOne)
    
    def test_equals(self):
        self.assertEqual(self.cardOne, self.cardOne)

        self.assertNotEqual(self.cardOne, self.cardTwo)
        self.assertNotEqual(self.cardTwo, self.cardOne)
        
        lowerCardOne = Card(name="werefox bodyguard", versions=[])
        self.assertEqual(self.cardOne, lowerCardOne, msg = "Should be case insensitive")

    def test_addition(self):
        with self.assertRaises(Exception) as error:
            cardError = self.cardOne + self.cardTwo

        # Assert that nothing happens on error
        self.assertEqual(str(error.exception), "Not adding copies of the same card!")
        self.assertEqual(self.cardOne.versions[0].card_count, 1)
        self.assertEqual(self.cardOne.versions[1].card_count, 1)

        cardAdded = self.cardOne + self.cardOne

        self.assertIsInstance(cardAdded, Card, msg="After addition the return value should remain Card")
        
        cardThree = Card (
            name="Werefox Bodyguard",
            versions=[CardVersion(card_count=2, set_code="woe", number=39), 
                    CardVersion(card_count=2, set_code="woe", number=39, foil=True)])
        
        # Ensure uniqueness of each cardversion after addition
        for ver in cardAdded.versions:
            self.assertEqual(cardAdded.versions.count(ver), 1)

        # Check that the versions are properly updated
        self.compareCards(cardAdded, cardThree)

class TestCardVersionModelMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.a = CardVersion(set_code="asa", number="39")
        self.b = CardVersion(set_code="asa", number="38")
        self.bi = CardVersion(set_code="asa", number=38)
        self.c = CardVersion(set_code="asa", number="39", foil=True)
        self.d = CardVersion(set_code="asap", number="39")
        self.e = CardVersion(set_code="asa", number="39", card_count=12)        

    def test_from_dict(self):
        verA= {
            "card_count": 1,
            "set_code": "asa",
            "number": "39"
        }
        verB = {
            "card_count": 1,
            "set_code": "asa",
            "number": "39",
            "foil": True
        }
        verC= {
            "card_count": 1,
            "set_code": "asa",
            "number": 39
        }
        
        f = CardVersion.from_dict(verA)
        g = CardVersion.from_dict(verB)
        h = CardVersion.from_dict(verC)
        
        self.assertFalse(f.foil)
        self.assertEqual(f.card_count, 1)
        self.assertEqual(f.set_code, "asa")
        self.assertEqual(f.number, "39")

        self.assertTrue(g.foil)
        self.assertEqual(g.card_count, 1)
        self.assertEqual(g.set_code, "asa")
        self.assertEqual(g.number, "39")

        self.assertFalse(h.foil)
        self.assertEqual(h.card_count, 1)
        self.assertEqual(h.set_code, "asa")
        self.assertEqual(h.number, "39")

        self.assertEqual(f, self.a)
        self.assertEqual(f, h)
        self.assertNotEqual(f, g)

    def test_eq(self):
        self.assertEqual(self.a, self.a)
        self.assertEqual(self.a, self.e)
        self.assertEqual(self.e, self.a)

        self.assertEqual(self.b, self.bi)

        self.assertNotEqual(self.a,self.b)
        self.assertNotEqual(self.a,self.bi)

        self.assertNotEqual(self.a, self.c)
        self.assertNotEqual(self.c, self.a)
        self.assertNotEqual(self.a, self.d)

    def test_gt(self):
        self.assertGreater(self. a, self.b)
        self.assertGreater(self.c, self.a)
        self.assertGreater(self.d, self.a)

    
    def test_add(self):
        with self.assertRaises(Exception) as ve:
            errorVer = self.a + self. c

        self.assertEqual(str(ve.exception), "Not adding copies of the same card!")
        f = self.a + self.e
        g = self.b + self.bi
        self.assertEqual(f.card_count, 13)
        self.assertEqual(f, self.a)
        self.assertEqual(f, self.e)

        self.assertEqual(g.card_count, 2)



def RunTests():
    unittest.main()

if __name__ == '__main__':
    RunTests()