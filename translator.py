# -*- coding: utf-8 -*-
from string import punctuation, digits, ascii_letters


class TranslationTable(object):
    def __init__(self, chr_=None, uni_=None, t1=None, pos=None):
        self.chr_name = chr_  # Name of Character
        self.uni_value = uni_  # Unicode String
        self.t1_value = t1  # Translation value of character
        self.t1_pos = pos  # position of character 0 before or 1 after

    def __str__(self):
        return self.uni_value.encode("UTF-8")

    def __repr__(self):
        return repr(self.uni_value)


class Tamil(object):  # Unicode Tamil
#TODO - use unicodedata module and lookup instead of hard-coding the characters
    def __init__(self, charset=None):
        self.om = TranslationTable('OM', u'\u0BD0')  # No Anu
        self.dot = TranslationTable('pulli', u'\u0BCD', u'\xf6')  # No Anu
        self.leg = TranslationTable('VOWEL SIGN AA', u'\u0BBE', u'V', 1)
        self.smhorn = TranslationTable('VOWEL SIGN I', u'\u0BBF',
                                       u'\xe5')  # No Anu
        self.bghorn = TranslationTable('VOWEL SIGN II', u'\u0BC0',
                                       u'\xe7')  # No Anu
        self.smu = TranslationTable('VOWEL SIGN U', u'\u0BC1',
                                    u'\xe9')  # No Anu
        self.bguu = TranslationTable('VOWEL SIGN UU', u'\u0BC2',
                                     u'\xe8')  # No Anu
        self.sme = TranslationTable('VOWEL SIGN E', u'\u0BC6', u'\xff', 0)
        self.bgee = TranslationTable('VOWEL SIGN EE', u'\u0BC7', u'\xba', 0)
        self.aii = TranslationTable('VOWEL SIGN AI', u'\u0BC8', u'\xc1', 0)
        self.smo = TranslationTable('VOWEL SIGN O', u'\u0BCA')
        self.bgoo = TranslationTable('VOWEL SIGN OO', u'\u0BCB')
        self.smau = TranslationTable('VOWEL SIGN AU', u'\u0BCC')
        self.llaau = TranslationTable('AU LENGTH MARK', u'\u0BD7')
        self.signs = [self.dot, self.smhorn, self.bghorn, self.smu, self.bguu,
                      self.sme, self.bgee, self.aii, self.smo, self.bgoo,
                      self.smau, self.llaau]
        self.a = TranslationTable('A', u'\u0B85', u'\u2202')
        self.aa = TranslationTable('AA', u'\u0B86', u'g')
        self.i = TranslationTable('I', u'\u0B87', u'\xf7')
        self.ii = TranslationTable('II', u'\u0B88', u'~')
        self.u = TranslationTable('U', u'\u0B89', u'c')
        self.uu = TranslationTable('UU', u'\u0B8A', u'\xaa')
        self.e = TranslationTable('E', u'\u0B8E', u'\xae')
        self.ee = TranslationTable('EE', u'\u0B8F', u'\u221e')
        self.ai = TranslationTable('AI', u'\u0B90', u'n')
        self.o = TranslationTable('O', u'\u0B92', u'\u0152')
        self.oo = TranslationTable('OO', u'\u0B93', u'{')
        self.au = TranslationTable('AU', u'\u0B94', u'\xa1')
        self.ak = TranslationTable('aytham', u'\u0B83', u'\u2021')
        self.indep_vowels = [self.a, self.aa, self.i, self.ii, self.u, self.uu,
                             self.e, self.ee, self.ai, self.o, self.oo, self.au,
                             self.ak]
        self.ka = TranslationTable('KA', u'\u0B95', u'\xd4')
        self.nga = TranslationTable('NGA', u'\u0B99', u'\xd9')
        self.ca = TranslationTable('CA', u'\u0B9A', u'\u0192')
        self.ja = TranslationTable('JA', u'\u0B9C', u'\xd6')
        self.nya = TranslationTable('NYA', u'\u0B9E', u'Q')
        self.tta = TranslationTable('TTA', u'\u0B9F', u'\xb6')
        self.nna = TranslationTable('NNA', u'\u0BA3', u'\xdc')
        self.ta = TranslationTable('TA', u'\u0BA4', u'>')
        self.na = TranslationTable('NA', u'\u0BA8', u'\xc2')
        self.nnna = TranslationTable('NNNA', u'\u0BA9', u'\u2122')
        self.pa = TranslationTable('PA', u'\u0BAA', u'\u221a')
        self.ma = TranslationTable('MA', u'\u0BAE', u'\\')
        self.ya = TranslationTable('YA', u'\u0BAF', u'B')
        self.ra = TranslationTable('RA', u'\u0BB0', u'\xb4')
        self.rra = TranslationTable('RRA', u'\u0BB1', u'\u2248')
        self.la = TranslationTable('LA', u'\u0BB2', u'\xc8')
        self.lla = TranslationTable('LLA', u'\u0BB3', u'e')
        self.llla = TranslationTable('LLLA', u'\u0BB4', u'w')
        self.va = TranslationTable('VA', u'\u0BB5', u'k')
        # Consonants -----------------------------------------------------------
        self.cons = [self.ka, self.nga, self.ca, self.ja, self.nya, self.tta,
                     self.nna, self.ta, self.na, self.nnna, self.pa, self.ma,
                     self.ya, self.ra, self.rra, self.la, self.lla, self.llla,
                     self.va]
        self.cons_dot = [x.uni_value + self.dot.uni_value for x in self.cons]
        self.cons_leg = [x.uni_value + self.leg.uni_value for x in self.cons]
        self.cons_smhorn = [x.uni_value + self.smhorn.uni_value for x in
                            self.cons]
        self.cons_bghorn = [x.uni_value + self.bghorn.uni_value for x in
                            self.cons]
        self.cons_smu = [x.uni_value + self.smu.uni_value for x in self.cons]
        self.cons_bguu = [x.uni_value + self.bguu.uni_value for x in self.cons]
        self.cons_sme = [x.uni_value + self.sme.uni_value for x in self.cons]
        self.cons_bgee = [x.uni_value + self.bgee.uni_value for x in self.cons]
        self.cons_aii = [x.uni_value + self.aii.uni_value for x in self.cons]
        self.cons_smo = [x.uni_value + self.smo.uni_value for x in self.cons]
        self.cons_bgoo = [x.uni_value + self.bgoo.uni_value for x in self.cons]
        self.cons_smau = [x.uni_value + self.smau.uni_value for x in self.cons]
        # ----------------------------------------------------------------------
        self.sha = TranslationTable('SHA', u'\u0BB6')  # No Anu
        self.ssa = TranslationTable('SSA', u'\u0BB7', u'\u2260')
        self.sa = TranslationTable('SA', u'\u0BB8', u'v')
        self.ha = TranslationTable('HA', u'\u0BB9', u'\xab')

        self.ssa_dot = TranslationTable('ISH',
                                        self.ssa.uni_value + self.dot.uni_value,
                                        u'i')
        self.ssa_smhorn = TranslationTable('SHE',
                                           self.ssa.uni_value +
                                           self.smhorn.uni_value, u'\xa5')
        self.ssa_bghorn = TranslationTable('SHEE',
                                           self.ssa.uni_value +
                                           self.bghorn.uni_value, u'U')
        self.ssa_smu = TranslationTable('SHU',
                                        self.ssa.uni_value +
                                        self.smu.uni_value, u'\u25ca')
        self.ssa_bguu = TranslationTable('SHU',
                                         self.ssa.uni_value +
                                         self.bguu.uni_value, u'\xa3')

        self.ssa_fm = [self.ssa_dot, self.ssa_smhorn, self.ssa_bghorn,
                       self.ssa_smu, self.ssa_bguu]
        self.sa_dot = TranslationTable('IS',
                                       self.sa.uni_value + self.dot.uni_value,
                                       u'\xb8')
        self.sa_smhorn = TranslationTable('SHE',
                                          self.sa.uni_value +
                                          self.smhorn.uni_value, u'L')
        self.sa_bghorn = TranslationTable('SHEE',
                                          self.sa.uni_value +
                                          self.bghorn.uni_value, u'\xa2')
        self.sa_smu = TranslationTable('SHU',
                                       self.sa.uni_value + self.smu.uni_value,
                                       u'q')
        self.sa_bguu = TranslationTable('SHU',
                                        self.sa.uni_value + self.bguu.uni_value,
                                        u'`')

        self.sa_fm = [self.sa_dot, self.sa_smhorn, self.sa_bghorn, self.sa_smu,
                      self.sa_bguu]
        self.ha_dot = TranslationTable('ISH',
                                       self.ha.uni_value + self.dot.uni_value,
                                       u'\u201e')
        self.ha_smhorn = TranslationTable('SHE',
                                          self.ha.uni_value +
                                          self.smhorn.uni_value, u'N')
        self.ha_bghorn = TranslationTable('SHEE',
                                          self.ha.uni_value +
                                          self.bghorn.uni_value, u'\xcd')
        self.ha_smu = TranslationTable('SHU',
                                       self.ha.uni_value + self.smu.uni_value,
                                       u'\xaf')
        self.ha_bguu = TranslationTable('SHU',
                                        self.ha.uni_value + self.bguu.uni_value,
                                        u'\xe3')
        self.ha_fm = [self.ha_dot, self.ha_smhorn, self.ha_bghorn, self.ha_smu,
                      self.ha_bguu]

        self.fancy = [self.ssa, self.sa, self.ha] + self.ssa_fm + self.sa_fm + \
                     self.ha_fm
        if charset == 'anu-mac':
            self.remove_invalid_chars()

    def remove_invalid_chars(self):
        self.cons_smhorn.pop(1)  # ஙி not in Anu
        self.cons_smhorn.pop(3)  # ஞி not in Anu

        self.cons_bghorn.pop(1)  # ஙீ not in Anu
        self.cons_bghorn.pop(3)  # ஞீ not in Anu

        self.cons_smu.pop(1)  # ஙு not in Anu
        self.cons_smu.pop(3)  # ஞு not in Anu

        self.cons_bguu.pop(1)  # ஙூ not in Anu
        self.cons_bguu.pop(3)  # ஞூ not in Anu

    def print_table(self):
        try:
            size = u' | '
            print '_' * 76
            print '| ' + size.join([x.uni_value for x in
                                    self.indep_vowels]) + ' |'
            for i, v in enumerate(self.cons):
                print '-' * 76
                line = '| ' + v.uni_value + size + self.cons_leg[i] \
                     + size + self.cons_smhorn[i] + size + \
                      self.cons_bghorn[i] + size + self.cons_smu[i] + size + \
                      self.cons_bguu[i] + size + self.cons_sme[i] + size + \
                      self.cons_bgee[i] + size + self.cons_aii[i] + size + \
                      self.cons_smo[i] + size + self.cons_bgoo[i] + size + \
                      self.cons_smau[i] + size + self.cons_dot[i] + ' |'
                print line
            print '-' * 76
        except IndexError:
            pass


def setup_anu_translator(unicode_tamil):
    trans = {}
    anu_consdot = u'\xac\u222b\xe1\xce\xe2\u201a\u0131\u203a\xd5[\xa9DF\xcf' \
                  u'u_^\xb5\xc0'
    anu_smhorn = u'\u02dbE\u02dc\xc9\xcb]WM\u220ftl\u02c6\xa7o\xd1as'
    anu_bghorn = u'\u02c7\xca\xe4\u0153\xdfy\xbf\xc3\xa8*XZS\u2039C\u2014T'
    anu_smu = u'z\xe0h|\xd3mO\u2013Ax\u2022\xda\xc6K\u201d\xf8\xb0'
    anu_bguu = u'\xcc\xdb\u2026\u02d8I#\xb1\u02da\xd8JR\u2018G\u0178j\xd2\u2206'

    for x in (unicode_tamil.indep_vowels + unicode_tamil.cons +
                  unicode_tamil.fancy):
        trans[x.uni_value] = x.t1_value

    trans[unicode_tamil.leg.uni_value] = unicode_tamil.leg.t1_value

    for i, x in enumerate(unicode_tamil.cons):
        cons_dot = x.uni_value + unicode_tamil.dot.uni_value
        trans[cons_dot] = anu_consdot[i]

    for i, x in enumerate(unicode_tamil.cons_smhorn):
        trans[x] = anu_smhorn[i]

    for i, x in enumerate(unicode_tamil.cons_bghorn):
        trans[x] = anu_bghorn[i]

    for i, x in enumerate(unicode_tamil.cons_smu):
        trans[x] = anu_smu[i]

    for i, x in enumerate(unicode_tamil.cons_bguu):
        trans[x] = anu_bguu[i]

    for i, x in enumerate(unicode_tamil.cons_sme):
        trans[x] = unicode_tamil.sme.t1_value + unicode_tamil.cons[i].t1_value

    for i, x in enumerate(unicode_tamil.cons_bgee):
        trans[x] = unicode_tamil.bgee.t1_value + unicode_tamil.cons[i].t1_value

    for i, x in enumerate(unicode_tamil.cons_aii):
        trans[x] = unicode_tamil.aii.t1_value + unicode_tamil.cons[i].t1_value

    for i, x in enumerate(unicode_tamil.cons_smo):
        trans[x] = unicode_tamil.sme.t1_value + unicode_tamil.cons[i].t1_value\
                   + unicode_tamil.leg.t1_value

    for i, x in enumerate(unicode_tamil.cons_bgoo):
        trans[x] = unicode_tamil.bgee.t1_value + unicode_tamil.cons[i].t1_value\
                   + unicode_tamil.leg.t1_value

    for i, x in enumerate(unicode_tamil.cons_smau):
        trans[x] = unicode_tamil.sme.t1_value + unicode_tamil.cons[i].t1_value\
                   + unicode_tamil.lla.t1_value
    return trans


def setup_unicode_translator(tamil_translator):
    trans = {v: k for k, v in tamil_translator.items()}
    trans[u'\xc3\x8f'] = _anu_tamil.ra.uni_value + _anu_tamil.dot.uni_value
    return trans


_anu_tamil = Tamil('anu-mac')
_anu_translate = setup_anu_translator(_anu_tamil)
_unicode_translate = setup_unicode_translator(_anu_translate)


def unicode_to_indica(verse):
    verse_lenght = len(verse) - 1
    results = u''
    # print 'Verse = ', verse, 'Lenght = ', verse_lenght
    for i, char in enumerate(verse):
        # print 'char:>>> ', i, char, repr(char)
        if (' ' in char or any(i in char for i in punctuation) or
                any(i in char for i in digits) or
                any(i in char for i in ascii_letters)):
            # print '<<<', char
            results += char
            continue  # Skip to end, avoid further processing
        if i < verse_lenght:
            next_char = verse[i + 1]
            if any(i.uni_value in next_char for i in _anu_tamil.signs):
                signed_char = char + next_char
                # print ">>>", signed_char
                if signed_char in _anu_translate:
                    #print i, _anu_translate[signed_char]
                    results += _anu_translate[signed_char]
            else:
                if char in _anu_translate:
                    #print i, _anu_translate[char]
                    results += _anu_translate[char]
    if results != u'':
        return results


def indica_to_unicode(verse):
    anu_signs = [_anu_tamil.sme.t1_value, _anu_tamil.bgee.t1_value,
                 _anu_tamil.aii.t1_value]
    results = u''
    inner = False
    for i, char in enumerate(verse):
        # print 'char:>>> ', i, char, repr(char)
        if char in _unicode_translate:
            # print '>>>', char
            if i > 0 and verse[i-1] not in anu_signs:
                if i < len(verse)-1:
                    if char == 'V' and verse[i-2] not in anu_signs:
                        # print _char+verse[i-1]
                        new_char = _unicode_translate[verse[i-1]] + \
                                   _unicode_translate['V']
                        # print new_char
                        results += new_char
                    else:
                        results += _unicode_translate[char]
        elif char in "~`{}[]@/\()*+#$%&,.?\"!':; " or char in digits:
            results += char
        elif char in anu_signs:
            if i < len(verse) - 2:
                if verse[i+2] == _anu_tamil.leg.t1_value:
                    new_char = char + verse[i+1] + verse[i+2]
                    # print _unicode_translate[new_char], new_char
                    if new_char in _unicode_translate:
                        results += _unicode_translate[new_char]
                        inner = True
            if i < len(verse) - 1 and not inner:
                new_char = char + verse[i+1]
                # print new_char, _unicode_translate[new_char]
                if new_char in _unicode_translate:
                    results += _unicode_translate[new_char]
            inner = False

    if results:
        tmp = ''
        rem = False
        for i, v in enumerate(results):
            if not rem:
                if i < len(results)-1:
                    if not v == results[i+1]:
                        # print i, 'Yes', v+results[i+1]
                        tmp += v
                    if v in [_anu_tamil.signs[8].uni_value,
                             _anu_tamil.signs[9].uni_value]:
                        rem = True
                else:
                    tmp += v
            else:
                rem = False

        if verse[-1] in "~`{}[]@/\()*+#$%&,.?\"!':; ":
            if tmp[-1] != verse[-1]:
                return tmp + verse[-1]
            else:
                return tmp
        else:
            try:
                return tmp + _unicode_translate[verse[-1]]
            except KeyError:
                pass


def translate_bible_verses(search_results, multi_verse=False):
    if search_results:
        #print search_results
        if multi_verse:
            for i in search_results:
                yield str(i[0]) + ': ' + unicode_to_indica(i[1])
        else:
            yield str(search_results[0]) + ': ' + unicode_to_indica(
                search_results[1])