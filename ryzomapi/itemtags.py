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

common_tags = (
    # Armors
    ('armor', re.compile('^ic[mtzfocb]a')),
    ('boots', re.compile('^ic[mtzfocb]a[lmh]b')),
    ('gloves', re.compile('^ic[mtzfocb]a[lmh]g')),
    ('pants', re.compile('^ic[mtzfocb]a[lmhc]p')),
    ('sleeves', re.compile('^ic[mtzfocb]a[lmh]s')),
    ('vest', re.compile('^ic[mtzfocb]a[lmh]v')),
    ('helmet', re.compile('^ic[mtzfocb]a[lmh]h')),
    ('light_armor', re.compile('^ic[mtzfocb]a[lc]')),
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

    # Shields
    ('shield', re.compile('^ic[mtzfocb](kar|kam)?s')),
    ('large_shield', re.compile('^ic[mtzfocb](kar|kam)?ss')),
    ('buckler', re.compile('^ic[mtzfocb](kar|kam)?sb')),

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

    # Teleporters
    ('teleporter', re.compile('^tp_')),
    ('karavan', re.compile('^tp_karavan')),
    ('kami', re.compile('^tp_kami')),
    ('fyros', re.compile('^tp_(karavan|kami)_(dyron|frahartowers|oflovaksoasis|outlawcanyon|pyr|sawdustmines|thescorchedcorridor|thesos)')),
    ('matis', re.compile('^tp_(karavan|kami)_(avalae|davae|fleetinggarden|groveofconfusion|hereticshovel|hiddensource|knollofdissent|natae|upperbog|yrkanis)')),
    ('tryker', re.compile('^tp_(karavan|kami)_(avendale|bountybeaches|crystabell|dewdrops|enchantedisle|fairhaven|lagoonsofloria|restingwater|thefount|windermeer|windsofmuse)')),
    ('zorai', re.compile('^tp_(karavan|kami)_(groveofumbra|havenofpurity|hoi_cho|jen_lai|knotofdementia|maidengrove|min_cho|thevoid|zora)')),
    ('prime_root', re.compile('^tp_(karavan|kami)_(almati|forbidden_depths|gate_of_obscurity|nexus_terre|the_abyss_of_ichor_matis|the_elusive_forest|the_land_of_continuity|the_sunken_city|the_trench_of_trials_zorai|the_under_spring_fyros|the_windy_gate)')),

    # Materials
    ('material', re.compile('^m\d')),
    ('forest', re.compile('^m.*f\w\d{2}$')),
    ('lac', re.compile('^m.*l\w\d{2}$')),
    ('jungle', re.compile('^m.*j\w\d{2}$')),
    ('desert', re.compile('^m.*d\w\d{2}$')),
    ('prime_root', re.compile('^m.*p\w\d{2}$')),
    ('common', re.compile('^m.*c\w\d{2}$')),

    # Enchantments
    ('crystalized_spell', re.compile('^crystalized_spell$')),
    ('sap_recharge', re.compile('^.*sap_recharge$')),

    # Pets
    ('pet', re.compile('^ia[ps]')),
    ('packer', re.compile('^iap')),
    ('mount', re.compile('^ias')),

    # marauder crystal
    ('marauder_crystal', re.compile('^marauder_teleport_crystal$')),

    # Jobs items
    ('job_item', re.compile('^rpjobitem')),

    # Consumables items
    ('fireworks', re.compile('^.*fireworks')),
    ('consumable', re.compile('^ip')),
    ('consumable', re.compile('^conso_')),

    # Misc
    ('skin1', re.compile('^ic[mtzfocb].*_1$')),
    ('skin2', re.compile('^ic[mtzfocb].*_2$')),
    ('skin3', re.compile('^ic[mtzfocb].*_3$')),
    ('matis', re.compile('^icm')),
    ('tryker', re.compile('^ict')),
    ('zorai', re.compile('^icz')),
    ('fyros', re.compile('^icf')),
    ('catalyser', re.compile('^ixpca01$')),
    ('piece_of_kitin', re.compile('^slaughter_week_token$')),
)

material_type_re = re.compile('m(\d+)\D')
material_specific_tags = {
    1: ['abhaya', 'wood', 'barrel', 'armor_shell'],
    6: ['anete', 'fiber', 'grip', 'clothes'],
    9: ['arma', 'spine', 'trigger', 'jewel_setting'],
    14: ['beckers', 'bark', 'shaft', 'ammo_bullet'],
    15: ['beng', 'amber', 'jewel', 'magic_focus'],
    16: ['big', 'shell', 'blade', 'point'],
    18: ['bodoc', 'horn', 'shaft', 'ammo_bullet'],
    19: ['bodoc', 'skin', 'grip', 'clothes'],
    20: ['bodoc', 'nail', 'trigger', 'jewel_setting'],
    21: ['buo', 'fiber', 'grip', 'clothes'],
    23: ['caprice', 'seed', 'trigger', 'jewel_setting'],
    25: ['capryni', 'hoof', 'hammer', 'counterweight'],
    31: ['cuty', 'shell', 'blade', 'point'],
    37: ['dzao', 'fiber', 'grip', 'clothes'],
    40: ['eyota', 'wood', 'barrel', 'armor_shell'],
    43: ['gingo', 'claw', 'blade', 'point'],
    44: ['gingo', 'leather', 'barrel', 'armor_shell'],
    46: ['glue', 'resin', 'ammo_jacket', 'lining'],
    48: ['goari', 'shell', 'barrel', 'armor_shell'],
    49: ['gulatch', 'oil', 'explosive', 'stuffing'],
    50: ['hash', 'amber', 'jewel', 'magic_focus'],
    53: ['horny', 'shell', 'blade', 'point'],
    64: ['kachine', 'wood', 'barrel', 'armor_shell'],
    66: ['kincher', 'shell', 'barrel', 'armor_shell'],
    67: ['kincher', 'sting', 'blade', 'point'],
    68: ['kiban', 'shell', 'barrel', 'armor_shell'],
    69: ['kipesta', 'shell', 'barrel', 'armor_shell'],
    72: ['kipee', 'shell', 'barrel', 'armor_shell'],
    73: ['kipucka', 'shell', 'barrel', 'armor_shell'],
    74: ['kipucka', 'rostrum', 'firing_pin', 'armor_clip'],
    76: ['kirosta', 'sting', 'blade', 'point'],
    77: ['kipucker', 'secretion'],
    78: ['kizoar', 'tail', 'firing_pin', 'armor_clip'],
    81: ['lumper', 'skin', 'grip', 'clothes'],
    82: ['lumper', 'spine', 'trigger', 'jewel_setting'],
    83: ['lumper', 'whiskers', 'ammo_jacket', 'lining'],
    86: ['mektoub', 'skin', 'grip', 'clothes'],
    87: ['mektoub', 'trunk', 'ammo_jacket', 'lining'],
    93: ['motega', 'wood', 'barrel', 'armor_shell'],
    100: ['patee', 'node', 'hammer', 'counterweight'],
    101: ['perfling', 'bark', 'shaft', 'ammo_bullet'],
    102: ['pha', 'amber', 'jewel', 'magic_focus'],
    103: ['pilan', 'oil', 'explosive', 'stuffing'],
    106: ['ragus', 'claw', 'blade', 'point'],
    107: ['ragus', 'leather', 'barrel', 'armor_shell'],
    109: ['redhot', 'sap', 'firing_pin', 'armor_clip'],
    113: ['sarina', 'seed', 'trigger', 'jewel_setting'],
    115: ['saurona', 'seed', 'trigger', 'jewel_setting'],
    116: ['jubla'],
    117: ['sha', 'amber', 'jewel', 'magic_focus'],
    118: ['shu', 'fiber', 'grip', 'clothes'],
    119: ['silverweed', 'sap', 'firing_pin', 'armor_clip'],
    123: ['smart', 'shell', 'blade', 'point'],
    124: ['soo', 'amber', 'jewel', 'magic_focus'],
    125: ['splinter', 'shell', 'blade', 'point'],
    128: ['tama', 'wood', 'barrel', 'armor_shell'],
    133: ['timari', 'skin', 'grip', 'clothes'],
    134: ['torbak', 'claw', 'blade', 'point'],
    135: ['torbak', 'fang', 'explosive', 'stuffing'],
    136: ['torbak', 'horn', 'shaft', 'ammo_bullet'],
    137: ['torbak', 'leather', 'barrel', 'armor_shell'],
    140: ['varinx', 'fang', 'explosive', 'stuffing'],
    141: ['varinx', 'leather', 'barrel', 'armor_shell'],
    142: ['visc', 'sap', 'firing_pin', 'armor_clip'],
    145: ['yber', 'leather', 'barrel', 'armor_shell'],
    147: ['yelk', 'moss', 'ammo_jacket', 'lining'],
    148: ['yelk', 'mushroom', 'jewel', 'magic_focus'],
    149: ['yelk', 'nail', 'trigger', 'jewel_setting'],
    152: ['yubo', 'skin', 'grip', 'clothes'],
    153: ['zerx', 'bone', 'shaft', 'ammo_bullet'],
    154: ['zerx', 'claw', 'blade', 'point'],
    155: ['zun', 'amber', 'jewel', 'magic_focus'],
    162: ['cratcha'],
    163: ['cratcha'],
    164: ['stinga'],
    165: ['stinga'],
    166: ['jubla'],
    167: ['jubla'],
    168: ['psykopla'],
    169: ['psykopla'],
    170: ['slaveni'],
    171: ['slaveni'],
    172: ['shooki'],
    173: ['shooki'],
    264: ['ragus', 'meat'],
    266: ['capryni', 'meat'],
    268: ['cray'],
    269: ['igara', 'meat'],
    270: ['izam', 'meat'],
    273: ['bodoc', 'meat'],
    281: ['kipee'],
    282: ['kizoar'],
    284: ['ocyx', 'bone', 'shaft', 'ammo_bullet'],
    288: ['gingo', 'blood'],
    289: ['ragus', 'blood'],
    291: ['kipee', 'blood'],
    294: ['cray', 'blood'],
    296: ['capryni'],
    298: ['gingo'],
    299: ['torbak'],
    300: ['ragus'],
    303: ['zerx'],
    304: ['bodoc'],
    312: ['kitin_larva', 'generic'],
    314: ['bodoc', 'skull'],
    315: ['capryni', 'skull'],
    316: ['gingo', 'skull'],
    319: ['torbak', 'skull'],
    321: ['igara', 'skull'],
    322: ['izam', 'skull'],
    324: ['ragus', 'skull'],
    325: ['najab', 'skull'],
    329: ['varinx'],
    331: ['zerx', 'skull'],
    335: ['javing', 'wing', 'explosive', 'stuffing'],
    336: ['clopper', 'shell', 'barrel', 'armor_shell'],
    338: ['varinx', 'bone', 'shaft', 'ammo_bullet'],
    339: ['gingo', 'bone', 'shaft', 'ammo_bullet'],
    341: ['cuttler', 'bone', 'shaft', 'ammo_bullet'],
    343: ['ragus', 'bone', 'shaft', 'ammo_bullet'],
    345: ['timari', 'tooth', 'ammo_jacket', 'lining'],
    346: ['ragus', 'fang', 'explosive', 'stuffing'],
    347: ['gingo', 'fang', 'explosive', 'stuffing'],
    348: ['cuttler', 'fang', 'explosive', 'stuffing'],
    349: ['yetin', 'fang', 'explosive', 'stuffing'],
    350: ['messab', 'tooth', 'ammo_jacket', 'lining'],
    356: ['zerx', 'fang', 'explosive', 'stuffing'],
    359: ['messab', 'nail', 'trigger', 'jewel_setting'],
    363: ['wombai', 'skin', 'grip', 'clothes'],
    364: ['bolobi', 'skin', 'grip', 'clothes'],
    365: ['messab', 'skin', 'grip', 'clothes'],
    366: ['yber', 'wing', 'explosive', 'stuffing'],
    367: ['bawaab', 'skin', 'grip', 'clothes'],
    368: ['horncher', 'shell', 'barrel', 'armor_shell'],
    369: ['najab', 'leather', 'barrel', 'armor_shell'],
    371: ['izam', 'leather', 'barrel', 'armor_shell'],
    372: ['igara', 'leather', 'barrel', 'armor_shell'],
    374: ['bawaab', 'nail', 'trigger', 'jewel_setting'],
    376: ['cuttler', 'leather', 'barrel', 'armor_shell'],
    378: ['messab', 'hoof', 'hammer', 'counterweight'],
    380: ['frippo', 'skin', 'grip', 'clothes'],
    383: ['gubani', 'tooth', 'ammo_jacket', 'lining'],
    384: ['ocyx', 'bone', 'shaft', 'ammo_bullet'],
    385: ['jugula', 'fang', 'explosive', 'stuffing'],
    386: ['tyrancha', 'claw', 'blade', 'point'],
    387: ['kidinak', 'claw', 'blade', 'point'],
    390: ['vorax', 'claw', 'blade', 'point'],
    395: ['bawaab', 'meat'],
    398: ['gnoof', 'meat'],
    400: ['shalah', 'meat'],
    401: ['ploderos', 'meat'],
    404: ['arana', 'meat'],
    406: ['javing', 'meat'],
    407: ['cuttler', 'meat'],
    415: ['bawaab', 'skull'],
    420: ['shalah', 'skull'],
    421: ['ploderos', 'skull'],
    427: ['cuttler', 'skull'],
    435: ['bawaab', 'blood'],
    438: ['gnoof', 'blood'],
    440: ['shalah', 'blood'],
    441: ['ploderos', 'blood'],
    444: ['arana', 'blood'],
    446: ['javing', 'blood'],
    447: ['cuttler', 'blood'],
    453: ['gnoof'],
    455: ['shalah'],
    459: ['arana', 'moss'],
    462: ['yber', 'bone', 'shaft', 'ammo_bullet'],
    463: ['vorax', 'leather', 'barrel', 'armor_shell'],
    464: ['vorax', 'bone', 'shaft', 'ammo_bullet'],
    465: ['vorax', 'fang', 'explosive', 'stuffing'],
    467: ['ocyx', 'claw', 'blade', 'point'],
    468: ['najab', 'claw', 'blade', 'point'],
    469: ['arana', 'wood', 'barrel', 'armor_shell'],
    470: ['cray', 'shell', 'barrel', 'armor_shell'],
    471: ['madakam', 'skin', 'grip', 'clothes'],
    472: ['jubla', 'bud', 'jewel', 'magic_focus'],
    473: ['stinga', 'bud', 'jewel', 'magic_focus'],
    474: ['psykopla', 'bud', 'jewel', 'magic_focus'],
    475: ['slaveni', 'bud', 'jewel', 'magic_focus'],
    476: ['cratcha', 'bud', 'jewel', 'magic_focus'],
    477: ['shooki', 'bud', 'jewel', 'magic_focus'],
    479: ['kinrey', 'shell', 'barrel', 'armor_shell'],
    480: ['kinrey', 'sting', 'blade', 'point'],
    481: ['kinrey', 'mandible', 'shaft', 'ammo_bullet'],
    485: ['kidinak', 'shell', 'barrel', 'armor_shell'],
    487: ['kidinak', 'mandible', 'shaft', 'ammo_bullet'],
    488: ['kidinak', 'tail', 'firing_pin', 'armor_clip'],
    490: ['kizarak', 'shell', 'barrel', 'armor_shell'],
    491: ['kizarak', 'sting', 'blade', 'point'],
    492: ['kizarak', 'mandible', 'shaft', 'ammo_bullet'],
    496: ['kipee', 'sting', 'blade', 'point'],
    497: ['adriel', 'bark', 'shaft', 'ammo_bullet'],
    498: ['arana', 'eye', 'jewel', 'magic_focus'],
    499: ['arana', 'nail', 'trigger', 'jewel_setting'],
    500: ['arana', 'pelvis', 'hammer', 'counterweight'],
    501: ['arana', 'tooth', 'ammo_jacket', 'lining'],
    502: ['arma', 'eye', 'jewel', 'magic_focus'],
    503: ['arma', 'skin', 'grip', 'clothes'],
    504: ['arma', 'pelvis', 'hammer', 'counterweight'],
    505: ['arma', 'tooth', 'ammo_jacket', 'lining'],
    506: ['bawaab', 'eye', 'jewel', 'magic_focus'],
    507: ['bawaab', 'pelvis', 'hammer', 'counterweight'],
    508: ['bawaab', 'tooth', 'ammo_jacket', 'lining'],
    509: ['bodoc', 'eye', 'jewel', 'magic_focus'],
    510: ['bodoc', 'pelvis', 'hammer', 'counterweight'],
    511: ['bodoc', 'tooth', 'ammo_jacket', 'lining'],
    512: ['bolobi', 'eye', 'jewel', 'magic_focus'],
    514: ['bolobi', 'nail', 'trigger', 'jewel_setting'],
    515: ['bolobi', 'pelvis', 'hammer', 'counterweight'],
    516: ['bolobi', 'tooth', 'ammo_jacket', 'lining'],
    517: ['capryni', 'eye', 'jewel', 'magic_focus'],
    518: ['capryni', 'skin', 'grip', 'clothes'],
    519: ['capryni', 'nail', 'trigger', 'jewel_setting'],
    520: ['capryni', 'tooth', 'ammo_jacket', 'lining'],
    521: ['clopper', 'mandible', 'shaft', 'ammo_bullet'],
    522: ['clopper', 'secretion', 'explosive', 'stuffing'],
    523: ['clopper', 'sting', 'blade', 'point'],
    524: ['clopper', 'tail', 'firing_pin', 'armor_clip'],
    525: ['cratcha', 'moss', 'ammo_jacket', 'lining'],
    526: ['cray', 'claw', 'blade', 'point'],
    527: ['cray', 'mandible', 'shaft', 'ammo_bullet'],
    528: ['cray', 'secretion', 'explosive', 'stuffing'],
    529: ['cray', 'tail', 'firing_pin', 'armor_clip'],
    530: ['cuttler', 'claw', 'blade', 'point'],
    531: ['cuttler', 'ligament', 'firing_pin', 'armor_clip'],
    533: ['dante', 'sap', 'firing_pin', 'armor_clip'],
    534: ['dung', 'resin', 'ammo_jacket', 'lining'],
    535: ['enola', 'sap', 'firing_pin', 'armor_clip'],
    536: ['frippo', 'eye', 'jewel', 'magic_focus'],
    538: ['frippo', 'nail', 'trigger', 'jewel_setting'],
    539: ['frippo', 'pelvis', 'hammer', 'counterweight'],
    540: ['frippo', 'tooth', 'ammo_jacket', 'lining'],
    541: ['fung', 'resin', 'ammo_jacket', 'lining'],
    542: ['gingo', 'ligament', 'firing_pin', 'armor_clip'],
    543: ['gnoof', 'eye', 'jewel', 'magic_focus'],
    544: ['gnoof', 'skin', 'grip', 'clothes'],
    545: ['gnoof', 'nail', 'trigger', 'jewel_setting'],
    546: ['gnoof', 'pelvis', 'hammer', 'counterweight'],
    547: ['gnoof', 'trunk', 'ammo_jacket', 'lining'],
    548: ['goari', 'mandible', 'shaft', 'ammo_bullet'],
    549: ['goari', 'secretion', 'explosive', 'stuffing'],
    550: ['goari', 'sting', 'blade', 'point'],
    551: ['goari', 'tail', 'firing_pin', 'armor_clip'],
    552: ['gubani', 'eye', 'jewel', 'magic_focus'],
    553: ['gubani', 'skin', 'grip', 'clothes'],
    554: ['gubani', 'nail', 'trigger', 'jewel_setting'],
    555: ['gubani', 'pelvis', 'hammer', 'counterweight'],
    556: ['horncher', 'mandible', 'shaft', 'ammo_bullet'],
    557: ['horncher', 'secretion', 'explosive', 'stuffing'],
    558: ['horncher', 'sting', 'blade', 'point'],
    559: ['horncher', 'tail', 'firing_pin', 'armor_clip'],
    560: ['igara', 'beak', 'blade', 'point'],
    561: ['igara', 'bone', 'shaft', 'ammo_bullet'],
    562: ['igara', 'ligament', 'firing_pin', 'armor_clip'],
    564: ['igara', 'wing', 'explosive', 'stuffing'],
    565: ['irin', 'oil', 'explosive', 'stuffing'],
    566: ['izam', 'beak', 'blade', 'point'],
    567: ['izam', 'bone', 'shaft', 'ammo_bullet'],
    568: ['izam', 'ligament', 'firing_pin', 'armor_clip'],
    570: ['izam', 'wing', 'explosive', 'stuffing'],
    571: ['javing', 'beak', 'blade', 'point'],
    572: ['javing', 'bone', 'shaft', 'ammo_bullet'],
    573: ['javing', 'ligament', 'firing_pin', 'armor_clip'],
    574: ['javing', 'leather', 'barrel', 'armor_shell'],
    575: ['jubla', 'moss', 'ammo_jacket', 'lining'],
    576: ['jugula', 'bone', 'shaft', 'ammo_bullet'],
    577: ['jugula', 'claw', 'blade', 'point'],
    578: ['jugula', 'ligament', 'firing_pin', 'armor_clip'],
    579: ['jugula', 'leather', 'barrel', 'armor_shell'],
    580: ['kiban', 'mandible', 'shaft', 'ammo_bullet'],
    581: ['kiban', 'secretion', 'explosive', 'stuffing'],
    582: ['kiban', 'sting', 'blade', 'point'],
    583: ['kiban', 'tail', 'firing_pin', 'armor_clip'],
    584: ['kidinak', 'secretion', 'explosive', 'stuffing'],
    585: ['kincher', 'mandible', 'shaft', 'ammo_bullet'],
    586: ['kincher', 'secretion', 'explosive', 'stuffing'],
    587: ['kincher', 'tail', 'firing_pin', 'armor_clip'],
    588: ['kinrey', 'secretion', 'explosive', 'stuffing'],
    589: ['kinrey', 'tail', 'firing_pin', 'armor_clip'],
    590: ['kipee', 'mandible', 'shaft', 'ammo_bullet'],
    591: ['kipee', 'secretion', 'explosive', 'stuffing'],
    592: ['kipee', 'tail', 'firing_pin', 'armor_clip'],
    593: ['kipesta', 'mandible', 'shaft', 'ammo_bullet'],
    594: ['kipesta', 'sting', 'blade', 'point'],
    595: ['kipesta', 'tail', 'firing_pin', 'armor_clip'],
    596: ['kipesta', 'wing', 'explosive', 'stuffing'],
    597: ['kipucka', 'claw', 'blade', 'point'],
    598: ['kipucka', 'mandible', 'shaft', 'ammo_bullet'],
    599: ['kipucka', 'secretion', 'explosive', 'stuffing'],
    600: ['kirosta', 'mandible', 'shaft', 'ammo_bullet'],
    601: ['kirosta', 'secretion', 'explosive', 'stuffing'],
    602: ['kirosta', 'shell', 'barrel', 'armor_shell'],
    603: ['kirosta', 'tail', 'firing_pin', 'armor_clip'],
    604: ['kizarak', 'secretion', 'explosive', 'stuffing'],
    605: ['kizarak', 'tail', 'firing_pin', 'armor_clip'],
    606: ['kizoar', 'mandible', 'shaft', 'ammo_bullet'],
    607: ['kizoar', 'shell', 'barrel', 'armor_shell'],
    608: ['kizoar', 'sting', 'blade', 'point'],
    609: ['kizoar', 'wing', 'explosive', 'stuffing'],
    610: ['koorin', 'oil', 'explosive', 'stuffing'],
    611: ['lumper', 'eye', 'jewel', 'magic_focus'],
    612: ['lumper', 'pelvis', 'hammer', 'counterweight'],
    613: ['madakam', 'eye', 'jewel', 'magic_focus'],
    615: ['madakam', 'nail', 'trigger', 'jewel_setting'],
    616: ['madakam', 'pelvis', 'hammer', 'counterweight'],
    617: ['madakam', 'tooth', 'ammo_jacket', 'lining'],
    618: ['mektoub', 'eye', 'jewel', 'magic_focus'],
    619: ['mektoub', 'nail', 'trigger', 'jewel_setting'],
    620: ['mektoub', 'pelvis', 'hammer', 'counterweight'],
    621: ['messab', 'eye', 'jewel', 'magic_focus'],
    623: ['mitexi', 'bark', 'shaft', 'ammo_bullet'],
    624: ['moon', 'resin', 'ammo_jacket', 'lining'],
    625: ['najab', 'bone', 'shaft', 'ammo_bullet'],
    626: ['najab', 'fang', 'explosive', 'stuffing'],
    627: ['najab', 'ligament', 'firing_pin', 'armor_clip'],
    629: ['nita', 'node', 'hammer', 'counterweight'],
    630: ['oath', 'bark', 'shaft', 'ammo_bullet'],
    632: ['ocyx', 'fang', 'explosive', 'stuffing'],
    633: ['ocyx', 'ligament', 'firing_pin', 'armor_clip'],
    634: ['ocyx', 'shell', 'barrel', 'armor_shell'],
    635: ['ploderos', 'eye', 'jewel', 'magic_focus'],
    636: ['ploderos', 'skin', 'grip', 'clothes'],
    637: ['ploderos', 'nail', 'trigger', 'jewel_setting'],
    638: ['ploderos', 'pelvis', 'hammer', 'counterweight'],
    639: ['ploderos', 'tooth', 'ammo_jacket', 'lining'],
    640: ['psykopla', 'moss', 'ammo_jacket', 'lining'],
    641: ['ragus', 'ligament', 'firing_pin', 'armor_clip'],
    642: ['raspal', 'eye', 'jewel', 'magic_focus'],
    643: ['raspal', 'skin', 'grip', 'clothes'],
    644: ['raspal', 'nail', 'trigger', 'jewel_setting'],
    645: ['raspal', 'pelvis', 'hammer', 'counterweight'],
    646: ['raspal', 'tooth', 'ammo_jacket', 'lining'],
    647: ['rendor', 'eye', 'jewel', 'magic_focus'],
    648: ['rendor', 'skin', 'grip', 'clothes'],
    649: ['rendor', 'nail', 'trigger', 'jewel_setting'],
    650: ['rendor', 'pelvis', 'hammer', 'counterweight'],
    651: ['rendor', 'tooth', 'ammo_jacket', 'lining'],
    653: ['shalah', 'eye', 'jewel', 'magic_focus'],
    654: ['shalah', 'skin', 'grip', 'clothes'],
    655: ['shalah', 'nail', 'trigger', 'jewel_setting'],
    656: ['shalah', 'pelvis', 'hammer', 'counterweight'],
    657: ['shalah', 'tooth', 'ammo_jacket', 'lining'],
    659: ['silvio', 'seed', 'trigger', 'jewel_setting'],
    652: ['scratch', 'node', 'hammer', 'counterweight'],
    658: ['shooki', 'moss', 'ammo_jacket', 'lining'],
    660: ['slaveni', 'moss', 'ammo_jacket', 'lining'],
    661: ['stinga', 'moss', 'ammo_jacket', 'lining'],
    662: ['tansy', 'node', 'hammer', 'counterweight'],
    663: ['timari', 'eye', 'jewel', 'magic_focus'],
    664: ['timari', 'nail', 'trigger', 'jewel_setting'],
    665: ['timari', 'pelvis', 'hammer', 'counterweight'],
    666: ['torbak', 'ligament', 'firing_pin', 'armor_clip'],
    667: ['tyrancha', 'bone', 'shaft', 'ammo_bullet'],
    668: ['tyrancha', 'fang', 'explosive', 'stuffing'],
    669: ['tyrancha', 'ligament', 'firing_pin', 'armor_clip'],
    670: ['tyrancha', 'leather', 'barrel', 'armor_shell'],
    671: ['varinx', 'claw', 'blade', 'point'],
    672: ['varinx', 'ligament', 'firing_pin', 'armor_clip'],
    673: ['vorax', 'ligament', 'firing_pin', 'armor_clip'],
    675: ['wombai', 'eye', 'jewel', 'magic_focus'],
    676: ['wombai', 'pelvis', 'hammer', 'counterweight'],
    677: ['wombai', 'spine', 'trigger', 'jewel_setting'],
    678: ['wombai', 'trunk', 'ammo_jacket', 'lining'],
    679: ['yana', 'node', 'hammer', 'counterweight'],
    680: ['yber', 'beak', 'blade', 'point'],
    681: ['yber', 'ligament', 'firing_pin', 'armor_clip'],
    682: ['yelk', 'skin', 'grip', 'clothes'],
    683: ['yelk', 'pelvis', 'hammer', 'counterweight'],
    684: ['yetin', 'bone', 'shaft', 'ammo_bullet'],
    685: ['yetin', 'claw', 'blade', 'point'],
    686: ['yetin', 'ligament', 'firing_pin', 'armor_clip'],
    687: ['yetin', 'leather', 'barrel', 'armor_shell'],
    688: ['yubo', 'eye', 'jewel', 'magic_focus'],
    690: ['yubo', 'nail', 'trigger', 'jewel_setting'],
    691: ['yubo', 'pelvis', 'hammer', 'counterweight'],
    692: ['yubo', 'tooth', 'ammo_jacket', 'lining'],
    693: ['zerx', 'ligament', 'firing_pin', 'armor_clip'],
    694: ['zerx', 'leather', 'barrel', 'armor_shell'],
    695: ['kipucker', 'claw'],
    #696: ['pendant'],
    710: ['goo'],
    741: ['tekorn', 'op_mat', 'modified'],
    742: ['maga', 'op_mat', 'modified'],
    743: ['armilo', 'op_mat', 'modified'],
    744: ['greslin', 'op_mat', 'modified'],
    745: ['tekorn', 'op_mat', 'purified'],
    746: ['maga', 'op_mat', 'purified'],
    747: ['armilo', 'op_mat', 'purified'],
    748: ['greslin', 'op_mat', 'purified'],
    749: ['vedice', 'op_mat', 'modified'],
    750: ['cheng', 'op_mat', 'modified'],
    751: ['rubbarn', 'op_mat', 'modified'],
    752: ['egiros', 'op_mat', 'modified'],
    753: ['vedice', 'op_mat', 'purified'],
    754: ['cheng', 'op_mat', 'purified'],
    755: ['rubbarn', 'op_mat', 'purified'],
    756: ['egiros', 'op_mat', 'purified'],
    758: ['gingo', 'fur', 'stuffing'],
    759: ['igara', 'skin', 'stuffing'],
    #: ['', ],
}
