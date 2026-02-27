"""FlexrayArTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 603)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import TpConnectionBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_node import (
    FlexrayArTpNode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayArTpConnection(TpConnection):
    """AUTOSAR FlexrayArTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connection_prio: Optional[Integer]
    direct_tp_sdu_ref: Optional[ARRef]
    multicast_ref: Optional[ARRef]
    reversed_tp_sdu_ref: Optional[ARRef]
    source_ref: Optional[ARRef]
    target_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FlexrayArTpConnection."""
        super().__init__()
        self.connection_prio: Optional[Integer] = None
        self.direct_tp_sdu_ref: Optional[ARRef] = None
        self.multicast_ref: Optional[ARRef] = None
        self.reversed_tp_sdu_ref: Optional[ARRef] = None
        self.source_ref: Optional[ARRef] = None
        self.target_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize FlexrayArTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayArTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection_prio
        if self.connection_prio is not None:
            serialized = SerializationHelper.serialize_item(self.connection_prio, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTION-PRIO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize direct_tp_sdu_ref
        if self.direct_tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.direct_tp_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast_ref
        if self.multicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.multicast_ref, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reversed_tp_sdu_ref
        if self.reversed_tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.reversed_tp_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVERSED-TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_ref
        if self.source_ref is not None:
            serialized = SerializationHelper.serialize_item(self.source_ref, "FlexrayArTpNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize target_refs (list to container "TARGET-REFS")
        if self.target_refs:
            wrapper = ET.Element("TARGET-REFS")
            for item in self.target_refs:
                serialized = SerializationHelper.serialize_item(item, "FlexrayArTpNode")
                if serialized is not None:
                    child_elem = ET.Element("TARGET-REF")
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
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpConnection":
        """Deserialize XML element to FlexrayArTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayArTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayArTpConnection, cls).deserialize(element)

        # Parse connection_prio
        child = SerializationHelper.find_child_element(element, "CONNECTION-PRIO")
        if child is not None:
            connection_prio_value = child.text
            obj.connection_prio = connection_prio_value

        # Parse direct_tp_sdu_ref
        child = SerializationHelper.find_child_element(element, "DIRECT-TP-SDU-REF")
        if child is not None:
            direct_tp_sdu_ref_value = ARRef.deserialize(child)
            obj.direct_tp_sdu_ref = direct_tp_sdu_ref_value

        # Parse multicast_ref
        child = SerializationHelper.find_child_element(element, "MULTICAST-REF")
        if child is not None:
            multicast_ref_value = ARRef.deserialize(child)
            obj.multicast_ref = multicast_ref_value

        # Parse reversed_tp_sdu_ref
        child = SerializationHelper.find_child_element(element, "REVERSED-TP-SDU-REF")
        if child is not None:
            reversed_tp_sdu_ref_value = ARRef.deserialize(child)
            obj.reversed_tp_sdu_ref = reversed_tp_sdu_ref_value

        # Parse source_ref
        child = SerializationHelper.find_child_element(element, "SOURCE-REF")
        if child is not None:
            source_ref_value = ARRef.deserialize(child)
            obj.source_ref = source_ref_value

        # Parse target_refs (list from container "TARGET-REFS")
        obj.target_refs = []
        container = SerializationHelper.find_child_element(element, "TARGET-REFS")
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
                    obj.target_refs.append(child_value)

        return obj



class FlexrayArTpConnectionBuilder(TpConnectionBuilder):
    """Builder for FlexrayArTpConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayArTpConnection = FlexrayArTpConnection()


    def with_connection_prio(self, value: Optional[Integer]) -> "FlexrayArTpConnectionBuilder":
        """Set connection_prio attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.connection_prio = value
        return self

    def with_direct_tp_sdu(self, value: Optional[IPdu]) -> "FlexrayArTpConnectionBuilder":
        """Set direct_tp_sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.direct_tp_sdu = value
        return self

    def with_multicast(self, value: Optional[TpAddress]) -> "FlexrayArTpConnectionBuilder":
        """Set multicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.multicast = value
        return self

    def with_reversed_tp_sdu(self, value: Optional[IPdu]) -> "FlexrayArTpConnectionBuilder":
        """Set reversed_tp_sdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.reversed_tp_sdu = value
        return self

    def with_source(self, value: Optional[FlexrayArTpNode]) -> "FlexrayArTpConnectionBuilder":
        """Set source attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source = value
        return self

    def with_targets(self, items: list[FlexrayArTpNode]) -> "FlexrayArTpConnectionBuilder":
        """Set targets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.targets = list(items) if items else []
        return self


    def add_target(self, item: FlexrayArTpNode) -> "FlexrayArTpConnectionBuilder":
        """Add a single item to targets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.targets.append(item)
        return self

    def clear_targets(self) -> "FlexrayArTpConnectionBuilder":
        """Clear all items from targets list.

        Returns:
            self for method chaining
        """
        self._obj.targets = []
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


    def build(self) -> FlexrayArTpConnection:
        """Build and return the FlexrayArTpConnection instance with validation."""
        self._validate_instance()
        pass
        return self._obj