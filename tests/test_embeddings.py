import math
import unittest

from embeddings.fake import DIM, FakeEmbedder


class FakeEmbedderTest(unittest.TestCase):
    def setUp(self):
        self.embedder = FakeEmbedder()

    def test_vectors_have_the_right_size_and_unit_length(self):
        for vec in self.embedder.embed_texts(["black trousers", "hoodie", ""]):
            self.assertEqual(len(vec), DIM)
            self.assertAlmostEqual(math.sqrt(sum(x * x for x in vec)), 1.0, places=6)

    def test_same_text_gives_the_same_vector(self):
        a, b = self.embedder.embed_texts(["blue jeans", "blue jeans"])
        self.assertEqual(a, b)

    def test_shared_words_are_closer_than_unrelated_ones(self):
        jeans, trousers, shoes = self.embedder.embed_texts(["blue jeans", "blue trousers", "white sneakers"])
        dot = lambda x, y: sum(p * q for p, q in zip(x, y))
        self.assertGreater(dot(jeans, trousers), dot(jeans, shoes))

    def test_images_use_the_file_name(self):
        a, b = self.embedder.embed_images(["data/images/1.jpg", "other/folder/1.jpg"])
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
