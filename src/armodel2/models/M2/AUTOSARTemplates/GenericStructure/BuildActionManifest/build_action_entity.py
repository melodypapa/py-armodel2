"""BuildActionEntity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_invocator import (
    BuildActionInvocator,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BuildActionEntity(Identifiable, ABC):
    """AUTOSAR BuildActionEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    delivery_artifacts: list[AutosarEngineeringObject]
    invocation: Optional[BuildActionInvocator]
    def __init__(self) -> None:
        """Initialize BuildActionEntity."""
        super().__init__()
        self.delivery_artifacts: list[AutosarEngineeringObject] = []
        self.invocation: Optional[BuildActionInvocator] = None

    def serialize(self) -> ET.Element:
        """Serialize BuildActionEntity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BuildActionEntity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize delivery_artifacts (list to container "DELIVERY-ARTIFACTS")
        if self.delivery_artifacts:
            wrapper = ET.Element("DELIVERY-ARTIFACTS")
            for item in self.delivery_artifacts:
                serialized = SerializationHelper.serialize_item(item, "AutosarEngineeringObject")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize invocation
        if self.invocation is not None:
            serialized = SerializationHelper.serialize_item(self.invocation, "BuildActionInvocator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INVOCATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionEntity":
        """Deserialize XML element to BuildActionEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionEntity, cls).deserialize(element)

        # Parse delivery_artifacts (list from container "DELIVERY-ARTIFACTS")
        obj.delivery_artifacts = []
        container = SerializationHelper.find_child_element(element, "DELIVERY-ARTIFACTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.delivery_artifacts.append(child_value)

        # Parse invocation
        child = SerializationHelper.find_child_element(element, "INVOCATION")
        if child is not None:
            invocation_value = SerializationHelper.deserialize_by_tag(child, "BuildActionInvocator")
            obj.invocation = invocation_value

        return obj



class BuildActionEntityBuilder(IdentifiableBuilder):
    """Builder for BuildActionEntity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BuildActionEntity = BuildActionEntity()


    def with_delivery_artifacts(self, items: list[AutosarEngineeringObject]) -> "BuildActionEntityBuilder":
        """Set delivery_artifacts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.delivery_artifacts = list(items) if items else []
        return self

    def with_invocation(self, value: Optional[BuildActionInvocator]) -> "BuildActionEntityBuilder":
        """Set invocation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.invocation = value
        return self


    def add_delivery_artifact(self, item: AutosarEngineeringObject) -> "BuildActionEntityBuilder":
        """Add a single item to delivery_artifacts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.delivery_artifacts.append(item)
        return self

    def clear_delivery_artifacts(self) -> "BuildActionEntityBuilder":
        """Clear all items from delivery_artifacts list.

        Returns:
            self for method chaining
        """
        self._obj.delivery_artifacts = []
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
    def build(self) -> BuildActionEntity:
        """Build and return the BuildActionEntity instance (abstract)."""
        raise NotImplementedError