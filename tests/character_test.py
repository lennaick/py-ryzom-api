##
## Copyright (c) 2014 Rodolphe Breard
## 
## Permission to use, copy, modify, and/or distribute this software for any
## purpose with or without fee is hereby granted, provided that the above
## copyright notice and this permission notice appear in all copies.
## 
## THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
## WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
## MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
## ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
## WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
## ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
## OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
##

import sys
sys.path.insert(0, '.')

from ryzomapi.exceptions import InvalidAPIKeyException
from ryzomapi.character import Character
import unittest

class CharacterTest(unittest.TestCase):
    def test_character_loading(self):
        character = Character(from_file='tests/data/character_1.xml')
        self.assertEqual(character.id, 4269)
        self.assertEqual(character.name, 'Debughomin')
        self.assertEqual(character.allegiance.nation, 'matis')
        self.assertEqual(character.allegiance.faction, 'karavan')

    def test_character_invalid_data(self):
        with self.assertRaises(InvalidAPIKeyException):
            Character('')

        with self.assertRaises(InvalidAPIKeyException):
            Character('invalid key')

if __name__ == '__main__':
    unittest.main()
