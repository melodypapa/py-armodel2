"""AtpBlueprint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 305)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)


class AtpBlueprint(Identifiable, ABC):
    """AUTOSAR AtpBlueprint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    _blueprint_policies: list[BlueprintPolicy]
    def __init__(self) -> None:
        """Initialize AtpBlueprint."""
        super().__init__()
        self._blueprint_policies: list[BlueprintPolicy] = []
    @property
    @xml_element_name("BLUEPRINT-POLICYS")
    def blueprint_policies(self) -> list[BlueprintPolicy]:
        """Get blueprint_policies with custom XML element name."""
        return self._blueprint_policies

    @blueprint_policies.setter
    def blueprint_policies(self, value: list[BlueprintPolicy]) -> None:
        """Set blueprint_policies with custom XML element name."""
        self._blueprint_policies = value


    def serialize(self) -> ET.Element:
        """Serialize AtpBlueprint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtpBlueprint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint_policies (list to container "BLUEPRINT-POLICYS")
        if self.blueprint_policies:
            wrapper = ET.Element("BLUEPRINT-POLICYS")
            for item in self.blueprint_policies:
                serialized = SerializationHelper.serialize_item(item, "BlueprintPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpBlueprint":
        """Deserialize XML element to AtpBlueprint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpBlueprint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpBlueprint, cls).deserialize(element)

        # Parse blueprint_policies (list from container "BLUEPRINT-POLICYS")
        obj.blueprint_policies = []
        container = SerializationHelper.find_child_element(element, "BLUEPRINT-POLICYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.blueprint_policies.append(child_value)

        return obj



class AtpBlueprintBuilder(IdentifiableBuilder):
    """Builder for AtpBlueprint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AtpBlueprint = AtpBlueprint()


    def with_blueprint_policies(self, items: list[BlueprintPolicy]) -> "AtpBlueprintBuilder":
        """Set blueprint_policies list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.blueprint_policies = list(items) if items else []
        return self


    def add_blueprint_policie(self, item: BlueprintPolicy) -> "AtpBlueprintBuilder":
        """Add a single item to blueprint_policies list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.blueprint_policies.append(item)
        return self

    def clear_blueprint_policies(self) -> "AtpBlueprintBuilder":
        """Clear all items from blueprint_policies list.

        Returns:
            self for method chaining
        """
        self._obj.blueprint_policies = []
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


    @abstractmethod
    def build(self) -> AtpBlueprint:
        """Build and return the AtpBlueprint instance (abstract)."""
        raise NotImplementedError