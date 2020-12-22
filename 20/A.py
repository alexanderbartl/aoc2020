import math

with open('input.txt') as f:
    raw_tiles = f.read().split('\n\n')


class Tile:
    def __init__(self, raw):
        lines = raw.strip().split('\n')
        self.id = int(lines[0][5:9])
        self.img = lines[1:]
        self.fingerprints = [self.fingerprint_left(), self.fingerprint_top(), self.fingerprint_right(), self.fingerprint_bottom()]

    def __repr__(self):
        return f'<Tile id={self.id}>'

    def get_next(self, direction):
        fingerprint = getattr(self, f'fingerprint_{direction}')()
        candidates = [t for t in tiles if t.id != self.id and fingerprint in t.fingerprints
                      or self._reversed(fingerprint) in t.fingerprints]
        if len(candidates) != 1:
            return None
        return candidates[0]

    def fingerprint_left(self):
        return self._fingerprint(''.join(l[0] for l in self.img))

    def fingerprint_top(self):
        return self._fingerprint(self.img[0])

    def fingerprint_right(self):
        return self._fingerprint(''.join(l[-1] for l in self.img))

    def fingerprint_bottom(self):
        return self._fingerprint(self.img[-1])

    def rotate(self):
        self.img = [''.join(l) for l in list(zip(*self.img[::-1]))]

    def flip(self):
        self.img = self.img[::-1]

    @staticmethod
    def _fingerprint(string):
        return int(string.replace('.', '0').replace('#', '1'), 2)

    @staticmethod
    def _reversed(n):
        return int(bin(n)[2:].zfill(10)[::-1], 2)


tiles = [Tile(t) for t in raw_tiles]
corners = [t for t in tiles if len([neighbor for neighbor in (t.get_next('right'), t.get_next('top'), t.get_next('left'), t.get_next('bottom')) if neighbor is not None]) == 2]
print(corners, math.prod(t.id for t in corners))