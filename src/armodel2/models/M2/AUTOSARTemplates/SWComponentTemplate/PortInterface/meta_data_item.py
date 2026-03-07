"""MetaDataItem AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 98)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2037)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Constants.text_value_specification import (
    TextValueSpecification,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MetaDataItem(ARObject):
    """AUTOSAR MetaDataItem."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "META-DATA-ITEM"


    length: Optional[PositiveInteger]
    meta_data_item: Optional[TextValueSpecification]
    _DESERIALIZE_DISPATCH = {
        "LENGTH": lambda obj, elem: setattr(obj, "length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "META-DATA-ITEM": lambda obj, elem: setattr(obj, "meta_data_item", SerializationHelper.deserialize_by_tag(elem, "TextValueSpecification")),
    }


    def __init__(self) -> None:
        """Initialize MetaDataItem."""
        super().__init__()
        self.length: Optional[PositiveInteger] = None
        self.meta_data_item: Optional[TextValueSpecification] = None

    def serialize(self) -> ET.Element:
        """Serialize MetaDataItem to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MetaDataItem, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize length
        if self.length is not None:
            serialized = SerializationHelper.serialize_item(self.length, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize meta_data_item
        if self.meta_data_item is not None:
            serialized = SerializationHelper.serialize_item(self.meta_data_item, "TextValueSpecification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("META-DATA-ITEM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MetaDataItem":
        """Deserialize XML element to MetaDataItem object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MetaDataItem object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MetaDataItem, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LENGTH":
                setattr(obj, "length", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "META-DATA-ITEM":
                setattr(obj, "meta_data_item", SerializationHelper.deserialize_by_tag(child, "TextValueSpecification"))

        return obj



class MetaDataItemBuilder(BuilderBase):
    """Builder for MetaDataItem with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MetaDataItem = MetaDataItem()


    def with_length(self, value: Optional[PositiveInteger]) -> "MetaDataItemBuilder":
        """Set length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'length' is required and cannot be None")
        self._obj.length = value
        return self

    def with_meta_data_item(self, value: Optional[TextValueSpecification]) -> "MetaDataItemBuilder":
        """Set meta_data_item attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'meta_data_item' is required and cannot be None")
        self._obj.meta_data_item = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "length",
        "metaDataItem",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> MetaDataItem:
        """Build and return the MetaDataItem instance with validation."""
        self._validate_instance()
        return self._obj