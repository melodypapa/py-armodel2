"""RptSupportData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 198)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_component import (
    RptComponent,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_service_point import (
    RptServicePoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class RptSupportData(ARObject):
    """AUTOSAR RptSupportData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    executions: list[RptExecutionContext]
    rpt_components: list[RptComponent]
    rpt_service_points: list[RptServicePoint]
    def __init__(self) -> None:
        """Initialize RptSupportData."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.rpt_components: list[RptComponent] = []
        self.rpt_service_points: list[RptServicePoint] = []

    def serialize(self) -> ET.Element:
        """Serialize RptSupportData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptSupportData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize executions (list to container "EXECUTIONS")
        if self.executions:
            wrapper = ET.Element("EXECUTIONS")
            for item in self.executions:
                serialized = SerializationHelper.serialize_item(item, "RptExecutionContext")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_components (list to container "RPT-COMPONENTS")
        if self.rpt_components:
            wrapper = ET.Element("RPT-COMPONENTS")
            for item in self.rpt_components:
                serialized = SerializationHelper.serialize_item(item, "RptComponent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_service_points (list to container "RPT-SERVICE-POINTS")
        if self.rpt_service_points:
            wrapper = ET.Element("RPT-SERVICE-POINTS")
            for item in self.rpt_service_points:
                serialized = SerializationHelper.serialize_item(item, "RptServicePoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptSupportData":
        """Deserialize XML element to RptSupportData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptSupportData object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptSupportData, cls).deserialize(element)

        # Parse executions (list from container "EXECUTIONS")
        obj.executions = []
        container = SerializationHelper.find_child_element(element, "EXECUTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.executions.append(child_value)

        # Parse rpt_components (list from container "RPT-COMPONENTS")
        obj.rpt_components = []
        container = SerializationHelper.find_child_element(element, "RPT-COMPONENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_components.append(child_value)

        # Parse rpt_service_points (list from container "RPT-SERVICE-POINTS")
        obj.rpt_service_points = []
        container = SerializationHelper.find_child_element(element, "RPT-SERVICE-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_service_points.append(child_value)

        return obj



class RptSupportDataBuilder(BuilderBase):
    """Builder for RptSupportData with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: RptSupportData = RptSupportData()


    def with_executions(self, items: list[RptExecutionContext]) -> "RptSupportDataBuilder":
        """Set executions list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.executions = list(items) if items else []
        return self

    def with_rpt_components(self, items: list[RptComponent]) -> "RptSupportDataBuilder":
        """Set rpt_components list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_components = list(items) if items else []
        return self

    def with_rpt_service_points(self, items: list[RptServicePoint]) -> "RptSupportDataBuilder":
        """Set rpt_service_points list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points = list(items) if items else []
        return self


    def add_execution(self, item: RptExecutionContext) -> "RptSupportDataBuilder":
        """Add a single item to executions list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.executions.append(item)
        return self

    def clear_executions(self) -> "RptSupportDataBuilder":
        """Clear all items from executions list.

        Returns:
            self for method chaining
        """
        self._obj.executions = []
        return self

    def add_rpt_component(self, item: RptComponent) -> "RptSupportDataBuilder":
        """Add a single item to rpt_components list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_components.append(item)
        return self

    def clear_rpt_components(self) -> "RptSupportDataBuilder":
        """Clear all items from rpt_components list.

        Returns:
            self for method chaining
        """
        self._obj.rpt_components = []
        return self

    def add_rpt_service_point(self, item: RptServicePoint) -> "RptSupportDataBuilder":
        """Add a single item to rpt_service_points list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.rpt_service_points.append(item)
        return self

    def clear_rpt_service_points(self) -> "RptSupportDataBuilder":
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


    def build(self) -> RptSupportData:
        """Build and return the RptSupportData instance with validation."""
        self._validate_instance()
        pass
        return self._obj