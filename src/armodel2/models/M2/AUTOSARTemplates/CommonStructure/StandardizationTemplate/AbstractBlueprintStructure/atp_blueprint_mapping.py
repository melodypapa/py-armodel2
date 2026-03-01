"""AtpBlueprintMapping AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

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
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AtpBlueprintMapping(ARObject, ABC):
    """AUTOSAR AtpBlueprintMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_blueprint_ref: ARRef
    atp_blueprinted_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "ATP-BLUEPRINT-REF": ("_POLYMORPHIC", "atp_blueprint_ref", ["ARPackage", "AbstractImplementationDataType", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AliasNameSet", "ApplicationDataType", "BswEntryRelationshipSet", "BswModuleDescription", "BswModuleEntry", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "CompuMethod", "ConsistencyNeeds", "DataConstr", "DataTypeMappingSet", "EcucDefinitionCollection", "EcucDestinationUriDefSet", "EcucModuleDef", "FlatMap", "ImpositionTime", "ImpositionTimeDefinitionGroup", "KeywordSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "ModeDeclarationGroup", "PortInterface", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "SwAddrMethod", "SwBaseType", "SwComponentType", "VfbTiming"]),
        "ATP-BLUEPRINTED-REF": ("_POLYMORPHIC", "atp_blueprinted_ref", ["ARPackage", "AbstractImplementationDataType", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AliasNameSet", "ApplicationDataType", "BswEntryRelationshipSet", "BswModuleDescription", "BswModuleEntry", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "CompuMethod", "ConsistencyNeeds", "DataConstr", "DataTypeMappingSet", "EcucDefinitionCollection", "EcucDestinationUriDefSet", "EcucModuleDef", "FlatMap", "ImpositionTime", "ImpositionTimeDefinitionGroup", "KeywordSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "ModeDeclarationGroup", "PortInterface", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototype", "SwAddrMethod", "SwBaseType", "SwComponentType", "VfbTiming"]),
    }


    def __init__(self) -> None:
        """Initialize AtpBlueprintMapping."""
        super().__init__()
        self.atp_blueprint_ref: ARRef = None
        self.atp_blueprinted_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize AtpBlueprintMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtpBlueprintMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize atp_blueprint_ref
        if self.atp_blueprint_ref is not None:
            serialized = SerializationHelper.serialize_item(self.atp_blueprint_ref, "AtpBlueprint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-BLUEPRINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize atp_blueprinted_ref
        if self.atp_blueprinted_ref is not None:
            serialized = SerializationHelper.serialize_item(self.atp_blueprinted_ref, "AtpBlueprintable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-BLUEPRINTED-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpBlueprintMapping":
        """Deserialize XML element to AtpBlueprintMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpBlueprintMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpBlueprintMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ATP-BLUEPRINT-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "AR-PACKAGE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "ARPackage"))
                    elif concrete_tag == "ABSTRACT-IMPLEMENTATION-DATA-TYPE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractImplementationDataType"))
                    elif concrete_tag == "ACL-OBJECT-SET":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "AclObjectSet"))
                    elif concrete_tag == "ACL-OPERATION":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "AclOperation"))
                    elif concrete_tag == "ACL-PERMISSION":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "AclPermission"))
                    elif concrete_tag == "ACL-ROLE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "AclRole"))
                    elif concrete_tag == "ALIAS-NAME-SET":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "AliasNameSet"))
                    elif concrete_tag == "APPLICATION-DATA-TYPE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationDataType"))
                    elif concrete_tag == "BSW-ENTRY-RELATIONSHIP-SET":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "BswEntryRelationshipSet"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleDescription"))
                    elif concrete_tag == "BSW-MODULE-ENTRY":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleEntry"))
                    elif concrete_tag == "BUILD-ACTION-ENTITY":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionEntity"))
                    elif concrete_tag == "BUILD-ACTION-ENVIRONMENT":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionEnvironment"))
                    elif concrete_tag == "BUILD-ACTION-MANIFEST":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionManifest"))
                    elif concrete_tag == "CLIENT-SERVER-INTERFACE-TO-BSW-MODULE-ENTRY-BLUEPRINT-MAPPING":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "ClientServerInterfaceToBswModuleEntryBlueprintMapping"))
                    elif concrete_tag == "COMPU-METHOD":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "CompuMethod"))
                    elif concrete_tag == "CONSISTENCY-NEEDS":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "ConsistencyNeeds"))
                    elif concrete_tag == "DATA-CONSTR":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "DataConstr"))
                    elif concrete_tag == "DATA-TYPE-MAPPING-SET":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "DataTypeMappingSet"))
                    elif concrete_tag == "ECUC-DEFINITION-COLLECTION":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucDefinitionCollection"))
                    elif concrete_tag == "ECUC-DESTINATION-URI-DEF-SET":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucDestinationUriDefSet"))
                    elif concrete_tag == "ECUC-MODULE-DEF":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucModuleDef"))
                    elif concrete_tag == "FLAT-MAP":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "FlatMap"))
                    elif concrete_tag == "IMPOSITION-TIME":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "ImpositionTime"))
                    elif concrete_tag == "IMPOSITION-TIME-DEFINITION-GROUP":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "ImpositionTimeDefinitionGroup"))
                    elif concrete_tag == "KEYWORD-SET":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "KeywordSet"))
                    elif concrete_tag == "LIFE-CYCLE-STATE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "LifeCycleState"))
                    elif concrete_tag == "LIFE-CYCLE-STATE-DEFINITION-GROUP":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "LifeCycleStateDefinitionGroup"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationGroup"))
                    elif concrete_tag == "PORT-INTERFACE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "PortInterface"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMapping"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING-SET":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMappingSet"))
                    elif concrete_tag == "PORT-PROTOTYPE-BLUEPRINT":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "PortPrototypeBlueprint"))
                    elif concrete_tag == "SW-ADDR-METHOD":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "SwAddrMethod"))
                    elif concrete_tag == "SW-BASE-TYPE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "SwBaseType"))
                    elif concrete_tag == "SW-COMPONENT-TYPE":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "SwComponentType"))
                    elif concrete_tag == "VFB-TIMING":
                        setattr(obj, "atp_blueprint_ref", SerializationHelper.deserialize_by_tag(child[0], "VfbTiming"))
            elif tag == "ATP-BLUEPRINTED-REF":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "AR-PACKAGE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "ARPackage"))
                    elif concrete_tag == "ABSTRACT-IMPLEMENTATION-DATA-TYPE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "AbstractImplementationDataType"))
                    elif concrete_tag == "ACL-OBJECT-SET":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "AclObjectSet"))
                    elif concrete_tag == "ACL-OPERATION":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "AclOperation"))
                    elif concrete_tag == "ACL-PERMISSION":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "AclPermission"))
                    elif concrete_tag == "ACL-ROLE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "AclRole"))
                    elif concrete_tag == "ALIAS-NAME-SET":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "AliasNameSet"))
                    elif concrete_tag == "APPLICATION-DATA-TYPE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "ApplicationDataType"))
                    elif concrete_tag == "BSW-ENTRY-RELATIONSHIP-SET":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "BswEntryRelationshipSet"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleDescription"))
                    elif concrete_tag == "BSW-MODULE-ENTRY":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "BswModuleEntry"))
                    elif concrete_tag == "BUILD-ACTION-ENTITY":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionEntity"))
                    elif concrete_tag == "BUILD-ACTION-ENVIRONMENT":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionEnvironment"))
                    elif concrete_tag == "BUILD-ACTION-MANIFEST":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "BuildActionManifest"))
                    elif concrete_tag == "COMPU-METHOD":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "CompuMethod"))
                    elif concrete_tag == "CONSISTENCY-NEEDS":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "ConsistencyNeeds"))
                    elif concrete_tag == "DATA-CONSTR":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "DataConstr"))
                    elif concrete_tag == "DATA-TYPE-MAPPING-SET":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "DataTypeMappingSet"))
                    elif concrete_tag == "ECUC-DEFINITION-COLLECTION":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucDefinitionCollection"))
                    elif concrete_tag == "ECUC-DESTINATION-URI-DEF-SET":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucDestinationUriDefSet"))
                    elif concrete_tag == "ECUC-MODULE-DEF":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "EcucModuleDef"))
                    elif concrete_tag == "FLAT-MAP":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "FlatMap"))
                    elif concrete_tag == "IMPOSITION-TIME":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "ImpositionTime"))
                    elif concrete_tag == "IMPOSITION-TIME-DEFINITION-GROUP":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "ImpositionTimeDefinitionGroup"))
                    elif concrete_tag == "KEYWORD-SET":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "KeywordSet"))
                    elif concrete_tag == "LIFE-CYCLE-STATE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "LifeCycleState"))
                    elif concrete_tag == "LIFE-CYCLE-STATE-DEFINITION-GROUP":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "LifeCycleStateDefinitionGroup"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationGroup"))
                    elif concrete_tag == "PORT-INTERFACE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "PortInterface"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMapping"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING-SET":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMappingSet"))
                    elif concrete_tag == "PORT-PROTOTYPE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "PortPrototype"))
                    elif concrete_tag == "SW-ADDR-METHOD":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "SwAddrMethod"))
                    elif concrete_tag == "SW-BASE-TYPE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "SwBaseType"))
                    elif concrete_tag == "SW-COMPONENT-TYPE":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "SwComponentType"))
                    elif concrete_tag == "VFB-TIMING":
                        setattr(obj, "atp_blueprinted_ref", SerializationHelper.deserialize_by_tag(child[0], "VfbTiming"))

        return obj



class AtpBlueprintMappingBuilder(BuilderBase, ABC):
    """Builder for AtpBlueprintMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AtpBlueprintMapping = AtpBlueprintMapping()


    def with_atp_blueprint(self, value: AtpBlueprint) -> "AtpBlueprintMappingBuilder":
        """Set atp_blueprint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.atp_blueprint = value
        return self

    def with_atp_blueprinted(self, value: AtpBlueprintable) -> "AtpBlueprintMappingBuilder":
        """Set atp_blueprinted attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.atp_blueprinted = value
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
    def build(self) -> AtpBlueprintMapping:
        """Build and return the AtpBlueprintMapping instance (abstract)."""
        raise NotImplementedError