"""DiagnosticEventInfoNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 760)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import DiagnosticCapabilityElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticEventInfoNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-EVENT-INFO-NEEDS"


    obd_dtc_number: Optional[PositiveInteger]
    uds_dtc_number: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "OBD-DTC-NUMBER": lambda obj, elem: setattr(obj, "obd_dtc_number", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "UDS-DTC-NUMBER": lambda obj, elem: setattr(obj, "uds_dtc_number", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticEventInfoNeeds."""
        super().__init__()
        self.obd_dtc_number: Optional[PositiveInteger] = None
        self.uds_dtc_number: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventInfoNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventInfoNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize obd_dtc_number
        if self.obd_dtc_number is not None:
            serialized = SerializationHelper.serialize_item(self.obd_dtc_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OBD-DTC-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uds_dtc_number
        if self.uds_dtc_number is not None:
            serialized = SerializationHelper.serialize_item(self.uds_dtc_number, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDS-DTC-NUMBER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventInfoNeeds":
        """Deserialize XML element to DiagnosticEventInfoNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventInfoNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventInfoNeeds, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OBD-DTC-NUMBER":
                setattr(obj, "obd_dtc_number", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "UDS-DTC-NUMBER":
                setattr(obj, "uds_dtc_number", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class DiagnosticEventInfoNeedsBuilder(DiagnosticCapabilityElementBuilder):
    """Builder for DiagnosticEventInfoNeeds with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEventInfoNeeds = DiagnosticEventInfoNeeds()


    def with_obd_dtc_number(self, value: Optional[PositiveInteger]) -> "DiagnosticEventInfoNeedsBuilder":
        """Set obd_dtc_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.obd_dtc_number = value
        return self

    def with_uds_dtc_number(self, value: Optional[PositiveInteger]) -> "DiagnosticEventInfoNeedsBuilder":
        """Set uds_dtc_number attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uds_dtc_number = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "obdDtcNumber",
        "udsDtcNumber",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticEventInfoNeeds:
        """Build and return the DiagnosticEventInfoNeeds instance with validation."""
        self._validate_instance()
        return self._obj