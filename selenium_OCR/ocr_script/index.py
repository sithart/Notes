# import the necessary packages
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import cv2
import os


import cv2
import pytesseract
from pytesseract import Output
import pandas as pd

class Ocrtodata:

    def __init__(self):
	       self.filename ='../packing-slip.png'

    def method_1():
        img = cv2.imread("../packing-slip.png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        custom_config = r'-l eng --oem 1 --psm 6 '
        d = pytesseract.image_to_data(thresh, config=custom_config, output_type=Output.DICT)
        df = pd.DataFrame(d)

        df1 = df[(df.conf != '-1') & (df.text != ' ') & (df.text != '')]
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)

        sorted_blocks = df1.groupby('block_num').first().sort_values('top').index.tolist()
        for block in sorted_blocks:
            curr = df1[df1['block_num'] == block]
            sel = curr[curr.text.str.len() > 3]
            # sel = curr
            char_w = (sel.width / sel.text.str.len()).mean()
            prev_par, prev_line, prev_left = 0, 0, 0
            text = ''
            for ix, ln in curr.iterrows():
                # add new line when necessary
                if prev_par != ln['par_num']:
                    text += '\n'
                    prev_par = ln['par_num']
                    prev_line = ln['line_num']
                    prev_left = 0
                elif prev_line != ln['line_num']:
                    text += '\n'
                    prev_line = ln['line_num']
                    prev_left = 0

                added = 0  # num of spaces that should be added
                if ln['left'] / char_w > prev_left + 1:
                    added = int((ln['left']) / char_w) - prev_left
                    text += ' ' * added
                text += ln['text'] + ' '
                prev_left += len(ln['text']) + added + 1
            text += '\n'
            print(text)

    def method_2(self):
        text = pytesseract.image_to_string(Image.open(self.filename),lang='eng')
        return text


if __name__ == '__main__':
    # x = Ocrtodata()
    # print(x.method_2())
    
