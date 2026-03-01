"""BswServiceDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 225)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 978)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import (
    ServiceDependency,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_dependency import ServiceDependencyBuilder
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.ServiceMapping.bsw_service_dependency_ident import (
    BswServiceDependencyIdent,
)
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.role_based_bsw_module_entry_assignment import (
    RoleBasedBswModuleEntryAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.role_based_data_assignment import (
    RoleBasedDataAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswServiceDependency(ServiceDependency):
    """AUTOSAR BswServiceDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-SERVICE-DEPENDENCY"


    assigned_datas: list[RoleBasedDataAssignment]
    assigned_entry_roles: list[RoleBasedBswModuleEntryAssignment]
    ident: Optional[BswServiceDependencyIdent]
    service_needs: Optional[ServiceNeeds]
    _DESERIALIZE_DISPATCH = {
        "ASSIGNED-DATAS": lambda obj, elem: obj.assigned_datas.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedDataAssignment")),
        "ASSIGNED-ENTRY-ROLES": lambda obj, elem: obj.assigned_entry_roles.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedBswModuleEntryAssignment")),
        "IDENT": lambda obj, elem: setattr(obj, "ident", SerializationHelper.deserialize_by_tag(elem, "BswServiceDependencyIdent")),
        "SERVICE-NEEDS": ("_POLYMORPHIC", "service_needs", ["BswMgrNeeds", "ComMgrUserNeeds", "CryptoKeyManagementNeeds", "CryptoServiceJobNeeds", "CryptoServiceNeeds", "DiagnosticCapabilityElement", "DiagnosticCommunicationManagerNeeds", "DiagnosticComponentNeeds", "DiagnosticControlNeeds", "DiagnosticEnableConditionNeeds", "DiagnosticEventInfoNeeds", "DiagnosticEventManagerNeeds", "DiagnosticEventNeeds", "DiagnosticIoControlNeeds", "DiagnosticOperationCycleNeeds", "DiagnosticRequestFileTransferNeeds", "DiagnosticRoutineNeeds", "DiagnosticStorageConditionNeeds", "DiagnosticUploadDownloadNeeds", "DiagnosticValueNeeds", "DiagnosticsCommunicationSecurityNeeds", "DltUserNeeds", "DoIpActivationLineNeeds", "DoIpGidNeeds", "DoIpGidSynchronizationNeeds", "DoIpPowerModeStatusNeeds", "DoIpRoutingActivationAuthenticationNeeds", "DoIpRoutingActivationConfirmationNeeds", "DoIpServiceNeeds", "DtcStatusChangeNotificationNeeds", "EcuStateMgrUserNeeds", "ErrorTracerNeeds", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "GlobalSupervisionNeeds", "HardwareTestNeeds", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IndicatorStatusNeeds", "J1939DcmDm19Support", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "NvBlockNeeds", "ObdControlServiceNeeds", "ObdInfoServiceNeeds", "ObdMonitorServiceNeeds", "ObdPidServiceNeeds", "ObdRatioDenominatorNeeds", "ObdRatioServiceNeeds", "SecureOnBoardCommunicationNeeds", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SyncTimeBaseMgrUserNeeds", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VendorSpecificServiceNeeds"]),
    }


    def __init__(self) -> None:
        """Initialize BswServiceDependency."""
        super().__init__()
        self.assigned_datas: list[RoleBasedDataAssignment] = []
        self.assigned_entry_roles: list[RoleBasedBswModuleEntryAssignment] = []
        self.ident: Optional[BswServiceDependencyIdent] = None
        self.service_needs: Optional[ServiceNeeds] = None

    def serialize(self) -> ET.Element:
        """Serialize BswServiceDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswServiceDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assigned_datas (list to container "ASSIGNED-DATAS")
        if self.assigned_datas:
            wrapper = ET.Element("ASSIGNED-DATAS")
            for item in self.assigned_datas:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize assigned_entry_roles (list to container "ASSIGNED-ENTRY-ROLES")
        if self.assigned_entry_roles:
            wrapper = ET.Element("ASSIGNED-ENTRY-ROLES")
            for item in self.assigned_entry_roles:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedBswModuleEntryAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ident
        if self.ident is not None:
            serialized = SerializationHelper.serialize_item(self.ident, "BswServiceDependencyIdent")
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

        # Serialize service_needs
        if self.service_needs is not None:
            serialized = SerializationHelper.serialize_item(self.service_needs, "ServiceNeeds")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-NEEDS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswServiceDependency":
        """Deserialize XML element to BswServiceDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswServiceDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswServiceDependency, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ASSIGNED-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.assigned_datas.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedDataAssignment"))
            elif tag == "ASSIGNED-ENTRY-ROLES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.assigned_entry_roles.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedBswModuleEntryAssignment"))
            elif tag == "IDENT":
                setattr(obj, "ident", SerializationHelper.deserialize_by_tag(child, "BswServiceDependencyIdent"))
            elif tag == "SERVICE-NEEDS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "BSW-MGR-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "BswMgrNeeds"))
                    elif concrete_tag == "COM-MGR-USER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ComMgrUserNeeds"))
                    elif concrete_tag == "CRYPTO-KEY-MANAGEMENT-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "CryptoKeyManagementNeeds"))
                    elif concrete_tag == "CRYPTO-SERVICE-JOB-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "CryptoServiceJobNeeds"))
                    elif concrete_tag == "CRYPTO-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "CryptoServiceNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-CAPABILITY-ELEMENT":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticCapabilityElement"))
                    elif concrete_tag == "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticCommunicationManagerNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-COMPONENT-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticComponentNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-CONTROL-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticControlNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-ENABLE-CONDITION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEnableConditionNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-EVENT-INFO-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEventInfoNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-EVENT-MANAGER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEventManagerNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-EVENT-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticEventNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-IO-CONTROL-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticIoControlNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-OPERATION-CYCLE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticOperationCycleNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-REQUEST-FILE-TRANSFER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRequestFileTransferNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-ROUTINE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticRoutineNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-STORAGE-CONDITION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticStorageConditionNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-UPLOAD-DOWNLOAD-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticUploadDownloadNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-VALUE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticValueNeeds"))
                    elif concrete_tag == "DIAGNOSTICS-COMMUNICATION-SECURITY-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DiagnosticsCommunicationSecurityNeeds"))
                    elif concrete_tag == "DLT-USER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DltUserNeeds"))
                    elif concrete_tag == "DO-IP-ACTIVATION-LINE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DoIpActivationLineNeeds"))
                    elif concrete_tag == "DO-IP-GID-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DoIpGidNeeds"))
                    elif concrete_tag == "DO-IP-GID-SYNCHRONIZATION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DoIpGidSynchronizationNeeds"))
                    elif concrete_tag == "DO-IP-POWER-MODE-STATUS-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DoIpPowerModeStatusNeeds"))
                    elif concrete_tag == "DO-IP-ROUTING-ACTIVATION-AUTHENTICATION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DoIpRoutingActivationAuthenticationNeeds"))
                    elif concrete_tag == "DO-IP-ROUTING-ACTIVATION-CONFIRMATION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DoIpRoutingActivationConfirmationNeeds"))
                    elif concrete_tag == "DO-IP-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DoIpServiceNeeds"))
                    elif concrete_tag == "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "DtcStatusChangeNotificationNeeds"))
                    elif concrete_tag == "ECU-STATE-MGR-USER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "EcuStateMgrUserNeeds"))
                    elif concrete_tag == "ERROR-TRACER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ErrorTracerNeeds"))
                    elif concrete_tag == "FUNCTION-INHIBITION-AVAILABILITY-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "FunctionInhibitionAvailabilityNeeds"))
                    elif concrete_tag == "FUNCTION-INHIBITION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "FunctionInhibitionNeeds"))
                    elif concrete_tag == "GLOBAL-SUPERVISION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "GlobalSupervisionNeeds"))
                    elif concrete_tag == "HARDWARE-TEST-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "HardwareTestNeeds"))
                    elif concrete_tag == "IDS-MGR-CUSTOM-TIMESTAMP-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "IdsMgrCustomTimestampNeeds"))
                    elif concrete_tag == "IDS-MGR-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "IdsMgrNeeds"))
                    elif concrete_tag == "INDICATOR-STATUS-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "IndicatorStatusNeeds"))
                    elif concrete_tag == "J1939-DCM-DM19-SUPPORT":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "J1939DcmDm19Support"))
                    elif concrete_tag == "J1939-RM-INCOMING-REQUEST-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "J1939RmIncomingRequestServiceNeeds"))
                    elif concrete_tag == "J1939-RM-OUTGOING-REQUEST-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "J1939RmOutgoingRequestServiceNeeds"))
                    elif concrete_tag == "NV-BLOCK-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "NvBlockNeeds"))
                    elif concrete_tag == "OBD-CONTROL-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ObdControlServiceNeeds"))
                    elif concrete_tag == "OBD-INFO-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ObdInfoServiceNeeds"))
                    elif concrete_tag == "OBD-MONITOR-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ObdMonitorServiceNeeds"))
                    elif concrete_tag == "OBD-PID-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ObdPidServiceNeeds"))
                    elif concrete_tag == "OBD-RATIO-DENOMINATOR-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ObdRatioDenominatorNeeds"))
                    elif concrete_tag == "OBD-RATIO-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "ObdRatioServiceNeeds"))
                    elif concrete_tag == "SECURE-ON-BOARD-COMMUNICATION-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "SecureOnBoardCommunicationNeeds"))
                    elif concrete_tag == "SUPERVISED-ENTITY-CHECKPOINT-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "SupervisedEntityCheckpointNeeds"))
                    elif concrete_tag == "SUPERVISED-ENTITY-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "SupervisedEntityNeeds"))
                    elif concrete_tag == "SYNC-TIME-BASE-MGR-USER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "SyncTimeBaseMgrUserNeeds"))
                    elif concrete_tag == "V2X-DATA-MANAGER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "V2xDataManagerNeeds"))
                    elif concrete_tag == "V2X-FAC-USER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "V2xFacUserNeeds"))
                    elif concrete_tag == "V2X-M-USER-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "V2xMUserNeeds"))
                    elif concrete_tag == "VENDOR-SPECIFIC-SERVICE-NEEDS":
                        setattr(obj, "service_needs", SerializationHelper.deserialize_by_tag(child[0], "VendorSpecificServiceNeeds"))

        return obj



class BswServiceDependencyBuilder(ServiceDependencyBuilder):
    """Builder for BswServiceDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswServiceDependency = BswServiceDependency()


    def with_assigned_datas(self, items: list[RoleBasedDataAssignment]) -> "BswServiceDependencyBuilder":
        """Set assigned_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas = list(items) if items else []
        return self

    def with_assigned_entry_roles(self, items: list[RoleBasedBswModuleEntryAssignment]) -> "BswServiceDependencyBuilder":
        """Set assigned_entry_roles list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.assigned_entry_roles = list(items) if items else []
        return self

    def with_ident(self, value: Optional[BswServiceDependencyIdent]) -> "BswServiceDependencyBuilder":
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

    def with_service_needs(self, value: Optional[ServiceNeeds]) -> "BswServiceDependencyBuilder":
        """Set service_needs attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_needs = value
        return self


    def add_assigned_data(self, item: RoleBasedDataAssignment) -> "BswServiceDependencyBuilder":
        """Add a single item to assigned_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas.append(item)
        return self

    def clear_assigned_datas(self) -> "BswServiceDependencyBuilder":
        """Clear all items from assigned_datas list.

        Returns:
            self for method chaining
        """
        self._obj.assigned_datas = []
        return self

    def add_assigned_entry_role(self, item: RoleBasedBswModuleEntryAssignment) -> "BswServiceDependencyBuilder":
        """Add a single item to assigned_entry_roles list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.assigned_entry_roles.append(item)
        return self

    def clear_assigned_entry_roles(self) -> "BswServiceDependencyBuilder":
        """Clear all items from assigned_entry_roles list.

        Returns:
            self for method chaining
        """
        self._obj.assigned_entry_roles = []
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


    def build(self) -> BswServiceDependency:
        """Build and return the BswServiceDependency instance with validation."""
        self._validate_instance()
        pass
        return self._obj