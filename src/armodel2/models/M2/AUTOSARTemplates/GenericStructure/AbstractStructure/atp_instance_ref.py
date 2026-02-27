"""AtpInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 971)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
    AtpClassifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_prototype import (
    AtpPrototype,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AtpInstanceRef(ARObject, ABC):
    """AUTOSAR AtpInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_base_ref: ARRef
    atp_context_refs: list[ARRef]
    atp_target_ref: ARRef
    def __init__(self) -> None:
        """Initialize AtpInstanceRef."""
        super().__init__()
        self.atp_base_ref: ARRef = None
        self.atp_context_refs: list[ARRef] = []
        self.atp_target_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize AtpInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtpInstanceRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize atp_base_ref
        if self.atp_base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.atp_base_ref, "AtpClassifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize atp_context_refs (list to container "ATP-CONTEXTS")
        if self.atp_context_refs:
            wrapper = ET.Element("ATP-CONTEXTS")
            for item in self.atp_context_refs:
                serialized = SerializationHelper.serialize_item(item, "AtpPrototype")
                if serialized is not None:
                    child_elem = ET.Element("ATP-CONTEXT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize atp_target_ref
        if self.atp_target_ref is not None:
            serialized = SerializationHelper.serialize_item(self.atp_target_ref, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpInstanceRef":
        """Deserialize XML element to AtpInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpInstanceRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpInstanceRef, cls).deserialize(element)

        # Parse atp_base_ref
        child = SerializationHelper.find_child_element(element, "ATP-BASE-REF")
        if child is not None:
            atp_base_ref_value = ARRef.deserialize(child)
            obj.atp_base_ref = atp_base_ref_value

        # Parse atp_context_refs (list from container "ATP-CONTEXTS")
        obj.atp_context_refs = []
        container = SerializationHelper.find_child_element(element, "ATP-CONTEXTS")
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
                    obj.atp_context_refs.append(child_value)

        # Parse atp_target_ref
        child = SerializationHelper.find_child_element(element, "ATP-TARGET-REF")
        if child is not None:
            atp_target_ref_value = ARRef.deserialize(child)
            obj.atp_target_ref = atp_target_ref_value

        return obj



class AtpInstanceRefBuilder(BuilderBase, ABC):
    """Builder for AtpInstanceRef with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AtpInstanceRef = AtpInstanceRef()


    def with_atp_base(self, value: AtpClassifier) -> "AtpInstanceRefBuilder":
        """Set atp_base attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.atp_base = value
        return self

    def with_atp_contexts(self, items: list[AtpPrototype]) -> "AtpInstanceRefBuilder":
        """Set atp_contexts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.atp_contexts = list(items) if items else []
        return self

    def with_atp_target(self, value: AtpFeature) -> "AtpInstanceRefBuilder":
        """Set atp_target attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.atp_target = value
        return self


    def add_atp_context(self, item: AtpPrototype) -> "AtpInstanceRefBuilder":
        """Add a single item to atp_contexts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.atp_contexts.append(item)
        return self

    def clear_atp_contexts(self) -> "AtpInstanceRefBuilder":
        """Clear all items from atp_contexts list.

        Returns:
            self for method chaining
        """
        self._obj.atp_contexts = []
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
    def build(self) -> AtpInstanceRef:
        """Build and return the AtpInstanceRef instance (abstract)."""
        raise NotImplementedError