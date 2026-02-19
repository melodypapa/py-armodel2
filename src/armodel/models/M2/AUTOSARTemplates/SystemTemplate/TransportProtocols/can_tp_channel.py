"""CanTpChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 608)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

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


class CanTpChannel(Identifiable):
    """AUTOSAR CanTpChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    channel_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize CanTpChannel."""
        super().__init__()
        self.channel_id: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize CanTpChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanTpChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize channel_id
        if self.channel_id is not None:
            serialized = ARObject._serialize_item(self.channel_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CHANNEL-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpChannel":
        """Deserialize XML element to CanTpChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanTpChannel, cls).deserialize(element)

        # Parse channel_id
        child = ARObject._find_child_element(element, "CHANNEL-ID")
        if child is not None:
            channel_id_value = child.text
            obj.channel_id = channel_id_value

        return obj



class CanTpChannelBuilder:
    """Builder for CanTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpChannel = CanTpChannel()

    def build(self) -> CanTpChannel:
        """Build and return CanTpChannel object.

        Returns:
            CanTpChannel instance
        """
        # TODO: Add validation
        return self._obj
