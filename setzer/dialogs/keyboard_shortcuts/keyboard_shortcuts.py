#!/usr/bin/env python3
# coding: utf-8

# Copyright (C) 2017-present Robert Griesel
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>


import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

import os.path
from setzer.keyboard_shortcuts.keybind_parser import KeybindParser

class KeyboardShortcutsDialog(object):

    def __init__(self, main_window):
        self.main_window = main_window

        data = list()

        def add_item(section, title, action_name, category=None):
            shortcut = KeybindParser.get_shortcut(action_name, category)
            if shortcut:
                shortcut = shortcut.replace('<', '&lt;').replace('>', '&gt;')
                section['items'].append({'title': title, 'shortcut': shortcut})

        section = {'title': _('Documents'), 'items': list()}
        add_item(section, _('Create new document'), 'new-latex-document', 'app')
        add_item(section, _('Open a document'), 'open-document-dialog', 'app')
        add_item(section, _('Show recent documents'), 'shortcut_show_document_chooser', 'app')
        add_item(section, _('Show open documents'), 'shortcut_show_open_docs', 'app')
        add_item(section, _('Switch to the next open document'), 'shortcut_switch_document', 'app')
        add_item(section, _('Save the current document'), 'save', 'app')
        add_item(section, _('Save the document with a new filename'), 'save-as', 'app')
        add_item(section, _('Close the current document'), 'close-active-document', 'app')
        data.append(section)

        section = {'title': _('Tools'), 'items': list()}
        add_item(section, _('Save and build .pdf-file from document'), 'save-and-build', 'app')
        add_item(section, _('Build .pdf-file from document'), 'build', 'app')
        add_item(section, _('Show current position in preview'), 'forward-sync', 'app')
        data.append(section)

        section = {'title': 'Windows and Panels', 'items': list()}
        add_item(section, _('Show help panel'), 'shortcut_help', 'app')
        add_item(section, _('Show build log'), 'shortcut_build_log', 'app')
        add_item(section, _('Show preview panel'), 'shortcut_preview', 'app')
        add_item(section, _('Show global menu'), 'shortcut_show_hamburger', 'app')
        add_item(section, _('Show context menu'), 'show-context-menu', 'document')
        add_item(section, _('Show keyboard shortcuts'), 'show-shortcuts-dialog', 'app')
        add_item(section, _('Close Application'), 'quit', 'app')
        data.append(section)

        section = {'title': _('Find and Replace'), 'items': list()}
        add_item(section, _('Find'), 'start-search', 'app')
        add_item(section, _('Find the next match'), 'find-next', 'app')
        add_item(section, _('Find the previous match'), 'find-previous', 'app')
        add_item(section, _('Find and Replace'), 'start-search-and-replace', 'app')
        data.append(section)

        section = {'title': _('Zoom'), 'items': list()}
        add_item(section, _('Zoom in'), 'zoom-in', 'app')
        add_item(section, _('Zoom out'), 'zoom-out', 'app')
        add_item(section, _('Reset zoom'), 'reset-zoom', 'app')
        data.append(section)

        section = {'title': 'Copy and Paste', 'items': list()}
        add_item(section, _('Copy selected text to clipboard'), 'copy', 'document')
        add_item(section, _('Cut selected text to clipboard'), 'cut', 'document')
        add_item(section, _('Paste text from clipboard'), 'paste', 'document')
        data.append(section)

        section = {'title': _('Undo and Redo'), 'items': list()}
        add_item(section, _('Undo previous text edit'), 'undo', 'document')
        add_item(section, _('Redo previous text edit'), 'redo', 'document')
        data.append(section)

        section = {'title': _('Selection'), 'items': list()}
        add_item(section, _('Select all text'), 'select-all', 'document')
        data.append(section)

        section = {'title': _('Editing'), 'items': list()}
        section['items'].append({'title': _('Toggle insert / overwrite'), 'shortcut': 'Insert'})
        section['items'].append({'title': _('Move current line up'), 'shortcut': '&lt;Alt&gt;Up'})
        section['items'].append({'title': _('Move current line down'), 'shortcut': '&lt;Alt&gt;Down'})
        section['items'].append({'title': _('Move current word left'), 'shortcut': '&lt;Alt&gt;Left'})
        section['items'].append({'title': _('Move current word right'), 'shortcut': '&lt;Alt&gt;Right'})
        section['items'].append({'title': _('Increment number at cursor'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;A'})
        section['items'].append({'title': _('Decrement number at cursor'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;X'})
        data.append(section)

        section = {'title': _('LaTeX Shortcuts'), 'items': list()}
        add_item(section, _('Comment / Uncomment current line(s)'), 'toggle-comment', 'latex')
        add_item(section, _('Quotation Marks'), 'shortcut_quotes', 'latex')
        section['items'].append({'title': _('New Line') + ' (\\\\)', 'shortcut': '&lt;ctrl&gt;Return'})
        section['items'].append({'title': _('Bold Text'), 'shortcut': '&lt;ctrl&gt;B'})
        section['items'].append({'title': _('Italic Text'), 'shortcut': '&lt;ctrl&gt;I'})
        section['items'].append({'title': _('Underlined Text'), 'shortcut': '&lt;ctrl&gt;U'})
        section['items'].append({'title': _('Typewriter Text'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;T'})
        section['items'].append({'title': _('Emphasized Text'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;E'})
        section['items'].append({'title': _('List Item'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;I'})
        section['items'].append({'title': _('Environment'), 'shortcut': '&lt;ctrl&gt;E'})
        data.append(section)

        section = {'title': _('Math Shortcuts'), 'items': list()}
        section['items'].append({'title': _('Inline Math Section'), 'shortcut': '&lt;ctrl&gt;M'})
        section['items'].append({'title': _('Display Math Section'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;M'})
        section['items'].append({'title': _('Equation'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;N'})
        section['items'].append({'title': _('Subscript'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;D'})
        section['items'].append({'title': _('Superscript'), 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;U'})
        section['items'].append({'title': _('Fraction'), 'shortcut': '&lt;alt&gt;&lt;shift&gt;F'})
        section['items'].append({'title': '\\left', 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;L'})
        section['items'].append({'title': '\\right', 'shortcut': '&lt;ctrl&gt;&lt;shift&gt;R'})
        data.append(section)

        self.data = data

    def run(self):
        self.setup()
        self.view.present()

    def setup(self):
        builder_string = '''<?xml version="1.0" encoding="UTF-8"?>
<interface>

  <object class="GtkShortcutsWindow" id="shortcuts-window">
    <property name="modal">1</property>
    <child>
      <object class="GtkShortcutsSection">
        <property name="visible">1</property>
        <property name="section-name">shortcuts</property>
        <property name="max-height">12</property>
'''

        for section in self.data:
            builder_string += '''        <child>
          <object class="GtkShortcutsGroup">
            <property name="visible">1</property>
            <property name="title" translatable="no">''' + section['title'] + '''</property>
'''

            for item in section['items']:
                builder_string += '''            <child>
              <object class="GtkShortcutsShortcut">
                <property name="visible">1</property>
                <property name="accelerator">''' + item['shortcut'] + '''</property>
                <property name="title" translatable="no">''' + item['title'] + '''</property>
              </object>
            </child>
'''

            builder_string += '''          </object>
        </child>
'''

        builder_string += '''      </object>
    </child>
  </object>

</interface>'''

        builder = Gtk.Builder.new_from_string(builder_string, -1)
        self.view = builder.get_object('shortcuts-window')
        self.view.set_transient_for(self.main_window)
        

