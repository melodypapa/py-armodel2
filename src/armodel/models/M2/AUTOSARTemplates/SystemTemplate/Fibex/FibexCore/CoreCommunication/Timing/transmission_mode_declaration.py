"""TransmissionModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication_Timing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.mode_driven_transmission_mode_condition import (
    ModeDrivenTransmissionModeCondition,
)


class TransmissionModeDeclaration(ARObject):
    """AUTOSAR TransmissionModeDeclaration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_drivens: list[ModeDrivenTransmissionModeCondition]
    transmission: Optional[Any]
    def __init__(self) -> None:
        """Initialize TransmissionModeDeclaration."""
        super().__init__()
        self.mode_drivens: list[ModeDrivenTransmissionModeCondition] = []
        self.transmission: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TransmissionModeDeclaration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransmissionModeDeclaration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode_drivens (list to container "MODE-DRIVENS")
        if self.mode_drivens:
            wrapper = ET.Element("MODE-DRIVENS")
            for item in self.mode_drivens:
                serialized = SerializationHelper.serialize_item(item, "ModeDrivenTransmissionModeCondition")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transmission
        if self.transmission is not None:
            serialized = SerializationHelper.serialize_item(self.transmission, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeDeclaration":
        """Deserialize XML element to TransmissionModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransmissionModeDeclaration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransmissionModeDeclaration, cls).deserialize(element)

        # Parse mode_drivens (list from container "MODE-DRIVENS")
        obj.mode_drivens = []
        container = SerializationHelper.find_child_element(element, "MODE-DRIVENS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_drivens.append(child_value)

        # Parse transmission
        child = SerializationHelper.find_child_element(element, "TRANSMISSION")
        if child is not None:
            transmission_value = child.text
            obj.transmission = transmission_value

        return obj



class TransmissionModeDeclarationBuilder(BuilderBase):
    """Builder for TransmissionModeDeclaration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransmissionModeDeclaration = TransmissionModeDeclaration()


    def with_mode_drivens(self, items: list[ModeDrivenTransmissionModeCondition]) -> "TransmissionModeDeclarationBuilder":
        """Set mode_drivens list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_drivens = list(items) if items else []
        return self

    def with_transmission(self, value: Optional[any (TransmissionMode)]) -> "TransmissionModeDeclarationBuilder":
        """Set transmission attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission = value
        return self


    def add_mode_driven(self, item: ModeDrivenTransmissionModeCondition) -> "TransmissionModeDeclarationBuilder":
        """Add a single item to mode_drivens list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_drivens.append(item)
        return self

    def clear_mode_drivens(self) -> "TransmissionModeDeclarationBuilder":
        """Clear all items from mode_drivens list.

        Returns:
            self for method chaining
        """
        self._obj.mode_drivens = []
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


    def build(self) -> TransmissionModeDeclaration:
        """Build and return the TransmissionModeDeclaration instance with validation."""
        self._validate_instance()
        pass
        return self._obj