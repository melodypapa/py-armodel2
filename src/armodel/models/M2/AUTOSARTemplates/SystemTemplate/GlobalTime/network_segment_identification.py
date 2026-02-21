"""NetworkSegmentIdentification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 859)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class NetworkSegmentIdentification(ARObject):
    """AUTOSAR NetworkSegmentIdentification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    network: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NetworkSegmentIdentification."""
        super().__init__()
        self.network: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize NetworkSegmentIdentification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NetworkSegmentIdentification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize network
        if self.network is not None:
            serialized = SerializationHelper.serialize_item(self.network, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NetworkSegmentIdentification":
        """Deserialize XML element to NetworkSegmentIdentification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NetworkSegmentIdentification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NetworkSegmentIdentification, cls).deserialize(element)

        # Parse network
        child = SerializationHelper.find_child_element(element, "NETWORK")
        if child is not None:
            network_value = child.text
            obj.network = network_value

        return obj



class NetworkSegmentIdentificationBuilder:
    """Builder for NetworkSegmentIdentification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: NetworkSegmentIdentification = NetworkSegmentIdentification()

    def build(self) -> NetworkSegmentIdentification:
        """Build and return NetworkSegmentIdentification object.

        Returns:
            NetworkSegmentIdentification instance
        """
        # TODO: Add validation
        return self._obj
