"""ECUMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)


class ECUMapping(Identifiable):
    """AUTOSAR ECUMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    comm_controllers: list[Any]
    ecu_ref: Optional[ARRef]
    ecu_instance_ref: Optional[ARRef]
    hw_port_mapping_ref: ARRef
    def __init__(self) -> None:
        """Initialize ECUMapping."""
        super().__init__()
        self.comm_controllers: list[Any] = []
        self.ecu_ref: Optional[ARRef] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.hw_port_mapping_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize ECUMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ECUMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_controllers (list to container "COMM-CONTROLLERS")
        if self.comm_controllers:
            wrapper = ET.Element("COMM-CONTROLLERS")
            for item in self.comm_controllers:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_ref
        if self.ecu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-REF")
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

        # Serialize hw_port_mapping_ref
        if self.hw_port_mapping_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_port_mapping_ref, "HwPortMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-PORT-MAPPING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ECUMapping":
        """Deserialize XML element to ECUMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ECUMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ECUMapping, cls).deserialize(element)

        # Parse comm_controllers (list from container "COMM-CONTROLLERS")
        obj.comm_controllers = []
        container = SerializationHelper.find_child_element(element, "COMM-CONTROLLERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.comm_controllers.append(child_value)

        # Parse ecu_ref
        child = SerializationHelper.find_child_element(element, "ECU-REF")
        if child is not None:
            ecu_ref_value = ARRef.deserialize(child)
            obj.ecu_ref = ecu_ref_value

        # Parse ecu_instance_ref
        child = SerializationHelper.find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse hw_port_mapping_ref
        child = SerializationHelper.find_child_element(element, "HW-PORT-MAPPING-REF")
        if child is not None:
            hw_port_mapping_ref_value = ARRef.deserialize(child)
            obj.hw_port_mapping_ref = hw_port_mapping_ref_value

        return obj



class ECUMappingBuilder(IdentifiableBuilder):
    """Builder for ECUMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ECUMapping = ECUMapping()


    def with_comm_controllers(self, items: list[any (Communication)]) -> "ECUMappingBuilder":
        """Set comm_controllers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.comm_controllers = list(items) if items else []
        return self

    def with_ecu(self, value: Optional[HwElement]) -> "ECUMappingBuilder":
        """Set ecu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu = value
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "ECUMappingBuilder":
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

    def with_hw_port_mapping(self, value: HwPortMapping) -> "ECUMappingBuilder":
        """Set hw_port_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hw_port_mapping = value
        return self


    def add_comm_controller(self, item: any (Communication)) -> "ECUMappingBuilder":
        """Add a single item to comm_controllers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.comm_controllers.append(item)
        return self

    def clear_comm_controllers(self) -> "ECUMappingBuilder":
        """Clear all items from comm_controllers list.

        Returns:
            self for method chaining
        """
        self._obj.comm_controllers = []
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


    def build(self) -> ECUMapping:
        """Build and return the ECUMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj