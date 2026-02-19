"""PortInterfaceMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 119)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)


class PortInterfaceMappingSet(ARElement):
    """AUTOSAR PortInterfaceMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    port_interface_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PortInterfaceMappingSet."""
        super().__init__()
        self.port_interface_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize PortInterfaceMappingSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortInterfaceMappingSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize port_interface_refs (list to container "PORT-INTERFACES")
        if self.port_interface_refs:
            wrapper = ET.Element("PORT-INTERFACES")
            for item in self.port_interface_refs:
                serialized = ARObject._serialize_item(item, "PortInterfaceMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortInterfaceMappingSet":
        """Deserialize XML element to PortInterfaceMappingSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortInterfaceMappingSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortInterfaceMappingSet, cls).deserialize(element)

        # Parse port_interface_refs (list from container "PORT-INTERFACES")
        obj.port_interface_refs = []
        container = ARObject._find_child_element(element, "PORT-INTERFACES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_interface_refs.append(child_value)

        return obj



class PortInterfaceMappingSetBuilder:
    """Builder for PortInterfaceMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterfaceMappingSet = PortInterfaceMappingSet()

    def build(self) -> PortInterfaceMappingSet:
        """Build and return PortInterfaceMappingSet object.

        Returns:
            PortInterfaceMappingSet instance
        """
        # TODO: Add validation
        return self._obj
