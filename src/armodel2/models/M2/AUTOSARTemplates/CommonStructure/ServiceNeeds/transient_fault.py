"""TransientFault AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1009)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import (
    TracedFailure,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.traced_failure import TracedFailureBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransientFault(TracedFailure):
    """AUTOSAR TransientFault."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRANSIENT-FAULT"


    possible_error_reactions: list[Any]
    _DESERIALIZE_DISPATCH = {
        "POSSIBLE-ERROR-REACTIONS": lambda obj, elem: obj.possible_error_reactions.append(SerializationHelper.deserialize_by_tag(elem, "any (PossibleErrorReaction)")),
    }


    def __init__(self) -> None:
        """Initialize TransientFault."""
        super().__init__()
        self.possible_error_reactions: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize TransientFault to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransientFault, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize possible_error_reactions (list to container "POSSIBLE-ERROR-REACTIONS")
        if self.possible_error_reactions:
            wrapper = ET.Element("POSSIBLE-ERROR-REACTIONS")
            for item in self.possible_error_reactions:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransientFault":
        """Deserialize XML element to TransientFault object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransientFault object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransientFault, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "POSSIBLE-ERROR-REACTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.possible_error_reactions.append(SerializationHelper.deserialize_by_tag(item_elem, "any (PossibleErrorReaction)"))

        return obj



class TransientFaultBuilder(TracedFailureBuilder):
    """Builder for TransientFault with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransientFault = TransientFault()


    def with_possible_error_reactions(self, items: list[Any]) -> "TransientFaultBuilder":
        """Set possible_error_reactions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.possible_error_reactions = list(items) if items else []
        return self


    def add_possible_error_reaction(self, item: Any) -> "TransientFaultBuilder":
        """Add a single item to possible_error_reactions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.possible_error_reactions.append(item)
        return self

    def clear_possible_error_reactions(self) -> "TransientFaultBuilder":
        """Clear all items from possible_error_reactions list.

        Returns:
            self for method chaining
        """
        self._obj.possible_error_reactions = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "possibleErrorReaction",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TransientFault:
        """Build and return the TransientFault instance with validation."""
        self._validate_instance()
        return self._obj