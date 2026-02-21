"""AbstractEthernetFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 578)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetFrame.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractEthernetFrame(Frame, ABC):
    """AUTOSAR AbstractEthernetFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractEthernetFrame."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize AbstractEthernetFrame to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractEthernetFrame, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEthernetFrame":
        """Deserialize XML element to AbstractEthernetFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractEthernetFrame object
        """
        # Delegate to parent class to handle inherited attributes
        return super(AbstractEthernetFrame, cls).deserialize(element)



class AbstractEthernetFrameBuilder:
    """Builder for AbstractEthernetFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEthernetFrame = AbstractEthernetFrame()

    def build(self) -> AbstractEthernetFrame:
        """Build and return AbstractEthernetFrame object.

        Returns:
            AbstractEthernetFrame instance
        """
        # TODO: Add validation
        return self._obj
