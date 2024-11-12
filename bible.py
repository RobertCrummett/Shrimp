# Reformat bible text file into bible tex file
# KJV text download: https://openbible.com/textfiles/kjv.txt
import datetime
import urllib.request
import sys

bible_text_url = "https://openbible.com/textfiles/kjv.txt"
bible_text_path = "kjv.txt"

try:
    urllib.request.urlretrieve(bible_text_url, bible_text_path)
    print(f"Successfully downloaded {bible_text_url} to {bible_text_path}")
except Exception as e:
    print(f"Failed to download {bible_text_url}: {e}")
    sys.exit(1)

bible_tex_path = "bible.tex"
header_lines = 2

with open(bible_text_path) as file:
    bible_text = file.readlines()

bible_text = bible_text[header_lines:]

number_to_word = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    21: "TwentyOne",
    22: "TwentyTwo",
    23: "TwentyThree",
    24: "TwentyFour",
    25: "TwentyFive",
    26: "TwentySix",
    27: "TwentySeven",
    28: "TwentyEight",
    29: "TwentyNine",
    30: "Thirty",
    31: "ThirtyOne",
    32: "ThirtyTwo",
    33: "ThirtyThree",
    34: "ThirtyFour",
    35: "ThirtyFive",
    36: "ThirtySix",
    37: "ThirtySeven",
    38: "ThirtyEight",
    39: "ThirtyNine",
    40: "Forty",
    41: "FortyOne",
    42: "FortyTwo",
    43: "FortyThree",
    44: "FortyFour",
    45: "FortyFive",
    46: "FortySix",
    47: "FortySeven",
    48: "FortyEight",
    49: "FortyNine",
    50: "Fifty",
    51: "FiftyOne",
    52: "FiftyTwo",
    53: "FiftyThree",
    54: "FiftyFour",
    55: "FiftyFive",
    56: "FiftySix",
    57: "FiftySeven",
    58: "FiftyEight",
    59: "FiftyNine",
    60: "Sixty",
    61: "SixtyOne",
    62: "SixtyTwo",
    63: "SixtyThree",
    64: "SixtyFour",
    65: "SixtyFive",
    66: "SixtySix",
    67: "SixtySeven",
    68: "SixtyEight",
    69: "SixtyNine",
    70: "Seventy",
    71: "SeventyOne",
    72: "SeventyTwo",
    73: "SeventyThree",
    74: "SeventyFour",
    75: "SeventyFive",
    76: "SeventySix",
    77: "SeventySeven",
    78: "SeventyEight",
    79: "SeventyNine",
    80: "Eighty",
    81: "EightyOne",
    82: "EightyTwo",
    83: "EightyThree",
    84: "EightyFour",
    85: "EightyFive",
    86: "EightySix",
    87: "EightySeven",
    88: "EightyEight",
    89: "EightyNine",
    90: "Ninety",
    91: "NinetyOne",
    92: "NinetyTwo",
    93: "NinetyThree",
    94: "NinetyFour",
    95: "NinetyFive",
    96: "NinetySix",
    97: "NinetySeven",
    98: "NinetyEight",
    99: "NinetyNine",
    100: "OneHundred",
    101: "OneHundredOne",
    102: "OneHundredTwo",
    103: "OneHundredThree",
    104: "OneHundredFour",
    105: "OneHundredFive",
    106: "OneHundredSix",
    107: "OneHundredSeven",
    108: "OneHundredEight",
    109: "OneHundredNine",
    110: "OneHundredTen",
    111: "OneHundredEleven",
    112: "OneHundredTwelve",
    113: "OneHundredThirteen",
    114: "OneHundredFourteen",
    115: "OneHundredFifteen",
    116: "OneHundredSixteen",
    117: "OneHundredSeventeen",
    118: "OneHundredEighteen",
    119: "OneHundredNineteen",
    120: "OneHundredTwenty",
    121: "OneHundredTwentyOne",
    122: "OneHundredTwentyTwo",
    123: "OneHundredTwentyThree",
    124: "OneHundredTwentyFour",
    125: "OneHundredTwentyFive",
    126: "OneHundredTwentySix",
    127: "OneHundredTwentySeven",
    128: "OneHundredTwentyEight",
    129: "OneHundredTwentyNine",
    130: "OneHundredThirty",
    131: "OneHundredThirtyOne",
    132: "OneHundredThirtyTwo",
    133: "OneHundredThirtyThree",
    134: "OneHundredThirtyFour",
    135: "OneHundredThirtyFive",
    136: "OneHundredThirtySix",
    137: "OneHundredThirtySeven",
    138: "OneHundredThirtyEight",
    139: "OneHundredThirtyNine",
    140: "OneHundredForty",
    141: "OneHundredFortyOne",
    142: "OneHundredFortyTwo",
    143: "OneHundredFortyThree",
    144: "OneHundredFortyFour",
    145: "OneHundredFortyFive",
    146: "OneHundredFortySix",
    147: "OneHundredFortySeven",
    148: "OneHundredFortyEight",
    149: "OneHundredFortyNine",
    150: "OneHundredFifty",
    151: "OneHundredFiftyOne",
    152: "OneHundredFiftyTwo",
    153: "OneHundredFiftyThree",
    154: "OneHundredFiftyFour",
    155: "OneHundredFiftyFive",
    156: "OneHundredFiftySix",
    157: "OneHundredFiftySeven",
    158: "OneHundredFiftyEight",
    159: "OneHundredFiftyNine",
    160: "OneHundredSixty",
    161: "OneHundredSixtyOne",
    162: "OneHundredSixtyTwo",
    163: "OneHundredSixtyThree",
    164: "OneHundredSixtyFour",
    165: "OneHundredSixtyFive",
    166: "OneHundredSixtySix",
    167: "OneHundredSixtySeven",
    168: "OneHundredSixtyEight",
    169: "OneHundredSixtyNine",
    170: "OneHundredSeventy",
    171: "OneHundredSeventyOne",
    172: "OneHundredSeventyTwo",
    173: "OneHundredSeventyThree",
    174: "OneHundredSeventyFour",
    175: "OneHundredSeventyFive",
    176: "OneHundredSeventySix",
}


with open(bible_tex_path, "w") as tex:

    tex.write("% --------------------------\n")
    tex.write("%     KJV bible verses\n")
    tex.write("%\n")
    tex.write("% Source: https://openbible.com/textfiles/kjv.txt\n")
    tex.write(f"% Written: {datetime.date.today()}\n")
    tex.write("% --------------------------\n\n")

    tex.write("\\newcommand{\\numberToWord}[1]{%\n")
    for key, value in number_to_word.items():
        tex.write("\t\\ifnum#1=" + str(key) + " " + value + "\\fi\n")
    tex.write("}\n\n")

    books = []

    for verse in bible_text:

        book_chapter, verse_text = verse.split(":", 1)
    
        book, chapter = book_chapter.rsplit(" ", 1)
        verse, text = verse_text.split("\t", 1)

        book = book.replace("1", "First")
        book = book.replace("2", "Second")
        book = book.replace("3", "Third")

        book = book.title().replace(" ", "")
        if not book in books:
            books.append(book)
        chapter = number_to_word[int(chapter)]
        verse = number_to_word[int(verse)]
        text = text.replace("\n", "")
    
        # Add italics
        text = text.replace("[", "\\textit{")
        text = text.replace("]", "}")

        # Add tetragrammaton
        text = text.replace("LORD'S", "\\textsc{Lord's}")
        text = text.replace("LORDS", "\\textsc{Lords}")
        text = text.replace("LORD", "\\textsc{Lord}")

        bookchapterverse = book + chapter + verse
        tex.write("\\newcommand{\\Bible" + \
                bookchapterverse + "}{" + text + "}\n")
    
    tex.write("\n")
    for book in books:
        tex.write("\\newcommand{\\" + book + "}[2]{%\n")
        tex.write("\t\\csname Bible" + book + \
                "\\numberToWord{#1}\\numberToWord{#2}\\endcsname%\n")
        tex.write("}\n\n")
        

