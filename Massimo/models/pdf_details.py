from dataclasses import dataclass,field

from .signature_details import SignatureDetails

@dataclass
class PdfDetails:
    content: list[str] = field(default_factory=list)
    signature_details: list[SignatureDetails] = field(default_factory=list)
