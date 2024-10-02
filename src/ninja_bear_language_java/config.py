from typing import Type

from .generator import Generator
from ninja_bear import LanguageConfigBase


class Config(LanguageConfigBase):
    """
    Java specific config. For more information about the config methods, refer to LanguageConfigBase.
    """

    def _file_extension(self) -> str:
        return 'java'

    def _generator_type(self) -> Type[Generator]:
        return Generator

    def _allowed_file_name_pattern(self) -> str:
        return fr'^{self.generator.get_type_name()}$'
