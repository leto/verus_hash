import verus_hash
from binascii import unhexlify, hexlify

import unittest
header_hex = ("deadbeefdeadbeef")
best_hash = ('codecodecode')

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_verus_hash(self):
        self.pow_hash = hexlify(verus_hash.header_hash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)

if __name__ == '__main__':
    unittest.main()

