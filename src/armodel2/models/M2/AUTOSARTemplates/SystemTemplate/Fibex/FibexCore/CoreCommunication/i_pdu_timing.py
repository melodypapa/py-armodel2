"""IPduTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 348)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import DescribableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.transmission_mode_declaration import (
    TransmissionModeDeclaration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IPduTiming(Describable):
    """AUTOSAR IPduTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-PDU-TIMING"


    minimum_delay: Optional[TimeValue]
    transmission_mode_declaration: Optional[TransmissionModeDeclaration]
    _DESERIALIZE_DISPATCH = {
        "MINIMUM-DELAY": lambda obj, elem: setattr(obj, "minimum_delay", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TRANSMISSION-MODE-DECLARATION": lambda obj, elem: setattr(obj, "transmission_mode_declaration", SerializationHelper.deserialize_by_tag(elem, "TransmissionModeDeclaration")),
    }


    def __init__(self) -> None:
        """Initialize IPduTiming."""
        super().__init__()
        self.minimum_delay: Optional[TimeValue] = None
        self.transmission_mode_declaration: Optional[TransmissionModeDeclaration] = None

    def serialize(self) -> ET.Element:
        """Serialize IPduTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IPduTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize minimum_delay
        if self.minimum_delay is not None:
            serialized = SerializationHelper.serialize_item(self.minimum_delay, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINIMUM-DELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission_mode_declaration
        if self.transmission_mode_declaration is not None:
            serialized = SerializationHelper.serialize_item(self.transmission_mode_declaration, "TransmissionModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-MODE-DECLARATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPduTiming":
        """Deserialize XML element to IPduTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPduTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IPduTiming, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MINIMUM-DELAY":
                setattr(obj, "minimum_delay", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TRANSMISSION-MODE-DECLARATION":
                setattr(obj, "transmission_mode_declaration", SerializationHelper.deserialize_by_tag(child, "TransmissionModeDeclaration"))

        return obj



class IPduTimingBuilder(DescribableBuilder):
    """Builder for IPduTiming with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IPduTiming = IPduTiming()


    def with_minimum_delay(self, value: Optional[TimeValue]) -> "IPduTimingBuilder":
        """Set minimum_delay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'minimum_delay' is required and cannot be None")
        self._obj.minimum_delay = value
        return self

    def with_transmission_mode_declaration(self, value: Optional[TransmissionModeDeclaration]) -> "IPduTimingBuilder":
        """Set transmission_mode_declaration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'transmission_mode_declaration' is required and cannot be None")
        self._obj.transmission_mode_declaration = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "minimumDelay",
        "transmissionModeDeclaration",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> IPduTiming:
        """Build and return the IPduTiming instance with validation."""
        self._validate_instance()
        return self._obj