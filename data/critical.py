from . import DATABASE, BASE

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.hybrid import hybrid_property
import json


@DATABASE.register('critical_action')
class Action(BASE):
    __tablename__ = "critical"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    data_str = Column(Text)

    def __init__(self, name: str, data: dict):
        super().__init__()
        self.name = name
        self.data_str = json.dumps(data) if data else None

    @hybrid_property
    def data(self) -> dict | None:
        return json.loads(self.data_str) if self.data_str else None
