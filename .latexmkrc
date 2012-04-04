# latexmkrc file for the master thesis template

# always process the following tex files
@default_files = ("thesis.tex");

# we use latex, not pdflatex, since postscript is a more open format and we
# want everything to be truly open source.
$pdf_mode = 1;

