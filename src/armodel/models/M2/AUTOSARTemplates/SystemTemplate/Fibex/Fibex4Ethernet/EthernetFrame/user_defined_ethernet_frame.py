"""UserDefinedEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 579)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame.abstract_ethernet_frame import (
    AbstractEthernetFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class UserDefinedEthernetFrame(AbstractEthernetFrame):
    """AUTOSAR UserDefinedEthernetFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize UserDefinedEthernetFrame."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize UserDefinedEthernetFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UserDefinedEthernetFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UserDefinedEthernetFrame":
        """Deserialize XML element to UserDefinedEthernetFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UserDefinedEthernetFrame object
        """
        # Delegate to parent class to handle inherited attributes
        return super(UserDefinedEthernetFrame, cls).deserialize(element)



class UserDefinedEthernetFrameBuilder:
    """Builder for UserDefinedEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: UserDefinedEthernetFrame = UserDefinedEthernetFrame()

    def build(self) -> UserDefinedEthernetFrame:
        """Build and return UserDefinedEthernetFrame object.

        Returns:
            UserDefinedEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
