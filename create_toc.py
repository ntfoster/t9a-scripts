#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    # Please do not use 'from scribus import *' . If you must use a 'from import',
    # Do so _after_ the 'import scribus' and only import the names you need, such
    # as commonly used constants.
    import scribus
except ImportError as err:
    print("This Python script is written for the Scribus scripting interface.")
    print("It can only be run from within Scribus.")
    sys.exit(1)

#########################
# YOUR IMPORTS GO HERE  #
#########################
from t9a.sla import LABfile

def set_toc_frame(frame,headers,style):
    text = ""
    for entry in headers:
        line = f'{entry["text"]}\t{entry["page"]}\n'
        text += line
    scribus.setText(text,frame)
    try:
        scribus.setParagraphStyle(style,frame)
    except scribus.NotFoundError:
        scribus.setParagraphStyle("TOC level 1", frame)

def main(argv):
    lab = LABfile(scribus.getDocName())
    
    background_headers = lab.parse_headers(["HEADER Level 1","HEADER Level 2"])
    set_toc_frame("TOC_Background",background_headers,"TOC1")

    rules_headers = lab.parse_headers(["HEADER Rules"])
    set_toc_frame("TOC_Rules",rules_headers,"TOC Rules")

def main_wrapper(argv):
    """The main_wrapper() function disables redrawing, sets a sensible generic
    status bar message, and optionally sets up the progress bar. It then runs
    the main() function. Once everything finishes it cleans up after the main()
    function, making sure everything is sane before the script terminates."""
    try:
        scribus.statusMessage("Running script...")
        scribus.progressReset()
        main(argv)
    finally:
        # Exit neatly even if the script terminated with an exception,
        # so we leave the progress bar and status bar blank and make sure
        # drawing is enabled.
        if scribus.haveDoc():
            scribus.setRedraw(True)
        scribus.statusMessage("")
        scribus.progressReset()

# This code detects if the script is being run as a script, or imported as a module.
# It only runs main() if being run as a script. This permits you to import your script
# and control it manually for debugging.
if __name__ == '__main__':
    main_wrapper(sys.argv)
