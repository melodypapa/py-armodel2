"""VlanConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 106)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

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


class VlanConfig(Identifiable):
    """AUTOSAR VlanConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    vlan_identifier: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize VlanConfig."""
        super().__init__()
        self.vlan_identifier: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize VlanConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VlanConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize vlan_identifier
        if self.vlan_identifier is not None:
            serialized = ARObject._serialize_item(self.vlan_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VlanConfig":
        """Deserialize XML element to VlanConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VlanConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VlanConfig, cls).deserialize(element)

        # Parse vlan_identifier
        child = ARObject._find_child_element(element, "VLAN-IDENTIFIER")
        if child is not None:
            vlan_identifier_value = child.text
            obj.vlan_identifier = vlan_identifier_value

        return obj



class VlanConfigBuilder:
    """Builder for VlanConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VlanConfig = VlanConfig()

    def build(self) -> VlanConfig:
        """Build and return VlanConfig object.

        Returns:
            VlanConfig instance
        """
        # TODO: Add validation
        return self._obj
