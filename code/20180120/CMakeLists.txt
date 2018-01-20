PROJECT(LawyerMarket)
INCLUDE(UseLATEX.cmake)
ADD_LATEX_DOCUMENT(main.tex
    INPUTS content.tex
    DEFAULT_PDF)
