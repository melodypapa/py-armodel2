"""DocumentationContext AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 327)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import MultilanguageReferrableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DocumentationContext(MultilanguageReferrable):
    """AUTOSAR DocumentationContext."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DOCUMENTATION-CONTEXT"


    feature: Optional[AtpFeature]
    identifiable_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "FEATURE": ("_POLYMORPHIC", "feature", ["AtpPrototype", "AtpStructureElement"]),
        "IDENTIFIABLE-REF": ("_POLYMORPHIC", "identifiable_ref", ["ARPackage", "AbstractDoIpLogicAddressProps", "AbstractEvent", "AbstractImplementationDataTypeElement", "AbstractSecurityEventFilter", "AbstractSecurityIdsmInstanceFilter", "AbstractServiceInstance", "AppOsTaskProxyToEcuTaskProxyMapping", "ApplicationEndpoint", "ApplicationError", "ApplicationPartitionToEcuPartitionMapping", "AppliedStandard", "AsynchronousServerCallResultPoint", "AtpBlueprint", "AtpBlueprintable", "AtpClassifier", "AtpFeature", "AutosarOperationArgumentInstance", "AutosarVariableInstance", "BinaryManifestAddressableObject", "BinaryManifestItemDefinition", "BinaryManifestResource", "BinaryManifestResourceDefinition", "BlockState", "BswInternalTriggeringPoint", "BswModuleDependency", "BuildActionEntity", "BuildActionEnvironment", "CanTpAddress", "CanTpChannel", "CanTpNode", "Chapter", "ClassContentConditional", "ClientIdDefinition", "ClientServerOperation", "Code", "CollectableElement", "ComManagementMapping", "CommConnectorPort", "CommunicationConnector", "CommunicationController", "Compiler", "ConsistencyNeeds", "ConsumedEventGroup", "CouplingElementAbstractDetails", "CouplingPort", "CouplingPortAbstractShaper", "CouplingPortStructuralElement", "CpSoftwareClusterResource", "CpSoftwareClusterResourceToApplicationPartitionMapping", "CpSoftwareClusterToApplicationPartitionMapping", "CpSoftwareClusterToEcuInstanceMapping", "CpSoftwareClusterToResourceMapping", "CryptoServiceMapping", "DataPrototypeGroup", "Data", "Transformation", "DdsCpDomain", "DdsCpPartition", "DdsCpQosProfile", "DdsCpTopic", "DependencyOnArtifact", "DiagEventDebounceAlgorithm", "DiagnosticAuthTransmitCertificateEvaluation", "DiagnosticConnectedIndicator", "DiagnosticDataElement", "DiagnosticDebounceAlgorithmProps", "DiagnosticFunctionInhibitSource", "DiagnosticParameterElement", "DiagnosticRoutineSubfunction", "DltApplication", "DltArgument", "DltLogChannel", "DltMessage", "DoIpInterface", "DoIpLogicAddress", "DoIpRoutingActivation", "ECUMapping", "EOCExecutableEntityRefAbstract", "EcuPartition", "EcucContainerValue", "EcucDefinitionElement", "EcucDestinationUriDef", "EcucEnumerationLiteralDef", "EcucQuery", "EcucValidationCondition", "EndToEndProtection", "EthernetWakeupSleepOnDatalineConfig", "EventHandler", "ExclusiveArea", "ExecutableEntity", "ExecutionTime", "FMAttributeDef", "FMFeatureMapAssertion", "FMFeatureMapCondition", "FMFeatureMapElement", "FMFeatureRelation", "FMFeatureRestriction", "FMFeatureSelection", "FlatInstanceDescriptor", "FlexrayArTpNode", "FlexrayTpConnectionControl", "FlexrayTpNode", "FlexrayTpPduPool", "FrameTriggering", "GeneralParameter", "GlobalTimeGateway", "GlobalTimeMaster", "GlobalTimeSlave", "HeapUsage", "HwAttributeDef", "HwAttributeLiteralDef", "HwPin", "HwPinGroup", "IEEE1722TpAcfBus", "IEEE1722TpAcfBusPart", "IPSecRule", "IPv6ExtHeaderFilterList", "ISignalToIPduMapping", "ISignalTriggering", "IdentCaption", "ImpositionTime", "InternalTriggeringPoint", "J1939SharedAddressCluster", "J1939TpNode", "Keyword", "LifeCycleState", "LinScheduleTable", "LinTpNode", "Linker", "MacMulticastGroup", "MacSecKayParticipant", "McDataInstance", "MemorySection", "ModeDeclaration", "ModeDeclarationMapping", "ModeSwitchPoint", "NetworkEndpoint", "NmCluster", "NmEcu", "NmNode", "NvBlockDescriptor", "PackageableElement", "ParameterAccess", "PduActivationRoutingGroup", "PduToFrameMapping", "PduTriggering", "PerInstanceMemory", "PhysicalChannel", "PortElementToCommunicationResourceMapping", "PortGroup", "PortInterfaceMapping", "PossibleErrorReaction", "ResourceConsumption", "RootSwCompositionPrototype", "RptComponent", "RptContainer", "RptExecutableEntity", "RptExecutableEntityEvent", "RptExecutionContext", "RptProfile", "RptServicePoint", "RteEventInCompositionSeparation", "RteEventInCompositionToOsTaskProxyMapping", "RteEventInSystemSeparation", "RteEventInSystemToOsTaskProxyMapping", "RunnableEntityGroup", "SdgAttribute", "SdgClass", "SecureCommunicationAuthenticationProps", "SecureCommunicationFreshnessProps", "SecurityEventContextProps", "ServerCallPoint", "ServiceNeeds", "SignalServiceTranslationElementProps", "SignalServiceTranslationEventProps", "SignalServiceTranslationProps", "SocketAddress", "SomeipTpChannel", "SpecElementReference", "StackUsage", "StaticSocketConnection", "StructuredReq", "SwGenericAxisParamType", "SwServiceArg", "SwcServiceDependency", "SwcToApplicationPartitionMapping", "SwcToEcuMapping", "SwcToImplMapping", "SwitchAsynchronousTrafficShaperGroupEntry", "SwitchFlowMeteringEntry", "SwitchStreamFilterActionDestPortModification", "SwitchStreamFilterEntry", "SwitchStreamFilterRule", "SwitchStreamGateEntry", "SwitchStreamIdentification", "SystemMapping", "SystemSignalGroupToCommunicationResourceMapping", "SystemSignalToCommunicationResourceMapping", "TDCpSoftwareClusterMapping", "TDCpSoftwareClusterResourceMapping", "TcpOptionFilterList", "TimingClock", "TimingClockSyncAccuracy", "TimingCondition", "TimingConstraint", "TimingDescription", "TimingExtensionResource", "TimingModeInstance", "TlsCryptoCipherSuite", "TlsCryptoCipherSuiteProps", "Topic1", "TpAddress", "TraceableTable", "TraceableText", "TracedFailure", "TransformationProps", "TransformationTechnology", "Trigger", "VariableAccess", "VariationPointProxy", "ViewMap", "VlanConfig", "WaitPoint"]),
    }


    def __init__(self) -> None:
        """Initialize DocumentationContext."""
        super().__init__()
        self.feature: Optional[AtpFeature] = None
        self.identifiable_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DocumentationContext to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DocumentationContext, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature
        if self.feature is not None:
            serialized = SerializationHelper.serialize_item(self.feature, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FEATURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize identifiable_ref
        if self.identifiable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.identifiable_ref, "Identifiable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENTIFIABLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentationContext":
        """Deserialize XML element to DocumentationContext object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DocumentationContext object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DocumentationContext, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FEATURE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-PROTOTYPE":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        setattr(obj, "feature", SerializationHelper.deserialize_by_tag(child[0], "AtpStructureElement"))
            elif tag == "IDENTIFIABLE-REF":
                setattr(obj, "identifiable_ref", ARRef.deserialize(child))

        return obj



class DocumentationContextBuilder(MultilanguageReferrableBuilder):
    """Builder for DocumentationContext with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DocumentationContext = DocumentationContext()


    def with_feature(self, value: Optional[AtpFeature]) -> "DocumentationContextBuilder":
        """Set feature attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.feature = value
        return self

    def with_identifiable(self, value: Optional[Identifiable]) -> "DocumentationContextBuilder":
        """Set identifiable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.identifiable = value
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


    def build(self) -> DocumentationContext:
        """Build and return the DocumentationContext instance with validation."""
        self._validate_instance()
        pass
        return self._obj