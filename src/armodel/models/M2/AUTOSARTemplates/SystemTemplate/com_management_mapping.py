"""ComManagementMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 282)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
    PortGroup,
)


class ComManagementMapping(Identifiable):
    """AUTOSAR ComManagementMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    com_refs: list[ARRef]
    physical_channel_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ComManagementMapping."""
        super().__init__()
        self.com_refs: list[ARRef] = []
        self.physical_channel_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ComManagementMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ComManagementMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize com_refs (list to container "COM-REFS")
        if self.com_refs:
            wrapper = ET.Element("COM-REFS")
            for item in self.com_refs:
                serialized = SerializationHelper.serialize_item(item, "PortGroup")
                if serialized is not None:
                    child_elem = ET.Element("COM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_channel_refs (list to container "PHYSICAL-CHANNEL-REFS")
        if self.physical_channel_refs:
            wrapper = ET.Element("PHYSICAL-CHANNEL-REFS")
            for item in self.physical_channel_refs:
                serialized = SerializationHelper.serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("PHYSICAL-CHANNEL-REF")
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
    def deserialize(cls, element: ET.Element) -> "ComManagementMapping":
        """Deserialize XML element to ComManagementMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ComManagementMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ComManagementMapping, cls).deserialize(element)

        # Parse com_refs (list from container "COM-REFS")
        obj.com_refs = []
        container = SerializationHelper.find_child_element(element, "COM-REFS")
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
                    obj.com_refs.append(child_value)

        # Parse physical_channel_refs (list from container "PHYSICAL-CHANNEL-REFS")
        obj.physical_channel_refs = []
        container = SerializationHelper.find_child_element(element, "PHYSICAL-CHANNEL-REFS")
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
                    obj.physical_channel_refs.append(child_value)

        return obj



class ComManagementMappingBuilder:
    """Builder for ComManagementMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ComManagementMapping = ComManagementMapping()

    def build(self) -> ComManagementMapping:
        """Build and return ComManagementMapping object.

        Returns:
            ComManagementMapping instance
        """
        # TODO: Add validation
        return self._obj
