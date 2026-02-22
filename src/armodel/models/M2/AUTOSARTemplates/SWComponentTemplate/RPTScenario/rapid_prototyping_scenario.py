"""RapidPrototypingScenario AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 846)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_container import (
    RptContainer,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_profile import (
    RptProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class RapidPrototypingScenario(ARElement):
    """AUTOSAR RapidPrototypingScenario."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    host_system_ref: Optional[ARRef]
    rpt_containers: list[RptContainer]
    rpt_profiles: list[RptProfile]
    rpt_system_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize RapidPrototypingScenario."""
        super().__init__()
        self.host_system_ref: Optional[ARRef] = None
        self.rpt_containers: list[RptContainer] = []
        self.rpt_profiles: list[RptProfile] = []
        self.rpt_system_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize RapidPrototypingScenario to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RapidPrototypingScenario, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize host_system_ref
        if self.host_system_ref is not None:
            serialized = SerializationHelper.serialize_item(self.host_system_ref, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HOST-SYSTEM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_containers (list to container "RPT-CONTAINERS")
        if self.rpt_containers:
            wrapper = ET.Element("RPT-CONTAINERS")
            for item in self.rpt_containers:
                serialized = SerializationHelper.serialize_item(item, "RptContainer")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_profiles (list to container "RPT-PROFILES")
        if self.rpt_profiles:
            wrapper = ET.Element("RPT-PROFILES")
            for item in self.rpt_profiles:
                serialized = SerializationHelper.serialize_item(item, "RptProfile")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_system_ref
        if self.rpt_system_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_system_ref, "System")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SYSTEM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RapidPrototypingScenario":
        """Deserialize XML element to RapidPrototypingScenario object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RapidPrototypingScenario object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RapidPrototypingScenario, cls).deserialize(element)

        # Parse host_system_ref
        child = SerializationHelper.find_child_element(element, "HOST-SYSTEM-REF")
        if child is not None:
            host_system_ref_value = ARRef.deserialize(child)
            obj.host_system_ref = host_system_ref_value

        # Parse rpt_containers (list from container "RPT-CONTAINERS")
        obj.rpt_containers = []
        container = SerializationHelper.find_child_element(element, "RPT-CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_containers.append(child_value)

        # Parse rpt_profiles (list from container "RPT-PROFILES")
        obj.rpt_profiles = []
        container = SerializationHelper.find_child_element(element, "RPT-PROFILES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_profiles.append(child_value)

        # Parse rpt_system_ref
        child = SerializationHelper.find_child_element(element, "RPT-SYSTEM-REF")
        if child is not None:
            rpt_system_ref_value = ARRef.deserialize(child)
            obj.rpt_system_ref = rpt_system_ref_value

        return obj



class RapidPrototypingScenarioBuilder:
    """Builder for RapidPrototypingScenario with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: RapidPrototypingScenario = RapidPrototypingScenario()


    def with_short_name(self, value: Identifier) -> "RapidPrototypingScenarioBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "RapidPrototypingScenarioBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "RapidPrototypingScenarioBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "RapidPrototypingScenarioBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "RapidPrototypingScenarioBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "RapidPrototypingScenarioBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "RapidPrototypingScenarioBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "RapidPrototypingScenarioBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "RapidPrototypingScenarioBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_host_system(self, value: Optional[System]) -> "RapidPrototypingScenarioBuilder":
        """Set host_system attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.host_system = value
        return self

    def with_rpt_containers(self, items: list[RptContainer]) -> "RapidPrototypingScenarioBuilder":
        """Set rpt_containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers = list(items) if items else []
        return self

    def with_rpt_profiles(self, items: list[RptProfile]) -> "RapidPrototypingScenarioBuilder":
        """Set rpt_profiles list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_profiles = list(items) if items else []
        return self

    def with_rpt_system(self, value: Optional[System]) -> "RapidPrototypingScenarioBuilder":
        """Set rpt_system attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_system = value
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "RapidPrototypingScenarioBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "RapidPrototypingScenarioBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "RapidPrototypingScenarioBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "RapidPrototypingScenarioBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_rpt_container(self, item: RptContainer) -> "RapidPrototypingScenarioBuilder":
        """Add a single item to rpt_containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers.append(item)
        return self

    def clear_rpt_containers(self) -> "RapidPrototypingScenarioBuilder":
        """Clear all items from rpt_containers list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers = []
        return self

    def add_rpt_profile(self, item: RptProfile) -> "RapidPrototypingScenarioBuilder":
        """Add a single item to rpt_profiles list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_profiles.append(item)
        return self

    def clear_rpt_profiles(self) -> "RapidPrototypingScenarioBuilder":
        """Clear all items from rpt_profiles list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_profiles = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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


    def build(self) -> RapidPrototypingScenario:
        """Build and return the RapidPrototypingScenario instance with validation."""
        self._validate_instance()
        pass
        return self._obj