"""HwElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 296)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 18)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 991)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2026)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_EcuResourceTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_pin_group import (
    HwPinGroup,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element_connector import (
        HwElementConnector,
    )



class HwElement(HwDescriptionEntity):
    """AUTOSAR HwElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hw_elements: list[HwElementConnector]
    hw_pin_group_refs: list[ARRef]
    nested_elements: list[HwElement]
    def __init__(self) -> None:
        """Initialize HwElement."""
        super().__init__()
        self.hw_elements: list[HwElementConnector] = []
        self.hw_pin_group_refs: list[ARRef] = []
        self.nested_elements: list[HwElement] = []
    def serialize(self) -> ET.Element:
        """Serialize HwElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(HwElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hw_elements (list to container "HW-ELEMENTS")
        if self.hw_elements:
            wrapper = ET.Element("HW-ELEMENTS")
            for item in self.hw_elements:
                serialized = ARObject._serialize_item(item, "HwElementConnector")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_pin_group_refs (list to container "HW-PIN-GROUPS")
        if self.hw_pin_group_refs:
            wrapper = ET.Element("HW-PIN-GROUPS")
            for item in self.hw_pin_group_refs:
                serialized = ARObject._serialize_item(item, "HwPinGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nested_elements (list to container "NESTED-ELEMENTS")
        if self.nested_elements:
            wrapper = ET.Element("NESTED-ELEMENTS")
            for item in self.nested_elements:
                serialized = ARObject._serialize_item(item, "HwElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "HwElement":
        """Deserialize XML element to HwElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized HwElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(HwElement, cls).deserialize(element)

        # Parse hw_elements (list from container "HW-ELEMENTS")
        obj.hw_elements = []
        container = ARObject._find_child_element(element, "HW-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_elements.append(child_value)

        # Parse hw_pin_group_refs (list from container "HW-PIN-GROUPS")
        obj.hw_pin_group_refs = []
        container = ARObject._find_child_element(element, "HW-PIN-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hw_pin_group_refs.append(child_value)

        # Parse nested_elements (list from container "NESTED-ELEMENTS")
        obj.nested_elements = []
        container = ARObject._find_child_element(element, "NESTED-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nested_elements.append(child_value)

        return obj



class HwElementBuilder:
    """Builder for HwElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: HwElement = HwElement()

    def build(self) -> HwElement:
        """Build and return HwElement object.

        Returns:
            HwElement instance
        """
        # TODO: Add validation
        return self._obj
