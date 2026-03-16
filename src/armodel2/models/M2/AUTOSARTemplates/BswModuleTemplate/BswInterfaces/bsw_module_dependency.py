"""BswModuleDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 47)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.bsw_module_description import (
        BswModuleDescription,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class BswModuleDependency(Identifiable):
    """AUTOSAR BswModuleDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-MODULE-DEPENDENCY"


    target_module_id: Optional[PositiveInteger]
    target_module_ref: Optional[ARRef]
    service_items: list[ServiceNeeds]
    _DESERIALIZE_DISPATCH = {
        "TARGET-MODULE-ID": lambda obj, elem: setattr(obj, "target_module_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "TARGET-MODULE-REF": lambda obj, elem: setattr(obj, "target_module_ref", ARRef.deserialize(elem)),
        "SERVICE-ITEMS": ("_POLYMORPHIC_LIST", "service_items", ["BswMgrNeeds", "ComMgrUserNeeds", "CryptoKeyManagementNeeds", "CryptoServiceJobNeeds", "CryptoServiceNeeds", "DiagnosticCapabilityElement", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticControlNeeds", "DiagnosticEnableConditionNeeds", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticIoControlNeeds", "DiagnosticOperationCycleNeeds", "DiagnosticRequestFileTransferNeeds", "DiagnosticRoutineNeeds", "DiagnosticStorageConditionNeeds", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticsCommunicationSecurityNeeds", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpServiceNeeds", "DtcStatusChangeNotificationNeeds", "EcuStateMgrUserNeeds", "ErrorTracerNeeds", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "GlobalSupervisionNeeds", "HardwareTestNeeds", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IndicatorStatusNeeds", "J1939DcmDm19Support", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "NvBlockNeeds", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "SecureOnBoardCommunicationNeeds", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SyncTimeBaseMgrUserNeeds", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VendorSpecificServiceNeeds"]),
    }


    def __init__(self) -> None:
        """Initialize BswModuleDependency."""
        super().__init__()
        self.target_module_id: Optional[PositiveInteger] = None
        self.target_module_ref: Optional[ARRef] = None
        self.service_items: list[ServiceNeeds] = []

    def serialize(self) -> ET.Element:
        """Serialize BswModuleDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize target_module_id
        if self.target_module_id is not None:
            serialized = SerializationHelper.serialize_item(self.target_module_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODULE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_module_ref
        if self.target_module_ref is not None:
            serialized = SerializationHelper.serialize_item(self.target_module_ref, "BswModuleDescription")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET-MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_items (list to container "SERVICE-ITEMS")
        if self.service_items:
            wrapper = ET.Element("SERVICE-ITEMS")
            for item in self.service_items:
                serialized = SerializationHelper.serialize_item(item, "ServiceNeeds")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleDependency":
        """Deserialize XML element to BswModuleDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleDependency, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TARGET-MODULE-ID":
                setattr(obj, "target_module_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "TARGET-MODULE-REF":
                setattr(obj, "target_module_ref", ARRef.deserialize(child))
            elif tag == "SERVICE-ITEMS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "BSW-MGR-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "BswMgrNeeds"))
                    elif concrete_tag == "COM-MGR-USER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ComMgrUserNeeds"))
                    elif concrete_tag == "CRYPTO-KEY-MANAGEMENT-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "CryptoKeyManagementNeeds"))
                    elif concrete_tag == "CRYPTO-SERVICE-JOB-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "CryptoServiceJobNeeds"))
                    elif concrete_tag == "CRYPTO-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "CryptoServiceNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-CAPABILITY-ELEMENT":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticCapabilityElement"))
                    elif concrete_tag == "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticCommunicationManagerNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-COMPONENT-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticComponentNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-CONTROL-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticControlNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-ENABLE-CONDITION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticEnableConditionNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-EVENT-INFO-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticEventInfoNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-EVENT-MANAGER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticEventManagerNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-EVENT-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticEventNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-IO-CONTROL-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticIoControlNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-OPERATION-CYCLE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticOperationCycleNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-FILE-TRANSFER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticRequestFileTransferNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-ROUTINE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticRoutineNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-STORAGE-CONDITION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticStorageConditionNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-UPLOAD-DOWNLOAD-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticUploadDownloadNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-VALUE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticValueNeeds"))
                    elif concrete_tag == "DIAGNOSTICS-COMMUNICATION-SECURITY-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DiagnosticsCommunicationSecurityNeeds"))
                    elif concrete_tag == "DLT-USER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DltUserNeeds"))
                    elif concrete_tag == "DO-IP-ACTIVATION-LINE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpActivationLineNeeds"))
                    elif concrete_tag == "DO-IP-GID-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpGidNeeds"))
                    elif concrete_tag == "DO-IP-GID-SYNCHRONIZATION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpGidSynchronizationNeeds"))
                    elif concrete_tag == "DO-IP-POWER-MODE-STATUS-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpPowerModeStatusNeeds"))
                    elif concrete_tag == "DO-IP-ROUTING-ACTIVATION-AUTHENTICATION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpRoutingActivationAuthenticationNeeds"))
                    elif concrete_tag == "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpRoutingActivationConfirmationNeeds"))
                    elif concrete_tag == "DO-IP-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpServiceNeeds"))
                    elif concrete_tag == "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "DtcStatusChangeNotificationNeeds"))
                    elif concrete_tag == "ECU-STATE-MGR-USER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "EcuStateMgrUserNeeds"))
                    elif concrete_tag == "ERROR-TRACER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ErrorTracerNeeds"))
                    elif concrete_tag == "FUNCTION-INHIBITION-AVAILABILITY-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "FunctionInhibitionAvailabilityNeeds"))
                    elif concrete_tag == "FUNCTION-INHIBITION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "FunctionInhibitionNeeds"))
                    elif concrete_tag == "GLOBAL-SUPERVISION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "GlobalSupervisionNeeds"))
                    elif concrete_tag == "HARDWARE-TEST-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "HardwareTestNeeds"))
                    elif concrete_tag == "IDS-MGR-CUSTOM-TIMESTAMP-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "IdsMgrCustomTimestampNeeds"))
                    elif concrete_tag == "IDS-MGR-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "IdsMgrNeeds"))
                    elif concrete_tag == "INDICATOR-STATUS-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "IndicatorStatusNeeds"))
                    elif concrete_tag == "J1939-DCM-DM19-SUPPORT":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "J1939DcmDm19Support"))
                    elif concrete_tag == "J1939-RM-INCOMING-REQUEST-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "J1939RmIncomingRequestServiceNeeds"))
                    elif concrete_tag == "J1939-RM-OUTGOING-REQUEST-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "J1939RmOutgoingRequestServiceNeeds"))
                    elif concrete_tag == "NV-BLOCK-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "NvBlockNeeds"))
                    elif concrete_tag == "OBD-CONTROL-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ObdControlServiceNeeds"))
                    elif concrete_tag == "OBD-INFO-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ObdInfoServiceNeeds"))
                    elif concrete_tag == "OBD-MONITOR-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ObdMonitorServiceNeeds"))
                    elif concrete_tag == "OBD-PID-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ObdPidServiceNeeds"))
                    elif concrete_tag == "OBD-RATIO-DENOMINATOR-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ObdRatioDenominatorNeeds"))
                    elif concrete_tag == "OBD-RATIO-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "ObdRatioServiceNeeds"))
                    elif concrete_tag == "SECURE-ON-BOARD-COMMUNICATION-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "SecureOnBoardCommunicationNeeds"))
                    elif concrete_tag == "SUPERVISED-ENTITY-CHECKPOINT-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "SupervisedEntityCheckpointNeeds"))
                    elif concrete_tag == "SUPERVISED-ENTITY-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "SupervisedEntityNeeds"))
                    elif concrete_tag == "SYNC-TIME-BASE-MGR-USER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "SyncTimeBaseMgrUserNeeds"))
                    elif concrete_tag == "V2X-DATA-MANAGER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "V2xDataManagerNeeds"))
                    elif concrete_tag == "V2X-FAC-USER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "V2xFacUserNeeds"))
                    elif concrete_tag == "V2X-M-USER-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "V2xMUserNeeds"))
                    elif concrete_tag == "VENDOR-SPECIFIC-SERVICE-NEEDS":
                        obj.service_items.append(SerializationHelper.deserialize_by_tag(item_elem, "VendorSpecificServiceNeeds"))

        return obj



class BswModuleDependencyBuilder(IdentifiableBuilder):
    """Builder for BswModuleDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswModuleDependency = BswModuleDependency()


    def with_target_module_id(self, value: Optional[PositiveInteger]) -> "BswModuleDependencyBuilder":
        """Set target_module_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_module_id' is required and cannot be None")
        self._obj.target_module_id = value
        return self

    def with_target_module(self, value: Optional[BswModuleDescription]) -> "BswModuleDependencyBuilder":
        """Set target_module attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'target_module' is required and cannot be None")
        self._obj.target_module = value
        return self

    def with_service_items(self, items: list[ServiceNeeds]) -> "BswModuleDependencyBuilder":
        """Set service_items list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.service_items = list(items) if items else []
        return self


    def add_service_item(self, item: ServiceNeeds) -> "BswModuleDependencyBuilder":
        """Add a single item to service_items list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.service_items.append(item)
        return self

    def clear_service_items(self) -> "BswModuleDependencyBuilder":
        """Clear all items from service_items list.

        Returns:
            self for method chaining
        """
        self._obj.service_items = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "serviceItem",
        "targetModule",
        "targetModuleId",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswModuleDependency:
        """Build and return the BswModuleDependency instance with validation."""
        self._validate_instance()
        return self._obj