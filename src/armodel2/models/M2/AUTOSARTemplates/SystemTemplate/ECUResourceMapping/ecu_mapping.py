"""ECUMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 182)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_ECUResourceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.ECUResourceMapping.hw_port_mapping import (
    HwPortMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ECUMapping(Identifiable):
    """AUTOSAR ECUMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "E-C-U-MAPPING"


    comm_controllers: list[Any]
    ecu_ref: Optional[ARRef]
    ecu_instance_ref: Optional[ARRef]
    hw_port_mapping_ref: ARRef
    _DESERIALIZE_DISPATCH = {
        "COMM-CONTROLLERS": lambda obj, elem: obj.comm_controllers.append(SerializationHelper.deserialize_by_tag(elem, "any (Communication)")),
        "ECU-REF": lambda obj, elem: setattr(obj, "ecu_ref", ARRef.deserialize(elem)),
        "ECU-INSTANCE-REF": lambda obj, elem: setattr(obj, "ecu_instance_ref", ARRef.deserialize(elem)),
        "HW-PORT-MAPPING-REF": lambda obj, elem: setattr(obj, "hw_port_mapping_ref", ARRef.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "COMM-CONTROLLERS":
                obj.comm_controllers.append(SerializationHelper.deserialize_by_tag(child, "any (Communication)"))
            elif tag == "ECU-REF":
                setattr(obj, "ecu_ref", ARRef.deserialize(child))
            elif tag == "ECU-INSTANCE-REF":
                setattr(obj, "ecu_instance_ref", ARRef.deserialize(child))
            elif tag == "HW-PORT-MAPPING-REF":
                setattr(obj, "hw_port_mapping_ref", ARRef.deserialize(child))

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


    def build(self) -> ECUMapping:
        """Build and return the ECUMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj