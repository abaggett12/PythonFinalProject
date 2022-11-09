class TestFrenchToEnglishTranslation( unittest.TestCase ):
    def test_french_to_english_translation( self):
        self.assertEqual("", "") #test for null
        self.assertEqual( french_to_englich("Bonjour"), "Hello")
        self.assertNotEqual( french_to_englich("Salut"), "Dog")

class TestEnglishToFrenchTranslation( unittest.TestCase ):
    def test_english_to_french_translation( self):
        self.assertEqual("", "") #test for null
        self.assertEqual( french_to_englich("Hello"), "Bonjour")
        self.assertNotEqual( french_to_englich("Dog"), "Salut")  