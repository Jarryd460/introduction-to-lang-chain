from dataclasses import dataclass,field

@dataclass
class SignatureDetails:
    name: str = field(default_factory=str),
    signed: bool = field(default=False),
    position: list[int] = field(default_factory=list),
