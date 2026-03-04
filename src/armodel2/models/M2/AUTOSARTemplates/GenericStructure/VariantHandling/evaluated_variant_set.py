"""EvaluatedVariantSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.predefined_variant import (
    PredefinedVariant,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EvaluatedVariantSet(ARElement):
    """AUTOSAR EvaluatedVariantSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EVALUATED-VARIANT-SET"


    approval_status: NameToken
    evaluated_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "APPROVAL-STATUS": lambda obj, elem: setattr(obj, "approval_status", SerializationHelper.deserialize_by_tag(elem, "NameToken")),
        "EVALUATED-REFS": lambda obj, elem: [obj.evaluated_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize EvaluatedVariantSet."""
        super().__init__()
        self.approval_status: NameToken = None
        self.evaluated_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize EvaluatedVariantSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EvaluatedVariantSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize approval_status
        if self.approval_status is not None:
            serialized = SerializationHelper.serialize_item(self.approval_status, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPROVAL-STATUS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize evaluated_refs (list to container "EVALUATED-REFS")
        if self.evaluated_refs:
            wrapper = ET.Element("EVALUATED-REFS")
            for item in self.evaluated_refs:
                serialized = SerializationHelper.serialize_item(item, "PredefinedVariant")
                if serialized is not None:
                    child_elem = ET.Element("EVALUATED-REF")
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
    def deserialize(cls, element: ET.Element) -> "EvaluatedVariantSet":
        """Deserialize XML element to EvaluatedVariantSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EvaluatedVariantSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EvaluatedVariantSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "APPROVAL-STATUS":
                setattr(obj, "approval_status", SerializationHelper.deserialize_by_tag(child, "NameToken"))
            elif tag == "EVALUATED-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.evaluated_refs.append(ARRef.deserialize(item_elem))

        return obj



class EvaluatedVariantSetBuilder(ARElementBuilder):
    """Builder for EvaluatedVariantSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EvaluatedVariantSet = EvaluatedVariantSet()


    def with_approval_status(self, value: NameToken) -> "EvaluatedVariantSetBuilder":
        """Set approval_status attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.approval_status = value
        return self

    def with_evaluateds(self, items: list[PredefinedVariant]) -> "EvaluatedVariantSetBuilder":
        """Set evaluateds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.evaluateds = list(items) if items else []
        return self


    def add_evaluated(self, item: PredefinedVariant) -> "EvaluatedVariantSetBuilder":
        """Add a single item to evaluateds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.evaluateds.append(item)
        return self

    def clear_evaluateds(self) -> "EvaluatedVariantSetBuilder":
        """Clear all items from evaluateds list.

        Returns:
            self for method chaining
        """
        self._obj.evaluateds = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "approvalStatus",
    }
    _OPTIONAL_ATTRIBUTES = {
        "evaluated",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "approvalStatus", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError(f"Required attribute 'approvalStatus' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn(f"Required attribute 'approvalStatus' is None", UserWarning)


    def build(self) -> EvaluatedVariantSet:
        """Build and return the EvaluatedVariantSet instance with validation."""
        self._validate_instance()
        return self._obj