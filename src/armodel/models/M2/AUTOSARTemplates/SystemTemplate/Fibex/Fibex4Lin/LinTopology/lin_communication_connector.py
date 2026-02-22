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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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



class LinCommunicationConnectorBuilder:
    """Builder for LinCommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: LinCommunicationConnector = LinCommunicationConnector()


    def with_short_name(self, value: Identifier) -> "LinCommunicationConnectorBuilder":
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

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "LinCommunicationConnectorBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "LinCommunicationConnectorBuilder":
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

    def with_admin_data(self, value: Optional[AdminData]) -> "LinCommunicationConnectorBuilder":
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

    def with_annotations(self, items: list[Annotation]) -> "LinCommunicationConnectorBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "LinCommunicationConnectorBuilder":
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

    def with_category(self, value: Optional[CategoryString]) -> "LinCommunicationConnectorBuilder":
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

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "LinCommunicationConnectorBuilder":
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

    def with_uuid(self, value: Optional[String]) -> "LinCommunicationConnectorBuilder":
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

    def with_comm_controller(self, value: Optional[any (Communication)]) -> "LinCommunicationConnectorBuilder":
        """Set comm_controller attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.comm_controller = value
        return self

    def with_create_ecu(self, value: Optional[Boolean]) -> "LinCommunicationConnectorBuilder":
        """Set create_ecu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.create_ecu = value
        return self

    def with_dynamic_pnc_to(self, value: Optional[Boolean]) -> "LinCommunicationConnectorBuilder":
        """Set dynamic_pnc_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_pnc_to = value
        return self

    def with_ecu_comm_ports(self, items: list[CommConnectorPort]) -> "LinCommunicationConnectorBuilder":
        """Set ecu_comm_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_ports = list(items) if items else []
        return self

    def with_pnc_filter_arrays(self, items: list[PositiveInteger]) -> "LinCommunicationConnectorBuilder":
        """Set pnc_filter_arrays list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_arrays = list(items) if items else []
        return self

    def with_pnc_gateway_type_enum(self, value: Optional[PncGatewayTypeEnum]) -> "LinCommunicationConnectorBuilder":
        """Set pnc_gateway_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_gateway_type_enum = value
        return self

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


    def add_short_name_fragment(self, item: ShortNameFragment) -> "LinCommunicationConnectorBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "LinCommunicationConnectorBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "LinCommunicationConnectorBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "LinCommunicationConnectorBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_ecu_comm_port(self, item: CommConnectorPort) -> "LinCommunicationConnectorBuilder":
        """Add a single item to ecu_comm_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_ports.append(item)
        return self

    def clear_ecu_comm_ports(self) -> "LinCommunicationConnectorBuilder":
        """Clear all items from ecu_comm_ports list.

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_ports = []
        return self

    def add_pnc_filter_array(self, item: PositiveInteger) -> "LinCommunicationConnectorBuilder":
        """Add a single item to pnc_filter_arrays list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_arrays.append(item)
        return self

    def clear_pnc_filter_arrays(self) -> "LinCommunicationConnectorBuilder":
        """Clear all items from pnc_filter_arrays list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_arrays = []
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


    def build(self) -> LinCommunicationConnector:
        """Build and return the LinCommunicationConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj