import unittest
from scrape_up.myanimelist import Anime


class AnimeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.anime = Anime("Demon Slayer")
        self.anime_from_id = Anime.from_id(38000)

    def test_url(self):
        self.assertEqual(
            self.anime.url, "https://myanimelist.net/anime/38000/Kimetsu_no_Yaiba"
        )
        self.assertEqual(
            self.anime_from_id.url,
            "https://myanimelist.net/anime/38000/Kimetsu_no_Yaiba",
        )

    def test_title(self):
        self.assertEqual(self.anime.title, "Kimetsu no Yaiba")
        self.assertEqual(self.anime_from_id.title, "Kimetsu no Yaiba")

    def test_title_english(self):
        self.assertEqual(self.anime.title_english, "Demon Slayer: Kimetsu no Yaiba")
        self.assertEqual(
            self.anime_from_id.title_english, "Demon Slayer: Kimetsu no Yaiba"
        )

    def test_title_jp(self):
        self.assertEqual(self.anime.title_jp, "鬼滅の刃")
        self.assertEqual(self.anime_from_id.title_jp, "鬼滅の刃")

    def test_score(self):
        self.assertIsNotNone(self.anime.score)
        self.assertIsInstance(self.anime.score, float)
        self.assertIsNotNone(self.anime_from_id.score)
        self.assertIsInstance(self.anime_from_id.score, float)

    def test_rank(self):
        self.assertIsNotNone(self.anime.rank)
        self.assertIsInstance(self.anime.rank, int)
        self.assertIsNotNone(self.anime_from_id.rank)
        self.assertIsInstance(self.anime_from_id.rank, int)

    def test_members(self):
        self.assertIsNotNone(self.anime.members)
        self.assertIsInstance(self.anime.members, int)
        self.assertIsNotNone(self.anime_from_id.members)
        self.assertIsInstance(self.anime_from_id.members, int)

    def test_popularity(self):
        self.assertIsNotNone(self.anime.popularity)
        self.assertIsInstance(self.anime.popularity, int)
        self.assertIsNotNone(self.anime_from_id.popularity)
        self.assertIsInstance(self.anime_from_id.popularity, int)

    def test_synopsis(self):
        self.assertIsNotNone(self.anime.synopsis)
        self.assertIsInstance(self.anime.synopsis, str)
        self.assertIsNotNone(self.anime_from_id.synopsis)
        self.assertIsInstance(self.anime_from_id.synopsis, str)

    def test_poster_url(self):
        self.assertIsNotNone(self.anime.poster_url)
        self.assertIsInstance(self.anime.poster_url, str)
        self.assertIsNotNone(self.anime_from_id.poster_url)
        self.assertIsInstance(self.anime_from_id.poster_url, str)

    def test_genres(self):
        self.assertIsNotNone(self.anime.genres)
        self.assertIsInstance(self.anime.genres, list)
        self.assertIsNotNone(self.anime_from_id.genres)
        self.assertIsInstance(self.anime_from_id.genres, list)

    def test_themes(self):
        self.assertIsNotNone(self.anime.themes)
        self.assertIsInstance(self.anime.themes, list)

        self.assertIsNotNone(self.anime_from_id.themes)
        self.assertIsInstance(self.anime_from_id.themes, list)


if __name__ == "__main__":
    unittest.main()
