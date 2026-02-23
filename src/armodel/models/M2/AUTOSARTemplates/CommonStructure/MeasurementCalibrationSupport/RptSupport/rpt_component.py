"""RptComponent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class RptComponent(Identifiable):
    """AUTOSAR RptComponent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mc_datas: list[RoleBasedMcDataAssignment]
    rp_impl_policy: Optional[RptImplPolicy]
    _rpt_executable_entities: list[RptExecutableEntity]
    def __init__(self) -> None:
        """Initialize RptComponent."""
        super().__init__()
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rp_impl_policy: Optional[RptImplPolicy] = None
        self._rpt_executable_entities: list[RptExecutableEntity] = []
    @property
    @xml_element_name("RPT-EXECUTABLE-ENTITYS")
    def rpt_executable_entities(self) -> list[RptExecutableEntity]:
        """Get rpt_executable_entities with custom XML element name."""
        return self._rpt_executable_entities

    @rpt_executable_entities.setter
    def rpt_executable_entities(self, value: list[RptExecutableEntity]) -> None:
        """Set rpt_executable_entities with custom XML element name."""
        self._rpt_executable_entities = value


    def serialize(self) -> ET.Element:
        """Serialize RptComponent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptComponent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mc_datas (list to container "MC-DATAS")
        if self.mc_datas:
            wrapper = ET.Element("MC-DATAS")
            for item in self.mc_datas:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rp_impl_policy
        if self.rp_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.rp_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RP-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_executable_entities (list to container "RPT-EXECUTABLE-ENTITYS")
        if self.rpt_executable_entities:
            wrapper = ET.Element("RPT-EXECUTABLE-ENTITYS")
            for item in self.rpt_executable_entities:
                serialized = SerializationHelper.serialize_item(item, "RptExecutableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptComponent":
        """Deserialize XML element to RptComponent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptComponent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptComponent, cls).deserialize(element)

        # Parse mc_datas (list from container "MC-DATAS")
        obj.mc_datas = []
        container = SerializationHelper.find_child_element(element, "MC-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_datas.append(child_value)

        # Parse rp_impl_policy
        child = SerializationHelper.find_child_element(element, "RP-IMPL-POLICY")
        if child is not None:
            rp_impl_policy_value = SerializationHelper.deserialize_by_tag(child, "RptImplPolicy")
            obj.rp_impl_policy = rp_impl_policy_value

        # Parse rpt_executable_entities (list from container "RPT-EXECUTABLE-ENTITYS")
        obj.rpt_executable_entities = []
        container = SerializationHelper.find_child_element(element, "RPT-EXECUTABLE-ENTITYS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_executable_entities.append(child_value)

        return obj



class RptComponentBuilder(IdentifiableBuilder):
    """Builder for RptComponent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptComponent = RptComponent()


    def with_mc_datas(self, items: list[RoleBasedMcDataAssignment]) -> "RptComponentBuilder":
        """Set mc_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = list(items) if items else []
        return self

    def with_rp_impl_policy(self, value: Optional[RptImplPolicy]) -> "RptComponentBuilder":
        """Set rp_impl_policy attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rp_impl_policy = value
        return self

    def with_rpt_executable_entities(self, items: list[RptExecutableEntity]) -> "RptComponentBuilder":
        """Set rpt_executable_entities list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities = list(items) if items else []
        return self


    def add_mc_data(self, item: RoleBasedMcDataAssignment) -> "RptComponentBuilder":
        """Add a single item to mc_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_datas.append(item)
        return self

    def clear_mc_datas(self) -> "RptComponentBuilder":
        """Clear all items from mc_datas list.

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = []
        return self

    def add_rpt_executable_entitie(self, item: RptExecutableEntity) -> "RptComponentBuilder":
        """Add a single item to rpt_executable_entities list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities.append(item)
        return self

    def clear_rpt_executable_entities(self) -> "RptComponentBuilder":
        """Clear all items from rpt_executable_entities list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_executable_entities = []
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


    def build(self) -> RptComponent:
        """Build and return the RptComponent instance with validation."""
        self._validate_instance()
        pass
        return self._obj