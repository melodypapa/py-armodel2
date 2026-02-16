"""DataTypePolicyEnum enumeration."""

from enum import Enum


class DataTypePolicyEnum(Enum):
    """AUTOSAR DataTypePolicyEnum enumeration."""

    DDSSERVICE = "ddsService"
    DDSSIGNAL = "ddsSignal"
    LEGACY = "legacy"
    NETWORK = "network"
    REPRESENTATION = "Representation"
    FROMCOMSPEC = "FromComSpec"
    OVERRIDE = "override"
    TRANSFORMINGISIGNAL = "transformingISignal"
