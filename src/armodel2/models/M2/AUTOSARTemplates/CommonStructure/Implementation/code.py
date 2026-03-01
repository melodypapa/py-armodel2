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
        "CALLBACK-HEADERS": ("_POLYMORPHIC_LIST", "callback_header_refs", ["BswMgrNeeds", "ComMgrUserNeeds", "CryptoKeyManagementNeeds", "CryptoServiceJobNeeds", "CryptoServiceNeeds", "DiagnosticCapabilityElement", "DltUserNeeds", "DoIpServiceNeeds", "EcuStateMgrUserNeeds", "ErrorTracerNeeds", "FunctionInhibitionAvailabilityNeeds", "FunctionInhibitionNeeds", "GlobalSupervisionNeeds", "HardwareTestNeeds", "IdsMgrCustomTimestampNeeds", "IdsMgrNeeds", "IndicatorStatusNeeds", "J1939DcmDm19Support", "J1939RmIncomingRequestServiceNeeds", "J1939RmOutgoingRequestServiceNeeds", "NvBlockNeeds", "SecureOnBoardCommunicationNeeds", "SupervisedEntityCheckpointNeeds", "SupervisedEntityNeeds", "SyncTimeBaseMgrUserNeeds", "V2xDataManagerNeeds", "V2xFacUserNeeds", "V2xMUserNeeds", "VendorSpecificServiceNeeds"]),
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
            elif tag == "CALLBACK-HEADERS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "BSW-MGR-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswMgrNeeds"))
                    elif concrete_tag == "COM-MGR-USER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ComMgrUserNeeds"))
                    elif concrete_tag == "CRYPTO-KEY-MANAGEMENT-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CryptoKeyManagementNeeds"))
                    elif concrete_tag == "CRYPTO-SERVICE-JOB-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CryptoServiceJobNeeds"))
                    elif concrete_tag == "CRYPTO-SERVICE-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CryptoServiceNeeds"))
                    elif concrete_tag == "DIAGNOSTIC-CAPABILITY-ELEMENT":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DiagnosticCapabilityElement"))
                    elif concrete_tag == "DLT-USER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DltUserNeeds"))
                    elif concrete_tag == "DO-IP-SERVICE-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DoIpServiceNeeds"))
                    elif concrete_tag == "ECU-STATE-MGR-USER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcuStateMgrUserNeeds"))
                    elif concrete_tag == "ERROR-TRACER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ErrorTracerNeeds"))
                    elif concrete_tag == "FUNCTION-INHIBITION-AVAILABILITY-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FunctionInhibitionAvailabilityNeeds"))
                    elif concrete_tag == "FUNCTION-INHIBITION-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FunctionInhibitionNeeds"))
                    elif concrete_tag == "GLOBAL-SUPERVISION-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "GlobalSupervisionNeeds"))
                    elif concrete_tag == "HARDWARE-TEST-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "HardwareTestNeeds"))
                    elif concrete_tag == "IDS-MGR-CUSTOM-TIMESTAMP-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IdsMgrCustomTimestampNeeds"))
                    elif concrete_tag == "IDS-MGR-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IdsMgrNeeds"))
                    elif concrete_tag == "INDICATOR-STATUS-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "IndicatorStatusNeeds"))
                    elif concrete_tag == "J1939-DCM-DM19-SUPPORT":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939DcmDm19Support"))
                    elif concrete_tag == "J1939-RM-INCOMING-REQUEST-SERVICE-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939RmIncomingRequestServiceNeeds"))
                    elif concrete_tag == "J1939-RM-OUTGOING-REQUEST-SERVICE-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "J1939RmOutgoingRequestServiceNeeds"))
                    elif concrete_tag == "NV-BLOCK-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "NvBlockNeeds"))
                    elif concrete_tag == "SECURE-ON-BOARD-COMMUNICATION-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SecureOnBoardCommunicationNeeds"))
                    elif concrete_tag == "SUPERVISED-ENTITY-CHECKPOINT-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SupervisedEntityCheckpointNeeds"))
                    elif concrete_tag == "SUPERVISED-ENTITY-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SupervisedEntityNeeds"))
                    elif concrete_tag == "SYNC-TIME-BASE-MGR-USER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SyncTimeBaseMgrUserNeeds"))
                    elif concrete_tag == "V2X-DATA-MANAGER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "V2xDataManagerNeeds"))
                    elif concrete_tag == "V2X-FAC-USER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "V2xFacUserNeeds"))
                    elif concrete_tag == "V2X-M-USER-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "V2xMUserNeeds"))
                    elif concrete_tag == "VENDOR-SPECIFIC-SERVICE-NEEDS":
                        obj.callback_header_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VendorSpecificServiceNeeds"))

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


    def build(self) -> Code:
        """Build and return the Code instance with validation."""
        self._validate_instance()
        pass
        return self._obj