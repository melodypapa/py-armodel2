"""SecurityEventStateFilter AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 22)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import (
    AbstractSecurityEventFilter,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.abstract_security_event_filter import AbstractSecurityEventFilterBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SecurityEventStateFilter(AbstractSecurityEventFilter):
    """AUTOSAR SecurityEventStateFilter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECURITY-EVENT-STATE-FILTER"


    block_if_state_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BLOCK-IF-STATE-REFS": lambda obj, elem: [obj.block_if_state_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize SecurityEventStateFilter."""
        super().__init__()
        self.block_if_state_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SecurityEventStateFilter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecurityEventStateFilter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize block_if_state_refs (list to container "BLOCK-IF-STATE-REFS")
        if self.block_if_state_refs:
            wrapper = ET.Element("BLOCK-IF-STATE-REFS")
            for item in self.block_if_state_refs:
                serialized = SerializationHelper.serialize_item(item, "BlockState")
                if serialized is not None:
                    child_elem = ET.Element("BLOCK-IF-STATE-REF")
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
    def deserialize(cls, element: ET.Element) -> "SecurityEventStateFilter":
        """Deserialize XML element to SecurityEventStateFilter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecurityEventStateFilter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecurityEventStateFilter, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BLOCK-IF-STATE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.block_if_state_refs.append(ARRef.deserialize(item_elem))

        return obj



class SecurityEventStateFilterBuilder(AbstractSecurityEventFilterBuilder):
    """Builder for SecurityEventStateFilter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SecurityEventStateFilter = SecurityEventStateFilter()


    def with_block_if_states(self, items: list[BlockState]) -> "SecurityEventStateFilterBuilder":
        """Set block_if_states list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.block_if_states = list(items) if items else []
        return self


    def add_block_if_state(self, item: BlockState) -> "SecurityEventStateFilterBuilder":
        """Add a single item to block_if_states list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.block_if_states.append(item)
        return self

    def clear_block_if_states(self) -> "SecurityEventStateFilterBuilder":
        """Clear all items from block_if_states list.

        Returns:
            self for method chaining
        """
        self._obj.block_if_states = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "blockIfState",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SecurityEventStateFilter:
        """Build and return the SecurityEventStateFilter instance with validation."""
        self._validate_instance()
        return self._obj