"""StreamFilterIEEE1722Tp AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 139)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
)


class StreamFilterIEEE1722Tp(ARObject):
    """AUTOSAR StreamFilterIEEE1722Tp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    stream_id: Optional[PositiveUnlimitedInteger]
    def __init__(self) -> None:
        """Initialize StreamFilterIEEE1722Tp."""
        super().__init__()
        self.stream_id: Optional[PositiveUnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterIEEE1722Tp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize stream_id
        if self.stream_id is not None:
            serialized = SerializationHelper.serialize_item(self.stream_id, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STREAM-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterIEEE1722Tp":
        """Deserialize XML element to StreamFilterIEEE1722Tp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterIEEE1722Tp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse stream_id
        child = SerializationHelper.find_child_element(element, "STREAM-ID")
        if child is not None:
            stream_id_value = child.text
            obj.stream_id = stream_id_value

        return obj



class StreamFilterIEEE1722TpBuilder:
    """Builder for StreamFilterIEEE1722Tp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StreamFilterIEEE1722Tp = StreamFilterIEEE1722Tp()

    def build(self) -> StreamFilterIEEE1722Tp:
        """Build and return StreamFilterIEEE1722Tp object.

        Returns:
            StreamFilterIEEE1722Tp instance
        """
        # TODO: Add validation
        return self._obj
