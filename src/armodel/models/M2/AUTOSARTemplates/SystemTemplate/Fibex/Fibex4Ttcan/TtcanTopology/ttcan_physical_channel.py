"""TtcanPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 77)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.abstract_can_physical_channel import (
    AbstractCanPhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class TtcanPhysicalChannel(AbstractCanPhysicalChannel):
    """AUTOSAR TtcanPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize TtcanPhysicalChannel."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize TtcanPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TtcanPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanPhysicalChannel":
        """Deserialize XML element to TtcanPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanPhysicalChannel object
        """
        # Delegate to parent class to handle inherited attributes
        return super(TtcanPhysicalChannel, cls).deserialize(element)



class TtcanPhysicalChannelBuilder:
    """Builder for TtcanPhysicalChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanPhysicalChannel = TtcanPhysicalChannel()

    def build(self) -> TtcanPhysicalChannel:
        """Build and return TtcanPhysicalChannel object.

        Returns:
            TtcanPhysicalChannel instance
        """
        # TODO: Add validation
        return self._obj
