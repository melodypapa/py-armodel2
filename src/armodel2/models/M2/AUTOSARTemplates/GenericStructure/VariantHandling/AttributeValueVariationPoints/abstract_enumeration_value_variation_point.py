"""AbstractEnumerationValueVariationPoint AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 421)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling_AttributeValueVariationPoints.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    Ref,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractEnumerationValueVariationPoint(ARObject, ABC):
    """AUTOSAR AbstractEnumerationValueVariationPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    base: Optional[Identifier]
    enum_table_ref: Optional[Ref]
    _DESERIALIZE_DISPATCH = {
        "BASE": lambda obj, elem: setattr(obj, "base", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "ENUM-TABLE-REF": lambda obj, elem: setattr(obj, "enum_table_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize AbstractEnumerationValueVariationPoint."""
        super().__init__()
        self.base: Optional[Identifier] = None
        self.enum_table_ref: Optional[Ref] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractEnumerationValueVariationPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractEnumerationValueVariationPoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize base
        if self.base is not None:
            serialized = SerializationHelper.serialize_item(self.base, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize enum_table_ref
        if self.enum_table_ref is not None:
            serialized = SerializationHelper.serialize_item(self.enum_table_ref, "Ref")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENUM-TABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEnumerationValueVariationPoint":
        """Deserialize XML element to AbstractEnumerationValueVariationPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractEnumerationValueVariationPoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractEnumerationValueVariationPoint, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BASE":
                setattr(obj, "base", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "ENUM-TABLE-REF":
                setattr(obj, "enum_table_ref", ARRef.deserialize(child))

        return obj



class AbstractEnumerationValueVariationPointBuilder(BuilderBase, ABC):
    """Builder for AbstractEnumerationValueVariationPoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractEnumerationValueVariationPoint = AbstractEnumerationValueVariationPoint()


    def with_base(self, value: Optional[Identifier]) -> "AbstractEnumerationValueVariationPointBuilder":
        """Set base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'base' is required and cannot be None")
        self._obj.base = value
        return self

    def with_enum_table(self, value: Optional[Ref]) -> "AbstractEnumerationValueVariationPointBuilder":
        """Set enum_table attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'enum_table' is required and cannot be None")
        self._obj.enum_table = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "base",
        "enumTable",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> AbstractEnumerationValueVariationPoint:
        """Build and return the AbstractEnumerationValueVariationPoint instance (abstract)."""
        raise NotImplementedError