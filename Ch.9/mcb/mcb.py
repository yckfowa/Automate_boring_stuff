"""
! python3
-Save and loads pieces of text to the clipboard.

Usage:
 py.exe mcb.pyw save<keyword> - Saves clipboard to keyword.
 py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
 py.exe mcb.pyw list - Loads all keywords to clipboard.
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    #delete method
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()