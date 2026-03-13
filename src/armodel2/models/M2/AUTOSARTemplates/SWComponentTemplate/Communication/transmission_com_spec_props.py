"""TransmissionComSpecProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 179)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2075)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    TransmissionModeDefinitionEnum,
)
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


    data_update_period: Optional[TimeValue]
    minimum_send_interval: Optional[TimeValue]
    transmission_mode: Optional[TransmissionModeDefinitionEnum]
    _DESERIALIZE_DISPATCH = {
        "DATA-UPDATE-PERIOD": lambda obj, elem: setattr(obj, "data_update_period", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "MINIMUM-SEND-INTERVAL": lambda obj, elem: setattr(obj, "minimum_send_interval", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TRANSMISSION-MODE": lambda obj, elem: setattr(obj, "transmission_mode", TransmissionModeDefinitionEnum.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TransmissionComSpecProps."""
        super().__init__()
        self.data_update_period: Optional[TimeValue] = None
        self.minimum_send_interval: Optional[TimeValue] = None
        self.transmission_mode: Optional[TransmissionModeDefinitionEnum] = None

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

        # Serialize data_update_period
        if self.data_update_period is not None:
            serialized = SerializationHelper.serialize_item(self.data_update_period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-UPDATE-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minimum_send_interval
        if self.minimum_send_interval is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_send_interval, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-SEND-INTERVAL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission_mode
        if self.transmission_mode is not None:
            serialized = SerializationHelper.serialize_item(self.transmission_mode, "TransmissionModeDefinitionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-MODE")
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
            if tag == "DATA-UPDATE-PERIOD":
                setattr(obj, "data_update_period", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "MINIMUM-SEND-INTERVAL":
                setattr(obj, "minimum_send_interval", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TRANSMISSION-MODE":
                setattr(obj, "transmission_mode", TransmissionModeDefinitionEnum.deserialize(child))

        return obj



class TransmissionComSpecPropsBuilder(BuilderBase):
    """Builder for TransmissionComSpecProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransmissionComSpecProps = TransmissionComSpecProps()


    def with_data_update_period(self, value: Optional[TimeValue]) -> "TransmissionComSpecPropsBuilder":
        """Set data_update_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_update_period' is required and cannot be None")
        self._obj.data_update_period = value
        return self

    def with_minimum_send_interval(self, value: Optional[TimeValue]) -> "TransmissionComSpecPropsBuilder":
        """Set minimum_send_interval attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minimum_send_interval' is required and cannot be None")
        self._obj.minimum_send_interval = value
        return self

    def with_transmission_mode(self, value: Optional[TransmissionModeDefinitionEnum]) -> "TransmissionComSpecPropsBuilder":
        """Set transmission_mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'transmission_mode' is required and cannot be None")
        self._obj.transmission_mode = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataUpdatePeriod",
        "minimumSendInterval",
        "transmissionMode",
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