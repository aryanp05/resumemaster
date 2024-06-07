from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Dictionary of font names and their paths
font_path_dict = {
    'Garamond': "fonts/garamond.ttf",
    'Garamond Bold': "fonts/garamond-bold.ttf",
    'Garamond Italics': "fonts/garamond-italics.ttf"
}

def calculate_num_of_space(font_name, font_size, text1, text2, lm, rm):
    # Load the font
    if font_name not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(TTFont(font_name, font_path_dict[font_name]))

    # Calculate text width
    width1 = pdfmetrics.stringWidth(text1, font_name, font_size)
    width2 = pdfmetrics.stringWidth(text2, font_name, font_size)
    width3 = pdfmetrics.stringWidth(" ", font_name, font_size)
    
    # Calculate the number of spaces needed
    available_space = 72 * (8.5 - lm - rm)  # 72 points per inch, letter size is 8.5 inches wide
    diff = available_space - width1 - width2
    num_of_space = " " * int(diff / width3)
    
    return num_of_space