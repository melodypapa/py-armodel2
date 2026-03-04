"""ConsistencyNeedsBlueprintSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 179)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_Blueprint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.consistency_needs import (
    ConsistencyNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConsistencyNeedsBlueprintSet(ARElement):
    """AUTOSAR ConsistencyNeedsBlueprintSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSISTENCY-NEEDS-BLUEPRINT-SET"


    consistency_needses: list[ConsistencyNeeds]
    _DESERIALIZE_DISPATCH = {
        "CONSISTENCY-NEEDSS": lambda obj, elem: obj.consistency_needses.append(SerializationHelper.deserialize_by_tag(elem, "ConsistencyNeeds")),
    }


    def __init__(self) -> None:
        """Initialize ConsistencyNeedsBlueprintSet."""
        super().__init__()
        self.consistency_needses: list[ConsistencyNeeds] = []

    def serialize(self) -> ET.Element:
        """Serialize ConsistencyNeedsBlueprintSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsistencyNeedsBlueprintSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consistency_needses (list to container "CONSISTENCY-NEEDSS")
        if self.consistency_needses:
            wrapper = ET.Element("CONSISTENCY-NEEDSS")
            for item in self.consistency_needses:
                serialized = SerializationHelper.serialize_item(item, "ConsistencyNeeds")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeedsBlueprintSet":
        """Deserialize XML element to ConsistencyNeedsBlueprintSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsistencyNeedsBlueprintSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsistencyNeedsBlueprintSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONSISTENCY-NEEDSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.consistency_needses.append(SerializationHelper.deserialize_by_tag(item_elem, "ConsistencyNeeds"))

        return obj



class ConsistencyNeedsBlueprintSetBuilder(ARElementBuilder):
    """Builder for ConsistencyNeedsBlueprintSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConsistencyNeedsBlueprintSet = ConsistencyNeedsBlueprintSet()


    def with_consistency_needses(self, items: list[ConsistencyNeeds]) -> "ConsistencyNeedsBlueprintSetBuilder":
        """Set consistency_needses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = list(items) if items else []
        return self


    def add_consistency_needs(self, item: ConsistencyNeeds) -> "ConsistencyNeedsBlueprintSetBuilder":
        """Add a single item to consistency_needses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses.append(item)
        return self

    def clear_consistency_needses(self) -> "ConsistencyNeedsBlueprintSetBuilder":
        """Clear all items from consistency_needses list.

        Returns:
            self for method chaining
        """
        self._obj.consistency_needses = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "consistencyNeeds",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ConsistencyNeedsBlueprintSet:
        """Build and return the ConsistencyNeedsBlueprintSet instance with validation."""
        self._validate_instance()
        return self._obj