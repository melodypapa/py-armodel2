"""DataPrototypeReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataPrototypeReference(ARObject, ABC):
    """AUTOSAR DataPrototypeReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    tag_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "TAG-ID": lambda obj, elem: setattr(obj, "tag_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DataPrototypeReference."""
        super().__init__()
        self.tag_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tag_id
        if self.tag_id is not None:
            serialized = SerializationHelper.serialize_item(self.tag_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TAG-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeReference":
        """Deserialize XML element to DataPrototypeReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeReference, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TAG-ID":
                setattr(obj, "tag_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DataPrototypeReferenceBuilder(BuilderBase, ABC):
    """Builder for DataPrototypeReference with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataPrototypeReference = DataPrototypeReference()


    def with_tag_id(self, value: Optional[PositiveInteger]) -> "DataPrototypeReferenceBuilder":
        """Set tag_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tag_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tagId",
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
    def build(self) -> DataPrototypeReference:
        """Build and return the DataPrototypeReference instance (abstract)."""
        raise NotImplementedError