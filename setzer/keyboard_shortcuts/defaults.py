#!/usr/bin/env python3
# coding: utf-8

# Note: For non-literal characters, use their descriptive names.
# This is required for correct parsing by the GTK shortcut system.
#
# | Character | Name       |
# | --------- | ---------- |
# | ?         | question   |
# | /         | slash      |
# | +         | plus       |
# | -         | minus      |
# | "         | quotedbl   |
# | Tab       | Tab        |
# | Return    | Return     |
# | Escape    | Escape     |
# | Space     | space      |

DEFAULT_KEYBINDS = {
    'app': {
        'new-latex-document': ['Ctrl', 'N'],
        'open-document-dialog': ['Ctrl', 'O'],
        'save': ['Ctrl', 'S'],
        'save-as': ['Ctrl', 'Shift', 'S'],
        'close-active-document': ['Ctrl', 'W'],
        'quit': ['Ctrl', 'Q'],
        'show-shortcuts-dialog': ['Ctrl', 'question'],
        'shortcut_show_open_docs': ['Ctrl', 'P'],
        'shortcut_switch_document': ['Ctrl', 'Tab'],
        'shortcut_show_document_chooser': ['Ctrl', 'Shift', 'P'],
        'zoom-in': ['Ctrl', 'plus'],
        'zoom-out': ['Ctrl', 'minus'],
        'reset-zoom': ['Ctrl', '0'],
        'start-search': ['Ctrl', 'F'],
        'start-search-and-replace': ['Ctrl', 'H'],
        'find-next': ['F3'],
        'find-previous': ['Shift', 'F3'],
        'shortcut_help': ['F1'],
        'shortcut_document_structure_toggle': ['F2'],
        'save-and-build': ['Ctrl', 'Alt', 'B'],
        'build': ['F6'],
        'forward-sync': ['Ctrl', 'Alt', 'J'],
        'shortcut_build_log': ['F8'],
        'shortcut_preview': ['Ctrl', 'Alt', 'V'],
        'shortcut_show_hamburger': ['F10']
    },
    'document': {
        'cut': ['Ctrl', 'X'],
        'copy': ['Ctrl', 'C'],
        'paste': ['Ctrl', 'V'],
        'select-all': ['Ctrl', 'A'],
        'undo': ['Ctrl', 'Z'],
        'redo': ['Ctrl', 'Shift', 'Z'],
        'redo_alt': ['Ctrl', 'Y'],
        'show-context-menu': ['F12']
    },
    'latex': {
        'toggle-comment': ['Ctrl', 'slash'],
        'shortcut_quotes': ['Ctrl', 'quotedbl']
    }
}
