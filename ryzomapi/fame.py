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

class Fame:
    __min = -600000
    __max = 600000
    faction = {'kami': 0, 'karavan': 0}
    nation = {'fyros': 0, 'matis': 0, 'tryker': 0, 'zorai': 0}
    tribe = {'tribe_ancient_dryads': 0, 'tribe_antikamis': 0, 'tribe_barkers': 0, 'tribe_beachcombers': 0, 'tribe_black_circle': 0, 'tribe_cholorogoos': 0, 'tribe_cockroaches': 0, 'tribe_company_of_the_eternal_tree': 0, 'tribe_corsair': 0, 'tribe_cute': 0, 'tribe_darkening_sap': 0, 'tribe_dune_riders': 0, 'tribe_ecowarriors': 0, 'tribe_firebrands': 0, 'tribe_first_deserter': 0, 'tribe_frahar': 0, 'tribe_frahar_hunters': 0, 'tribe_gibbay': 0, 'tribe_goo_heads': 0, 'tribe_green_seed': 0, 'tribe_hamazans_of_the_dead_seed': 0, 'tribe_icon_workshipers': 0, 'tribe_keepers': 0, 'tribe_kitin_gatheres': 0, 'tribe_lagoon_brothers': 0, 'tribe_lawless': 0, 'tribe_leviers': 0, 'tribe_master_of_the_goo': 0, 'tribe_matisian_border_guards': 0, 'tribe_night_turners': 0, 'tribe_oasis_diggers': 0, 'tribe_pyromancers': 0, 'tribe_recoverers': 0, 'tribe_renegades': 0, 'tribe_restorers': 0, 'tribe_root_tappers': 0, 'tribe_sacred_sap': 0, 'tribe_sap_gleaners': 0, 'tribe_sap_slaves': 0, 'tribe_scorchers': 0, 'tribe_shadow_runners': 0, 'tribe_siblings_of_the_weeds': 0, 'tribe_silt_sculptors': 0, 'tribe_slavers': 0, 'tribe_smuglers': 0, 'tribe_the_arid_matis': 0, 'tribe_the_kuilde': 0, 'tribe_the_slash_and_burn': 0, 'tribe_tutors': 0, 'tribe_water_breakers': 0, 'tribe_woven_bridles': 0}

    def __init__(self, it):
        for f in it:
            if f.tag in self.faction:
                self.faction[f.tag] = round(self.clamp(f.text)/6000 ,3)
            if f.tag in self.nation:
                self.nation[f.tag] = round(self.clamp(f.text)/6000 ,3)
            if f.tag in self.tribe:
                self.tribe[f.tag] = round(self.clamp(f.text)/6000 ,3)

    def clamp(self, value):
        return sorted((self.__min, int(value), self.__max))[1]

class Allegiance:
    faction = None
    nation = None

    def __init__(self, faction=None, nation=None):
        if faction is not None and faction.lower() in Fame.faction:
            self.faction = faction.lower()
        if nation is not None and nation.lower() in Fame.nation:
            self.nation = nation.lower()
