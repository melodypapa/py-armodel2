"""DataTransformationKindEnum enumeration."""

from enum import Enum


class DataTransformationKindEnum(Enum):
    """AUTOSAR DataTransformationKindEnum enumeration."""

    ASYMMETRICFROM = "asymmetricFrom"
    ASYMMETRICTOBYTEARRAY = "asymmetricToByteArray"
    SYMMETRIC = "symmetric"
