"""EndToEndTransformationISignalProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 808)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import atp_variant

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


@atp_variant()

class EndToEndTransformationISignalProps(ARObject):
    """AUTOSAR EndToEndTransformationISignalProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS"


    data_length: Optional[PositiveInteger]
    max_data_length: Optional[PositiveInteger]
    min_data_length: Optional[PositiveInteger]
    source_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "DATA-LENGTH": lambda obj, elem: setattr(obj, "data_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MAX-DATA-LENGTH": lambda obj, elem: setattr(obj, "max_data_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MIN-DATA-LENGTH": lambda obj, elem: setattr(obj, "min_data_length", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOURCE-ID": lambda obj, elem: setattr(obj, "source_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize EndToEndTransformationISignalProps."""
        super().__init__()
        self.data_length: Optional[PositiveInteger] = None
        self.max_data_length: Optional[PositiveInteger] = None
        self.min_data_length: Optional[PositiveInteger] = None
        self.source_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize EndToEndTransformationISignalProps to XML element with atp_variant wrapper.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EndToEndTransformationISignalProps, self).serialize()

        # Copy all attributes from parent element to outer element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element to outer element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Create inner element to hold attributes before wrapping
        inner_elem = ET.Element("INNER")

        # Copy parent's children: metadata to outer element, others to inner element
        metadata_tags = {'SHORT-NAME', 'LONG-NAME', 'DESC', 'ADMIN-DATA'}
        for child in parent_elem:
            tag = SerializationHelper.strip_namespace(child.tag)
            if tag in metadata_tags:
                # Metadata elements stay outside the atp_variant wrapper
                elem.append(child)
            else:
                # Other elements go inside the atp_variant wrapper
                inner_elem.append(child)

        # Serialize data_length
        if self.data_length is not None:
            serialized = SerializationHelper.serialize_item(self.data_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize max_data_length
        if self.max_data_length is not None:
            serialized = SerializationHelper.serialize_item(self.max_data_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("MAX-DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize min_data_length
        if self.min_data_length is not None:
            serialized = SerializationHelper.serialize_item(self.min_data_length, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("MIN-DATA-LENGTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Serialize source_id
        if self.source_id is not None:
            serialized = SerializationHelper.serialize_item(self.source_id, "PositiveInteger")
            if serialized is not None:
                wrapped = ET.Element("SOURCE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                inner_elem.append(wrapped)

        # Wrap inner element in atp_variant VARIANTS/CONDITIONAL structure
        wrapped = SerializationHelper.serialize_with_atp_variant(inner_elem, "EndToEndTransformationISignalProps")
        elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndTransformationISignalProps":
        """Deserialize XML element to EndToEndTransformationISignalProps object with atp_variant unwrapping.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EndToEndTransformationISignalProps object
        """
        # Unwrap atp_variant VARIANTS/CONDITIONAL structure
        inner_elem = SerializationHelper.deserialize_from_atp_variant(element, "EndToEndTransformationISignalProps")
        if inner_elem is None:
            # No wrapper structure found, create instance with default values
            obj = cls.__new__(cls)
            obj.__init__()
            return obj

        # Temporarily copy children from inner element to outer element
        # so parent's deserialize can find inherited attributes
        for child in list(inner_elem):
            element.append(child)

        # Call parent's deserialize with outer element (now contains parent's children)
        obj = super(EndToEndTransformationISignalProps, cls).deserialize(element)

        # Clean up: remove the temporarily copied children from outer element
        # (they are now in obj, so we don't need them in element anymore)
        for child in list(inner_elem):
            element.remove(child)

        # Parse data_length
        child = SerializationHelper.find_child_element(inner_elem, "DATA-LENGTH")
        if child is not None:
            data_length_value = child.text
            obj.data_length = data_length_value

        # Parse max_data_length
        child = SerializationHelper.find_child_element(inner_elem, "MAX-DATA-LENGTH")
        if child is not None:
            max_data_length_value = child.text
            obj.max_data_length = max_data_length_value

        # Parse min_data_length
        child = SerializationHelper.find_child_element(inner_elem, "MIN-DATA-LENGTH")
        if child is not None:
            min_data_length_value = child.text
            obj.min_data_length = min_data_length_value

        # Parse source_id
        child = SerializationHelper.find_child_element(inner_elem, "SOURCE-ID")
        if child is not None:
            source_id_value = child.text
            obj.source_id = source_id_value

        return obj



class EndToEndTransformationISignalPropsBuilder(BuilderBase):
    """Builder for EndToEndTransformationISignalProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EndToEndTransformationISignalProps = EndToEndTransformationISignalProps()


    def with_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_length' is required and cannot be None")
        self._obj.data_length = value
        return self

    def with_max_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set max_data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'max_data_length' is required and cannot be None")
        self._obj.max_data_length = value
        return self

    def with_min_data_length(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set min_data_length attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'min_data_length' is required and cannot be None")
        self._obj.min_data_length = value
        return self

    def with_source_id(self, value: Optional[PositiveInteger]) -> "EndToEndTransformationISignalPropsBuilder":
        """Set source_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'source_id' is required and cannot be None")
        self._obj.source_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataLength",
        "maxDataLength",
        "minDataLength",
        "sourceId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EndToEndTransformationISignalProps:
        """Build and return the EndToEndTransformationISignalProps instance with validation."""
        self._validate_instance()
        return self._obj