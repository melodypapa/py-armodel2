"""GlobalTimeFrSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 878)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import (
    GlobalTimeSlave,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.global_time_slave import GlobalTimeSlaveBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class GlobalTimeFrSlave(GlobalTimeSlave):
    """AUTOSAR GlobalTimeFrSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GLOBAL-TIME-FR-SLAVE"


    crc_validated: Optional[Any]
    sequence: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "CRC-VALIDATED": lambda obj, elem: setattr(obj, "crc_validated", SerializationHelper.deserialize_by_tag(elem, "any (GlobalTimeCrc)")),
        "SEQUENCE": lambda obj, elem: setattr(obj, "sequence", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize GlobalTimeFrSlave."""
        super().__init__()
        self.crc_validated: Optional[Any] = None
        self.sequence: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeFrSlave to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeFrSlave, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crc_validated
        if self.crc_validated is not None:
            serialized = SerializationHelper.serialize_item(self.crc_validated, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRC-VALIDATED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sequence
        if self.sequence is not None:
            serialized = SerializationHelper.serialize_item(self.sequence, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEQUENCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeFrSlave":
        """Deserialize XML element to GlobalTimeFrSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeFrSlave object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeFrSlave, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CRC-VALIDATED":
                setattr(obj, "crc_validated", SerializationHelper.deserialize_by_tag(child, "any (GlobalTimeCrc)"))
            elif tag == "SEQUENCE":
                setattr(obj, "sequence", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class GlobalTimeFrSlaveBuilder(GlobalTimeSlaveBuilder):
    """Builder for GlobalTimeFrSlave with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeFrSlave = GlobalTimeFrSlave()


    def with_crc_validated(self, value: Optional[any (GlobalTimeCrc)]) -> "GlobalTimeFrSlaveBuilder":
        """Set crc_validated attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.crc_validated = value
        return self

    def with_sequence(self, value: Optional[PositiveInteger]) -> "GlobalTimeFrSlaveBuilder":
        """Set sequence attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sequence = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "crcValidated",
        "sequence",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> GlobalTimeFrSlave:
        """Build and return the GlobalTimeFrSlave instance with validation."""
        self._validate_instance()
        return self._obj