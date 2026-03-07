"""ReferenceTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 115)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import AttributeTailoringBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.unresolved_reference_restriction_with_severity import (
    UnresolvedReferenceRestrictionWithSeverity,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ReferenceTailoring(AttributeTailoring):
    """AUTOSAR ReferenceTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "REFERENCE-TAILORING"


    type_tailorings: list[ClassTailoring]
    unresolved_restriction_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "TYPE-TAILORINGS": ("_POLYMORPHIC_LIST", "type_tailorings", ["AbstractClassTailoring", "ConcreteClassTailoring"]),
        "UNRESOLVED-RESTRICTION-REF": lambda obj, elem: setattr(obj, "unresolved_restriction_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ReferenceTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []
        self.unresolved_restriction_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ReferenceTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReferenceTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_tailorings (list to container "TYPE-TAILORINGS")
        if self.type_tailorings:
            wrapper = ET.Element("TYPE-TAILORINGS")
            for item in self.type_tailorings:
                serialized = SerializationHelper.serialize_item(item, "ClassTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize unresolved_restriction_ref
        if self.unresolved_restriction_ref is not None:
            serialized = SerializationHelper.serialize_item(self.unresolved_restriction_ref, "UnresolvedReferenceRestrictionWithSeverity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNRESOLVED-RESTRICTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReferenceTailoring":
        """Deserialize XML element to ReferenceTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReferenceTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReferenceTailoring, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TYPE-TAILORINGS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "ABSTRACT-CLASS-TAILORING":
                        obj.type_tailorings.append(SerializationHelper.deserialize_by_tag(item_elem, "AbstractClassTailoring"))
                    elif concrete_tag == "CONCRETE-CLASS-TAILORING":
                        obj.type_tailorings.append(SerializationHelper.deserialize_by_tag(item_elem, "ConcreteClassTailoring"))
            elif tag == "UNRESOLVED-RESTRICTION-REF":
                setattr(obj, "unresolved_restriction_ref", ARRef.deserialize(child))

        return obj



class ReferenceTailoringBuilder(AttributeTailoringBuilder):
    """Builder for ReferenceTailoring with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ReferenceTailoring = ReferenceTailoring()


    def with_type_tailorings(self, items: list[ClassTailoring]) -> "ReferenceTailoringBuilder":
        """Set type_tailorings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.type_tailorings = list(items) if items else []
        return self

    def with_unresolved_restriction(self, value: Optional[UnresolvedReferenceRestrictionWithSeverity]) -> "ReferenceTailoringBuilder":
        """Set unresolved_restriction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'unresolved_restriction' is required and cannot be None")
        self._obj.unresolved_restriction = value
        return self


    def add_type_tailoring(self, item: ClassTailoring) -> "ReferenceTailoringBuilder":
        """Add a single item to type_tailorings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.type_tailorings.append(item)
        return self

    def clear_type_tailorings(self) -> "ReferenceTailoringBuilder":
        """Clear all items from type_tailorings list.

        Returns:
            self for method chaining
        """
        self._obj.type_tailorings = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "typeTailoring",
        "unresolvedRestriction",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ReferenceTailoring:
        """Build and return the ReferenceTailoring instance with validation."""
        self._validate_instance()
        return self._obj