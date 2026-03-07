"""DiagnosticEnableConditionGroup AUTOSAR element.

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


class DiagnosticEnableConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticEnableConditionGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-ENABLE-CONDITION-GROUP"


    enable_condition_refs: list[Any]
    _DESERIALIZE_DISPATCH = {
        "ENABLE-CONDITION-REFS": lambda obj, elem: [obj.enable_condition_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize DiagnosticEnableConditionGroup."""
        super().__init__()
        self.enable_condition_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnableConditionGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnableConditionGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize enable_condition_refs (list to container "ENABLE-CONDITION-REFS")
        if self.enable_condition_refs:
            wrapper = ET.Element("ENABLE-CONDITION-REFS")
            for item in self.enable_condition_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("ENABLE-CONDITION-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableConditionGroup":
        """Deserialize XML element to DiagnosticEnableConditionGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnableConditionGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnableConditionGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ENABLE-CONDITION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.enable_condition_refs.append(ARRef.deserialize(item_elem))

        return obj



class DiagnosticEnableConditionGroupBuilder(DiagnosticConditionGroupBuilder):
    """Builder for DiagnosticEnableConditionGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEnableConditionGroup = DiagnosticEnableConditionGroup()


    def with_enable_conditions(self, items: list[Any]) -> "DiagnosticEnableConditionGroupBuilder":
        """Set enable_conditions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.enable_conditions = list(items) if items else []
        return self


    def add_enable_condition(self, item: Any) -> "DiagnosticEnableConditionGroupBuilder":
        """Add a single item to enable_conditions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.enable_conditions.append(item)
        return self

    def clear_enable_conditions(self) -> "DiagnosticEnableConditionGroupBuilder":
        """Clear all items from enable_conditions list.

        Returns:
            self for method chaining
        """
        self._obj.enable_conditions = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "enableCondition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticEnableConditionGroup:
        """Build and return the DiagnosticEnableConditionGroup instance with validation."""
        self._validate_instance()
        return self._obj