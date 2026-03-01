"""AclObjectSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 383)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights import (
    AclScopeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ReferrableSubtypesEnum,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.atp_blueprint import (
    AtpBlueprint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collection import (
    Collection,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AclObjectSet(ARElement):
    """AUTOSAR AclObjectSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ACL-OBJECT-SET"


    acl_object_clas_refs: list[ReferrableSubtypesEnum]
    acl_scope: AclScopeEnum
    collection_ref: Optional[ARRef]
    derived_from_refs: list[ARRef]
    engineerings: list[AutosarEngineeringObject]
    _DESERIALIZE_DISPATCH = {
        "ACL-OBJECT-CLASSES": lambda obj, elem: obj.acl_object_clas_refs.append(ARRef.deserialize(elem)),
        "ACL-SCOPE": lambda obj, elem: setattr(obj, "acl_scope", AclScopeEnum.deserialize(elem)),
        "COLLECTION-REF": lambda obj, elem: setattr(obj, "collection_ref", ARRef.deserialize(elem)),
        "DERIVED-FROMS": ("_POLYMORPHIC_LIST", "derived_from_refs", ["ARPackage", "AbstractImplementationDataType", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AliasNameSet", "ApplicationDataType", "BswEntryRelationshipSet", "BswModuleDescription", "BswModuleEntry", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "CompuMethod", "ConsistencyNeeds", "DataConstr", "DataTypeMappingSet", "EcucDefinitionCollection", "EcucDestinationUriDefSet", "EcucModuleDef", "FlatMap", "ImpositionTime", "ImpositionTimeDefinitionGroup", "KeywordSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "ModeDeclarationGroup", "PortInterface", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "SwAddrMethod", "SwBaseType", "SwComponentType", "VfbTiming"]),
        "ENGINEERINGS": lambda obj, elem: obj.engineerings.append(SerializationHelper.deserialize_by_tag(elem, "AutosarEngineeringObject")),
    }


    def __init__(self) -> None:
        """Initialize AclObjectSet."""
        super().__init__()
        self.acl_object_clas_refs: list[ReferrableSubtypesEnum] = []
        self.acl_scope: AclScopeEnum = None
        self.collection_ref: Optional[ARRef] = None
        self.derived_from_refs: list[ARRef] = []
        self.engineerings: list[AutosarEngineeringObject] = []

    def serialize(self) -> ET.Element:
        """Serialize AclObjectSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AclObjectSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize acl_object_clas_refs (list to container "ACL-OBJECT-CLASS-REFS")
        if self.acl_object_clas_refs:
            wrapper = ET.Element("ACL-OBJECT-CLASS-REFS")
            for item in self.acl_object_clas_refs:
                serialized = SerializationHelper.serialize_item(item, "ReferrableSubtypesEnum")
                if serialized is not None:
                    child_elem = ET.Element("ACL-OBJECT-CLAS-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize acl_scope
        if self.acl_scope is not None:
            serialized = SerializationHelper.serialize_item(self.acl_scope, "AclScopeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACL-SCOPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize collection_ref
        if self.collection_ref is not None:
            serialized = SerializationHelper.serialize_item(self.collection_ref, "Collection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize derived_from_refs (list to container "DERIVED-FROM-REFS")
        if self.derived_from_refs:
            wrapper = ET.Element("DERIVED-FROM-REFS")
            for item in self.derived_from_refs:
                serialized = SerializationHelper.serialize_item(item, "AtpBlueprint")
                if serialized is not None:
                    child_elem = ET.Element("DERIVED-FROM-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize engineerings (list to container "ENGINEERINGS")
        if self.engineerings:
            wrapper = ET.Element("ENGINEERINGS")
            for item in self.engineerings:
                serialized = SerializationHelper.serialize_item(item, "AutosarEngineeringObject")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclObjectSet":
        """Deserialize XML element to AclObjectSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclObjectSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclObjectSet, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACL-OBJECT-CLASSES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.acl_object_clas_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ReferrableSubtypesEnum"))
            elif tag == "ACL-SCOPE":
                setattr(obj, "acl_scope", AclScopeEnum.deserialize(child))
            elif tag == "COLLECTION-REF":
                setattr(obj, "collection_ref", ARRef.deserialize(child))
            elif tag == "DERIVED-FROMS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "AR-PACKAGE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ARPackage"))
                    elif concrete_tag == "ABSTRACT-IMPLEMENTATION-DATA-TYPE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractImplementationDataType"))
                    elif concrete_tag == "ACL-OBJECT-SET":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AclObjectSet"))
                    elif concrete_tag == "ACL-OPERATION":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AclOperation"))
                    elif concrete_tag == "ACL-PERMISSION":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AclPermission"))
                    elif concrete_tag == "ACL-ROLE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AclRole"))
                    elif concrete_tag == "ALIAS-NAME-SET":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AliasNameSet"))
                    elif concrete_tag == "APPLICATION-DATA-TYPE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ApplicationDataType"))
                    elif concrete_tag == "BSW-ENTRY-RELATIONSHIP-SET":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswEntryRelationshipSet"))
                    elif concrete_tag == "BSW-MODULE-DESCRIPTION":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleDescription"))
                    elif concrete_tag == "BSW-MODULE-ENTRY":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BswModuleEntry"))
                    elif concrete_tag == "BUILD-ACTION-ENTITY":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BuildActionEntity"))
                    elif concrete_tag == "BUILD-ACTION-ENVIRONMENT":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BuildActionEnvironment"))
                    elif concrete_tag == "BUILD-ACTION-MANIFEST":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "BuildActionManifest"))
                    elif concrete_tag == "CLIENT-SERVER-INTERFACE-TO-BSW-MODULE-ENTRY-BLUEPRINT-MAPPING":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ClientServerInterfaceToBswModuleEntryBlueprintMapping"))
                    elif concrete_tag == "COMPU-METHOD":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "CompuMethod"))
                    elif concrete_tag == "CONSISTENCY-NEEDS":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ConsistencyNeeds"))
                    elif concrete_tag == "DATA-CONSTR":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DataConstr"))
                    elif concrete_tag == "DATA-TYPE-MAPPING-SET":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "DataTypeMappingSet"))
                    elif concrete_tag == "ECUC-DEFINITION-COLLECTION":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucDefinitionCollection"))
                    elif concrete_tag == "ECUC-DESTINATION-URI-DEF-SET":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucDestinationUriDefSet"))
                    elif concrete_tag == "ECUC-MODULE-DEF":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EcucModuleDef"))
                    elif concrete_tag == "FLAT-MAP":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlatMap"))
                    elif concrete_tag == "IMPOSITION-TIME":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ImpositionTime"))
                    elif concrete_tag == "IMPOSITION-TIME-DEFINITION-GROUP":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ImpositionTimeDefinitionGroup"))
                    elif concrete_tag == "KEYWORD-SET":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "KeywordSet"))
                    elif concrete_tag == "LIFE-CYCLE-STATE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LifeCycleState"))
                    elif concrete_tag == "LIFE-CYCLE-STATE-DEFINITION-GROUP":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LifeCycleStateDefinitionGroup"))
                    elif concrete_tag == "MODE-DECLARATION-GROUP":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "ModeDeclarationGroup"))
                    elif concrete_tag == "PORT-INTERFACE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortInterface"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMapping"))
                    elif concrete_tag == "PORT-INTERFACE-MAPPING-SET":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortInterfaceMappingSet"))
                    elif concrete_tag == "PORT-PROTOTYPE-BLUEPRINT":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "PortPrototypeBlueprint"))
                    elif concrete_tag == "SW-ADDR-METHOD":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwAddrMethod"))
                    elif concrete_tag == "SW-BASE-TYPE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwBaseType"))
                    elif concrete_tag == "SW-COMPONENT-TYPE":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "SwComponentType"))
                    elif concrete_tag == "VFB-TIMING":
                        obj.derived_from_refs.append(SerializationHelper.deserialize_by_tag(child[0], "VfbTiming"))
            elif tag == "ENGINEERINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.engineerings.append(SerializationHelper.deserialize_by_tag(item_elem, "AutosarEngineeringObject"))

        return obj



class AclObjectSetBuilder(ARElementBuilder):
    """Builder for AclObjectSet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AclObjectSet = AclObjectSet()


    def with_acl_object_classes(self, items: list[ReferrableSubtypesEnum]) -> "AclObjectSetBuilder":
        """Set acl_object_classes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.acl_object_classes = list(items) if items else []
        return self

    def with_acl_scope(self, value: AclScopeEnum) -> "AclObjectSetBuilder":
        """Set acl_scope attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.acl_scope = value
        return self

    def with_collection(self, value: Optional[Collection]) -> "AclObjectSetBuilder":
        """Set collection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collection = value
        return self

    def with_derived_froms(self, items: list[AtpBlueprint]) -> "AclObjectSetBuilder":
        """Set derived_froms list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.derived_froms = list(items) if items else []
        return self

    def with_engineerings(self, items: list[AutosarEngineeringObject]) -> "AclObjectSetBuilder":
        """Set engineerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.engineerings = list(items) if items else []
        return self


    def add_acl_object_class(self, item: ReferrableSubtypesEnum) -> "AclObjectSetBuilder":
        """Add a single item to acl_object_classes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.acl_object_classes.append(item)
        return self

    def clear_acl_object_classes(self) -> "AclObjectSetBuilder":
        """Clear all items from acl_object_classes list.

        Returns:
            self for method chaining
        """
        self._obj.acl_object_classes = []
        return self

    def add_derived_from(self, item: AtpBlueprint) -> "AclObjectSetBuilder":
        """Add a single item to derived_froms list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.derived_froms.append(item)
        return self

    def clear_derived_froms(self) -> "AclObjectSetBuilder":
        """Clear all items from derived_froms list.

        Returns:
            self for method chaining
        """
        self._obj.derived_froms = []
        return self

    def add_engineering(self, item: AutosarEngineeringObject) -> "AclObjectSetBuilder":
        """Add a single item to engineerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.engineerings.append(item)
        return self

    def clear_engineerings(self) -> "AclObjectSetBuilder":
        """Clear all items from engineerings list.

        Returns:
            self for method chaining
        """
        self._obj.engineerings = []
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


    def build(self) -> AclObjectSet:
        """Build and return the AclObjectSet instance with validation."""
        self._validate_instance()
        pass
        return self._obj