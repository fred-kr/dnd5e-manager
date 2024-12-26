import enum

import requests

from .app_config import Config


class DBInterface:
    _base_url = Config.database.base_url
    _headers = {"Accept": "application/json"}

    class Endpoint(enum.Enum):
        ABILITY_SCORES = "/ability-scores"
        ALIGNMENTS = "/alignments"
        BACKGROUNDS = "/backgrounds"
        CLASSES = "/classes"
        CONDITIONS = "/conditions"
        DAMAGE_TYPES = "/damage-types"
        EQUIPMENT = "/equipment"
        EQUIPMENT_CATEGORIES = "/equipment-categories"
        FEATS = "/feats"
        FEATURES = "/features"
        LANGUAGES = "/languages"
        MAGIC_ITEMS = "/magic-items"
        MAGIC_SCHOOLS = "/magic-schools"
        MONSTERS = "/monsters"
        PROFICIENCIES = "/proficiencies"
        RACES = "/races"
        RULE_SECTIONS = "/rule-sections"
        RULES = "/rules"
        SKILLS = "/skills"
        SPELLS = "/spells"
        SUBCLASSES = "/subclasses"
        SUBRACES = "/subraces"
        TRAITS = "/traits"
        WEAPON_PROPERTIES = "/weapon-properties"

        @property
        def url(self) -> str:
            return f"{DBInterface._base_url}{self.value}"

    def all_resources(self) -> dict[str, str]:
        return self.get(self._base_url)

    def all_endpoint_resources(self, endpoint: Endpoint) -> dict[str, str]:
        return self.get(endpoint.url)

    def get(self, url: str) -> dict[str, str]:
        payload: dict[str, str] = {}
        response = requests.request("GET", url, headers=self._headers, data=payload)

        return response.json()
