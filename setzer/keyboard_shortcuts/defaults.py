#!/usr/bin/env python3
# coding: utf-8

DEFAULT_KEYBINDS = {
    'app': {
        '<Control>n': 'new-latex-document',
        '<Control>o': 'open-document-dialog',
        '<Control>s': 'save',
        '<Control><Shift>s': 'save-as',
        '<Control>w': 'close-active-document',
        '<Control>q': 'quit',
        '<Control>question': 'show-shortcuts-dialog',
        '<Control>p': 'shortcut_show_open_docs',
        '<Control>Tab': 'shortcut_switch_document',
        '<Control><Shift>p': 'shortcut_show_document_chooser',
        '<Control>plus': 'zoom-in',
        '<Control>minus': 'zoom-out',
        '<Control>0': 'reset-zoom',
        '<Control>f': 'start-search',
        '<Control>h': 'start-search-and-replace',
        'F3': 'find-next',
        '<Shift>F3': 'find-previous',
        'F1': 'shortcut_help',
        'F2': 'shortcut_document_structure_toggle',
        '<Control><Alt>b': 'save-and-build',
        'F6': 'build',
        '<Control><Alt>j': 'forward-sync',
        'F8': 'shortcut_build_log',
        '<Control><Alt>v': 'shortcut_preview',
        'F10': 'shortcut_show_hamburger'
    },
    'document': {
        '<Control>x': 'cut',
        '<Control>c': 'copy',
        '<Control>v': 'paste',
        '<Control>a': 'select-all',
        '<Control>z': 'undo',
        '<Control><Shift>z': 'redo',
        '<Control>y': 'redo',
        'F12': 'show-context-menu'
    },
    'latex': {
        '<Control>slash': 'toggle-comment',
        '<Control>quotedbl': 'shortcut_quotes'
    }
}
