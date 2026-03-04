"""DiagnosticDataIdentifierSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticDataIdentifierSet(DiagnosticCommonElement):
    """AUTOSAR DiagnosticDataIdentifierSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-DATA-IDENTIFIER-SET"


    data_identifier_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-IDENTIFIER-REFS": lambda obj, elem: [obj.data_identifier_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifierSet."""
        super().__init__()
        self.data_identifier_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticDataIdentifierSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticDataIdentifierSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_identifier_refs (list to container "DATA-IDENTIFIER-REFS")
        if self.data_identifier_refs:
            wrapper = ET.Element("DATA-IDENTIFIER-REFS")
            for item in self.data_identifier_refs:
                serialized = SerializationHelper.serialize_item(item, "DiagnosticDataIdentifier")
                if serialized is not None:
                    child_elem = ET.Element("DATA-IDENTIFIER-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticDataIdentifierSet":
        """Deserialize XML element to DiagnosticDataIdentifierSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticDataIdentifierSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticDataIdentifierSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-IDENTIFIER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.data_identifier_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticDataIdentifierSetBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticDataIdentifierSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticDataIdentifierSet = DiagnosticDataIdentifierSet()


    def with_data_identifiers(self, items: list[DiagnosticDataIdentifier]) -> "DiagnosticDataIdentifierSetBuilder":
        """Set data_identifiers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_identifiers = list(items) if items else []
        return self


    def add_data_identifier(self, item: DiagnosticDataIdentifier) -> "DiagnosticDataIdentifierSetBuilder":
        """Add a single item to data_identifiers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_identifiers.append(item)
        return self

    def clear_data_identifiers(self) -> "DiagnosticDataIdentifierSetBuilder":
        """Clear all items from data_identifiers list.

        Returns:
            self for method chaining
        """
        self._obj.data_identifiers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataIdentifier",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticDataIdentifierSet:
        """Build and return the DiagnosticDataIdentifierSet instance with validation."""
        self._validate_instance()
        return self._obj