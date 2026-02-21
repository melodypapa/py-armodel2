"""VariableAndParameterInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 124)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2077)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)


class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR VariableAndParameterInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_mapping_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize VariableAndParameterInterfaceMapping."""
        super().__init__()
        self.data_mapping_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize VariableAndParameterInterfaceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariableAndParameterInterfaceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_mapping_refs (list to container "DATA-MAPPING-REFS")
        if self.data_mapping_refs:
            wrapper = ET.Element("DATA-MAPPING-REFS")
            for item in self.data_mapping_refs:
                serialized = ARObject._serialize_item(item, "DataPrototypeMapping")
                if serialized is not None:
                    child_elem = ET.Element("DATA-MAPPING-REF")
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
    def deserialize(cls, element: ET.Element) -> "VariableAndParameterInterfaceMapping":
        """Deserialize XML element to VariableAndParameterInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableAndParameterInterfaceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariableAndParameterInterfaceMapping, cls).deserialize(element)

        # Parse data_mapping_refs (list from container "DATA-MAPPING-REFS")
        obj.data_mapping_refs = []
        container = ARObject._find_child_element(element, "DATA-MAPPING-REFS")
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
                    obj.data_mapping_refs.append(child_value)

        return obj



class VariableAndParameterInterfaceMappingBuilder:
    """Builder for VariableAndParameterInterfaceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableAndParameterInterfaceMapping = VariableAndParameterInterfaceMapping()

    def build(self) -> VariableAndParameterInterfaceMapping:
        """Build and return VariableAndParameterInterfaceMapping object.

        Returns:
            VariableAndParameterInterfaceMapping instance
        """
        # TODO: Add validation
        return self._obj
