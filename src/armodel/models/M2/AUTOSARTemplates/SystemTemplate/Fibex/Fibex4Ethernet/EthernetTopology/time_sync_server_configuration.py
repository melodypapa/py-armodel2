"""TimeSyncServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    TimeSyncTechnologyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)


class TimeSyncServerConfiguration(Referrable):
    """AUTOSAR TimeSyncServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    priority: Optional[PositiveInteger]
    sync_interval: Optional[TimeValue]
    time_sync_server_identifier: Optional[String]
    time_sync: Optional[TimeSyncTechnologyEnum]
    def __init__(self) -> None:
        """Initialize TimeSyncServerConfiguration."""
        super().__init__()
        self.priority: Optional[PositiveInteger] = None
        self.sync_interval: Optional[TimeValue] = None
        self.time_sync_server_identifier: Optional[String] = None
        self.time_sync: Optional[TimeSyncTechnologyEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize TimeSyncServerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TimeSyncServerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sync_interval
        if self.sync_interval is not None:
            serialized = ARObject._serialize_item(self.sync_interval, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYNC-INTERVAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync_server_identifier
        if self.time_sync_server_identifier is not None:
            serialized = ARObject._serialize_item(self.time_sync_server_identifier, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-SERVER-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync
        if self.time_sync is not None:
            serialized = ARObject._serialize_item(self.time_sync, "TimeSyncTechnologyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TimeSyncServerConfiguration":
        """Deserialize XML element to TimeSyncServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TimeSyncServerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TimeSyncServerConfiguration, cls).deserialize(element)

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse sync_interval
        child = ARObject._find_child_element(element, "SYNC-INTERVAL")
        if child is not None:
            sync_interval_value = child.text
            obj.sync_interval = sync_interval_value

        # Parse time_sync_server_identifier
        child = ARObject._find_child_element(element, "TIME-SYNC-SERVER-IDENTIFIER")
        if child is not None:
            time_sync_server_identifier_value = child.text
            obj.time_sync_server_identifier = time_sync_server_identifier_value

        # Parse time_sync
        child = ARObject._find_child_element(element, "TIME-SYNC")
        if child is not None:
            time_sync_value = TimeSyncTechnologyEnum.deserialize(child)
            obj.time_sync = time_sync_value

        return obj



class TimeSyncServerConfigurationBuilder:
    """Builder for TimeSyncServerConfiguration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TimeSyncServerConfiguration = TimeSyncServerConfiguration()

    def build(self) -> TimeSyncServerConfiguration:
        """Build and return TimeSyncServerConfiguration object.

        Returns:
            TimeSyncServerConfiguration instance
        """
        # TODO: Add validation
        return self._obj
