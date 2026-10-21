"""A fake embedder for tests: no download, no GPU, same two methods as the real FashionCLIP embedder.

Words that two texts share give similar vectors, but synonyms do not ("hoodie" is not close to "sweatshirt").
That is fine for tests; only the real embedder is semantic.

The interface every embedder follows:
    embed_texts(texts)  -> list of vectors, one per text
    embed_images(paths) -> list of vectors, one per image file
Every vector has DIM numbers and length 1.
"""

import hashlib
import math

DIM = 512


def _normalize(vec):
    norm = math.sqrt(sum(x * x for x in vec)) or 1.0
    return [x / norm for x in vec]


class FakeEmbedder:
    def _embed(self, text):
        vec = [0.0] * DIM
        for word in text.lower().split():
            h = hashlib.sha256(word.encode()).digest()
            vec[int.from_bytes(h[:4], "big") % DIM] += 1.0
        return _normalize(vec) if any(vec) else _normalize([1.0] * DIM)

    def embed_texts(self, texts):
        return [self._embed(t) for t in texts]

    def embed_images(self, paths):
        # Uses the file name as a stand-in for the image content.
        return [self._embed(str(p).replace("\\", "/").rsplit("/", 1)[-1]) for p in paths]
