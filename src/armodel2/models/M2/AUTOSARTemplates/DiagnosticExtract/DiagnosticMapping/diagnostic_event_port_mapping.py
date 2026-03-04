"""DiagnosticEventPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 249)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import DiagnosticSwMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticEventPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEventPortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-EVENT-PORT-MAPPING"


    bsw_service_ref: Optional[Any]
    diagnostic_event_ref: Optional[ARRef]
    swc_flat_service_ref: Optional[Any]
    swc_service: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "BSW-SERVICE-REF": lambda obj, elem: setattr(obj, "bsw_service_ref", ARRef.deserialize(elem)),
        "DIAGNOSTIC-EVENT-REF": lambda obj, elem: setattr(obj, "diagnostic_event_ref", ARRef.deserialize(elem)),
        "SWC-FLAT-SERVICE-REF": lambda obj, elem: setattr(obj, "swc_flat_service_ref", ARRef.deserialize(elem)),
        "SWC-SERVICE": lambda obj, elem: setattr(obj, "swc_service", SerializationHelper.deserialize_by_tag(elem, "any (SwcService)")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticEventPortMapping."""
        super().__init__()
        self.bsw_service_ref: Optional[Any] = None
        self.diagnostic_event_ref: Optional[ARRef] = None
        self.swc_flat_service_ref: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventPortMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventPortMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_service_ref
        if self.bsw_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_service_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_event_ref
        if self.diagnostic_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_event_ref, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_flat_service_ref
        if self.swc_flat_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_flat_service_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-FLAT-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_service
        if self.swc_service is not None:
            serialized = SerializationHelper.serialize_item(self.swc_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventPortMapping":
        """Deserialize XML element to DiagnosticEventPortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventPortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventPortMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BSW-SERVICE-REF":
                setattr(obj, "bsw_service_ref", ARRef.deserialize(child))
            elif tag == "DIAGNOSTIC-EVENT-REF":
                setattr(obj, "diagnostic_event_ref", ARRef.deserialize(child))
            elif tag == "SWC-FLAT-SERVICE-REF":
                setattr(obj, "swc_flat_service_ref", ARRef.deserialize(child))
            elif tag == "SWC-SERVICE":
                setattr(obj, "swc_service", SerializationHelper.deserialize_by_tag(child, "any (SwcService)"))

        return obj



class DiagnosticEventPortMappingBuilder(DiagnosticSwMappingBuilder):
    """Builder for DiagnosticEventPortMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticEventPortMapping = DiagnosticEventPortMapping()


    def with_bsw_service(self, value: Optional[any (BswService)]) -> "DiagnosticEventPortMappingBuilder":
        """Set bsw_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.bsw_service = value
        return self

    def with_diagnostic_event(self, value: Optional[DiagnosticEvent]) -> "DiagnosticEventPortMappingBuilder":
        """Set diagnostic_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic_event = value
        return self

    def with_swc_flat_service(self, value: Optional[any (SwcService)]) -> "DiagnosticEventPortMappingBuilder":
        """Set swc_flat_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_flat_service = value
        return self

    def with_swc_service(self, value: Optional[any (SwcService)]) -> "DiagnosticEventPortMappingBuilder":
        """Set swc_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_service = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bswService",
        "diagnosticEvent",
        "swcFlatService",
        "swcService",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticEventPortMapping:
        """Build and return the DiagnosticEventPortMapping instance with validation."""
        self._validate_instance()
        return self._obj