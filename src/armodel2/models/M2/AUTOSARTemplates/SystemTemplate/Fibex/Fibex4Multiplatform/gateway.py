"""Gateway AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 837)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.frame_mapping import (
    FrameMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_pdu_mapping import (
    IPduMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.i_signal_mapping import (
    ISignalMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Gateway(FibexElement):
    """AUTOSAR Gateway."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "GATEWAY"


    ecu_ref: Optional[ARRef]
    frame_mapping_refs: list[ARRef]
    i_pdu_mapping_refs: list[ARRef]
    signal_mapping_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ECU-REF": lambda obj, elem: setattr(obj, "ecu_ref", ARRef.deserialize(elem)),
        "FRAME-MAPPINGS": lambda obj, elem: obj.frame_mapping_refs.append(ARRef.deserialize(elem)),
        "I-PDU-MAPPINGS": lambda obj, elem: obj.i_pdu_mapping_refs.append(ARRef.deserialize(elem)),
        "SIGNAL-MAPPINGS": lambda obj, elem: obj.signal_mapping_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize Gateway."""
        super().__init__()
        self.ecu_ref: Optional[ARRef] = None
        self.frame_mapping_refs: list[ARRef] = []
        self.i_pdu_mapping_refs: list[ARRef] = []
        self.signal_mapping_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize Gateway to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Gateway, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_ref
        if self.ecu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_ref, "EcuInstance")
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

        # Serialize frame_mapping_refs (list to container "FRAME-MAPPING-REFS")
        if self.frame_mapping_refs:
            wrapper = ET.Element("FRAME-MAPPING-REFS")
            for item in self.frame_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "FrameMapping")
                if serialized is not None:
                    child_elem = ET.Element("FRAME-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_pdu_mapping_refs (list to container "I-PDU-MAPPING-REFS")
        if self.i_pdu_mapping_refs:
            wrapper = ET.Element("I-PDU-MAPPING-REFS")
            for item in self.i_pdu_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "IPduMapping")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize signal_mapping_refs (list to container "SIGNAL-MAPPING-REFS")
        if self.signal_mapping_refs:
            wrapper = ET.Element("SIGNAL-MAPPING-REFS")
            for item in self.signal_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalMapping")
                if serialized is not None:
                    child_elem = ET.Element("SIGNAL-MAPPING-REF")
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
    def deserialize(cls, element: ET.Element) -> "Gateway":
        """Deserialize XML element to Gateway object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Gateway object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Gateway, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ECU-REF":
                setattr(obj, "ecu_ref", ARRef.deserialize(child))
            elif tag == "FRAME-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.frame_mapping_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "FrameMapping"))
            elif tag == "I-PDU-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.i_pdu_mapping_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "IPduMapping"))
            elif tag == "SIGNAL-MAPPINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.signal_mapping_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ISignalMapping"))

        return obj



class GatewayBuilder(FibexElementBuilder):
    """Builder for Gateway with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Gateway = Gateway()


    def with_ecu(self, value: Optional[EcuInstance]) -> "GatewayBuilder":
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

    def with_frame_mappings(self, items: list[FrameMapping]) -> "GatewayBuilder":
        """Set frame_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.frame_mappings = list(items) if items else []
        return self

    def with_i_pdu_mappings(self, items: list[IPduMapping]) -> "GatewayBuilder":
        """Set i_pdu_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_mappings = list(items) if items else []
        return self

    def with_signal_mappings(self, items: list[ISignalMapping]) -> "GatewayBuilder":
        """Set signal_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.signal_mappings = list(items) if items else []
        return self


    def add_frame_mapping(self, item: FrameMapping) -> "GatewayBuilder":
        """Add a single item to frame_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.frame_mappings.append(item)
        return self

    def clear_frame_mappings(self) -> "GatewayBuilder":
        """Clear all items from frame_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.frame_mappings = []
        return self

    def add_i_pdu_mapping(self, item: IPduMapping) -> "GatewayBuilder":
        """Add a single item to i_pdu_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_mappings.append(item)
        return self

    def clear_i_pdu_mappings(self) -> "GatewayBuilder":
        """Clear all items from i_pdu_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_mappings = []
        return self

    def add_signal_mapping(self, item: ISignalMapping) -> "GatewayBuilder":
        """Add a single item to signal_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.signal_mappings.append(item)
        return self

    def clear_signal_mappings(self) -> "GatewayBuilder":
        """Clear all items from signal_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.signal_mappings = []
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


    def build(self) -> Gateway:
        """Build and return the Gateway instance with validation."""
        self._validate_instance()
        pass
        return self._obj