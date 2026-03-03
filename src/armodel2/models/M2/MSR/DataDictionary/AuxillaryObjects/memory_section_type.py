"""AUTOSAR MemorySectionType enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 146)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 417)

JSON Source: packages/M2_MSR_DataDictionary_AuxillaryObjects.enums.json"""

from __future__ import annotations
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class MemorySectionType(AREnum):
    """AUTOSAR MemorySectionType enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    CALIBRATION_VARIABLES = "CALIBRATION-VARIABLES"
    CALPRM = "CALPRM"
    CODE = "CODE"
    CONFIG_DATA = "CONFIG-DATA"
    CONST = "CONST"
    EXCLUDE_FROM_FLASH = "EXCLUDE-FROM-FLASH"
    VAR = "VAR"

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MemorySectionType":
        """Deserialize XML element to MemorySectionType.

        Note: Validation is skipped for this enum to support
        legacy values not in the current AUTOSAR specification.
        Decorator: skip_validation

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MemorySectionType instance

        Raises:
            ValueError: If element is empty
        """
        if element.text:
            text = element.text.strip()
            # Use object.__new__ to bypass Enum validation
            obj = object.__new__(cls)
            obj._value_ = text
            return obj
        raise ValueError(f"Cannot deserialize {cls.__name__} from empty element")
