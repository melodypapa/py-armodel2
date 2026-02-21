"""TtcanCommunicationController AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ttcan_TtcanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import atp_variant

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)


@atp_variant()

class TtcanCommunicationController(ARObject):
    """AUTOSAR TtcanCommunicationController."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    appl_watchdog: Optional[Integer]
    expected_tx: Optional[Integer]
    external_clock: Optional[Boolean]
    initial_ref_offset: Optional[Integer]
    master: Optional[Boolean]
    time_master: Optional[Integer]
    time_triggered: Optional[Integer]
    tx_enable: Optional[Integer]
    def __init__(self) -> None:
        """Initialize TtcanCommunicationController."""
        super().__init__()
        self.appl_watchdog: Optional[Integer] = None
        self.expected_tx: Optional[Integer] = None
        self.external_clock: Optional[Boolean] = None
        self.initial_ref_offset: Optional[Integer] = None
        self.master: Optional[Boolean] = None
        self.time_master: Optional[Integer] = None
        self.time_triggered: Optional[Integer] = None
        self.tx_enable: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize TtcanCommunicationController to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Serialize appl_watchdog
        if self.appl_watchdog is not None:
            serialized = SerializationHelper.serialize_item(self.appl_watchdog, "Integer")
            if serialized is not None:
                wrapped = ET.Element("APPL-WATCHDOG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize expected_tx
        if self.expected_tx is not None:
            serialized = SerializationHelper.serialize_item(self.expected_tx, "Integer")
            if serialized is not None:
                wrapped = ET.Element("EXPECTED-TX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize external_clock
        if self.external_clock is not None:
            serialized = SerializationHelper.serialize_item(self.external_clock, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("EXTERNAL-CLOCK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize initial_ref_offset
        if self.initial_ref_offset is not None:
            serialized = SerializationHelper.serialize_item(self.initial_ref_offset, "Integer")
            if serialized is not None:
                wrapped = ET.Element("INITIAL-REF-OFFSET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize master
        if self.master is not None:
            serialized = SerializationHelper.serialize_item(self.master, "Boolean")
            if serialized is not None:
                wrapped = ET.Element("MASTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize time_master
        if self.time_master is not None:
            serialized = SerializationHelper.serialize_item(self.time_master, "Integer")
            if serialized is not None:
                wrapped = ET.Element("TIME-MASTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize time_triggered
        if self.time_triggered is not None:
            serialized = SerializationHelper.serialize_item(self.time_triggered, "Integer")
            if serialized is not None:
                wrapped = ET.Element("TIME-TRIGGERED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize tx_enable
        if self.tx_enable is not None:
            serialized = SerializationHelper.serialize_item(self.tx_enable, "Integer")
            if serialized is not None:
                wrapped = ET.Element("TX-ENABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "TtcanCommunicationController")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TtcanCommunicationController":
        """Deserialize XML element to TtcanCommunicationController object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TtcanCommunicationController object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Handle ARObject inherited attributes (checksum and timestamp)
        # Parse timestamp (XML attribute 'T')
        timestamp_value = element.get("T")
        if timestamp_value is not None:
            obj.timestamp = timestamp_value

        # Parse checksum (child element)
        checksum_elem = SerializationHelper.find_child_element(element, "CHECKSUM")
        if checksum_elem is not None:
            checksum_value = checksum_elem.text
            if checksum_value is not None:
                obj.checksum = checksum_value

        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "TtcanCommunicationController")
        if inner_elem is None:
            # No wrapper structure found, return object with default values
            return obj

        # Parse appl_watchdog
        child = SerializationHelper.find_child_element(inner_elem, "APPL-WATCHDOG")
        if child is not None:
            appl_watchdog_value = child.text
            obj.appl_watchdog = appl_watchdog_value

        # Parse expected_tx
        child = SerializationHelper.find_child_element(inner_elem, "EXPECTED-TX")
        if child is not None:
            expected_tx_value = child.text
            obj.expected_tx = expected_tx_value

        # Parse external_clock
        child = SerializationHelper.find_child_element(inner_elem, "EXTERNAL-CLOCK")
        if child is not None:
            external_clock_value = child.text
            obj.external_clock = external_clock_value

        # Parse initial_ref_offset
        child = SerializationHelper.find_child_element(inner_elem, "INITIAL-REF-OFFSET")
        if child is not None:
            initial_ref_offset_value = child.text
            obj.initial_ref_offset = initial_ref_offset_value

        # Parse master
        child = SerializationHelper.find_child_element(inner_elem, "MASTER")
        if child is not None:
            master_value = child.text
            obj.master = master_value

        # Parse time_master
        child = SerializationHelper.find_child_element(inner_elem, "TIME-MASTER")
        if child is not None:
            time_master_value = child.text
            obj.time_master = time_master_value

        # Parse time_triggered
        child = SerializationHelper.find_child_element(inner_elem, "TIME-TRIGGERED")
        if child is not None:
            time_triggered_value = child.text
            obj.time_triggered = time_triggered_value

        # Parse tx_enable
        child = SerializationHelper.find_child_element(inner_elem, "TX-ENABLE")
        if child is not None:
            tx_enable_value = child.text
            obj.tx_enable = tx_enable_value

        return obj



class TtcanCommunicationControllerBuilder:
    """Builder for TtcanCommunicationController."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TtcanCommunicationController = TtcanCommunicationController()

    def build(self) -> TtcanCommunicationController:
        """Build and return TtcanCommunicationController object.

        Returns:
            TtcanCommunicationController instance
        """
        # TODO: Add validation
        return self._obj
