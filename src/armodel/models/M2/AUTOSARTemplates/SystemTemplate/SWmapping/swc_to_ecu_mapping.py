"""SwcToEcuMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SwcToEcuMapping(Identifiable):
    """AUTOSAR SwcToEcuMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    components: list[Any]
    controlled_hw_ref: Optional[ARRef]
    ecu_instance_ref: Optional[ARRef]
    processing_unit_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcToEcuMapping."""
        super().__init__()
        self.components: list[Any] = []
        self.controlled_hw_ref: Optional[ARRef] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.processing_unit_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcToEcuMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcToEcuMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize components (list to container "COMPONENTS")
        if self.components:
            wrapper = ET.Element("COMPONENTS")
            for item in self.components:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize controlled_hw_ref
        if self.controlled_hw_ref is not None:
            serialized = SerializationHelper.serialize_item(self.controlled_hw_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTROLLED-HW-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize processing_unit_ref
        if self.processing_unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.processing_unit_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToEcuMapping":
        """Deserialize XML element to SwcToEcuMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToEcuMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcToEcuMapping, cls).deserialize(element)

        # Parse components (list from container "COMPONENTS")
        obj.components = []
        container = SerializationHelper.find_child_element(element, "COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.components.append(child_value)

        # Parse controlled_hw_ref
        child = SerializationHelper.find_child_element(element, "CONTROLLED-HW-REF")
        if child is not None:
            controlled_hw_ref_value = ARRef.deserialize(child)
            obj.controlled_hw_ref = controlled_hw_ref_value

        # Parse ecu_instance_ref
        child = SerializationHelper.find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse processing_unit_ref
        child = SerializationHelper.find_child_element(element, "PROCESSING-UNIT-REF")
        if child is not None:
            processing_unit_ref_value = ARRef.deserialize(child)
            obj.processing_unit_ref = processing_unit_ref_value

        return obj



class SwcToEcuMappingBuilder(IdentifiableBuilder):
    """Builder for SwcToEcuMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcToEcuMapping = SwcToEcuMapping()


    def with_components(self, items: list[any (SwComponent)]) -> "SwcToEcuMappingBuilder":
        """Set components list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.components = list(items) if items else []
        return self

    def with_controlled_hw(self, value: Optional[HwElement]) -> "SwcToEcuMappingBuilder":
        """Set controlled_hw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.controlled_hw = value
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "SwcToEcuMappingBuilder":
        """Set ecu_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_instance = value
        return self

    def with_processing_unit(self, value: Optional[HwElement]) -> "SwcToEcuMappingBuilder":
        """Set processing_unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.processing_unit = value
        return self


    def add_component(self, item: any (SwComponent)) -> "SwcToEcuMappingBuilder":
        """Add a single item to components list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.components.append(item)
        return self

    def clear_components(self) -> "SwcToEcuMappingBuilder":
        """Clear all items from components list.

        Returns:
            self for method chaining
        """
        self._obj.components = []
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


    def build(self) -> SwcToEcuMapping:
        """Build and return the SwcToEcuMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj