"""J1939NmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    J1939NmAddressConfigurationCapabilityEnum,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_node_name import (
    J1939NodeName,
)


class J1939NmNode(NmNode):
    """AUTOSAR J1939NmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address: Optional[J1939NmAddressConfigurationCapabilityEnum]
    node_name: Optional[J1939NodeName]
    def __init__(self) -> None:
        """Initialize J1939NmNode."""
        super().__init__()
        self.address: Optional[J1939NmAddressConfigurationCapabilityEnum] = None
        self.node_name: Optional[J1939NodeName] = None

    def serialize(self) -> ET.Element:
        """Serialize J1939NmNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939NmNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize address
        if self.address is not None:
            serialized = ARObject._serialize_item(self.address, "J1939NmAddressConfigurationCapabilityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize node_name
        if self.node_name is not None:
            serialized = ARObject._serialize_item(self.node_name, "J1939NodeName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NmNode":
        """Deserialize XML element to J1939NmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939NmNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939NmNode, cls).deserialize(element)

        # Parse address
        child = ARObject._find_child_element(element, "ADDRESS")
        if child is not None:
            address_value = J1939NmAddressConfigurationCapabilityEnum.deserialize(child)
            obj.address = address_value

        # Parse node_name
        child = ARObject._find_child_element(element, "NODE-NAME")
        if child is not None:
            node_name_value = ARObject._deserialize_by_tag(child, "J1939NodeName")
            obj.node_name = node_name_value

        return obj



class J1939NmNodeBuilder:
    """Builder for J1939NmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939NmNode = J1939NmNode()

    def build(self) -> J1939NmNode:
        """Build and return J1939NmNode object.

        Returns:
            J1939NmNode instance
        """
        # TODO: Add validation
        return self._obj
