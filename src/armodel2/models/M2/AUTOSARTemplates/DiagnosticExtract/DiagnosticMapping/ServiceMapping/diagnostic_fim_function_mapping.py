"""DiagnosticFimFunctionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 264)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

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


class DiagnosticFimFunctionMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticFimFunctionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-FIM-FUNCTION-MAPPING"


    mapped_bsw_ref: Optional[Any]
    mapped_flat_swc_ref: Optional[Any]
    mapped_ref: Optional[Any]
    mapped_swc: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "MAPPED-BSW-REF": lambda obj, elem: setattr(obj, "mapped_bsw_ref", ARRef.deserialize(elem)),
        "MAPPED-FLAT-SWC-REF": lambda obj, elem: setattr(obj, "mapped_flat_swc_ref", ARRef.deserialize(elem)),
        "MAPPED-REF": lambda obj, elem: setattr(obj, "mapped_ref", ARRef.deserialize(elem)),
        "MAPPED-SWC": lambda obj, elem: setattr(obj, "mapped_swc", SerializationHelper.deserialize_by_tag(elem, "any (SwcService)")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticFimFunctionMapping."""
        super().__init__()
        self.mapped_bsw_ref: Optional[Any] = None
        self.mapped_flat_swc_ref: Optional[Any] = None
        self.mapped_ref: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFimFunctionMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFimFunctionMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mapped_bsw_ref
        if self.mapped_bsw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_bsw_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-BSW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_flat_swc_ref
        if self.mapped_flat_swc_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_flat_swc_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-FLAT-SWC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_ref
        if self.mapped_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_swc
        if self.mapped_swc is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_swc, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-SWC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFimFunctionMapping":
        """Deserialize XML element to DiagnosticFimFunctionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFimFunctionMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticFimFunctionMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAPPED-BSW-REF":
                setattr(obj, "mapped_bsw_ref", ARRef.deserialize(child))
            elif tag == "MAPPED-FLAT-SWC-REF":
                setattr(obj, "mapped_flat_swc_ref", ARRef.deserialize(child))
            elif tag == "MAPPED-REF":
                setattr(obj, "mapped_ref", ARRef.deserialize(child))
            elif tag == "MAPPED-SWC":
                setattr(obj, "mapped_swc", SerializationHelper.deserialize_by_tag(child, "any (SwcService)"))

        return obj



class DiagnosticFimFunctionMappingBuilder(DiagnosticSwMappingBuilder):
    """Builder for DiagnosticFimFunctionMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticFimFunctionMapping = DiagnosticFimFunctionMapping()


    def with_mapped_bsw(self, value: Optional[any (BswService)]) -> "DiagnosticFimFunctionMappingBuilder":
        """Set mapped_bsw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapped_bsw = value
        return self

    def with_mapped_flat_swc(self, value: Optional[any (SwcService)]) -> "DiagnosticFimFunctionMappingBuilder":
        """Set mapped_flat_swc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapped_flat_swc = value
        return self

    def with_mapped(self, value: Optional[any (DiagnosticFunction)]) -> "DiagnosticFimFunctionMappingBuilder":
        """Set mapped attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapped = value
        return self

    def with_mapped_swc(self, value: Optional[any (SwcService)]) -> "DiagnosticFimFunctionMappingBuilder":
        """Set mapped_swc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mapped_swc = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "mapped",
        "mappedBsw",
        "mappedFlatSwc",
        "mappedSwc",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticFimFunctionMapping:
        """Build and return the DiagnosticFimFunctionMapping instance with validation."""
        self._validate_instance()
        return self._obj