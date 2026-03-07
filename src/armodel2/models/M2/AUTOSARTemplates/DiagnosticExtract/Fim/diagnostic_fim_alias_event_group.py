"""DiagnosticFimAliasEventGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 263)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import (
    DiagnosticAbstractAliasEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_abstract_alias_event import DiagnosticAbstractAliasEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticFimAliasEventGroup(DiagnosticAbstractAliasEvent):
    """AUTOSAR DiagnosticFimAliasEventGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP"


    grouped_alia_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "GROUPED-ALIAS-REFS": lambda obj, elem: [obj.grouped_alia_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticFimAliasEventGroup."""
        super().__init__()
        self.grouped_alia_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimAliasEventGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimAliasEventGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize grouped_alia_refs (list to container "GROUPED-ALIAS-REFS")
        if self.grouped_alia_refs:
            wrapper = ET.Element("GROUPED-ALIAS-REFS")
            for item in self.grouped_alia_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("GROUPED-ALIA-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimAliasEventGroup":
        """Deserialize XML element to DiagnosticFimAliasEventGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimAliasEventGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimAliasEventGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "GROUPED-ALIAS-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.grouped_alia_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticFimAliasEventGroupBuilder(DiagnosticAbstractAliasEventBuilder):
    """Builder for DiagnosticFimAliasEventGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticFimAliasEventGroup = DiagnosticFimAliasEventGroup()


    def with_grouped_aliases(self, items: list[Any]) -> "DiagnosticFimAliasEventGroupBuilder":
        """Set grouped_aliases list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.grouped_aliases = list(items) if items else []
        return self


    def add_grouped_alias(self, item: Any) -> "DiagnosticFimAliasEventGroupBuilder":
        """Add a single item to grouped_aliases list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.grouped_aliases.append(item)
        return self

    def clear_grouped_aliases(self) -> "DiagnosticFimAliasEventGroupBuilder":
        """Clear all items from grouped_aliases list.

        Returns:
            self for method chaining
        """
        self._obj.grouped_aliases = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "groupedAlias",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticFimAliasEventGroup:
        """Build and return the DiagnosticFimAliasEventGroup instance with validation."""
        self._validate_instance()
        return self._obj