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

from ryzomapi.apikey import *
import unittest

class APIKeyTest(unittest.TestCase):
    def setUp(self):
        self.invalid_keys = ('', 'g', 'c', '42',
                             'uc9f86ed78c10aa1874353af146cd543c460a74b8',
                             'c96fa67c68d378f2bd36148debe7d0k3b5552d5e2',
                             'g96fa67c68d378f2bd36148debe7d0d3b555kd5e2',
                             'c531a50bddf4749505d03cc05e8115e621c82c3f',
                             'c531a50bddf4749505d03cc05e8115e621c82c3f21',
                             '0b9c2625dc21ef05f6ad4ddf47c5f203837aa32c')
        self.character_keys = ('c0b9c2625dc21ef05f6ad4ddf47c5f203837aa32c',
                               'ceb3c97d345ee254bfed58913f4fdd9b5acdad6a6',
                               'c3a00c5e0156c4bebea4989669042865f004c783e',
                               'cf54ba8836fb1008b37eb3b6619f29056d2a79b77',
                               'c4425eede33bf6f31709e2c3b2c78df68ec1e41d5')
        self.guild_keys = ('g0b9c2625dc21ef05f6ad4ddf47c5f203837aa32c',
                           'g6d3d1870042e01291dfdc5bb127c0367827de6f9',
                           'g35d2949c41b31f0db0db3ba8006b658a0ec50a1f',
                           'geb557ba8d9b6bfb3f57be2ea03e0beda923a731a',
                           'gc00a8959be39473e458439b1ada539122bc2ff41')

    def test_guild_valid(self):
        for key in self.guild_keys:
            self.assertEqual(guild_api_key_is_valid(key), True, key)

    def test_character_valid(self):
        for key in self.character_keys:
            self.assertEqual(character_api_key_is_valid(key), True, key)

    def test_character_invalid(self):
        for key in self.invalid_keys:
            self.assertEqual(guild_api_key_is_valid(key), False, key)
            self.assertEqual(character_api_key_is_valid(key), False, key)

if __name__ == '__main__':
    unittest.main()
