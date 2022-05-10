# -*- coding: utf-8 -*-

"""
Provides util functions
"""

import yaml


def load_config(config_path: str) -> dict:
    """Load a YAML config file"""

    with open(config_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    return config
