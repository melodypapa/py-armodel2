"""DiagnosticServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommonService.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import DiagnosticCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.diagnostic_access_permission import (
    DiagnosticAccessPermission,
)
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticServiceInstance(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    access_ref: Optional[ARRef]
    service_class_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ACCESS-REF": lambda obj, elem: setattr(obj, "access_ref", ARRef.deserialize(elem)),
        "SERVICE-CLASS-REF": ("_POLYMORPHIC", "service_class_ref", ["DiagnosticAuthenticationClass", "DiagnosticClearDiagnosticInformationClass", "DiagnosticClearResetEmissionRelatedInfoClass", "DiagnosticComControlClass", "DiagnosticControlDTCSettingClass", "DiagnosticCustomServiceClass", "DiagnosticDataTransferClass", "DiagnosticDynamicallyDefineDataIdentifierClass", "DiagnosticEcuResetClass", "DiagnosticIoControlClass", "DiagnosticReadDTCInformationClass", "DiagnosticReadDataByIdentifierClass", "DiagnosticReadDataByPeriodicIDClass", "DiagnosticReadMemoryByAddressClass", "DiagnosticReadScalingDataByIdentifierClass", "DiagnosticRequestControlOfOnBoardDeviceClass", "DiagnosticRequestCurrentPowertrainDataClass", "DiagnosticRequestDownloadClass", "DiagnosticRequestEmissionRelatedDTCClass", "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass", "DiagnosticRequestFileTransferClass", "DiagnosticRequestOnBoardMonitoringTestResultsClass", "DiagnosticRequestPowertrainFreezeFrameDataClass", "DiagnosticRequestUploadClass", "DiagnosticRequestVehicleInfoClass", "DiagnosticResponseOnEventClass", "DiagnosticRoutineControlClass", "DiagnosticSecurityAccessClass", "DiagnosticSessionControlClass", "DiagnosticTransferExitClass", "DiagnosticWriteDataByIdentifierClass", "DiagnosticWriteMemoryByAddressClass"]),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticServiceInstance."""
        super().__init__()
        self.access_ref: Optional[ARRef] = None
        self.service_class_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_ref
        if self.access_ref is not None:
            serialized = SerializationHelper.serialize_item(self.access_ref, "DiagnosticAccessPermission")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_class_ref
        if self.service_class_ref is not None:
            serialized = SerializationHelper.serialize_item(self.service_class_ref, "DiagnosticServiceClass")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-CLASS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceInstance":
        """Deserialize XML element to DiagnosticServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ACCESS-REF":
                setattr(obj, "access_ref", ARRef.deserialize(child))
            elif tag == "SERVICE-CLASS-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "DIAGNOSTIC-AUTHENTICATION-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticAuthenticationClass"))
                    elif concrete_tag == "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticClearDiagnosticInformationClass"))
                    elif concrete_tag == "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticClearResetEmissionRelatedInfoClass"))
                    elif concrete_tag == "DIAGNOSTIC-COM-CONTROL-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticComControlClass"))
                    elif concrete_tag == "DIAGNOSTIC-CONTROL-D-T-C-SETTING-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticControlDTCSettingClass"))
                    elif concrete_tag == "DIAGNOSTIC-CUSTOM-SERVICE-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticCustomServiceClass"))
                    elif concrete_tag == "DIAGNOSTIC-DATA-TRANSFER-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDataTransferClass"))
                    elif concrete_tag == "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticDynamicallyDefineDataIdentifierClass"))
                    elif concrete_tag == "DIAGNOSTIC-ECU-RESET-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEcuResetClass"))
                    elif concrete_tag == "DIAGNOSTIC-IO-CONTROL-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticIoControlClass"))
                    elif concrete_tag == "DIAGNOSTIC-READ-D-T-C-INFORMATION-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticReadDTCInformationClass"))
                    elif concrete_tag == "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticReadDataByIdentifierClass"))
                    elif concrete_tag == "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticReadDataByPeriodicIDClass"))
                    elif concrete_tag == "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticReadMemoryByAddressClass"))
                    elif concrete_tag == "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticReadScalingDataByIdentifierClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestControlOfOnBoardDeviceClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestCurrentPowertrainDataClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestDownloadClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-D-T-C-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestEmissionRelatedDTCClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-EMISSION-RELATED-D-T-C-PERMANENT-STATUS-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestEmissionRelatedDTCPermanentStatusClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestFileTransferClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestOnBoardMonitoringTestResultsClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestPowertrainFreezeFrameDataClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-UPLOAD-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestUploadClass"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestVehicleInfoClass"))
                    elif concrete_tag == "DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticResponseOnEventClass"))
                    elif concrete_tag == "DIAGNOSTIC-ROUTINE-CONTROL-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRoutineControlClass"))
                    elif concrete_tag == "DIAGNOSTIC-SECURITY-ACCESS-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticSecurityAccessClass"))
                    elif concrete_tag == "DIAGNOSTIC-SESSION-CONTROL-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticSessionControlClass"))
                    elif concrete_tag == "DIAGNOSTIC-TRANSFER-EXIT-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticTransferExitClass"))
                    elif concrete_tag == "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticWriteDataByIdentifierClass"))
                    elif concrete_tag == "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS":
                        setattr(obj, "service_class_ref", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticWriteMemoryByAddressClass"))

        return obj



class DiagnosticServiceInstanceBuilder(DiagnosticCommonElementBuilder):
    """Builder for DiagnosticServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticServiceInstance = DiagnosticServiceInstance()


    def with_access(self, value: Optional[DiagnosticAccessPermission]) -> "DiagnosticServiceInstanceBuilder":
        """Set access attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.access = value
        return self

    def with_service_class(self, value: Optional[DiagnosticServiceClass]) -> "DiagnosticServiceInstanceBuilder":
        """Set service_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_class = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    @abstractmethod
    def build(self) -> DiagnosticServiceInstance:
        """Build and return the DiagnosticServiceInstance instance (abstract)."""
        raise NotImplementedError