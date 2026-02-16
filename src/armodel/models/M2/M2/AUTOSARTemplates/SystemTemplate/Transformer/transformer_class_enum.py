"""TransformerClassEnum enumeration."""

from enum import Enum


class TransformerClassEnum(Enum):
    """AUTOSAR TransformerClassEnum enumeration."""

    CUSTOM = "custom"
    SAFETY = "safety"
    SECURITY = "security"
    SERIALIZER = "serializer"
