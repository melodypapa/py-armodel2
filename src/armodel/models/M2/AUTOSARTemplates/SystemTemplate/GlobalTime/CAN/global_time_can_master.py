"""GlobalTimeCanMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_master import (
    GlobalTimeMaster,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime import (
    GlobalTimeCrcSupportEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class GlobalTimeCanMaster(GlobalTimeMaster):
    """AUTOSAR GlobalTimeCanMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crc_secured: Optional[GlobalTimeCrcSupportEnum]
    sync: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeCanMaster."""
        super().__init__()
        self.crc_secured: Optional[GlobalTimeCrcSupportEnum] = None
        self.sync: Optional[TimeValue] = None
    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeCanMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeCanMaster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crc_secured
        if self.crc_secured is not None:
            serialized = ARObject._serialize_item(self.crc_secured, "GlobalTimeCrcSupportEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-SECURED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync
        if self.sync is not None:
            serialized = ARObject._serialize_item(self.sync, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeCanMaster":
        """Deserialize XML element to GlobalTimeCanMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeCanMaster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeCanMaster, cls).deserialize(element)

        # Parse crc_secured
        child = ARObject._find_child_element(element, "CRC-SECURED")
        if child is not None:
            crc_secured_value = GlobalTimeCrcSupportEnum.deserialize(child)
            obj.crc_secured = crc_secured_value

        # Parse sync
        child = ARObject._find_child_element(element, "SYNC")
        if child is not None:
            sync_value = child.text
            obj.sync = sync_value

        return obj



class GlobalTimeCanMasterBuilder:
    """Builder for GlobalTimeCanMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCanMaster = GlobalTimeCanMaster()

    def build(self) -> GlobalTimeCanMaster:
        """Build and return GlobalTimeCanMaster object.

        Returns:
            GlobalTimeCanMaster instance
        """
        # TODO: Add validation
        return self._obj
