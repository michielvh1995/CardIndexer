import json
import unittest
from tmp.database.base import Database
from tmp.models import Card, CardVersion
from tmp.database.MockDB import MockEngine

questing = Card(name="Questing Druid // Seek the Beast", colour=["B", "G"], versions=[
        CardVersion(card_count=2, finish="foil", set_code="woe", number="234")
    ])

pacifism = Card(name="Pacifism", colour=['W'], versions=[
        CardVersion(card_count=3, finish="nonfoil", set_code="m14", number="25"),
        CardVersion(card_count=14, finish="nonfoil", set_code="m13", number="24"),
        CardVersion(card_count=9, finish="nonfoil", set_code="m11", number="23"),
    ])

asinineAnt = Card(
    name="Asinine Antics",
    colour= ['U'],
    versions = [
        CardVersion(card_count=2, set_code="woe", number="42", rarity="m", foil = False, finish = "nonfoil"),
        CardVersion(card_count=2, set_code="woe", number="42", rarity="m", foil = True, finish = "foil")
    ])

werefox = Card (
    name="Werefox Bodyguard",
    colour= ['W'],
    versions=[
        CardVersion(card_count=2, set_code="woe", number="39", rarity="c",  foil = False, finish = "nonfoil"), 
        CardVersion(card_count=2, set_code="woe", number="39", rarity="c",  foil = True, finish = "foil"),
        CardVersion(card_count=2, set_code="eow", number="39", rarity="c",  foil = True, finish = "foil")
    ])


class TestMockDBethods(unittest.TestCase):
    def setUp(self) -> None:
        # self.cardData = {}

        # try:
        #     with open('./src/tmp/cardsdata.json', 'r+') as fil:
        #         self.cardData = json.load(fil)
        # except:
        #     pass

        Database.InitDatabase(MockEngine, cards = {})
    
    def test_InsertCard(self):
        self.assertEqual(len(Database.Engine.Data), 0)

        Database.InsertCards([asinineAnt])        
        self.assertEqual(len(Database.Engine.Data), 1)
        self.assertEqual(Database.Engine.Data, {"Asinine Antics": asinineAnt})
        self.assertEqual(len(Database.Engine.Data["Asinine Antics"].versions), 2)

        Database.InsertCards([asinineAnt])        
        self.assertEqual(len(Database.Engine.Data), 1)
        self.assertEqual(Database.Engine.Data, {"Asinine Antics": asinineAnt})
        self.assertEqual(Database.Engine.Data["Asinine Antics"].versions[0].card_count, 4)
        self.assertEqual(len(Database.Engine.Data["Asinine Antics"].versions), 2)
        
        Database.InsertCards([werefox])        
        self.assertEqual(len(Database.Engine.Data), 2)
        self.assertEqual(Database.Engine.Data, {"Asinine Antics": asinineAnt, "Werefox Bodyguard": werefox})

        Database.InsertCards([questing, pacifism])
        self.assertEqual(len(Database.Engine.Data), 4)

    def test_QueryCards_name(self):
        # Correct data type:
        self.assertIsInstance(Database.QueryCards({})[0], Card, msg="Correct data type")

        # Case insensitive:
        self.assertEqual(Database.QueryCards(filters={"name": "asinine Antics"}), [asinineAnt])
        self.assertEqual(Database.QueryCards(filters={"name": "asINIne Antics"}), [asinineAnt])

        # Name can be a subset:
        self.assertEqual(Database.QueryCards(filters={"name": "Asinine"}), [asinineAnt])

        # If the name is not found, output should be nothing:
        self.assertFalse(Database.QueryCards(filters={"name": "NotInDB"}), msg="When the item is not present, should return an empty list")
        

    def test_QueryCards_colour(self):
        colFilterEqU = {"colours": ['U'], "cmt": '='}
        colFilterEqW = {"colours": ['W'], "cmt": '='}
        colFilterEqB = {"colours": ['B'], "cmt": '='}
        colFilterGtU = {"colours": ['U'], "cmt": '>='}
        colFilterLtU = {"colours": ['U'], "cmt": '<='}

        colFilterEqBG = {"colours": ['B', 'G'], "cmt": '='}
        colFilterGtG = {"colours": ['G'], "cmt": '>='}
        colFilterEqG = {"colours": ['G'], "cmt": '='}

        colFilterLtWURBG = {"colours": ['W','U','B','R','G', 'C'], "cmt": '<='}

        self.assertIsInstance(Database.QueryCards(colFilterEqU)[0], Card, msg="Correct data type")
        self.assertEqual([asinineAnt], Database.QueryCards(colFilterEqU))

        self.assertFalse(Database.QueryCards(colFilterEqB))

        self.assertEqual([asinineAnt], Database.QueryCards(colFilterGtU))
        self.assertEqual([asinineAnt], Database.QueryCards(colFilterLtU))

        self.assertEqual(len(Database.QueryCards(colFilterEqW)), 2)
        self.assertEqual(len(Database.QueryCards(colFilterEqBG)), 1)
        self.assertEqual(Database.QueryCards(colFilterEqBG), [questing])

        self.assertEqual(len(Database.QueryCards(colFilterGtG)), 1)
        self.assertEqual(Database.QueryCards(colFilterGtG), [questing])
        
        self.assertEqual(len(Database.QueryCards(colFilterEqG)), 0)
        self.assertEqual(Database.QueryCards(colFilterEqG), [])

        # Should return all cards in the database
        self.assertEqual(len(Database.QueryCards(colFilterLtWURBG)), 4)
        self.assertEqual(Database.QueryCards(colFilterLtWURBG), [asinineAnt, werefox, questing, pacifism])
    
    def test_QueryCards_set(self):
        filterWOE = {"set_code":"woe"}
        filterEOW = {"set_code":"eow"}
        filterNone = {"set_code":"NONE"}

        woe = Database.QueryCards(filterWOE)
        self.assertEqual(len(woe), 3)
        self.assertTrue(werefox in woe)
        self.assertFalse(pacifism in woe)

        eow = Database.QueryCards(filterEOW)
        self.assertEqual(len(eow), 1)
        self.assertTrue(werefox in eow)
        self.assertEqual(len(eow[0]), 1, msg="Werefox only has one version in set EOW")

        none = Database.QueryCards(filterNone)
        self.assertFalse(none)

    def test_QueryCards_versions(self):
        filterfoil = {"finish" : "foil"}
        filternonfoil = {"finish" : "nonfoil"}

        foils = Database.QueryCards(filterfoil)
        nonfoils = Database.QueryCards(filternonfoil)

        self.assertEqual(len(foils), 3)
        self.assertFalse(pacifism in foils)
        self.assertTrue(werefox in foils)
        self.assertTrue(pacifism in nonfoils)

        doublefilter = {"finish" : "nonfoil", "set_code":"woe"}
        doubles = Database.QueryCards(doublefilter)
        self.assertEqual(len(doubles), 2)
        self.assertFalse(questing in doubles)

        self.assertTrue(asinineAnt in doubles)
        
        queriedAs = [queriedAs for queriedAs in doubles if queriedAs == asinineAnt][0]
        self.assertEqual(len(queriedAs), 1)


def printQueryOutput(cards : list[Card]) -> None:
    print()
    for card in cards:
        print(" ", card.name, f" ({card.colour}), {len(card.versions)} versions")
        for version in card.versions:
            print(f"    {version.set_code}, {version.number}, {version.finish} ({version.rarity}): {version.card_count}")
    print()

def RunTests():
    unittest.main()

if __name__ == '__main__':
    RunTests()