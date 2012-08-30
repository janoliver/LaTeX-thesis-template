## My LaTeX thesis template

This is the LaTeX template I used for my master thesis. 
I tried to document it nicely and have it compile without any errors or
warnings. The file and folder structure is clean and intuitive.

The setup I compile the thesis with is

    * Arch Linux
    * TexLive 2011.something
    * Latexmk 4.28c

To run/edit the figure examples, you need

    * Python2.7
    * matplotlib and pyplot
    * some vector editing software, like inkscape

Special attention should be paid for __Latexmk__: This is an amazing make-like
perl script with hundreds of options to fully compile latex
documents. Please check it out. In the root folder of my thesis lies a
.latexmkrc file, so that compilation can be done by running 

    latexmk

and NOTHING else!

# File and folder structure

Now to the file and folder structure: 

* __preamble/__
  Everything that makes the preamble
  goes into the folder named "preamble". You will find the following
  files there: 

    * __docclass.tex__
      This file contains the document class and all of it's options. Some
      basic packages are also included here, like the content encoding
      and the language, and packages that do geometrical stuff like
      margins of the document and so on. 

    * __packages.tex__
      This file includes all external packages that introduce new
      functionality or replace existing functionality. In general, I use
      packages only if they are really needed, to keep everything as
      simple as possible. Every packages is justified in the preceding
      comment. There may be packages that can be removed when the thesis
      is done, like the blindtext package. These serve the purpose of
      having content in this template and are marked as removable in the
      comments. 

    * __commands.tex__
      This file contains custom commands that are not important enough
      for their own .sty file. All commands are described in great
      detail. (At least I hope that I stick to it. :-) )

    * __settings.tex__
      I chose to separate some KOMA related settings from the package
      inclusion. This file contains customized stuff.

* __bibliography/__
  This folder contains the bib file and additional non-tex files that are
  needed for the bibliography. A custom bib style would go here as well.

    * __bibliography.bib__
      The file with all the references defined. 

* __sources/__
  In this folder, I gathered all the sources (plotting scripts, svg files)
  for figures and so on. It contains two files:

    * __plots/__
    A folder where all my plots go into

    * __exmample.py__
      An example pyplot script that generates
      ../../content/figures/example.pdf

    * __matplotlibrc__
      Some settings, all matplotlib scripts share.

* __molecule.svg__
  The svg source file of my molecule figure
        
* __content/__
  Here comes all the content (text and figures, mainly)

    * __figures/__
      All figures should go in this folder. 

    * __introduction.tex, elements.tex, somecontent.tex__
      The actual content is in these. Name those wisely so you don't lose
      the overview, when this folder grows.

* __pages/__
  Pages that can not really be described as content go here, like the
  frontpage, appendix, table of contents, etc.

    *  __appendix.tex__
       The appendix of the thesis

    * __bibliography.tex__
      The references page.

    * __frontpage.tex__
      The front (title) page of the thesis. Note that in this template I
      use some kind of simple place holder.

    * __acknowledgements.tex__
      The Acknowledgements

    * __tableofcontents.tex__
      The table of contents page. 

* __thesis.tex__
  The main tex file. It glues together all the external files and should
  be the one that is compiled  (latexmk takes care of that!)

* __.latexmkrc__
  The latexmk configuration file.

* __.gitignore__
  The stuff that should be ignored by git.

* __README.md__
  this file
    
