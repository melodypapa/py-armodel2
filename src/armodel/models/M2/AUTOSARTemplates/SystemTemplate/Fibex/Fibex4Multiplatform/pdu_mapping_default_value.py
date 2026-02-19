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
    def serialize(self) -> ET.Element:
        """Serialize PduMappingDefaultValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize default_values (list to container "DEFAULT-VALUES")
        if self.default_values:
            wrapper = ET.Element("DEFAULT-VALUES")
            for item in self.default_values:
                serialized = ARObject._serialize_item(item, "DefaultValueElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

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

        # Parse default_values (list from container "DEFAULT-VALUES")
        obj.default_values = []
        container = ARObject._find_child_element(element, "DEFAULT-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.default_values.append(child_value)

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
