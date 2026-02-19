"""AbstractCanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveUnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology.can_cluster_bus_off_recovery import (
    CanClusterBusOffRecovery,
)
from abc import ABC, abstractmethod


class AbstractCanCluster(ARObject, ABC):
    """AUTOSAR AbstractCanCluster."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    bus_off_recovery: Optional[CanClusterBusOffRecovery]
    can_fd_baudrate: Optional[PositiveUnlimitedInteger]
    can_xl_baudrate: Optional[PositiveUnlimitedInteger]
    def __init__(self) -> None:
        """Initialize AbstractCanCluster."""
        super().__init__()
        self.bus_off_recovery: Optional[CanClusterBusOffRecovery] = None
        self.can_fd_baudrate: Optional[PositiveUnlimitedInteger] = None
        self.can_xl_baudrate: Optional[PositiveUnlimitedInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractCanCluster to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize bus_off_recovery
        if self.bus_off_recovery is not None:
            serialized = ARObject._serialize_item(self.bus_off_recovery, "CanClusterBusOffRecovery")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUS-OFF-RECOVERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_fd_baudrate
        if self.can_fd_baudrate is not None:
            serialized = ARObject._serialize_item(self.can_fd_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-FD-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize can_xl_baudrate
        if self.can_xl_baudrate is not None:
            serialized = ARObject._serialize_item(self.can_xl_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-XL-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCluster":
        """Deserialize XML element to AbstractCanCluster object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCluster object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bus_off_recovery
        child = ARObject._find_child_element(element, "BUS-OFF-RECOVERY")
        if child is not None:
            bus_off_recovery_value = ARObject._deserialize_by_tag(child, "CanClusterBusOffRecovery")
            obj.bus_off_recovery = bus_off_recovery_value

        # Parse can_fd_baudrate
        child = ARObject._find_child_element(element, "CAN-FD-BAUDRATE")
        if child is not None:
            can_fd_baudrate_value = child.text
            obj.can_fd_baudrate = can_fd_baudrate_value

        # Parse can_xl_baudrate
        child = ARObject._find_child_element(element, "CAN-XL-BAUDRATE")
        if child is not None:
            can_xl_baudrate_value = child.text
            obj.can_xl_baudrate = can_xl_baudrate_value

        return obj



class AbstractCanClusterBuilder:
    """Builder for AbstractCanCluster."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCluster = AbstractCanCluster()

    def build(self) -> AbstractCanCluster:
        """Build and return AbstractCanCluster object.

        Returns:
            AbstractCanCluster instance
        """
        # TODO: Add validation
        return self._obj
