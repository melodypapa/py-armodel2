"""PortGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 203)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2045)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class PortGroup(Identifiable):
    """AUTOSAR PortGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    inner_group_refs: list[ARRef]
    outer_port_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PortGroup."""
        super().__init__()
        self.inner_group_refs: list[ARRef] = []
        self.outer_port_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PortGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize inner_group_refs (list to container "INNER-GROUP-REFS")
        if self.inner_group_refs:
            wrapper = ET.Element("INNER-GROUP-REFS")
            for item in self.inner_group_refs:
                serialized = SerializationHelper.serialize_item(item, "PortGroup")
                if serialized is not None:
                    child_elem = ET.Element("INNER-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize outer_port_refs (list to container "OUTER-PORT-REFS")
        if self.outer_port_refs:
            wrapper = ET.Element("OUTER-PORT-REFS")
            for item in self.outer_port_refs:
                serialized = SerializationHelper.serialize_item(item, "PortPrototype")
                if serialized is not None:
                    child_elem = ET.Element("OUTER-PORT-REF")
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
    def deserialize(cls, element: ET.Element) -> "PortGroup":
        """Deserialize XML element to PortGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortGroup, cls).deserialize(element)

        # Parse inner_group_refs (list from container "INNER-GROUP-REFS")
        obj.inner_group_refs = []
        container = SerializationHelper.find_child_element(element, "INNER-GROUP-REFS")
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
                    obj.inner_group_refs.append(child_value)

        # Parse outer_port_refs (list from container "OUTER-PORT-REFS")
        obj.outer_port_refs = []
        container = SerializationHelper.find_child_element(element, "OUTER-PORT-REFS")
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
                    obj.outer_port_refs.append(child_value)

        return obj



class PortGroupBuilder:
    """Builder for PortGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortGroup = PortGroup()

    def build(self) -> PortGroup:
        """Build and return PortGroup object.

        Returns:
            PortGroup instance
        """
        # TODO: Add validation
        return self._obj
