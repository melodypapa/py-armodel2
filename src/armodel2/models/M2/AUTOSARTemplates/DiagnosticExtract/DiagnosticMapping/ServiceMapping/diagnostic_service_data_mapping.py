"""DiagnosticServiceDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 228)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import DiagnosticSwMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-SERVICE-DATA-MAPPING"


    diagnostic_data_ref: Optional[ARRef]
    diagnostic_ref: Optional[ARRef]
    mapped_data_ref: Optional[ARRef]
    parameter: Optional[DiagnosticParameter]
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTIC-DATA-REF": lambda obj, elem: setattr(obj, "diagnostic_data_ref", ARRef.deserialize(elem)),
        "DIAGNOSTIC-REF": lambda obj, elem: setattr(obj, "diagnostic_ref", ARRef.deserialize(elem)),
        "MAPPED-DATA-REF": ("_POLYMORPHIC", "mapped_data_ref", ["ApplicationArrayElement", "ApplicationCompositeElementDataPrototype", "ApplicationRecordElement", "ArgumentDataPrototype", "AutosarDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "PARAMETER": lambda obj, elem: setattr(obj, "parameter", SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticServiceDataMapping."""
        super().__init__()
        self.diagnostic_data_ref: Optional[ARRef] = None
        self.diagnostic_ref: Optional[ARRef] = None
        self.mapped_data_ref: Optional[ARRef] = None
        self.parameter: Optional[DiagnosticParameter] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceDataMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticServiceDataMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_data_ref
        if self.diagnostic_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_data_ref, "DiagnosticDataElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_ref
        if self.diagnostic_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_ref, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mapped_data_ref
        if self.mapped_data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mapped_data_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAPPED-DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter
        if self.parameter is not None:
            serialized = SerializationHelper.serialize_item(self.parameter, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceDataMapping":
        """Deserialize XML element to DiagnosticServiceDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceDataMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceDataMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAGNOSTIC-DATA-REF":
                setattr(obj, "diagnostic_data_ref", ARRef.deserialize(child))
            elif tag == "DIAGNOSTIC-REF":
                setattr(obj, "diagnostic_ref", ARRef.deserialize(child))
            elif tag == "MAPPED-DATA-REF":
                setattr(obj, "mapped_data_ref", ARRef.deserialize(child))
            elif tag == "PARAMETER":
                setattr(obj, "parameter", SerializationHelper.deserialize_by_tag(child, "DiagnosticParameter"))

        return obj



class DiagnosticServiceDataMappingBuilder(DiagnosticSwMappingBuilder):
    """Builder for DiagnosticServiceDataMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticServiceDataMapping = DiagnosticServiceDataMapping()


    def with_diagnostic_data(self, value: Optional[DiagnosticDataElement]) -> "DiagnosticServiceDataMappingBuilder":
        """Set diagnostic_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'diagnostic_data' is required and cannot be None")
        self._obj.diagnostic_data = value
        return self

    def with_diagnostic(self, value: Optional[DiagnosticParameter]) -> "DiagnosticServiceDataMappingBuilder":
        """Set diagnostic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'diagnostic' is required and cannot be None")
        self._obj.diagnostic = value
        return self

    def with_mapped_data(self, value: Optional[DataPrototype]) -> "DiagnosticServiceDataMappingBuilder":
        """Set mapped_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'mapped_data' is required and cannot be None")
        self._obj.mapped_data = value
        return self

    def with_parameter(self, value: Optional[DiagnosticParameter]) -> "DiagnosticServiceDataMappingBuilder":
        """Set parameter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'parameter' is required and cannot be None")
        self._obj.parameter = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "diagnostic",
        "diagnosticData",
        "mappedData",
        "parameter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticServiceDataMapping:
        """Build and return the DiagnosticServiceDataMapping instance with validation."""
        self._validate_instance()
        return self._obj