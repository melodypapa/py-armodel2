"""Collection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2009)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 398)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 175)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ElementCollection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    AutoCollectEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef.any_instance_ref import (
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class Collection(ARElement):
    """AUTOSAR Collection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    auto_collect: Optional[AutoCollectEnum]
    collected_instance_irefs: list[AnyInstanceRef]
    collection_semantics: Optional[NameToken]
    element_role: Optional[Identifier]
    element_refs: list[ARRef]
    source_element_refs: list[ARRef]
    source_instance_irefs: list[AnyInstanceRef]
    def __init__(self) -> None:
        """Initialize Collection."""
        super().__init__()
        self.auto_collect: Optional[AutoCollectEnum] = None
        self.collected_instance_irefs: list[AnyInstanceRef] = []
        self.collection_semantics: Optional[NameToken] = None
        self.element_role: Optional[Identifier] = None
        self.element_refs: list[ARRef] = []
        self.source_element_refs: list[ARRef] = []
        self.source_instance_irefs: list[AnyInstanceRef] = []

    def serialize(self) -> ET.Element:
        """Serialize Collection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Collection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize auto_collect
        if self.auto_collect is not None:
            serialized = SerializationHelper.serialize_item(self.auto_collect, "AutoCollectEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-COLLECT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize collected_instance_irefs (list of instance references with wrapper "COLLECTED-INSTANCE-IREF")
        if self.collected_instance_irefs:
            serialized = SerializationHelper.serialize_item(self.collected_instance_irefs, "AnyInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("COLLECTED-INSTANCE-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        # Serialize collection_semantics
        if self.collection_semantics is not None:
            serialized = SerializationHelper.serialize_item(self.collection_semantics, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COLLECTION-SEMANTICS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_role
        if self.element_role is not None:
            serialized = SerializationHelper.serialize_item(self.element_role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT-ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element_refs (list to container "ELEMENT-REFS")
        if self.element_refs:
            wrapper = ET.Element("ELEMENT-REFS")
            for item in self.element_refs:
                serialized = SerializationHelper.serialize_item(item, "Identifiable")
                if serialized is not None:
                    child_elem = ET.Element("ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_element_refs (list to container "SOURCE-ELEMENT-REFS")
        if self.source_element_refs:
            wrapper = ET.Element("SOURCE-ELEMENT-REFS")
            for item in self.source_element_refs:
                serialized = SerializationHelper.serialize_item(item, "Identifiable")
                if serialized is not None:
                    child_elem = ET.Element("SOURCE-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize source_instance_irefs (list of instance references with wrapper "SOURCE-INSTANCES-IREF")
        if self.source_instance_irefs:
            serialized = SerializationHelper.serialize_item(self.source_instance_irefs, "AnyInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("SOURCE-INSTANCES-IREF")
                # Append the serialized element as a child (don't flatten it)
                iref_wrapper.append(serialized)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Collection":
        """Deserialize XML element to Collection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Collection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Collection, cls).deserialize(element)

        # Parse auto_collect
        child = SerializationHelper.find_child_element(element, "AUTO-COLLECT")
        if child is not None:
            auto_collect_value = AutoCollectEnum.deserialize(child)
            obj.auto_collect = auto_collect_value

        # Parse collected_instance_irefs (instance reference from wrapper "COLLECTED-INSTANCE-IREF")
        wrapper = SerializationHelper.find_child_element(element, "COLLECTED-INSTANCE-IREF")
        if wrapper is not None:
            # Get the first child element (the actual reference)
            children = list(wrapper)
            if children:
                inner_elem = children[0]
                collected_instance_irefs_value = SerializationHelper.deserialize_by_tag(inner_elem)
                obj.collected_instance_irefs = collected_instance_irefs_value

        # Parse collection_semantics
        child = SerializationHelper.find_child_element(element, "COLLECTION-SEMANTICS")
        if child is not None:
            collection_semantics_value = child.text
            obj.collection_semantics = collection_semantics_value

        # Parse element_role
        child = SerializationHelper.find_child_element(element, "ELEMENT-ROLE")
        if child is not None:
            element_role_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.element_role = element_role_value

        # Parse element_refs (list from container "ELEMENT-REFS")
        obj.element_refs = []
        container = SerializationHelper.find_child_element(element, "ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.element_refs.append(child_value)

        # Parse source_element_refs (list from container "SOURCE-ELEMENT-REFS")
        obj.source_element_refs = []
        container = SerializationHelper.find_child_element(element, "SOURCE-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.source_element_refs.append(child_value)

        # Parse source_instance_irefs (instance reference from wrapper "SOURCE-INSTANCES-IREF")
        wrapper = SerializationHelper.find_child_element(element, "SOURCE-INSTANCES-IREF")
        if wrapper is not None:
            # Get the first child element (the actual reference)
            children = list(wrapper)
            if children:
                inner_elem = children[0]
                source_instance_irefs_value = SerializationHelper.deserialize_by_tag(inner_elem)
                obj.source_instance_irefs = source_instance_irefs_value

        return obj



class CollectionBuilder(ARElementBuilder):
    """Builder for Collection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Collection = Collection()


    def with_auto_collect(self, value: Optional[AutoCollectEnum]) -> "CollectionBuilder":
        """Set auto_collect attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auto_collect = value
        return self

    def with_collected_instance(self, items: list[AnyInstanceRef]) -> "CollectionBuilder":
        """Set collected_instance list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.collected_instance = list(items) if items else []
        return self

    def with_collection_semantics(self, value: Optional[NameToken]) -> "CollectionBuilder":
        """Set collection_semantics attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.collection_semantics = value
        return self

    def with_element_role(self, value: Optional[Identifier]) -> "CollectionBuilder":
        """Set element_role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.element_role = value
        return self

    def with_elements(self, items: list[Identifiable]) -> "CollectionBuilder":
        """Set elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.elements = list(items) if items else []
        return self

    def with_source_elements(self, items: list[Identifiable]) -> "CollectionBuilder":
        """Set source_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.source_elements = list(items) if items else []
        return self

    def with_source_instances(self, items: list[AnyInstanceRef]) -> "CollectionBuilder":
        """Set source_instances list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.source_instances = list(items) if items else []
        return self


    def add_collected_instanc(self, item: AnyInstanceRef) -> "CollectionBuilder":
        """Add a single item to collected_instance list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.collected_instance.append(item)
        return self

    def clear_collected_instance(self) -> "CollectionBuilder":
        """Clear all items from collected_instance list.

        Returns:
            self for method chaining
        """
        self._obj.collected_instance = []
        return self

    def add_element(self, item: Identifiable) -> "CollectionBuilder":
        """Add a single item to elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.elements.append(item)
        return self

    def clear_elements(self) -> "CollectionBuilder":
        """Clear all items from elements list.

        Returns:
            self for method chaining
        """
        self._obj.elements = []
        return self

    def add_source_element(self, item: Identifiable) -> "CollectionBuilder":
        """Add a single item to source_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.source_elements.append(item)
        return self

    def clear_source_elements(self) -> "CollectionBuilder":
        """Clear all items from source_elements list.

        Returns:
            self for method chaining
        """
        self._obj.source_elements = []
        return self

    def add_source_instance(self, item: AnyInstanceRef) -> "CollectionBuilder":
        """Add a single item to source_instances list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.source_instances.append(item)
        return self

    def clear_source_instances(self) -> "CollectionBuilder":
        """Clear all items from source_instances list.

        Returns:
            self for method chaining
        """
        self._obj.source_instances = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> Collection:
        """Build and return the Collection instance with validation."""
        self._validate_instance()
        pass
        return self._obj