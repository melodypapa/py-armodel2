"""OrderedMaster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 470)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.time_sync_server_configuration import (
    TimeSyncServerConfiguration,
)


class OrderedMaster(ARObject):
    """AUTOSAR OrderedMaster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    index: Optional[PositiveInteger]
    time_sync_server_configuration_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize OrderedMaster."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None
        self.time_sync_server_configuration_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize OrderedMaster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize index
        if self.index is not None:
            serialized = SerializationHelper.serialize_item(self.index, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_sync_server_configuration_ref
        if self.time_sync_server_configuration_ref is not None:
            serialized = SerializationHelper.serialize_item(self.time_sync_server_configuration_ref, "TimeSyncServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-SYNC-SERVER-CONFIGURATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OrderedMaster":
        """Deserialize XML element to OrderedMaster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized OrderedMaster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse index
        child = SerializationHelper.find_child_element(element, "INDEX")
        if child is not None:
            index_value = child.text
            obj.index = index_value

        # Parse time_sync_server_configuration_ref
        child = SerializationHelper.find_child_element(element, "TIME-SYNC-SERVER-CONFIGURATION-REF")
        if child is not None:
            time_sync_server_configuration_ref_value = ARRef.deserialize(child)
            obj.time_sync_server_configuration_ref = time_sync_server_configuration_ref_value

        return obj



class OrderedMasterBuilder:
    """Builder for OrderedMaster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OrderedMaster = OrderedMaster()

    def build(self) -> OrderedMaster:
        """Build and return OrderedMaster object.

        Returns:
            OrderedMaster instance
        """
        # TODO: Add validation
        return self._obj
