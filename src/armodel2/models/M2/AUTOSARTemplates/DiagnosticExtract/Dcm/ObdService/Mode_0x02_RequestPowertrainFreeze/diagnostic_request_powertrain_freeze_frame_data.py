"""DiagnosticRequestPowertrainFreezeFrameData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 152)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x02_RequestPowertrainFreeze.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import DiagnosticServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.ObdService.Mode_0x02_RequestPowertrainFreeze.diagnostic_powertrain_freeze_frame import (
    DiagnosticPowertrainFreezeFrame,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticRequestPowertrainFreezeFrameData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestPowertrainFreezeFrameData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA"


    freeze_frame_freeze_frame_ref: Optional[ARRef]
    request_ref: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "FREEZE-FRAME-FREEZE-FRAME-REF": lambda obj, elem: setattr(obj, "freeze_frame_freeze_frame_ref", ARRef.deserialize(elem)),
        "REQUEST-REF": lambda obj, elem: setattr(obj, "request_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticRequestPowertrainFreezeFrameData."""
        super().__init__()
        self.freeze_frame_freeze_frame_ref: Optional[ARRef] = None
        self.request_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestPowertrainFreezeFrameData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestPowertrainFreezeFrameData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize freeze_frame_freeze_frame_ref
        if self.freeze_frame_freeze_frame_ref is not None:
            serialized = SerializationHelper.serialize_item(self.freeze_frame_freeze_frame_ref, "DiagnosticPowertrainFreezeFrame")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FREEZE-FRAME-FREEZE-FRAME-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_ref
        if self.request_ref is not None:
            serialized = SerializationHelper.serialize_item(self.request_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestPowertrainFreezeFrameData":
        """Deserialize XML element to DiagnosticRequestPowertrainFreezeFrameData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestPowertrainFreezeFrameData object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestPowertrainFreezeFrameData, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FREEZE-FRAME-FREEZE-FRAME-REF":
                setattr(obj, "freeze_frame_freeze_frame_ref", ARRef.deserialize(child))
            elif tag == "REQUEST-REF":
                setattr(obj, "request_ref", ARRef.deserialize(child))

        return obj



class DiagnosticRequestPowertrainFreezeFrameDataBuilder(DiagnosticServiceInstanceBuilder):
    """Builder for DiagnosticRequestPowertrainFreezeFrameData with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticRequestPowertrainFreezeFrameData = DiagnosticRequestPowertrainFreezeFrameData()


    def with_freeze_frame_freeze_frame(self, value: Optional[DiagnosticPowertrainFreezeFrame]) -> "DiagnosticRequestPowertrainFreezeFrameDataBuilder":
        """Set freeze_frame_freeze_frame attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.freeze_frame_freeze_frame = value
        return self

    def with_request(self, value: Optional[any (DiagnosticRequest)]) -> "DiagnosticRequestPowertrainFreezeFrameDataBuilder":
        """Set request attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.request = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "freezeFrameFreezeFrame",
        "request",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticRequestPowertrainFreezeFrameData:
        """Build and return the DiagnosticRequestPowertrainFreezeFrameData instance with validation."""
        self._validate_instance()
        return self._obj