"""DiagnosticStorageConditionGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticConditionGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
    DiagnosticConditionGroup,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import DiagnosticConditionGroupBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticStorageConditionGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-STORAGE-CONDITION-GROUP"


    storage_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "STORAGE-REFS": lambda obj, elem: [obj.storage_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionGroup."""
        super().__init__()
        self.storage_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStorageConditionGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStorageConditionGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize storage_refs (list to container "STORAGE-REFS")
        if self.storage_refs:
            wrapper = ET.Element("STORAGE-REFS")
            for item in self.storage_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("STORAGE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionGroup":
        """Deserialize XML element to DiagnosticStorageConditionGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageConditionGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStorageConditionGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "STORAGE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.storage_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticStorageConditionGroupBuilder(DiagnosticConditionGroupBuilder):
    """Builder for DiagnosticStorageConditionGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticStorageConditionGroup = DiagnosticStorageConditionGroup()


    def with_storages(self, items: list[any (DiagnosticStorage)]) -> "DiagnosticStorageConditionGroupBuilder":
        """Set storages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.storages = list(items) if items else []
        return self


    def add_storage(self, item: any (DiagnosticStorage)) -> "DiagnosticStorageConditionGroupBuilder":
        """Add a single item to storages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.storages.append(item)
        return self

    def clear_storages(self) -> "DiagnosticStorageConditionGroupBuilder":
        """Clear all items from storages list.

        Returns:
            self for method chaining
        """
        self._obj.storages = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "storage",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticStorageConditionGroup:
        """Build and return the DiagnosticStorageConditionGroup instance with validation."""
        self._validate_instance()
        return self._obj