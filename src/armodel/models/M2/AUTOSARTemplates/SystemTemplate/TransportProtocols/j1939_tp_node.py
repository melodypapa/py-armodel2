"""J1939TpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 626)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class J1939TpNode(Identifiable):
    """AUTOSAR J1939TpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connector: Optional[Any]
    tp_address: Optional[TpAddress]
    def __init__(self) -> None:
        """Initialize J1939TpNode."""
        super().__init__()
        self.connector: Optional[Any] = None
        self.tp_address: Optional[TpAddress] = None
    def serialize(self) -> ET.Element:
        """Serialize J1939TpNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939TpNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connector
        if self.connector is not None:
            serialized = ARObject._serialize_item(self.connector, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_address
        if self.tp_address is not None:
            serialized = ARObject._serialize_item(self.tp_address, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpNode":
        """Deserialize XML element to J1939TpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939TpNode, cls).deserialize(element)

        # Parse connector
        child = ARObject._find_child_element(element, "CONNECTOR")
        if child is not None:
            connector_value = child.text
            obj.connector = connector_value

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_address = tp_address_value

        return obj



class J1939TpNodeBuilder:
    """Builder for J1939TpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpNode = J1939TpNode()

    def build(self) -> J1939TpNode:
        """Build and return J1939TpNode object.

        Returns:
            J1939TpNode instance
        """
        # TODO: Add validation
        return self._obj
