"""ReceptionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ReceptionComSpecProps(ARObject):
    """AUTOSAR ReceptionComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RECEPTION-COM-SPEC-PROPS"


    data_update: Optional[TimeValue]
    timeout: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "DATA-UPDATE": lambda obj, elem: setattr(obj, "data_update", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TIMEOUT": lambda obj, elem: setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize ReceptionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize ReceptionComSpecProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ReceptionComSpecProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_update
        if self.data_update is not None:
            serialized = SerializationHelper.serialize_item(self.data_update, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-UPDATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout
        if self.timeout is not None:
            serialized = SerializationHelper.serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ReceptionComSpecProps":
        """Deserialize XML element to ReceptionComSpecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ReceptionComSpecProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ReceptionComSpecProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-UPDATE":
                setattr(obj, "data_update", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TIMEOUT":
                setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class ReceptionComSpecPropsBuilder(BuilderBase):
    """Builder for ReceptionComSpecProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ReceptionComSpecProps = ReceptionComSpecProps()


    def with_data_update(self, value: Optional[TimeValue]) -> "ReceptionComSpecPropsBuilder":
        """Set data_update attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_update = value
        return self

    def with_timeout(self, value: Optional[TimeValue]) -> "ReceptionComSpecPropsBuilder":
        """Set timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataUpdate",
        "timeout",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ReceptionComSpecProps:
        """Build and return the ReceptionComSpecProps instance with validation."""
        self._validate_instance()
        return self._obj