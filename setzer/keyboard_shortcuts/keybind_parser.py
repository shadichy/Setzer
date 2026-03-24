#!/usr/bin/env python3
# coding: utf-8

import json
import os
from setzer.app.service_locator import ServiceLocator
from setzer.keyboard_shortcuts.defaults import DEFAULT_KEYBINDS

class KeybindParser:
    _keybinds = None

    @classmethod
    def load_keybinds(cls):
        if cls._keybinds is not None:
            return
            
        # Initialize with a deep copy of defaults
        cls._keybinds = {cat: dict(binds) for cat, binds in DEFAULT_KEYBINDS.items()}
        
        config_path = ServiceLocator.get_keymap_config_path()
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if 'keybinds' in data and isinstance(data['keybinds'], dict):
                        # Merge config into defaults
                        for category, binds in data['keybinds'].items():
                            if category in cls._keybinds and isinstance(binds, dict):
                                cls._keybinds[category].update(binds)
            except Exception as e:
                print(f"Failed to load keybinds from config file {config_path}: {e}")

    @classmethod
    def get_category_keybinds(cls, category):
        cls.load_keybinds()
        return cls._keybinds.get(category, {})

    @classmethod
    def get_shortcut(cls, action_name, category=None):
        """
        Reverse lookup: find the shortcut for a given action name in a category.
        If category is None, search all categories.
        """
        cls.load_keybinds()
        if category:
            categories = [category]
        else:
            categories = cls._keybinds.keys()
            
        for cat in categories:
            for shortcut, action in cls._keybinds[cat].items():
                if action == action_name:
                    return shortcut
        return None
