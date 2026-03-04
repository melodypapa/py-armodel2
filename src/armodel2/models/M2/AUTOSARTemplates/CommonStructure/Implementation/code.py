"""Code AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 130)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 622)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Code(Identifiable):
    """AUTOSAR Code."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CODE"


    artifact_descriptors: list[AutosarEngineeringObject]
    callback_header_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ARTIFACT-DESCRIPTORS": lambda obj, elem: obj.artifact_descriptors.append(SerializationHelper.deserialize_by_tag(elem, "AutosarEngineeringObject")),
        "CALLBACK-HEADER-REFS": ("_POLYMORPHIC_LIST", "callback_header_refs", ["BswMgrNeeds", "ComMgrUserNeeds", "CryptoKeyManagementNeeds", "CryptoServiceJobNeeds", "CryptoServiceNeeds", "DiagnosticCapabilityElement", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticControlNeeds", "DiagnosticEnableConditionNeeds", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticIoControlNeeds", "DiagnosticOperationCycleNeeds", "DiagnosticRequestFileTransferNeeds", "DiagnosticRoutineNeeds", "DiagnosticStorageConditionNeeds", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticsCommunicationSecurityNeeds", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpServiceNeeds", "DtcStatusChangeNotificationNeeds", "EcuStateMgrUserNeeds", "ErrorTracerNeeds", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "GlobalSupervisionNeeds", "HardwareTestNeeds", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IndicatorStatusNeeds", "J1939DcmDm19Support", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "NvBlockNeeds", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "SecureOnBoardCommunicationNeeds", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SyncTimeBaseMgrUserNeeds", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VendorSpecificServiceNeeds"]),
    }


    def __init__(self) -> None:
        """Initialize Code."""
        super().__init__()
        self.artifact_descriptors: list[AutosarEngineeringObject] = []
        self.callback_header_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize Code to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Code, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize artifact_descriptors (list to container "ARTIFACT-DESCRIPTORS")
        if self.artifact_descriptors:
            wrapper = ET.Element("ARTIFACT-DESCRIPTORS")
            for item in self.artifact_descriptors:
                serialized = SerializationHelper.serialize_item(item, "AutosarEngineeringObject")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize callback_header_refs (list to container "CALLBACK-HEADER-REFS")
        if self.callback_header_refs:
            wrapper = ET.Element("CALLBACK-HEADER-REFS")
            for item in self.callback_header_refs:
                serialized = SerializationHelper.serialize_item(item, "ServiceNeeds")
                if serialized is not None:
                    child_elem = ET.Element("CALLBACK-HEADER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Code":
        """Deserialize XML element to Code object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Code object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Code, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARTIFACT-DESCRIPTORS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.artifact_descriptors.append(SerializationHelper.deserialize_by_tag(item_elem, "AutosarEngineeringObject"))
            elif tag == "CALLBACK-HEADER-REFS":
                for item_elem in child:
                    obj.callback_header_refs.append(ARRef.deserialize(item_elem))

        return obj



class CodeBuilder(IdentifiableBuilder):
    """Builder for Code with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Code = Code()


    def with_artifact_descriptors(self, items: list[AutosarEngineeringObject]) -> "CodeBuilder":
        """Set artifact_descriptors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.artifact_descriptors = list(items) if items else []
        return self

    def with_callback_headers(self, items: list[ServiceNeeds]) -> "CodeBuilder":
        """Set callback_headers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.callback_headers = list(items) if items else []
        return self


    def add_artifact_descriptor(self, item: AutosarEngineeringObject) -> "CodeBuilder":
        """Add a single item to artifact_descriptors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.artifact_descriptors.append(item)
        return self

    def clear_artifact_descriptors(self) -> "CodeBuilder":
        """Clear all items from artifact_descriptors list.

        Returns:
            self for method chaining
        """
        self._obj.artifact_descriptors = []
        return self

    def add_callback_header(self, item: ServiceNeeds) -> "CodeBuilder":
        """Add a single item to callback_headers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.callback_headers.append(item)
        return self

    def clear_callback_headers(self) -> "CodeBuilder":
        """Clear all items from callback_headers list.

        Returns:
            self for method chaining
        """
        self._obj.callback_headers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "artifactDescriptor",
        "callbackHeader",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Code:
        """Build and return the Code instance with validation."""
        self._validate_instance()
        return self._obj