"""GlobalTimeCanSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class GlobalTimeCanSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeCanSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_validated: Optional[Any]
    sequence: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize GlobalTimeCanSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None
        self.sequence: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeCanSlave to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeCanSlave, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crc_validated
        if self.crc_validated is not None:
            serialized = ARObject._serialize_item(self.crc_validated, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-VALIDATED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sequence
        if self.sequence is not None:
            serialized = ARObject._serialize_item(self.sequence, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEQUENCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCanSlave":
        """Deserialize XML element to GlobalTimeCanSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCanSlave object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeCanSlave, cls).deserialize(element)

        # Parse crc_validated
        child = ARObject._find_child_element(element, "CRC-VALIDATED")
        if child is not None:
            crc_validated_value = child.text
            obj.crc_validated = crc_validated_value

        # Parse sequence
        child = ARObject._find_child_element(element, "SEQUENCE")
        if child is not None:
            sequence_value = child.text
            obj.sequence = sequence_value

        return obj



class GlobalTimeCanSlaveBuilder:
    """Builder for GlobalTimeCanSlave."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCanSlave = GlobalTimeCanSlave()

    def build(self) -> GlobalTimeCanSlave:
        """Build and return GlobalTimeCanSlave object.

        Returns:
            GlobalTimeCanSlave instance
        """
        # TODO: Add validation
        return self._obj
