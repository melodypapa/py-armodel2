"""HwPinConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin import (
    HwPin,
)


class HwPinConnector(Describable):
    """AUTOSAR HwPinConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_pins: list[HwPin]
    def __init__(self) -> None:
        """Initialize HwPinConnector."""
        super().__init__()
        self.hw_pins: list[HwPin] = []

    def serialize(self) -> ET.Element:
        """Serialize HwPinConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwPinConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_pins (list to container "HW-PINS")
        if self.hw_pins:
            wrapper = ET.Element("HW-PINS")
            for item in self.hw_pins:
                serialized = ARObject._serialize_item(item, "HwPin")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwPinConnector":
        """Deserialize XML element to HwPinConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwPinConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwPinConnector, cls).deserialize(element)

        # Parse hw_pins (list from container "HW-PINS")
        obj.hw_pins = []
        container = ARObject._find_child_element(element, "HW-PINS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_pins.append(child_value)

        return obj



class HwPinConnectorBuilder:
    """Builder for HwPinConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwPinConnector = HwPinConnector()

    def build(self) -> HwPinConnector:
        """Build and return HwPinConnector object.

        Returns:
            HwPinConnector instance
        """
        # TODO: Add validation
        return self._obj
