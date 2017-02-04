# -*- coding: utf-8 -*-

import os
from configparser import ConfigParser

_directory_path = os.path.abspath(os.path.dirname(__file__))
_conf_path = "{0}/../settings.conf".format(_directory_path)


def _load_conf_file(conf_file_path) -> ConfigParser:
    config = ConfigParser()
    config.read(conf_file_path, encoding='utf-8')
    return config


class Settings(object):
    """環境依存の設定を保持するクラス"""

    _line = "line"

    def __init__(self):
        self.config_parser = _load_conf_file(_conf_path)

    def get_line_conf(self):
        return {
            'Secret':self.config_parser.get(Settings._line, "Secret"),
            'Token':self.config_parser.get(Settings._line, "Token"),
        }


settings = Settings()
