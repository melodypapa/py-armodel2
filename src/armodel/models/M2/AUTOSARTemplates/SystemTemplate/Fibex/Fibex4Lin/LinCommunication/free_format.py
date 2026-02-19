"""FreeFormat AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 439)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.free_format_entry import (
    FreeFormatEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class FreeFormat(FreeFormatEntry):
    """AUTOSAR FreeFormat."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    byte_values: list[Integer]
    def __init__(self) -> None:
        """Initialize FreeFormat."""
        super().__init__()
        self.byte_values: list[Integer] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "FreeFormat":
        """Deserialize XML element to FreeFormat object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FreeFormat object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse byte_values (list)
        obj.byte_values = []
        for child in ARObject._find_all_child_elements(element, "BYTE-VALUES"):
            byte_values_value = child.text
            obj.byte_values.append(byte_values_value)

        return obj



class FreeFormatBuilder:
    """Builder for FreeFormat."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FreeFormat = FreeFormat()

    def build(self) -> FreeFormat:
        """Build and return FreeFormat object.

        Returns:
            FreeFormat instance
        """
        # TODO: Add validation
        return self._obj
