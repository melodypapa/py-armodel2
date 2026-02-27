"""RptContainer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 847)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_hook import (
    RptHook,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_profile import (
    RptProfile,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_sw_prototyping_access import (
    RptSwPrototypingAccess,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptContainer(Identifiable):
    """AUTOSAR RptContainer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    by_pass_points: list[AtpFeature]
    explicit_rpt_refs: list[ARRef]
    rpt_containers: list[RptContainer]
    rpt_executable_entity: Optional[RptExecutableEntity]
    rpt_hook: Optional[RptHook]
    rpt_impl_policy: Optional[RptImplPolicy]
    rpt_sw: Optional[RptSwPrototypingAccess]
    def __init__(self) -> None:
        """Initialize RptContainer."""
        super().__init__()
        self.by_pass_points: list[AtpFeature] = []
        self.explicit_rpt_refs: list[ARRef] = []
        self.rpt_containers: list[RptContainer] = []
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_hook: Optional[RptHook] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_sw: Optional[RptSwPrototypingAccess] = None

    def serialize(self) -> ET.Element:
        """Serialize RptContainer to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptContainer, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize by_pass_points (list to container "BY-PASS-POINTS")
        if self.by_pass_points:
            wrapper = ET.Element("BY-PASS-POINTS")
            for item in self.by_pass_points:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize explicit_rpt_refs (list to container "EXPLICIT-RPTS")
        if self.explicit_rpt_refs:
            wrapper = ET.Element("EXPLICIT-RPTS")
            for item in self.explicit_rpt_refs:
                serialized = SerializationHelper.serialize_item(item, "RptProfile")
                if serialized is not None:
                    child_elem = ET.Element("EXPLICIT-RPT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_containers (list to container "RPT-CONTAINERS")
        if self.rpt_containers:
            wrapper = ET.Element("RPT-CONTAINERS")
            for item in self.rpt_containers:
                serialized = SerializationHelper.serialize_item(item, "RptContainer")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_executable_entity
        if self.rpt_executable_entity is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_executable_entity, "RptExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-EXECUTABLE-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_hook
        if self.rpt_hook is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_hook, "RptHook")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-HOOK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_impl_policy
        if self.rpt_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_sw
        if self.rpt_sw is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_sw, "RptSwPrototypingAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptContainer":
        """Deserialize XML element to RptContainer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptContainer object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptContainer, cls).deserialize(element)

        # Parse by_pass_points (list from container "BY-PASS-POINTS")
        obj.by_pass_points = []
        container = SerializationHelper.find_child_element(element, "BY-PASS-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.by_pass_points.append(child_value)

        # Parse explicit_rpt_refs (list from container "EXPLICIT-RPTS")
        obj.explicit_rpt_refs = []
        container = SerializationHelper.find_child_element(element, "EXPLICIT-RPTS")
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
                    obj.explicit_rpt_refs.append(child_value)

        # Parse rpt_containers (list from container "RPT-CONTAINERS")
        obj.rpt_containers = []
        container = SerializationHelper.find_child_element(element, "RPT-CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_containers.append(child_value)

        # Parse rpt_executable_entity
        child = SerializationHelper.find_child_element(element, "RPT-EXECUTABLE-ENTITY")
        if child is not None:
            rpt_executable_entity_value = SerializationHelper.deserialize_by_tag(child, "RptExecutableEntity")
            obj.rpt_executable_entity = rpt_executable_entity_value

        # Parse rpt_hook
        child = SerializationHelper.find_child_element(element, "RPT-HOOK")
        if child is not None:
            rpt_hook_value = SerializationHelper.deserialize_by_tag(child, "RptHook")
            obj.rpt_hook = rpt_hook_value

        # Parse rpt_impl_policy
        child = SerializationHelper.find_child_element(element, "RPT-IMPL-POLICY")
        if child is not None:
            rpt_impl_policy_value = SerializationHelper.deserialize_by_tag(child, "RptImplPolicy")
            obj.rpt_impl_policy = rpt_impl_policy_value

        # Parse rpt_sw
        child = SerializationHelper.find_child_element(element, "RPT-SW")
        if child is not None:
            rpt_sw_value = SerializationHelper.deserialize_by_tag(child, "RptSwPrototypingAccess")
            obj.rpt_sw = rpt_sw_value

        return obj



class RptContainerBuilder(IdentifiableBuilder):
    """Builder for RptContainer with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptContainer = RptContainer()


    def with_by_pass_points(self, items: list[AtpFeature]) -> "RptContainerBuilder":
        """Set by_pass_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.by_pass_points = list(items) if items else []
        return self

    def with_explicit_rpts(self, items: list[RptProfile]) -> "RptContainerBuilder":
        """Set explicit_rpts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.explicit_rpts = list(items) if items else []
        return self

    def with_rpt_containers(self, items: list[RptContainer]) -> "RptContainerBuilder":
        """Set rpt_containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers = list(items) if items else []
        return self

    def with_rpt_executable_entity(self, value: Optional[RptExecutableEntity]) -> "RptContainerBuilder":
        """Set rpt_executable_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_executable_entity = value
        return self

    def with_rpt_hook(self, value: Optional[RptHook]) -> "RptContainerBuilder":
        """Set rpt_hook attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_hook = value
        return self

    def with_rpt_impl_policy(self, value: Optional[RptImplPolicy]) -> "RptContainerBuilder":
        """Set rpt_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_impl_policy = value
        return self

    def with_rpt_sw(self, value: Optional[RptSwPrototypingAccess]) -> "RptContainerBuilder":
        """Set rpt_sw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_sw = value
        return self


    def add_by_pass_point(self, item: AtpFeature) -> "RptContainerBuilder":
        """Add a single item to by_pass_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.by_pass_points.append(item)
        return self

    def clear_by_pass_points(self) -> "RptContainerBuilder":
        """Clear all items from by_pass_points list.

        Returns:
            self for method chaining
        """
        self._obj.by_pass_points = []
        return self

    def add_explicit_rpt(self, item: RptProfile) -> "RptContainerBuilder":
        """Add a single item to explicit_rpts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.explicit_rpts.append(item)
        return self

    def clear_explicit_rpts(self) -> "RptContainerBuilder":
        """Clear all items from explicit_rpts list.

        Returns:
            self for method chaining
        """
        self._obj.explicit_rpts = []
        return self

    def add_rpt_container(self, item: RptContainer) -> "RptContainerBuilder":
        """Add a single item to rpt_containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers.append(item)
        return self

    def clear_rpt_containers(self) -> "RptContainerBuilder":
        """Clear all items from rpt_containers list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_containers = []
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


    def build(self) -> RptContainer:
        """Build and return the RptContainer instance with validation."""
        self._validate_instance()
        pass
        return self._obj