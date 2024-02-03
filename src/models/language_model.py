from database.db import db
from models.abstract_model import AbstractModel


class LanguageModel(AbstractModel):
    _collection = db["languages"]

    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def to_dict(self) -> dict:
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
        }

    @classmethod
    def list_dicts(cls) -> list:
        return [language.to_dict() for language in cls.find()]
