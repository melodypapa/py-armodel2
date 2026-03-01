"""RptExecutableEntityEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_service_point import (
    RptServicePoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptExecutableEntityEvent(Identifiable):
    """AUTOSAR RptExecutableEntityEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "RPT-EXECUTABLE-ENTITY-EVENT"


    execution_refs: list[ARRef]
    mc_datas: list[RoleBasedMcDataAssignment]
    rpt_event_id: Optional[PositiveInteger]
    rpt_executable_entity: Optional[RptExecutableEntity]
    rpt_impl_policy: Optional[RptImplPolicy]
    rpt_service_point_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "EXECUTION-REFS": lambda obj, elem: [obj.execution_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "MC-DATAS": lambda obj, elem: obj.mc_datas.append(SerializationHelper.deserialize_by_tag(elem, "RoleBasedMcDataAssignment")),
        "RPT-EVENT-ID": lambda obj, elem: setattr(obj, "rpt_event_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "RPT-EXECUTABLE-ENTITY": lambda obj, elem: setattr(obj, "rpt_executable_entity", SerializationHelper.deserialize_by_tag(elem, "RptExecutableEntity")),
        "RPT-IMPL-POLICY": lambda obj, elem: setattr(obj, "rpt_impl_policy", SerializationHelper.deserialize_by_tag(elem, "RptImplPolicy")),
        "RPT-SERVICE-POINT-REFS": lambda obj, elem: [obj.rpt_service_point_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize RptExecutableEntityEvent."""
        super().__init__()
        self.execution_refs: list[ARRef] = []
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_service_point_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize RptExecutableEntityEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptExecutableEntityEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize execution_refs (list to container "EXECUTION-REFS")
        if self.execution_refs:
            wrapper = ET.Element("EXECUTION-REFS")
            for item in self.execution_refs:
                serialized = SerializationHelper.serialize_item(item, "RptExecutionContext")
                if serialized is not None:
                    child_elem = ET.Element("EXECUTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_datas (list to container "MC-DATAS")
        if self.mc_datas:
            wrapper = ET.Element("MC-DATAS")
            for item in self.mc_datas:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_event_id
        if self.rpt_event_id is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_event_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-EVENT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize rpt_service_point_refs (list to container "RPT-SERVICE-POINT-REFS")
        if self.rpt_service_point_refs:
            wrapper = ET.Element("RPT-SERVICE-POINT-REFS")
            for item in self.rpt_service_point_refs:
                serialized = SerializationHelper.serialize_item(item, "RptServicePoint")
                if serialized is not None:
                    child_elem = ET.Element("RPT-SERVICE-POINT-REF")
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
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntityEvent":
        """Deserialize XML element to RptExecutableEntityEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptExecutableEntityEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptExecutableEntityEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EXECUTION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.execution_refs.append(ARRef.deserialize(item_elem))
            elif tag == "MC-DATAS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mc_datas.append(SerializationHelper.deserialize_by_tag(item_elem, "RoleBasedMcDataAssignment"))
            elif tag == "RPT-EVENT-ID":
                setattr(obj, "rpt_event_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "RPT-EXECUTABLE-ENTITY":
                setattr(obj, "rpt_executable_entity", SerializationHelper.deserialize_by_tag(child, "RptExecutableEntity"))
            elif tag == "RPT-IMPL-POLICY":
                setattr(obj, "rpt_impl_policy", SerializationHelper.deserialize_by_tag(child, "RptImplPolicy"))
            elif tag == "RPT-SERVICE-POINT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.rpt_service_point_refs.append(ARRef.deserialize(item_elem))

        return obj



class RptExecutableEntityEventBuilder(IdentifiableBuilder):
    """Builder for RptExecutableEntityEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptExecutableEntityEvent = RptExecutableEntityEvent()


    def with_executions(self, items: list[RptExecutionContext]) -> "RptExecutableEntityEventBuilder":
        """Set executions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.executions = list(items) if items else []
        return self

    def with_mc_datas(self, items: list[RoleBasedMcDataAssignment]) -> "RptExecutableEntityEventBuilder":
        """Set mc_datas list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = list(items) if items else []
        return self

    def with_rpt_event_id(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityEventBuilder":
        """Set rpt_event_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rpt_event_id = value
        return self

    def with_rpt_executable_entity(self, value: Optional[RptExecutableEntity]) -> "RptExecutableEntityEventBuilder":
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

    def with_rpt_impl_policy(self, value: Optional[RptImplPolicy]) -> "RptExecutableEntityEventBuilder":
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

    def with_rpt_service_points(self, items: list[RptServicePoint]) -> "RptExecutableEntityEventBuilder":
        """Set rpt_service_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points = list(items) if items else []
        return self


    def add_execution(self, item: RptExecutionContext) -> "RptExecutableEntityEventBuilder":
        """Add a single item to executions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.executions.append(item)
        return self

    def clear_executions(self) -> "RptExecutableEntityEventBuilder":
        """Clear all items from executions list.

        Returns:
            self for method chaining
        """
        self._obj.executions = []
        return self

    def add_mc_data(self, item: RoleBasedMcDataAssignment) -> "RptExecutableEntityEventBuilder":
        """Add a single item to mc_datas list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mc_datas.append(item)
        return self

    def clear_mc_datas(self) -> "RptExecutableEntityEventBuilder":
        """Clear all items from mc_datas list.

        Returns:
            self for method chaining
        """
        self._obj.mc_datas = []
        return self

    def add_rpt_service_point(self, item: RptServicePoint) -> "RptExecutableEntityEventBuilder":
        """Add a single item to rpt_service_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points.append(item)
        return self

    def clear_rpt_service_points(self) -> "RptExecutableEntityEventBuilder":
        """Clear all items from rpt_service_points list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points = []
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


    def build(self) -> RptExecutableEntityEvent:
        """Build and return the RptExecutableEntityEvent instance with validation."""
        self._validate_instance()
        pass
        return self._obj