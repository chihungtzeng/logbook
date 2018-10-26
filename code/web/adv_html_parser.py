# -*- coding: utf-8 -*-
import os
import AdvancedHTMLParser


def __get_html_file():
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(cur_dir, "data", "motor.html")


def main():
    parser = AdvancedHTMLParser.AdvancedHTMLParser()
    parser.parseFile(__get_html_file())
    cl_hotrank = parser.getElementById("cl-hotrank")

    for pdset in cl_hotrank.getElementsByClassName("pdset"):
        item_text_tag = pdset.getElementsByClassName("text")[0]
        print(item_text_tag.textContent, end=" ")
        price_tag = pdset.getElementsByClassName("red-price")[0]
        print(price_tag.textContent)

if __name__ == "__main__":
    main()
