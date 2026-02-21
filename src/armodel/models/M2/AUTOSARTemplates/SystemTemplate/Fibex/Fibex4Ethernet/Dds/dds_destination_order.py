"""DdsDestinationOrder AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 536)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DdsDestinationOrder(ARObject):
    """AUTOSAR DdsDestinationOrder."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    destination: Optional[DdsDestinationOrder]
    def __init__(self) -> None:
        """Initialize DdsDestinationOrder."""
        super().__init__()
        self.destination: Optional[DdsDestinationOrder] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsDestinationOrder to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize destination
        if self.destination is not None:
            serialized = SerializationHelper.serialize_item(self.destination, "DdsDestinationOrder")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsDestinationOrder":
        """Deserialize XML element to DdsDestinationOrder object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsDestinationOrder object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse destination
        child = SerializationHelper.find_child_element(element, "DESTINATION")
        if child is not None:
            destination_value = SerializationHelper.deserialize_by_tag(child, "DdsDestinationOrder")
            obj.destination = destination_value

        return obj



class DdsDestinationOrderBuilder:
    """Builder for DdsDestinationOrder."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDestinationOrder = DdsDestinationOrder()

    def build(self) -> DdsDestinationOrder:
        """Build and return DdsDestinationOrder object.

        Returns:
            DdsDestinationOrder instance
        """
        # TODO: Add validation
        return self._obj
