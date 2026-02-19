"""ComplexDeviceDriverSwComponentType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 310)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 648)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2010)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 218)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
    AtomicSwComponentType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_description_entity import (
    HwDescriptionEntity,
)


class ComplexDeviceDriverSwComponentType(AtomicSwComponentType):
    """AUTOSAR ComplexDeviceDriverSwComponentType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    hardwares: list[HwDescriptionEntity]
    def __init__(self) -> None:
        """Initialize ComplexDeviceDriverSwComponentType."""
        super().__init__()
        self.hardwares: list[HwDescriptionEntity] = []

    def serialize(self) -> ET.Element:
        """Serialize ComplexDeviceDriverSwComponentType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ComplexDeviceDriverSwComponentType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hardwares (list to container "HARDWARES")
        if self.hardwares:
            wrapper = ET.Element("HARDWARES")
            for item in self.hardwares:
                serialized = ARObject._serialize_item(item, "HwDescriptionEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ComplexDeviceDriverSwComponentType":
        """Deserialize XML element to ComplexDeviceDriverSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComplexDeviceDriverSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComplexDeviceDriverSwComponentType, cls).deserialize(element)

        # Parse hardwares (list from container "HARDWARES")
        obj.hardwares = []
        container = ARObject._find_child_element(element, "HARDWARES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hardwares.append(child_value)

        return obj



class ComplexDeviceDriverSwComponentTypeBuilder:
    """Builder for ComplexDeviceDriverSwComponentType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComplexDeviceDriverSwComponentType = ComplexDeviceDriverSwComponentType()

    def build(self) -> ComplexDeviceDriverSwComponentType:
        """Build and return ComplexDeviceDriverSwComponentType object.

        Returns:
            ComplexDeviceDriverSwComponentType instance
        """
        # TODO: Add validation
        return self._obj
