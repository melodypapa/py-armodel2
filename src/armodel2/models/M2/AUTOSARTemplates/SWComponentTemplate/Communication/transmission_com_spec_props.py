"""TransmissionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2075)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransmissionComSpecProps(ARObject):
    """AUTOSAR TransmissionComSpecProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRANSMISSION-COM-SPEC-PROPS"


    data_update: Optional[TimeValue]
    minimum_send: Optional[TimeValue]
    transmission: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DATA-UPDATE": lambda obj, elem: setattr(obj, "data_update", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "MINIMUM-SEND": lambda obj, elem: setattr(obj, "minimum_send", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TRANSMISSION": lambda obj, elem: setattr(obj, "transmission", SerializationHelper.deserialize_by_tag(elem, "any (TransmissionMode)")),
    }


    def __init__(self) -> None:
        """Initialize TransmissionComSpecProps."""
        super().__init__()
        self.data_update: Optional[TimeValue] = None
        self.minimum_send: Optional[TimeValue] = None
        self.transmission: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TransmissionComSpecProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransmissionComSpecProps, self).serialize()

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

        # Serialize minimum_send
        if self.minimum_send is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_send, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-SEND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission
        if self.transmission is not None:
            serialized = SerializationHelper.serialize_item(self.transmission, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionComSpecProps":
        """Deserialize XML element to TransmissionComSpecProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionComSpecProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransmissionComSpecProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-UPDATE":
                setattr(obj, "data_update", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "MINIMUM-SEND":
                setattr(obj, "minimum_send", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TRANSMISSION":
                setattr(obj, "transmission", SerializationHelper.deserialize_by_tag(child, "any (TransmissionMode)"))

        return obj



class TransmissionComSpecPropsBuilder(BuilderBase):
    """Builder for TransmissionComSpecProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransmissionComSpecProps = TransmissionComSpecProps()


    def with_data_update(self, value: Optional[TimeValue]) -> "TransmissionComSpecPropsBuilder":
        """Set data_update attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_update' is required and cannot be None")
        self._obj.data_update = value
        return self

    def with_minimum_send(self, value: Optional[TimeValue]) -> "TransmissionComSpecPropsBuilder":
        """Set minimum_send attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minimum_send' is required and cannot be None")
        self._obj.minimum_send = value
        return self

    def with_transmission(self, value: Optional[Any]) -> "TransmissionComSpecPropsBuilder":
        """Set transmission attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'transmission' is required and cannot be None")
        self._obj.transmission = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataUpdate",
        "minimumSend",
        "transmission",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TransmissionComSpecProps:
        """Build and return the TransmissionComSpecProps instance with validation."""
        self._validate_instance()
        return self._obj