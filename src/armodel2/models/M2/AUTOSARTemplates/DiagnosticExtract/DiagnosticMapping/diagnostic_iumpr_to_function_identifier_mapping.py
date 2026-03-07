"""DiagnosticIumprToFunctionIdentifierMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 265)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import DiagnosticMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticIumprToFunctionIdentifierMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticIumprToFunctionIdentifierMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-IUMPR-TO-FUNCTION-IDENTIFIER-MAPPING"


    function_ref: Optional[Any]
    iumpr_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FUNCTION-REF": lambda obj, elem: setattr(obj, "function_ref", ARRef.deserialize(elem)),
        "IUMPR-REF": lambda obj, elem: setattr(obj, "iumpr_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticIumprToFunctionIdentifierMapping."""
        super().__init__()
        self.function_ref: Optional[Any] = None
        self.iumpr_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticIumprToFunctionIdentifierMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticIumprToFunctionIdentifierMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize function_ref
        if self.function_ref is not None:
            serialized = SerializationHelper.serialize_item(self.function_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize iumpr_ref
        if self.iumpr_ref is not None:
            serialized = SerializationHelper.serialize_item(self.iumpr_ref, "DiagnosticIumpr")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IUMPR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprToFunctionIdentifierMapping":
        """Deserialize XML element to DiagnosticIumprToFunctionIdentifierMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprToFunctionIdentifierMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIumprToFunctionIdentifierMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FUNCTION-REF":
                setattr(obj, "function_ref", ARRef.deserialize(child))
            elif tag == "IUMPR-REF":
                setattr(obj, "iumpr_ref", ARRef.deserialize(child))

        return obj



class DiagnosticIumprToFunctionIdentifierMappingBuilder(DiagnosticMappingBuilder):
    """Builder for DiagnosticIumprToFunctionIdentifierMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticIumprToFunctionIdentifierMapping = DiagnosticIumprToFunctionIdentifierMapping()


    def with_function(self, value: Optional[Any]) -> "DiagnosticIumprToFunctionIdentifierMappingBuilder":
        """Set function attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'function' is required and cannot be None")
        self._obj.function = value
        return self

    def with_iumpr(self, value: Optional[DiagnosticIumpr]) -> "DiagnosticIumprToFunctionIdentifierMappingBuilder":
        """Set iumpr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'iumpr' is required and cannot be None")
        self._obj.iumpr = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "function",
        "iumpr",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticIumprToFunctionIdentifierMapping:
        """Build and return the DiagnosticIumprToFunctionIdentifierMapping instance with validation."""
        self._validate_instance()
        return self._obj