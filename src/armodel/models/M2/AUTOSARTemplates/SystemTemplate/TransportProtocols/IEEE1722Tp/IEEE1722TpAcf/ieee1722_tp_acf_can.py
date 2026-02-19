"""IEEE1722TpAcfCan AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 661)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAcf.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus import (
    IEEE1722TpAcfBus,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class IEEE1722TpAcfCan(IEEE1722TpAcfBus):
    """AUTOSAR IEEE1722TpAcfCan."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    message_type_message_type_enum: Optional[IEEE1722TpAcfCan]
    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfCan."""
        super().__init__()
        self.message_type_message_type_enum: Optional[IEEE1722TpAcfCan] = None

    def serialize(self) -> ET.Element:
        """Serialize IEEE1722TpAcfCan to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IEEE1722TpAcfCan, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize message_type_message_type_enum
        if self.message_type_message_type_enum is not None:
            serialized = ARObject._serialize_item(self.message_type_message_type_enum, "IEEE1722TpAcfCan")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MESSAGE-TYPE-MESSAGE-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfCan":
        """Deserialize XML element to IEEE1722TpAcfCan object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IEEE1722TpAcfCan object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IEEE1722TpAcfCan, cls).deserialize(element)

        # Parse message_type_message_type_enum
        child = ARObject._find_child_element(element, "MESSAGE-TYPE-MESSAGE-TYPE-ENUM")
        if child is not None:
            message_type_message_type_enum_value = ARObject._deserialize_by_tag(child, "IEEE1722TpAcfCan")
            obj.message_type_message_type_enum = message_type_message_type_enum_value

        return obj



class IEEE1722TpAcfCanBuilder:
    """Builder for IEEE1722TpAcfCan."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfCan = IEEE1722TpAcfCan()

    def build(self) -> IEEE1722TpAcfCan:
        """Build and return IEEE1722TpAcfCan object.

        Returns:
            IEEE1722TpAcfCan instance
        """
        # TODO: Add validation
        return self._obj
