"""DiagnosticParameter AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 36)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_parameter import (
    DiagnosticAbstractParameter,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_parameter import DiagnosticAbstractParameterBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticParameter(DiagnosticAbstractParameter):
    """AUTOSAR DiagnosticParameter."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-PARAMETER"


    ident: Optional[DiagnosticParameter]
    support_info: Optional[DiagnosticParameter]
    _DESERIALIZE_DISPATCH = {
        "IDENT": lambda obj, elem: setattr(obj, "ident", SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
        "SUPPORT-INFO": lambda obj, elem: setattr(obj, "support_info", SerializationHelper.deserialize_by_tag(elem, "DiagnosticParameter")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticParameter."""
        super().__init__()
        self.ident: Optional[DiagnosticParameter] = None
        self.support_info: Optional[DiagnosticParameter] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticParameter to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticParameter, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize support_info
        if self.support_info is not None:
            serialized = SerializationHelper.serialize_item(self.support_info, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPORT-INFO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameter":
        """Deserialize XML element to DiagnosticParameter object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameter object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticParameter, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IDENT":
                setattr(obj, "ident", SerializationHelper.deserialize_by_tag(child, "DiagnosticParameter"))
            elif tag == "SUPPORT-INFO":
                setattr(obj, "support_info", SerializationHelper.deserialize_by_tag(child, "DiagnosticParameter"))

        return obj



class DiagnosticParameterBuilder(DiagnosticAbstractParameterBuilder):
    """Builder for DiagnosticParameter with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticParameter = DiagnosticParameter()


    def with_ident(self, value: Optional[DiagnosticParameter]) -> "DiagnosticParameterBuilder":
        """Set ident attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ident = value
        return self

    def with_support_info(self, value: Optional[DiagnosticParameter]) -> "DiagnosticParameterBuilder":
        """Set support_info attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.support_info = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ident",
        "supportInfo",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticParameter:
        """Build and return the DiagnosticParameter instance with validation."""
        self._validate_instance()
        return self._obj