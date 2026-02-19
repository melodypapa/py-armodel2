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
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize inner_group_refs (list to container "INNER-GROUPS")
        if self.inner_group_refs:
            wrapper = ET.Element("INNER-GROUPS")
            for item in self.inner_group_refs:
                serialized = ARObject._serialize_item(item, "PortGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize outer_port_refs (list to container "OUTER-PORTS")
        if self.outer_port_refs:
            wrapper = ET.Element("OUTER-PORTS")
            for item in self.outer_port_refs:
                serialized = ARObject._serialize_item(item, "PortPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
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

        # Parse inner_group_refs (list from container "INNER-GROUPS")
        obj.inner_group_refs = []
        container = ARObject._find_child_element(element, "INNER-GROUPS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.inner_group_refs.append(child_value)

        # Parse outer_port_refs (list from container "OUTER-PORTS")
        obj.outer_port_refs = []
        container = ARObject._find_child_element(element, "OUTER-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
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
