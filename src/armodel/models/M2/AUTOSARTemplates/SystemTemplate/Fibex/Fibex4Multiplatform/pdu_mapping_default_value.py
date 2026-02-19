"""PduMappingDefaultValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.default_value_element import (
    DefaultValueElement,
)


class PduMappingDefaultValue(ARObject):
    """AUTOSAR PduMappingDefaultValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_values: list[DefaultValueElement]
    def __init__(self) -> None:
        """Initialize PduMappingDefaultValue."""
        super().__init__()
        self.default_values: list[DefaultValueElement] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduMappingDefaultValue":
        """Deserialize XML element to PduMappingDefaultValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduMappingDefaultValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse default_values (list)
        obj.default_values = []
        for child in ARObject._find_all_child_elements(element, "DEFAULT-VALUES"):
            default_values_value = ARObject._deserialize_by_tag(child, "DefaultValueElement")
            obj.default_values.append(default_values_value)

        return obj



class PduMappingDefaultValueBuilder:
    """Builder for PduMappingDefaultValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PduMappingDefaultValue = PduMappingDefaultValue()

    def build(self) -> PduMappingDefaultValue:
        """Build and return PduMappingDefaultValue object.

        Returns:
            PduMappingDefaultValue instance
        """
        # TODO: Add validation
        return self._obj
