"""HwElementConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 21)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_connector import (
    HwPinConnector,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group_connector import (
    HwPinGroupConnector,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
        HwElement,
    )



class HwElementConnector(Describable):
    """AUTOSAR HwElementConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_element_refs: list[ARRef]
    hw_pins: list[HwPinConnector]
    hw_pin_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize HwElementConnector."""
        super().__init__()
        self.hw_element_refs: list[ARRef] = []
        self.hw_pins: list[HwPinConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize HwElementConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwElementConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_element_refs (list to container "HW-ELEMENT-REFS")
        if self.hw_element_refs:
            wrapper = ET.Element("HW-ELEMENT-REFS")
            for item in self.hw_element_refs:
                serialized = SerializationHelper.serialize_item(item, "HwElement")
                if serialized is not None:
                    child_elem = ET.Element("HW-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pins (list to container "HW-PINS")
        if self.hw_pins:
            wrapper = ET.Element("HW-PINS")
            for item in self.hw_pins:
                serialized = SerializationHelper.serialize_item(item, "HwPinConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pin_group_refs (list to container "HW-PIN-GROUP-REFS")
        if self.hw_pin_group_refs:
            wrapper = ET.Element("HW-PIN-GROUP-REFS")
            for item in self.hw_pin_group_refs:
                serialized = SerializationHelper.serialize_item(item, "HwPinGroupConnector")
                if serialized is not None:
                    child_elem = ET.Element("HW-PIN-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElementConnector":
        """Deserialize XML element to HwElementConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwElementConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwElementConnector, cls).deserialize(element)

        # Parse hw_element_refs (list from container "HW-ELEMENT-REFS")
        obj.hw_element_refs = []
        container = SerializationHelper.find_child_element(element, "HW-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_element_refs.append(child_value)

        # Parse hw_pins (list from container "HW-PINS")
        obj.hw_pins = []
        container = SerializationHelper.find_child_element(element, "HW-PINS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_pins.append(child_value)

        # Parse hw_pin_group_refs (list from container "HW-PIN-GROUP-REFS")
        obj.hw_pin_group_refs = []
        container = SerializationHelper.find_child_element(element, "HW-PIN-GROUP-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_pin_group_refs.append(child_value)

        return obj



class HwElementConnectorBuilder:
    """Builder for HwElementConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElementConnector = HwElementConnector()

    def build(self) -> HwElementConnector:
        """Build and return HwElementConnector object.

        Returns:
            HwElementConnector instance
        """
        # TODO: Add validation
        return self._obj
