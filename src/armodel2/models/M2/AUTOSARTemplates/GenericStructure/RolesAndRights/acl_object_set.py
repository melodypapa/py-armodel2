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
        "ACL-OBJECT-CLASS-REFS": lambda obj, elem: [obj.acl_object_clas_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "ACL-SCOPE": lambda obj, elem: setattr(obj, "acl_scope", AclScopeEnum.deserialize(elem)),
        "COLLECTION-REF": lambda obj, elem: setattr(obj, "collection_ref", ARRef.deserialize(elem)),
        "DERIVED-FROM-REFS": ("_POLYMORPHIC_LIST", "derived_from_refs", ["ARPackage", "AbstractImplementationDataType", "AclObjectSet", "AclOperation", "AclPermission", "AclRole", "AliasNameSet", "ApplicationArrayDataType", "ApplicationDataType", "ApplicationPrimitiveDataType", "ApplicationRecordDataType", "ApplicationSwComponentType", "BswEntryRelationshipSet", "BswModuleDescription", "BswModuleEntry", "BuildAction", "BuildActionEntity", "BuildActionEnvironment", "BuildActionManifest", "ClientServerInterface", "ClientServerInterfaceMapping", "ClientServerInterfaceToBswModuleEntryBlueprintMapping", "ComplexDeviceDriverSwComponentType", "CompositionSwComponentType", "CompuMethod", "ConsistencyNeeds", "DataConstr", "DataTypeMappingSet", "EcuAbstractionSwComponentType", "EcucDefinitionCollection", "EcucDestinationUriDefSet", "EcucModuleDef", "FlatMap", "ImplementationDataType", "ImpositionTime", "ImpositionTimeDefinitionGroup", "KeywordSet", "LifeCycleState", "LifeCycleStateDefinitionGroup", "ModeDeclarationGroup", "ModeInterfaceMapping", "ModeSwitchInterface", "NvBlockSwComponentType", "NvDataInterface", "ParameterInterface", "ParameterSwComponentType", "PortInterface", "PortInterfaceMapping", "PortInterfaceMappingSet", "PortPrototypeBlueprint", "SenderReceiverInterface", "SensorActuatorSwComponentType", "ServiceProxySwComponentType", "ServiceSwComponentType", "SwAddrMethod", "SwBaseType", "SwComponentType", "TriggerInterface", "TriggerInterfaceMapping", "VfbTiming"]),
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
            if tag == "ACL-OBJECT-CLASS-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.acl_object_clas_refs.append(ARRef.deserialize(item_elem))
            elif tag == "ACL-SCOPE":
                setattr(obj, "acl_scope", AclScopeEnum.deserialize(child))
            elif tag == "COLLECTION-REF":
                setattr(obj, "collection_ref", ARRef.deserialize(child))
            elif tag == "DERIVED-FROM-REFS":
                for item_elem in child:
                    obj.derived_from_refs.append(ARRef.deserialize(item_elem))
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
            raise ValueError("Attribute 'acl_scope' is required and cannot be None")
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
            raise ValueError("Attribute 'collection' is required and cannot be None")
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


    # Pre-computed validation constants (generated from JSON schema)
    _REQUIRED_ATTRIBUTES = {
        "aclScope",
    }
    _OPTIONAL_ATTRIBUTES = {
        "aclObjectClass",
        "collection",
        "derivedFrom",
        "engineering",
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
        if getattr(self._obj, "aclScope", None) is None:
            if mode == BuilderValidationMode.STRICT:
                raise ValueError("Required attribute 'aclScope' is None")
            elif mode == BuilderValidationMode.LENIENT:
                import warnings
                warnings.warn("Required attribute 'aclScope' is None", UserWarning)


    def build(self) -> AclObjectSet:
        """Build and return the AclObjectSet instance with validation."""
        self._validate_instance()
        return self._obj