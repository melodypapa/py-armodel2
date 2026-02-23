"""LinCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 98)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import CommunicationConnectorBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
    LinConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
    LinOrderedConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class LinCommunicationConnector(CommunicationConnector):
    """AUTOSAR LinCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    initial_nad: Optional[Integer]
    lin_configurable_frames: list[LinConfigurableFrame]
    lin_ordereds: list[LinOrderedConfigurableFrame]
    schedule: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize LinCommunicationConnector."""
        super().__init__()
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.schedule: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize LinCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize initial_nad
        if self.initial_nad is not None:
            serialized = SerializationHelper.serialize_item(self.initial_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_configurable_frames (list to container "LIN-CONFIGURABLE-FRAMES")
        if self.lin_configurable_frames:
            wrapper = ET.Element("LIN-CONFIGURABLE-FRAMES")
            for item in self.lin_configurable_frames:
                serialized = SerializationHelper.serialize_item(item, "LinConfigurableFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lin_ordereds (list to container "LIN-ORDEREDS")
        if self.lin_ordereds:
            wrapper = ET.Element("LIN-ORDEREDS")
            for item in self.lin_ordereds:
                serialized = SerializationHelper.serialize_item(item, "LinOrderedConfigurableFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize schedule
        if self.schedule is not None:
            serialized = SerializationHelper.serialize_item(self.schedule, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SCHEDULE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinCommunicationConnector":
        """Deserialize XML element to LinCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinCommunicationConnector, cls).deserialize(element)

        # Parse initial_nad
        child = SerializationHelper.find_child_element(element, "INITIAL-NAD")
        if child is not None:
            initial_nad_value = child.text
            obj.initial_nad = initial_nad_value

        # Parse lin_configurable_frames (list from container "LIN-CONFIGURABLE-FRAMES")
        obj.lin_configurable_frames = []
        container = SerializationHelper.find_child_element(element, "LIN-CONFIGURABLE-FRAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_configurable_frames.append(child_value)

        # Parse lin_ordereds (list from container "LIN-ORDEREDS")
        obj.lin_ordereds = []
        container = SerializationHelper.find_child_element(element, "LIN-ORDEREDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_ordereds.append(child_value)

        # Parse schedule
        child = SerializationHelper.find_child_element(element, "SCHEDULE")
        if child is not None:
            schedule_value = child.text
            obj.schedule = schedule_value

        return obj



class LinCommunicationConnectorBuilder(CommunicationConnectorBuilder):
    """Builder for LinCommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinCommunicationConnector = LinCommunicationConnector()


    def with_initial_nad(self, value: Optional[Integer]) -> "LinCommunicationConnectorBuilder":
        """Set initial_nad attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_nad = value
        return self

    def with_lin_configurable_frames(self, items: list[LinConfigurableFrame]) -> "LinCommunicationConnectorBuilder":
        """Set lin_configurable_frames list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_configurable_frames = list(items) if items else []
        return self

    def with_lin_ordereds(self, items: list[LinOrderedConfigurableFrame]) -> "LinCommunicationConnectorBuilder":
        """Set lin_ordereds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.lin_ordereds = list(items) if items else []
        return self

    def with_schedule(self, value: Optional[Boolean]) -> "LinCommunicationConnectorBuilder":
        """Set schedule attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.schedule = value
        return self


    def add_lin_configurable_frame(self, item: LinConfigurableFrame) -> "LinCommunicationConnectorBuilder":
        """Add a single item to lin_configurable_frames list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_configurable_frames.append(item)
        return self

    def clear_lin_configurable_frames(self) -> "LinCommunicationConnectorBuilder":
        """Clear all items from lin_configurable_frames list.

        Returns:
            self for method chaining
        """
        self._obj.lin_configurable_frames = []
        return self

    def add_lin_ordered(self, item: LinOrderedConfigurableFrame) -> "LinCommunicationConnectorBuilder":
        """Add a single item to lin_ordereds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.lin_ordereds.append(item)
        return self

    def clear_lin_ordereds(self) -> "LinCommunicationConnectorBuilder":
        """Clear all items from lin_ordereds list.

        Returns:
            self for method chaining
        """
        self._obj.lin_ordereds = []
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


    def build(self) -> LinCommunicationConnector:
        """Build and return the LinCommunicationConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj