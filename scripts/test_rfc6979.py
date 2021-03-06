#!/usr/bin/env python3

import unittest
from rfc6979 import sha256, rfc6979

class Testrfc6979(unittest.TestCase):
    def test_rfc6979(self):
        # source: https://bitcointalk.org/index.php?topic=285142.40
        msg = sha256(b'Satoshi Nakamoto').digest()
        x = 0x1
        nonce = rfc6979(x, msg)
        expected = 0x8F8A276C19F4149656B280621E358CCE24F5F52542772691EE69063B74F15D15
        self.assertEqual(nonce, expected)


if __name__ == "__main__":
    # execute only if run as a script
    unittest.main()
