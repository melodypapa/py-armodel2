"""DiagnosticFimEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 217)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticFimEventGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFimEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-FIM-EVENT-GROUP"


    event_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "EVENT-REFS": lambda obj, elem: [obj.event_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticFimEventGroup."""
        super().__init__()
        self.event_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimEventGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimEventGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize event_refs (list to container "EVENT-REFS")
        if self.event_refs:
            wrapper = ET.Element("EVENT-REFS")
            for item in self.event_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticEvent")
                if serialized is not None:
                    child_elem = ET.Element("EVENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimEventGroup":
        """Deserialize XML element to DiagnosticFimEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimEventGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimEventGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EVENT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.event_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticFimEventGroupBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticFimEventGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticFimEventGroup = DiagnosticFimEventGroup()


    def with_events(self, items: list[DiagnosticEvent]) -> "DiagnosticFimEventGroupBuilder":
        """Set events list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.events = list(items) if items else []
        return self


    def add_event(self, item: DiagnosticEvent) -> "DiagnosticFimEventGroupBuilder":
        """Add a single item to events list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.events.append(item)
        return self

    def clear_events(self) -> "DiagnosticFimEventGroupBuilder":
        """Clear all items from events list.

        Returns:
            self for method chaining
        """
        self._obj.events = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "event",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticFimEventGroup:
        """Build and return the DiagnosticFimEventGroup instance with validation."""
        self._validate_instance()
        return self._obj