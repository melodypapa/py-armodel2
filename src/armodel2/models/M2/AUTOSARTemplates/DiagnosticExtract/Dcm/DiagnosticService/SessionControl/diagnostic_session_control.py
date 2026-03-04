"""DiagnosticSessionControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SessionControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_session import (
    DiagnosticSession,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticSessionControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticSessionControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-SESSION-CONTROL"


    diagnostic_session_session_ref: Optional[ARRef]
    session_control_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DIAGNOSTIC-SESSION-SESSION-REF": lambda obj, elem: setattr(obj, "diagnostic_session_session_ref", ARRef.deserialize(elem)),
        "SESSION-CONTROL-REF": lambda obj, elem: setattr(obj, "session_control_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticSessionControl."""
        super().__init__()
        self.diagnostic_session_session_ref: Optional[ARRef] = None
        self.session_control_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticSessionControl to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticSessionControl, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_session_session_ref
        if self.diagnostic_session_session_ref is not None:
            serialized = SerializationHelper.serialize_item(self.diagnostic_session_session_ref, "DiagnosticSession")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-SESSION-SESSION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize session_control_ref
        if self.session_control_ref is not None:
            serialized = SerializationHelper.serialize_item(self.session_control_ref, "DiagnosticSession")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SESSION-CONTROL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSessionControl":
        """Deserialize XML element to DiagnosticSessionControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSessionControl object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticSessionControl, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIAGNOSTIC-SESSION-SESSION-REF":
                setattr(obj, "diagnostic_session_session_ref", ARRef.deserialize(child))
            elif tag == "SESSION-CONTROL-REF":
                setattr(obj, "session_control_ref", ARRef.deserialize(child))

        return obj



class DiagnosticSessionControlBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticSessionControl with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticSessionControl = DiagnosticSessionControl()


    def with_diagnostic_session_session(self, value: Optional[DiagnosticSession]) -> "DiagnosticSessionControlBuilder":
        """Set diagnostic_session_session attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.diagnostic_session_session = value
        return self

    def with_session_control(self, value: Optional[DiagnosticSession]) -> "DiagnosticSessionControlBuilder":
        """Set session_control attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.session_control = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "diagnosticSessionSession",
        "sessionControl",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticSessionControl:
        """Build and return the DiagnosticSessionControl instance with validation."""
        self._validate_instance()
        return self._obj