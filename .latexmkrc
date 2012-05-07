# latexmkrc file for the master thesis template

# always process the following tex files
@default_files = ("thesis.tex");

# I use pdflatex.
$pdf_mode = 1;

$pdflatex = 'xelatex --shell-escape %O %S';