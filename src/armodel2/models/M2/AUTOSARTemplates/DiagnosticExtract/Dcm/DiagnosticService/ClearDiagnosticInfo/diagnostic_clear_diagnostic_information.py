"""DiagnosticClearDiagnosticInformation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ClearDiagnosticInfo.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticClearDiagnosticInformation(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticClearDiagnosticInformation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION"


    clear_diagnostic_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "CLEAR-DIAGNOSTIC-REF": lambda obj, elem: setattr(obj, "clear_diagnostic_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticClearDiagnosticInformation."""
        super().__init__()
        self.clear_diagnostic_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticClearDiagnosticInformation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticClearDiagnosticInformation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize clear_diagnostic_ref
        if self.clear_diagnostic_ref is not None:
            serialized = SerializationHelper.serialize_item(self.clear_diagnostic_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLEAR-DIAGNOSTIC-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticClearDiagnosticInformation":
        """Deserialize XML element to DiagnosticClearDiagnosticInformation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticClearDiagnosticInformation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticClearDiagnosticInformation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CLEAR-DIAGNOSTIC-REF":
                setattr(obj, "clear_diagnostic_ref", ARRef.deserialize(child))

        return obj



class DiagnosticClearDiagnosticInformationBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticClearDiagnosticInformation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticClearDiagnosticInformation = DiagnosticClearDiagnosticInformation()


    def with_clear_diagnostic(self, value: Optional[Any]) -> "DiagnosticClearDiagnosticInformationBuilder":
        """Set clear_diagnostic attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'clear_diagnostic' is required and cannot be None")
        self._obj.clear_diagnostic = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "clearDiagnostic",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticClearDiagnosticInformation:
        """Build and return the DiagnosticClearDiagnosticInformation instance with validation."""
        self._validate_instance()
        return self._obj