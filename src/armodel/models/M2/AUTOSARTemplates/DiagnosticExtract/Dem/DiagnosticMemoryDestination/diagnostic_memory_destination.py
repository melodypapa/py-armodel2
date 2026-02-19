"""DiagnosticMemoryDestination AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination import (
    DiagnosticMemoryEntryStorageTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from abc import ABC, abstractmethod


class DiagnosticMemoryDestination(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticMemoryDestination."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    aging_requires: Optional[Boolean]
    clear_dtc: Optional[Any]
    dtc_status: Optional[PositiveInteger]
    event: Optional[DiagnosticEvent]
    max_number_of: Optional[PositiveInteger]
    memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum]
    status_bit: Optional[Boolean]
    type_of_freeze: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestination."""
        super().__init__()
        self.aging_requires: Optional[Boolean] = None
        self.clear_dtc: Optional[Any] = None
        self.dtc_status: Optional[PositiveInteger] = None
        self.event: Optional[DiagnosticEvent] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum] = None
        self.status_bit: Optional[Boolean] = None
        self.type_of_freeze: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticMemoryDestination to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticMemoryDestination, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aging_requires
        if self.aging_requires is not None:
            serialized = ARObject._serialize_item(self.aging_requires, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGING-REQUIRES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize clear_dtc
        if self.clear_dtc is not None:
            serialized = ARObject._serialize_item(self.clear_dtc, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-DTC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dtc_status
        if self.dtc_status is not None:
            serialized = ARObject._serialize_item(self.dtc_status, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DTC-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event
        if self.event is not None:
            serialized = ARObject._serialize_item(self.event, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = ARObject._serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize memory_entry
        if self.memory_entry is not None:
            serialized = ARObject._serialize_item(self.memory_entry, "DiagnosticMemoryEntryStorageTriggerEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MEMORY-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize status_bit
        if self.status_bit is not None:
            serialized = ARObject._serialize_item(self.status_bit, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATUS-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize type_of_freeze
        if self.type_of_freeze is not None:
            serialized = ARObject._serialize_item(self.type_of_freeze, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TYPE-OF-FREEZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMemoryDestination":
        """Deserialize XML element to DiagnosticMemoryDestination object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMemoryDestination object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMemoryDestination, cls).deserialize(element)

        # Parse aging_requires
        child = ARObject._find_child_element(element, "AGING-REQUIRES")
        if child is not None:
            aging_requires_value = child.text
            obj.aging_requires = aging_requires_value

        # Parse clear_dtc
        child = ARObject._find_child_element(element, "CLEAR-DTC")
        if child is not None:
            clear_dtc_value = child.text
            obj.clear_dtc = clear_dtc_value

        # Parse dtc_status
        child = ARObject._find_child_element(element, "DTC-STATUS")
        if child is not None:
            dtc_status_value = child.text
            obj.dtc_status = dtc_status_value

        # Parse event
        child = ARObject._find_child_element(element, "EVENT")
        if child is not None:
            event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.event = event_value

        # Parse max_number_of
        child = ARObject._find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse memory_entry
        child = ARObject._find_child_element(element, "MEMORY-ENTRY")
        if child is not None:
            memory_entry_value = DiagnosticMemoryEntryStorageTriggerEnum.deserialize(child)
            obj.memory_entry = memory_entry_value

        # Parse status_bit
        child = ARObject._find_child_element(element, "STATUS-BIT")
        if child is not None:
            status_bit_value = child.text
            obj.status_bit = status_bit_value

        # Parse type_of_freeze
        child = ARObject._find_child_element(element, "TYPE-OF-FREEZE")
        if child is not None:
            type_of_freeze_value = child.text
            obj.type_of_freeze = type_of_freeze_value

        return obj



class DiagnosticMemoryDestinationBuilder:
    """Builder for DiagnosticMemoryDestination."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestination = DiagnosticMemoryDestination()

    def build(self) -> DiagnosticMemoryDestination:
        """Build and return DiagnosticMemoryDestination object.

        Returns:
            DiagnosticMemoryDestination instance
        """
        # TODO: Add validation
        return self._obj
