"""DiagnosticStorageConditionPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 253)

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
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticStorageConditionPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticStorageConditionPortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING"


    diagnostic_storage_ref: Optional[Any]
    swc_flat_service_ref: Optional[Any]
    swc_service: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTIC-STORAGE-REF": lambda obj, elem: setattr(obj, "diagnostic_storage_ref", ARRef.deserialize(elem)),
        "SWC-FLAT-SERVICE-REF": lambda obj, elem: setattr(obj, "swc_flat_service_ref", ARRef.deserialize(elem)),
        "SWC-SERVICE": lambda obj, elem: setattr(obj, "swc_service", SerializationHelper.deserialize_by_tag(elem, "any (SwcService)")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionPortMapping."""
        super().__init__()
        self.diagnostic_storage_ref: Optional[Any] = None
        self.swc_flat_service_ref: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStorageConditionPortMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStorageConditionPortMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_storage_ref
        if self.diagnostic_storage_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_storage_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-STORAGE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionPortMapping":
        """Deserialize XML element to DiagnosticStorageConditionPortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageConditionPortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStorageConditionPortMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAGNOSTIC-STORAGE-REF":
                setattr(obj, "diagnostic_storage_ref", ARRef.deserialize(child))
            elif tag == "SWC-FLAT-SERVICE-REF":
                setattr(obj, "swc_flat_service_ref", ARRef.deserialize(child))
            elif tag == "SWC-SERVICE":
                setattr(obj, "swc_service", SerializationHelper.deserialize_by_tag(child, "any (SwcService)"))

        return obj



class DiagnosticStorageConditionPortMappingBuilder(DiagnosticSwMappingBuilder):
    """Builder for DiagnosticStorageConditionPortMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticStorageConditionPortMapping = DiagnosticStorageConditionPortMapping()


    def with_diagnostic_storage(self, value: Optional[Any]) -> "DiagnosticStorageConditionPortMappingBuilder":
        """Set diagnostic_storage attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'diagnostic_storage' is required and cannot be None")
        self._obj.diagnostic_storage = value
        return self

    def with_swc_flat_service(self, value: Optional[Any]) -> "DiagnosticStorageConditionPortMappingBuilder":
        """Set swc_flat_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'swc_flat_service' is required and cannot be None")
        self._obj.swc_flat_service = value
        return self

    def with_swc_service(self, value: Optional[Any]) -> "DiagnosticStorageConditionPortMappingBuilder":
        """Set swc_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'swc_service' is required and cannot be None")
        self._obj.swc_service = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "diagnosticStorage",
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


    def build(self) -> DiagnosticStorageConditionPortMapping:
        """Build and return the DiagnosticStorageConditionPortMapping instance with validation."""
        self._validate_instance()
        return self._obj