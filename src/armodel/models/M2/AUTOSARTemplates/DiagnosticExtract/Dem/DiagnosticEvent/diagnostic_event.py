"""DiagnosticEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 164)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import (
    DiagnosticClearEventAllowedBehaviorEnum,
    DiagnosticEventClearAllowedEnum,
    DiagnosticEventKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class DiagnosticEvent(DiagnosticCommonElement):
    """AUTOSAR DiagnosticEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    associated: Optional[PositiveInteger]
    clear_event: Optional[DiagnosticClearEventAllowedBehaviorEnum]
    confirmation: Optional[PositiveInteger]
    connecteds: list[Any]
    event_clear: Optional[DiagnosticEventClearAllowedEnum]
    event_kind: Optional[DiagnosticEventKindEnum]
    prestorage: Optional[Boolean]
    prestored: Optional[Boolean]
    recoverable_in: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticEvent."""
        super().__init__()
        self.associated: Optional[PositiveInteger] = None
        self.clear_event: Optional[DiagnosticClearEventAllowedBehaviorEnum] = None
        self.confirmation: Optional[PositiveInteger] = None
        self.connecteds: list[Any] = []
        self.event_clear: Optional[DiagnosticEventClearAllowedEnum] = None
        self.event_kind: Optional[DiagnosticEventKindEnum] = None
        self.prestorage: Optional[Boolean] = None
        self.prestored: Optional[Boolean] = None
        self.recoverable_in: Optional[Boolean] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize associated
        if self.associated is not None:
            serialized = ARObject._serialize_item(self.associated, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ASSOCIATED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize clear_event
        if self.clear_event is not None:
            serialized = ARObject._serialize_item(self.clear_event, "DiagnosticClearEventAllowedBehaviorEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize confirmation
        if self.confirmation is not None:
            serialized = ARObject._serialize_item(self.confirmation, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIRMATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize connecteds (list to container "CONNECTEDS")
        if self.connecteds:
            wrapper = ET.Element("CONNECTEDS")
            for item in self.connecteds:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize event_clear
        if self.event_clear is not None:
            serialized = ARObject._serialize_item(self.event_clear, "DiagnosticEventClearAllowedEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-CLEAR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_kind
        if self.event_kind is not None:
            serialized = ARObject._serialize_item(self.event_kind, "DiagnosticEventKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize prestorage
        if self.prestorage is not None:
            serialized = ARObject._serialize_item(self.prestorage, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRESTORAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize prestored
        if self.prestored is not None:
            serialized = ARObject._serialize_item(self.prestored, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRESTORED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize recoverable_in
        if self.recoverable_in is not None:
            serialized = ARObject._serialize_item(self.recoverable_in, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RECOVERABLE-IN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEvent":
        """Deserialize XML element to DiagnosticEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEvent, cls).deserialize(element)

        # Parse associated
        child = ARObject._find_child_element(element, "ASSOCIATED")
        if child is not None:
            associated_value = child.text
            obj.associated = associated_value

        # Parse clear_event
        child = ARObject._find_child_element(element, "CLEAR-EVENT")
        if child is not None:
            clear_event_value = DiagnosticClearEventAllowedBehaviorEnum.deserialize(child)
            obj.clear_event = clear_event_value

        # Parse confirmation
        child = ARObject._find_child_element(element, "CONFIRMATION")
        if child is not None:
            confirmation_value = child.text
            obj.confirmation = confirmation_value

        # Parse connecteds (list from container "CONNECTEDS")
        obj.connecteds = []
        container = ARObject._find_child_element(element, "CONNECTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connecteds.append(child_value)

        # Parse event_clear
        child = ARObject._find_child_element(element, "EVENT-CLEAR")
        if child is not None:
            event_clear_value = DiagnosticEventClearAllowedEnum.deserialize(child)
            obj.event_clear = event_clear_value

        # Parse event_kind
        child = ARObject._find_child_element(element, "EVENT-KIND")
        if child is not None:
            event_kind_value = DiagnosticEventKindEnum.deserialize(child)
            obj.event_kind = event_kind_value

        # Parse prestorage
        child = ARObject._find_child_element(element, "PRESTORAGE")
        if child is not None:
            prestorage_value = child.text
            obj.prestorage = prestorage_value

        # Parse prestored
        child = ARObject._find_child_element(element, "PRESTORED")
        if child is not None:
            prestored_value = child.text
            obj.prestored = prestored_value

        # Parse recoverable_in
        child = ARObject._find_child_element(element, "RECOVERABLE-IN")
        if child is not None:
            recoverable_in_value = child.text
            obj.recoverable_in = recoverable_in_value

        return obj



class DiagnosticEventBuilder:
    """Builder for DiagnosticEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEvent = DiagnosticEvent()

    def build(self) -> DiagnosticEvent:
        """Build and return DiagnosticEvent object.

        Returns:
            DiagnosticEvent instance
        """
        # TODO: Add validation
        return self._obj
