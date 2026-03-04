"""DiagnosticRequestCurrentPowertrainData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x01_RequestCurrentPowertrain.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestCurrentPowertrainData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA"


    pid_ref: Optional[ARRef]
    request_current_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "PID-REF": lambda obj, elem: setattr(obj, "pid_ref", ARRef.deserialize(elem)),
        "REQUEST-CURRENT-REF": lambda obj, elem: setattr(obj, "request_current_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainData."""
        super().__init__()
        self.pid_ref: Optional[ARRef] = None
        self.request_current_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestCurrentPowertrainData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestCurrentPowertrainData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pid_ref
        if self.pid_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pid_ref, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_current_ref
        if self.request_current_ref is not None:
            serialized = SerializationHelper.serialize_item(self.request_current_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-CURRENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestCurrentPowertrainData":
        """Deserialize XML element to DiagnosticRequestCurrentPowertrainData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestCurrentPowertrainData object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestCurrentPowertrainData, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PID-REF":
                setattr(obj, "pid_ref", ARRef.deserialize(child))
            elif tag == "REQUEST-CURRENT-REF":
                setattr(obj, "request_current_ref", ARRef.deserialize(child))

        return obj



class DiagnosticRequestCurrentPowertrainDataBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticRequestCurrentPowertrainData with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticRequestCurrentPowertrainData = DiagnosticRequestCurrentPowertrainData()


    def with_pid(self, value: Optional[DiagnosticParameter]) -> "DiagnosticRequestCurrentPowertrainDataBuilder":
        """Set pid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pid = value
        return self

    def with_request_current(self, value: Optional[any (DiagnosticRequest)]) -> "DiagnosticRequestCurrentPowertrainDataBuilder":
        """Set request_current attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request_current = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "pid",
        "requestCurrent",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticRequestCurrentPowertrainData:
        """Build and return the DiagnosticRequestCurrentPowertrainData instance with validation."""
        self._validate_instance()
        return self._obj