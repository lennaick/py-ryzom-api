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

import re

available_tags = (
    # Armors
    ('armor', re.compile('^ic[mtzfocb]a')),
    ('boots', re.compile('^ic[mtzfocb]a[lmh]b')),
    ('gloves', re.compile('^ic[mtzfocb]a[lmh]g')),
    ('pants', re.compile('^ic[mtzfocb]a[lmh]p')),
    ('sleeves', re.compile('^ic[mtzfocb]a[lmh]s')),
    ('vest', re.compile('^ic[mtzfocb]a[lmh]v')),
    ('helmet', re.compile('^ic[mtzfocb]a[lmh]h')),
    ('light_armor', re.compile('^ic[mtzfocb]al')),
    ('medium_armor', re.compile('^ic[mtzfocb]am')),
    ('heavy_armor', re.compile('^ic[mtzfocb]ah')),

    # Weapons
    ('weapon', re.compile('^ic[mtzfocb][mr]')),

    # Melee weapons
    ('melee_weapon', re.compile('^ic[mtzfocb](kar|kam)?m')),
    ('one_handed', re.compile('^ic[mtzfocb](kar|kam)?m1')),
    ('two_handed', re.compile('^ic[mtzfocb](kar|kam)?m2')),
    ('sword', re.compile('^ic[mtzfocb](kar|kam)?m[12]ss[elbw]?')),
    ('mace', re.compile('^ic[mtzfocb](kar|kam)?m[12]bm[elbw]?')),
    ('axe', re.compile('^ic[mtzfocb](kar|kam)?m[12]sa[elbw]?')),
    ('spear', re.compile('^ic[mtzfocb](kar|kam)?m[12]ps[elbw]?')),
    ('dagger', re.compile('^ic[mtzfocb](kar|kam)?m[12]pd[elbw]?')),
    ('magic_amplifier', re.compile('^ic[mtzfocb](kar|kam)?m[12]ms[elbw]?')),
    ('pike', re.compile('^ic[mtzfocb](kar|kam)?m[12]pp[elbw]?')),
    ('staff', re.compile('^ic[mtzfocb](kar|kam)?m[12]bs[elbw]?')),

    # Range weapon
    ('range_weapon', re.compile('^ic[mtzfocb](kar|kam)?r')),
    ('autolauncher', re.compile('^ic[mtzfocb](kar|kam)?r2a[elbw]?')),
    ('launcher', re.compile('^ic[mtzfocb](kar|kam)?r2l[elbw]?')),
    ('pistol', re.compile('^ic[mtzfocb](kar|kam)?r1p[elbw]?')),
    ('bowpistol', re.compile('^ic[mtzfocb](kar|kam)?r1b[elbw]?')),
    ('rifle', re.compile('^ic[mtzfocb](kar|kam)?r2r[elbw]?')),
    ('bowrifle', re.compile('^ic[mtzfocb](kar|kam)?r2b[elbw]?')),

    # Ammo
    ('ammo', re.compile('ic[mtzfocb]p')),
    ('smashing_ammo', re.compile('ic[mtzfocb]p[12][abplr]b')),
    ('piercing_ammo', re.compile('ic[mtzfocb]p[12][abplr]p')),
    ('slashing_ammo', re.compile('ic[mtzfocb]p[12][abplr]s')),
    ('autolauncher_ammo', re.compile('ic[mtzfocb]p2a[bps]')),
    ('launcher_ammo', re.compile('ic[mtzfocb]p2l[bps]')),
    ('pistol_ammo', re.compile('ic[mtzfocb]p1p[bps]')),
    ('bowpistol_ammo', re.compile('ic[mtzfocb]p2b[bps]')),
    ('rifle_ammo', re.compile('ic[mtzfocb]p2r[bps]')),
    ('bowrifle_ammo', re.compile('ic[mtzfocb]p2b[bps]')),

    # Jewels
    ('jewel', re.compile('^ic[mtzfocb]j[abdepr]')),
    ('anklet', re.compile('^ic[mtzfocb]ja')),
    ('bracelet', re.compile('^ic[mtzfocb]jb')),
    ('diadem', re.compile('^ic[mtzfocb]jd')),
    ('earring', re.compile('^ic[mtzfocb]je')),
    ('pendant', re.compile('^ic[mtzfocb]jp')),
    ('ring', re.compile('^ic[mtzfocb]jr')),

    # Tools
    ('tool', re.compile('^it')),
    ('tool', re.compile('^ic[mtzfocb](kar|kam)t')),
    ('armor_tool', re.compile('^itarmor')),
    ('armor_tool', re.compile('^ic[mtzfocb](kar|kam)tarmor')),
    ('ammo_tool', re.compile('^itammo')),
    ('ammo_tool', re.compile('^ic[mtzfocb](kar|kam)tammo')),
    ('melee_weapon_tool', re.compile('^itmwea')),
    ('melee_weapon_tool', re.compile('^ic[mtzfocb](kar|kam)tmwea')),
    ('range_weapon_tool', re.compile('^itrwea')),
    ('range_weapon_tool', re.compile('^ic[mtzfocb](kar|kam)trwea')),
    ('jewel_tool', re.compile('^itjewel')),
    ('jewel_tool', re.compile('^ic[mtzfocb](kar|kam)tjewel')),
    ('tool_tool', re.compile('^ittool')),
    ('tool_tool', re.compile('^ic[mtzfocb](kar|kam)ttool')),
    ('pick', re.compile('^itforage')),
    ('pick', re.compile('^ic[mtzfocb](kar|kam)tforage')),

    # Materials
    ('material', re.compile('^m')),
    ('forest', re.compile('^m.*f\w\d{2}$')),
    ('lac', re.compile('^m.*l\w\d{2}$')),
    ('jungle', re.compile('^m.*j\w\d{2}$')),
    ('desert', re.compile('^m.*d\w\d{2}$')),
    ('prime_root', re.compile('^m.*p\w\d{2}$')),

    # Misc
    ('skin1', re.compile('^ic[mtzfocb].*_1$')),
    ('skin2', re.compile('^ic[mtzfocb].*_2$')),
    ('skin3', re.compile('^ic[mtzfocb].*_3$')),
    ('matis', re.compile('^icm')),
    ('tryker', re.compile('^ict')),
    ('zorai', re.compile('^icz')),
    ('fyros', re.compile('^icf')),
    ('catalyser', re.compile('^ixpca01$')),
)
