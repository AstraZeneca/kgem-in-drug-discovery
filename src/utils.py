# -*- coding: utf-8 -*-

import yaml


def load_config(config_path: str) -> dict:

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config
