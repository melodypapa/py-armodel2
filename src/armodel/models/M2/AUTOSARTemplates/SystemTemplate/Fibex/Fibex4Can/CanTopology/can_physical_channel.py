"""CanPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 73)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_physical_channel import (
    AbstractCanPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class CanPhysicalChannel(AbstractCanPhysicalChannel):
    """AUTOSAR CanPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize CanPhysicalChannel."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize CanPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanPhysicalChannel":
        """Deserialize XML element to CanPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanPhysicalChannel object
        """
        # Delegate to parent class to handle inherited attributes
        return super(CanPhysicalChannel, cls).deserialize(element)



class CanPhysicalChannelBuilder:
    """Builder for CanPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanPhysicalChannel = CanPhysicalChannel()

    def build(self) -> CanPhysicalChannel:
        """Build and return CanPhysicalChannel object.

        Returns:
            CanPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
