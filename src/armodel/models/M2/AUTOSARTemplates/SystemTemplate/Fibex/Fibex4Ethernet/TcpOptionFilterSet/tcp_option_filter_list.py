"""TcpOptionFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class TcpOptionFilterList(Identifiable):
    """AUTOSAR TcpOptionFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_tcp_options: list[PositiveInteger]
    def __init__(self) -> None:
        """Initialize TcpOptionFilterList."""
        super().__init__()
        self.allowed_tcp_options: list[PositiveInteger] = []

    def serialize(self) -> ET.Element:
        """Serialize TcpOptionFilterList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TcpOptionFilterList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_tcp_options (list to container "ALLOWED-TCP-OPTIONS")
        if self.allowed_tcp_options:
            wrapper = ET.Element("ALLOWED-TCP-OPTIONS")
            for item in self.allowed_tcp_options:
                serialized = ARObject._serialize_item(item, "PositiveInteger")
                if serialized is not None:
                    child_elem = ET.Element("ALLOWED-TCP-OPTION")
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
    def deserialize(cls, element: ET.Element) -> "TcpOptionFilterList":
        """Deserialize XML element to TcpOptionFilterList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TcpOptionFilterList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TcpOptionFilterList, cls).deserialize(element)

        # Parse allowed_tcp_options (list from container "ALLOWED-TCP-OPTIONS")
        obj.allowed_tcp_options = []
        container = ARObject._find_child_element(element, "ALLOWED-TCP-OPTIONS")
        if container is not None:
            for child in container:
                # Extract primitive value (PositiveInteger) as text
                child_value = child.text
                if child_value is not None:
                    obj.allowed_tcp_options.append(child_value)

        return obj



class TcpOptionFilterListBuilder:
    """Builder for TcpOptionFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterList = TcpOptionFilterList()

    def build(self) -> TcpOptionFilterList:
        """Build and return TcpOptionFilterList object.

        Returns:
            TcpOptionFilterList instance
        """
        # TODO: Add validation
        return self._obj
