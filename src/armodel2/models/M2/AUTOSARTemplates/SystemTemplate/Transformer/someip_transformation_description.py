"""SOMEIPTransformationDescription AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 777)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import (
    TransformationDescription,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_description import TransformationDescriptionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SOMEIPTransformationDescription(TransformationDescription):
    """AUTOSAR SOMEIPTransformationDescription."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "S-O-M-E-I-P-TRANSFORMATION-DESCRIPTION"


    alignment: Optional[PositiveInteger]
    byte_order: Optional[ByteOrderEnum]
    interface_version: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALIGNMENT": lambda obj, elem: setattr(obj, "alignment", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "BYTE-ORDER": lambda obj, elem: setattr(obj, "byte_order", ByteOrderEnum.deserialize(elem)),
        "INTERFACE-VERSION": lambda obj, elem: setattr(obj, "interface_version", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize SOMEIPTransformationDescription."""
        super().__init__()
        self.alignment: Optional[PositiveInteger] = None
        self.byte_order: Optional[ByteOrderEnum] = None
        self.interface_version: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize SOMEIPTransformationDescription to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SOMEIPTransformationDescription, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alignment
        if self.alignment is not None:
            serialized = SerializationHelper.serialize_item(self.alignment, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIGNMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize byte_order
        if self.byte_order is not None:
            serialized = SerializationHelper.serialize_item(self.byte_order, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BYTE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize interface_version
        if self.interface_version is not None:
            serialized = SerializationHelper.serialize_item(self.interface_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INTERFACE-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SOMEIPTransformationDescription":
        """Deserialize XML element to SOMEIPTransformationDescription object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SOMEIPTransformationDescription object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SOMEIPTransformationDescription, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALIGNMENT":
                setattr(obj, "alignment", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "BYTE-ORDER":
                setattr(obj, "byte_order", ByteOrderEnum.deserialize(child))
            elif tag == "INTERFACE-VERSION":
                setattr(obj, "interface_version", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class SOMEIPTransformationDescriptionBuilder(TransformationDescriptionBuilder):
    """Builder for SOMEIPTransformationDescription with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SOMEIPTransformationDescription = SOMEIPTransformationDescription()


    def with_alignment(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationDescriptionBuilder":
        """Set alignment attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alignment = value
        return self

    def with_byte_order(self, value: Optional[ByteOrderEnum]) -> "SOMEIPTransformationDescriptionBuilder":
        """Set byte_order attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.byte_order = value
        return self

    def with_interface_version(self, value: Optional[PositiveInteger]) -> "SOMEIPTransformationDescriptionBuilder":
        """Set interface_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.interface_version = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "alignment",
        "byteOrder",
        "interfaceVersion",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SOMEIPTransformationDescription:
        """Build and return the SOMEIPTransformationDescription instance with validation."""
        self._validate_instance()
        return self._obj