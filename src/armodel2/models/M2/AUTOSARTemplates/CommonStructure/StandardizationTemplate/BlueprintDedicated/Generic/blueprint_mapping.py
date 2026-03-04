"""BlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 163)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_BlueprintDedicated_Generic.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprintable import (
    AtpBlueprintable,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BlueprintMapping(ARObject):
    """AUTOSAR BlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BLUEPRINT-MAPPING"


    blueprint_ref: ARRef
    derived_object_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "BLUEPRINT-REF": ("_POLYMORPHIC", "blueprint_ref", ["ARPackage", "AbstractImplementationDataType", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AliasNameSet", "ApplicationArrayDataType", "ApplicationDataType", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationSwComponentType", "BswEntryRelationshipSet", "BswModuleDescription", "BswModuleEntry", "BuildAction", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConsistencyNeeds", "DataConstr", "DataTypeMappingSet", "EcuAbstractionSwComponentType", "EcucDefinitionCollection", "EcucDestinationUriDefSet", "EcucModuleDef", "FlatMap", "ImplementationDataType", "ImpositionTime", "ImpositionTimeDefinitionGroup", "KeywordSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "ModeDeclarationGroup", "ModeInterfaceMapping", "ModeSwitchInterface", "NvBlockSwComponentType", "NvDataInterface", "ParameterInterface", "ParameterSwComponentType", "PortInterface", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType", "SwAddrMethod", "SwBaseType", "SwComponentType", "TriggerInterface", "TriggerInterfaceMapping", "VfbTiming"]),
        "DERIVED-OBJECT-REF": ("_POLYMORPHIC", "derived_object_ref", ["ARPackage", "AbstractImplementationDataType", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AliasNameSet", "ApplicationArrayDataType", "ApplicationDataType", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationSwComponentType", "BswEntryRelationshipSet", "BswModuleDescription", "BswModuleEntry", "BuildAction", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "ClientServerInterface", "ClientServerInterfaceMapping", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConsistencyNeeds", "DataConstr", "DataTypeMappingSet", "EcuAbstractionSwComponentType", "EcucDefinitionCollection", "EcucDestinationUriDefSet", "EcucModuleDef", "FlatMap", "ImplementationDataType", "ImpositionTime", "ImpositionTimeDefinitionGroup", "KeywordSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "ModeDeclarationGroup", "ModeInterfaceMapping", "ModeSwitchInterface", "NvBlockSwComponentType", "NvDataInterface", "PPortPrototype", "PRPortPrototype", "ParameterInterface", "ParameterSwComponentType", "PortInterface", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototype", "RPortPrototype", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType", "SwAddrMethod", "SwBaseType", "SwComponentType", "TriggerInterface", "TriggerInterfaceMapping", "VfbTiming"]),
    }


    def __init__(self) -> None:
        """Initialize BlueprintMapping."""
        super().__init__()
        self.blueprint_ref: ARRef = None
        self.derived_object_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize BlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BlueprintMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint_ref
        if self.blueprint_ref is not None:
            serialized = SerializationHelper.serialize_item(self.blueprint_ref, "AtpBlueprint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BLUEPRINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize derived_object_ref
        if self.derived_object_ref is not None:
            serialized = SerializationHelper.serialize_item(self.derived_object_ref, "AtpBlueprintable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DERIVED-OBJECT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BlueprintMapping":
        """Deserialize XML element to BlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BlueprintMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BlueprintMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BLUEPRINT-REF":
                setattr(obj, "blueprint_ref", ARRef.deserialize(child))
            elif tag == "DERIVED-OBJECT-REF":
                setattr(obj, "derived_object_ref", ARRef.deserialize(child))

        return obj



class BlueprintMappingBuilder(BuilderBase):
    """Builder for BlueprintMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BlueprintMapping = BlueprintMapping()


    def with_blueprint(self, value: AtpBlueprint) -> "BlueprintMappingBuilder":
        """Set blueprint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.blueprint = value
        return self

    def with_derived_object(self, value: AtpBlueprintable) -> "BlueprintMappingBuilder":
        """Set derived_object attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.derived_object = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "blueprint",
        "derivedObject",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Validate required attributes using pre-computed constants (O(1) lookup)
        # This is much faster than calling get_type_hints() at runtime
        if getattr(self._obj, "blueprint", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'blueprint' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'blueprint' is None", UserWarning)
        if getattr(self._obj, "derivedObject", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'derivedObject' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'derivedObject' is None", UserWarning)


    def build(self) -> BlueprintMapping:
        """Build and return the BlueprintMapping instance with validation."""
        self._validate_instance()
        return self._obj