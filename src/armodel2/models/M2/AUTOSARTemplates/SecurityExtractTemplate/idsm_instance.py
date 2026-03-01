"""IdsmInstance AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import (
    IdsCommonElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.ids_common_element import IdsCommonElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.block_state import (
    BlockState,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem.idsm_module_instantiation import (
    IdsmModuleInstantiation,
)
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_rate_limitation import (
    IdsmRateLimitation,
)
from armodel2.models.M2.AUTOSARTemplates.SecurityExtractTemplate.idsm_traffic_limitation import (
    IdsmTrafficLimitation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class IdsmInstance(IdsCommonElement):
    """AUTOSAR IdsmInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IDSM-INSTANCE"


    block_states: list[BlockState]
    ecu_instance_ref: Optional[ARRef]
    idsm_instance_id: Optional[PositiveInteger]
    idsm_module_ref: Optional[ARRef]
    rate_limitation_ref: Optional[ARRef]
    signature: Optional[Any]
    timestamp: Optional[String]
    traffic_limitation_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "BLOCK-STATES": lambda obj, elem: obj.block_states.append(SerializationHelper.deserialize_by_tag(elem, "BlockState")),
        "ECU-INSTANCE-REF": lambda obj, elem: setattr(obj, "ecu_instance_ref", ARRef.deserialize(elem)),
        "IDSM-INSTANCE-ID": lambda obj, elem: setattr(obj, "idsm_instance_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "IDSM-MODULE-REF": lambda obj, elem: setattr(obj, "idsm_module_ref", ARRef.deserialize(elem)),
        "RATE-LIMITATION-REF": lambda obj, elem: setattr(obj, "rate_limitation_ref", ARRef.deserialize(elem)),
        "SIGNATURE": lambda obj, elem: setattr(obj, "signature", SerializationHelper.deserialize_by_tag(elem, "any (IdsmSignatureSupport)")),
        "TIMESTAMP": lambda obj, elem: setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(elem, "String")),
        "TRAFFIC-LIMITATION-REF": lambda obj, elem: setattr(obj, "traffic_limitation_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize IdsmInstance."""
        super().__init__()
        self.block_states: list[BlockState] = []
        self.ecu_instance_ref: Optional[ARRef] = None
        self.idsm_instance_id: Optional[PositiveInteger] = None
        self.idsm_module_ref: Optional[ARRef] = None
        self.rate_limitation_ref: Optional[ARRef] = None
        self.signature: Optional[Any] = None
        self.timestamp: Optional[String] = None
        self.traffic_limitation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IdsmInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(IdsmInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize block_states (list to container "BLOCK-STATES")
        if self.block_states:
            wrapper = ET.Element("BLOCK-STATES")
            for item in self.block_states:
                serialized = SerializationHelper.serialize_item(item, "BlockState")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        # Serialize idsm_instance_id
        if self.idsm_instance_id is not None:
            serialized = SerializationHelper.serialize_item(self.idsm_instance_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDSM-INSTANCE-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize idsm_module_ref
        if self.idsm_module_ref is not None:
            serialized = SerializationHelper.serialize_item(self.idsm_module_ref, "IdsmModuleInstantiation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDSM-MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rate_limitation_ref
        if self.rate_limitation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rate_limitation_ref, "IdsmRateLimitation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RATE-LIMITATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signature
        if self.signature is not None:
            serialized = SerializationHelper.serialize_item(self.signature, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SIGNATURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timestamp
        if self.timestamp is not None:
            serialized = SerializationHelper.serialize_item(self.timestamp, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMESTAMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize traffic_limitation_ref
        if self.traffic_limitation_ref is not None:
            serialized = SerializationHelper.serialize_item(self.traffic_limitation_ref, "IdsmTrafficLimitation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRAFFIC-LIMITATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmInstance":
        """Deserialize XML element to IdsmInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(IdsmInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BLOCK-STATES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.block_states.append(SerializationHelper.deserialize_by_tag(item_elem, "BlockState"))
            elif tag == "ECU-INSTANCE-REF":
                setattr(obj, "ecu_instance_ref", ARRef.deserialize(child))
            elif tag == "IDSM-INSTANCE-ID":
                setattr(obj, "idsm_instance_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "IDSM-MODULE-REF":
                setattr(obj, "idsm_module_ref", ARRef.deserialize(child))
            elif tag == "RATE-LIMITATION-REF":
                setattr(obj, "rate_limitation_ref", ARRef.deserialize(child))
            elif tag == "SIGNATURE":
                setattr(obj, "signature", SerializationHelper.deserialize_by_tag(child, "any (IdsmSignatureSupport)"))
            elif tag == "TIMESTAMP":
                setattr(obj, "timestamp", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "TRAFFIC-LIMITATION-REF":
                setattr(obj, "traffic_limitation_ref", ARRef.deserialize(child))

        return obj



class IdsmInstanceBuilder(IdsCommonElementBuilder):
    """Builder for IdsmInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: IdsmInstance = IdsmInstance()


    def with_block_states(self, items: list[BlockState]) -> "IdsmInstanceBuilder":
        """Set block_states list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.block_states = list(items) if items else []
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "IdsmInstanceBuilder":
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

    def with_idsm_instance_id(self, value: Optional[PositiveInteger]) -> "IdsmInstanceBuilder":
        """Set idsm_instance_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.idsm_instance_id = value
        return self

    def with_idsm_module(self, value: Optional[IdsmModuleInstantiation]) -> "IdsmInstanceBuilder":
        """Set idsm_module attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.idsm_module = value
        return self

    def with_rate_limitation(self, value: Optional[IdsmRateLimitation]) -> "IdsmInstanceBuilder":
        """Set rate_limitation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rate_limitation = value
        return self

    def with_signature(self, value: Optional[any (IdsmSignatureSupport)]) -> "IdsmInstanceBuilder":
        """Set signature attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.signature = value
        return self

    def with_timestamp(self, value: Optional[String]) -> "IdsmInstanceBuilder":
        """Set timestamp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timestamp = value
        return self

    def with_traffic_limitation(self, value: Optional[IdsmTrafficLimitation]) -> "IdsmInstanceBuilder":
        """Set traffic_limitation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.traffic_limitation = value
        return self


    def add_block_state(self, item: BlockState) -> "IdsmInstanceBuilder":
        """Add a single item to block_states list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.block_states.append(item)
        return self

    def clear_block_states(self) -> "IdsmInstanceBuilder":
        """Clear all items from block_states list.

        Returns:
            self for method chaining
        """
        self._obj.block_states = []
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


    def build(self) -> IdsmInstance:
        """Build and return the IdsmInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj