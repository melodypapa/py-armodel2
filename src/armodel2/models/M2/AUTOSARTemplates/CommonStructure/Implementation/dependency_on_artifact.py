"""DependencyOnArtifact AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 131)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

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
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    DependencyUsageEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DependencyOnArtifact(Identifiable):
    """AUTOSAR DependencyOnArtifact."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    artifact_descriptor: Optional[AutosarEngineeringObject]
    usage_refs: list[DependencyUsageEnum]
    def __init__(self) -> None:
        """Initialize DependencyOnArtifact."""
        super().__init__()
        self.artifact_descriptor: Optional[AutosarEngineeringObject] = None
        self.usage_refs: list[DependencyUsageEnum] = []

    def serialize(self) -> ET.Element:
        """Serialize DependencyOnArtifact to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DependencyOnArtifact, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize artifact_descriptor
        if self.artifact_descriptor is not None:
            serialized = SerializationHelper.serialize_item(self.artifact_descriptor, "AutosarEngineeringObject")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARTIFACT-DESCRIPTOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize usage_refs (list to container "USAGE-REFS")
        if self.usage_refs:
            wrapper = ET.Element("USAGE-REFS")
            for item in self.usage_refs:
                serialized = SerializationHelper.serialize_item(item, "DependencyUsageEnum")
                if serialized is not None:
                    child_elem = ET.Element("USAGE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DependencyOnArtifact":
        """Deserialize XML element to DependencyOnArtifact object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DependencyOnArtifact object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DependencyOnArtifact, cls).deserialize(element)

        # Parse artifact_descriptor
        child = SerializationHelper.find_child_element(element, "ARTIFACT-DESCRIPTOR")
        if child is not None:
            artifact_descriptor_value = SerializationHelper.deserialize_by_tag(child, "AutosarEngineeringObject")
            obj.artifact_descriptor = artifact_descriptor_value

        # Parse usage_refs (list from container "USAGE-REFS")
        obj.usage_refs = []
        container = SerializationHelper.find_child_element(element, "USAGE-REFS")
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
                    obj.usage_refs.append(child_value)

        return obj



class DependencyOnArtifactBuilder(IdentifiableBuilder):
    """Builder for DependencyOnArtifact with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DependencyOnArtifact = DependencyOnArtifact()


    def with_artifact_descriptor(self, value: Optional[AutosarEngineeringObject]) -> "DependencyOnArtifactBuilder":
        """Set artifact_descriptor attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.artifact_descriptor = value
        return self

    def with_usages(self, items: list[DependencyUsageEnum]) -> "DependencyOnArtifactBuilder":
        """Set usages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.usages = list(items) if items else []
        return self


    def add_usage(self, item: DependencyUsageEnum) -> "DependencyOnArtifactBuilder":
        """Add a single item to usages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.usages.append(item)
        return self

    def clear_usages(self) -> "DependencyOnArtifactBuilder":
        """Clear all items from usages list.

        Returns:
            self for method chaining
        """
        self._obj.usages = []
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


    def build(self) -> DependencyOnArtifact:
        """Build and return the DependencyOnArtifact instance with validation."""
        self._validate_instance()
        pass
        return self._obj