#!/usr/bin/env python3

import sys

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables.E_B_D_T_ import table_E_B_D_T_
from fontTools.ttLib.tables.E_B_L_C_ import table_E_B_L_C_

# Need at least 2 input files and 1 output
if len(sys.argv) < 4:
    print("usage: combine.py input1.ttf input2.ttf [input3.ttf ... ] out.ttf")
    sys.exit(1)

fonts = []

for index in range(1, len(sys.argv) - 1):
    fonts.append(TTFont(sys.argv[index], lazy=False))
    if fonts[0].getGlyphOrder() != fonts[-1].getGlyphOrder():
        glyphs1 = fonts[0].getGlyphOrder()
        glyphs2 = fonts[-1].getGlyphOrder()

        missing = [glyph for glyph in glyphs1 if glyph not in glyphs2]
        extra = [glyph for glyph in glyphs2 if glyph not in glyphs1]
        print("all fonts must have the same glyph order!")
        print("missing from {}:".format(sys.argv[index]))
        print(missing)
        print("extra from {}:".format(sys.argv[index]))
        print(extra)
        sys.exit(1)

out_font = TTFont()
out_font.setGlyphOrder(fonts[0].getGlyphOrder())

# Most tables are just copied from the first input file
# TODO: em values and PPEM will vary, does this matter?
for tag in ("head", "hhea", "maxp", "OS/2", "hmtx", "cmap", "name", "post"):
    out_font[tag] = fonts[0][tag]

out_font["EBLC"] = eblc = table_E_B_L_C_()
out_font["EBDT"] = ebdt = table_E_B_D_T_()

eblc.version = fonts[0]["EBLC"].version
ebdt.version = fonts[0]["EBDT"].version

eblc.strikes = []
ebdt.strikeData = []

for font in fonts:
    eblc.strikes.extend(font["EBLC"].strikes)
    ebdt.strikeData.extend(font["EBDT"].strikeData)

out_font.save(sys.argv[-1])
