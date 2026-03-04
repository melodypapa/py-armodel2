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
            if tag == "ACCESS-REF":
                setattr(obj, "access_ref", ARRef.deserialize(child))
            elif tag == "SERVICE-CLASS-REF":
                setattr(obj, "service_class_ref", ARRef.deserialize(child))

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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "access",
        "serviceClass",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> DiagnosticServiceInstance:
        """Build and return the DiagnosticServiceInstance instance (abstract)."""
        raise NotImplementedError