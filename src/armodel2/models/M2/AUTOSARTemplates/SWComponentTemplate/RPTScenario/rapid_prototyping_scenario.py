"""RapidPrototypingScenario AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 327)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 846)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_container import (
    RptContainer,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_profile import (
    RptProfile,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RapidPrototypingScenario(ARElement):
    """AUTOSAR RapidPrototypingScenario."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RAPID-PROTOTYPING-SCENARIO"


    host_system_ref: Optional[ARRef]
    rpt_containers: list[RptContainer]
    rpt_profiles: list[RptProfile]
    rpt_system_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "HOST-SYSTEM-REF": lambda obj, elem: setattr(obj, "host_system_ref", ARRef.deserialize(elem)),
        "RPT-CONTAINERS": lambda obj, elem: obj.rpt_containers.append(SerializationHelper.deserialize_by_tag(elem, "RptContainer")),
        "RPT-PROFILES": lambda obj, elem: obj.rpt_profiles.append(SerializationHelper.deserialize_by_tag(elem, "RptProfile")),
        "RPT-SYSTEM-REF": lambda obj, elem: setattr(obj, "rpt_system_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "HOST-SYSTEM-REF":
                setattr(obj, "host_system_ref", ARRef.deserialize(child))
            elif tag == "RPT-CONTAINERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rpt_containers.append(SerializationHelper.deserialize_by_tag(item_elem, "RptContainer"))
            elif tag == "RPT-PROFILES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rpt_profiles.append(SerializationHelper.deserialize_by_tag(item_elem, "RptProfile"))
            elif tag == "RPT-SYSTEM-REF":
                setattr(obj, "rpt_system_ref", ARRef.deserialize(child))

        return obj



class RapidPrototypingScenarioBuilder(ARElementBuilder):
    """Builder for RapidPrototypingScenario with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RapidPrototypingScenario = RapidPrototypingScenario()


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


    def build(self) -> RapidPrototypingScenario:
        """Build and return the RapidPrototypingScenario instance with validation."""
        self._validate_instance()
        pass
        return self._obj