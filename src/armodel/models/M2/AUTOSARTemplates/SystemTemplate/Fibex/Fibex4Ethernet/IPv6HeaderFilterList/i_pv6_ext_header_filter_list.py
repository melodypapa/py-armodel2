"""IPv6ExtHeaderFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 455)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_IPv6HeaderFilterList.classes.json"""

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


class IPv6ExtHeaderFilterList(Identifiable):
    """AUTOSAR IPv6ExtHeaderFilterList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_i_pv6_exts: list[PositiveInteger]
    def __init__(self) -> None:
        """Initialize IPv6ExtHeaderFilterList."""
        super().__init__()
        self.allowed_i_pv6_exts: list[PositiveInteger] = []

    def serialize(self) -> ET.Element:
        """Serialize IPv6ExtHeaderFilterList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPv6ExtHeaderFilterList, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_i_pv6_exts (list to container "ALLOWED-I-PV6-EXTS")
        if self.allowed_i_pv6_exts:
            wrapper = ET.Element("ALLOWED-I-PV6-EXTS")
            for item in self.allowed_i_pv6_exts:
                serialized = ARObject._serialize_item(item, "PositiveInteger")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPv6ExtHeaderFilterList":
        """Deserialize XML element to IPv6ExtHeaderFilterList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPv6ExtHeaderFilterList object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPv6ExtHeaderFilterList, cls).deserialize(element)

        # Parse allowed_i_pv6_exts (list from container "ALLOWED-I-PV6-EXTS")
        obj.allowed_i_pv6_exts = []
        container = ARObject._find_child_element(element, "ALLOWED-I-PV6-EXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.allowed_i_pv6_exts.append(child_value)

        return obj



class IPv6ExtHeaderFilterListBuilder:
    """Builder for IPv6ExtHeaderFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPv6ExtHeaderFilterList = IPv6ExtHeaderFilterList()

    def build(self) -> IPv6ExtHeaderFilterList:
        """Build and return IPv6ExtHeaderFilterList object.

        Returns:
            IPv6ExtHeaderFilterList instance
        """
        # TODO: Add validation
        return self._obj
