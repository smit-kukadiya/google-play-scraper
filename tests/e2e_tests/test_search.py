from unittest import TestCase

from google_play_scraper.features.search import search


class TestSearch(TestCase):
    def test_e2e_scenario_1(self):
        """
        Check if apps are found based on the search query and if all app properies are correct.
        """
        results = search("best Pikachu game")

        self.assertGreater(len(results), 0)

        for result in results:
            if result["trackCensoredName"] == "com.nianticlabs.pokemongo":
                break

        self.assertTrue("Pokémon GO" in result["title"])
        self.assertEqual("com.nianticlabs.pokemongo", result["trackCensoredName"])
        self.assertTrue("Explore and discover Pokémon" in result["description"])
        self.assertTrue("<br>" in result["descriptionHTML"])
        self.assertTrue(result["installs"].endswith("000+"))
        self.assertTrue(1.0 < result["averageUserRating"] < 5.0)
        self.assertEqual(0, result["price"])
        self.assertTrue(result["free"])
        self.assertEqual("USD", result["currency"])
        self.assertEqual("Niantic, Inc.", result["sellerName"])
        self.assertEqual("Adventure", result["genre"])
        self.assertEqual(
            "https://play-lh.googleusercontent.com/wAWerkEu_g2_BMCl85WKqN2mxn0xW1O22nV6yJOayrMKu9pqtrLMn7S2Zd1xaykKm0g",
            result["icon"],
        )
        self.assertTrue(result["screenshots"])
        for screenshot_url in result["screenshots"]:
            self.assertTrue(
                screenshot_url.startswith("https://play-lh.googleusercontent.com/")
            )
        self.assertTrue(result["video"].startswith("https://www.youtube.com"))
        self.assertTrue(result["videoImage"].endswith(".jpg"))

    def test_e2e_scenario_2(self):
        """
        Test for different language and country.
        """
        results = search("Bestes Pikachu Spiel", lang="de", country="de")

        self.assertGreater(len(results), 0)

    def test_e2e_scenario_3(self):
        """
        Test for limited number of results.
        """
        n_hits = 3
        results = search("best Pikachu game", n_hits=n_hits)
        self.assertEqual(len(results), n_hits)
