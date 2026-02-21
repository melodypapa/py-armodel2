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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    hardware_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ComplexDeviceDriverSwComponentType."""
        super().__init__()
        self.hardware_refs: list[ARRef] = []

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

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize hardware_refs (list to container "HARDWARE-REFS")
        if self.hardware_refs:
            wrapper = ET.Element("HARDWARE-REFS")
            for item in self.hardware_refs:
                serialized = ARObject._serialize_item(item, "HwDescriptionEntity")
                if serialized is not None:
                    child_elem = ET.Element("HARDWARE-REF")
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
    def deserialize(cls, element: ET.Element) -> "ComplexDeviceDriverSwComponentType":
        """Deserialize XML element to ComplexDeviceDriverSwComponentType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComplexDeviceDriverSwComponentType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComplexDeviceDriverSwComponentType, cls).deserialize(element)

        # Parse hardware_refs (list from container "HARDWARE-REFS")
        obj.hardware_refs = []
        container = ARObject._find_child_element(element, "HARDWARE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.hardware_refs.append(child_value)

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
