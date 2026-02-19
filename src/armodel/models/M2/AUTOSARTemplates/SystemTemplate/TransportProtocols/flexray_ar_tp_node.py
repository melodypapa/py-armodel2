"""FlexrayArTpNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 602)

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


class FlexrayArTpNode(Identifiable):
    """AUTOSAR FlexrayArTpNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connectors: list[Any]
    tp_address: Optional[TpAddress]
    def __init__(self) -> None:
        """Initialize FlexrayArTpNode."""
        super().__init__()
        self.connectors: list[Any] = []
        self.tp_address: Optional[TpAddress] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayArTpNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayArTpNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connectors (list to container "CONNECTORS")
        if self.connectors:
            wrapper = ET.Element("CONNECTORS")
            for item in self.connectors:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpNode":
        """Deserialize XML element to FlexrayArTpNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayArTpNode, cls).deserialize(element)

        # Parse connectors (list from container "CONNECTORS")
        obj.connectors = []
        container = ARObject._find_child_element(element, "CONNECTORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connectors.append(child_value)

        # Parse tp_address
        child = ARObject._find_child_element(element, "TP-ADDRESS")
        if child is not None:
            tp_address_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.tp_address = tp_address_value

        return obj



class FlexrayArTpNodeBuilder:
    """Builder for FlexrayArTpNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpNode = FlexrayArTpNode()

    def build(self) -> FlexrayArTpNode:
        """Build and return FlexrayArTpNode object.

        Returns:
            FlexrayArTpNode instance
        """
        # TODO: Add validation
        return self._obj
