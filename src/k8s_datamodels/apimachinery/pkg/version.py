# generated by datamodel-codegen:
#   filename:  v3
#   timestamp: 2022-07-06T09:40:03+00:00

from __future__ import annotations

from pydantic import BaseModel


class Info(BaseModel):
    buildDate: str
    compiler: str
    gitCommit: str
    gitTreeState: str
    gitVersion: str
    goVersion: str
    major: str
    minor: str
    platform: str
