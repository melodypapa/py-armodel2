"""AbstractCanCluster AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
        """Serialize AbstractCanCluster to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractCanCluster, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize bus_off_recovery
        if self.bus_off_recovery is not None:
            serialized = SerializationHelper.serialize_item(self.bus_off_recovery, "CanClusterBusOffRecovery")
            if serialized is not None:
                wrapped = ET.Element("BUS-OFF-RECOVERY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize can_fd_baudrate
        if self.can_fd_baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.can_fd_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                wrapped = ET.Element("CAN-FD-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize can_xl_baudrate
        if self.can_xl_baudrate is not None:
            serialized = SerializationHelper.serialize_item(self.can_xl_baudrate, "PositiveUnlimitedInteger")
            if serialized is not None:
                wrapped = ET.Element("CAN-XL-BAUDRATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "AbstractCanCluster")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCluster":
        """Deserialize XML element to AbstractCanCluster object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCluster object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractCanCluster, cls).deserialize(element)

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "AbstractCanCluster")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse bus_off_recovery
        child = SerializationHelper.find_child_element(inner_elem, "BUS-OFF-RECOVERY")
        if child is not None:
            bus_off_recovery_value = SerializationHelper.deserialize_by_tag(child, "CanClusterBusOffRecovery")
            obj.bus_off_recovery = bus_off_recovery_value

        # Parse can_fd_baudrate
        child = SerializationHelper.find_child_element(inner_elem, "CAN-FD-BAUDRATE")
        if child is not None:
            can_fd_baudrate_value = child.text
            obj.can_fd_baudrate = can_fd_baudrate_value

        # Parse can_xl_baudrate
        child = SerializationHelper.find_child_element(inner_elem, "CAN-XL-BAUDRATE")
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
