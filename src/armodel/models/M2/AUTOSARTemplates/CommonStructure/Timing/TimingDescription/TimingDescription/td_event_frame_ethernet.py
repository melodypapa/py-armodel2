"""TDEventFrameEthernet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 69)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import (
    TDEventCom,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_com import TDEventComBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
    StaticSocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_header_id_range import (
    TDHeaderIdRange,
)


class TDEventFrameEthernet(TDEventCom):
    """AUTOSAR TDEventFrameEthernet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    static_socket_ref: Optional[ARRef]
    td_event_type: Optional[TDEventFrameEthernet]
    td_header_id_filters: list[TDHeaderIdRange]
    td_pdu_triggering_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize TDEventFrameEthernet."""
        super().__init__()
        self.static_socket_ref: Optional[ARRef] = None
        self.td_event_type: Optional[TDEventFrameEthernet] = None
        self.td_header_id_filters: list[TDHeaderIdRange] = []
        self.td_pdu_triggering_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize TDEventFrameEthernet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventFrameEthernet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize static_socket_ref
        if self.static_socket_ref is not None:
            serialized = SerializationHelper.serialize_item(self.static_socket_ref, "StaticSocketConnection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("STATIC-SOCKET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_type
        if self.td_event_type is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_type, "TDEventFrameEthernet")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_header_id_filters (list to container "TD-HEADER-ID-FILTERS")
        if self.td_header_id_filters:
            wrapper = ET.Element("TD-HEADER-ID-FILTERS")
            for item in self.td_header_id_filters:
                serialized = SerializationHelper.serialize_item(item, "TDHeaderIdRange")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize td_pdu_triggering_refs (list to container "TD-PDU-TRIGGERING-REFS")
        if self.td_pdu_triggering_refs:
            wrapper = ET.Element("TD-PDU-TRIGGERING-REFS")
            for item in self.td_pdu_triggering_refs:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("TD-PDU-TRIGGERING-REF")
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
    def deserialize(cls, element: ET.Element) -> "TDEventFrameEthernet":
        """Deserialize XML element to TDEventFrameEthernet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventFrameEthernet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventFrameEthernet, cls).deserialize(element)

        # Parse static_socket_ref
        child = SerializationHelper.find_child_element(element, "STATIC-SOCKET-REF")
        if child is not None:
            static_socket_ref_value = ARRef.deserialize(child)
            obj.static_socket_ref = static_socket_ref_value

        # Parse td_event_type
        child = SerializationHelper.find_child_element(element, "TD-EVENT-TYPE")
        if child is not None:
            td_event_type_value = SerializationHelper.deserialize_by_tag(child, "TDEventFrameEthernet")
            obj.td_event_type = td_event_type_value

        # Parse td_header_id_filters (list from container "TD-HEADER-ID-FILTERS")
        obj.td_header_id_filters = []
        container = SerializationHelper.find_child_element(element, "TD-HEADER-ID-FILTERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.td_header_id_filters.append(child_value)

        # Parse td_pdu_triggering_refs (list from container "TD-PDU-TRIGGERING-REFS")
        obj.td_pdu_triggering_refs = []
        container = SerializationHelper.find_child_element(element, "TD-PDU-TRIGGERING-REFS")
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
                    obj.td_pdu_triggering_refs.append(child_value)

        return obj



class TDEventFrameEthernetBuilder(TDEventComBuilder):
    """Builder for TDEventFrameEthernet with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TDEventFrameEthernet = TDEventFrameEthernet()


    def with_static_socket(self, value: Optional[StaticSocketConnection]) -> "TDEventFrameEthernetBuilder":
        """Set static_socket attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.static_socket = value
        return self

    def with_td_event_type(self, value: Optional[TDEventFrameEthernet]) -> "TDEventFrameEthernetBuilder":
        """Set td_event_type attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.td_event_type = value
        return self

    def with_td_header_id_filters(self, items: list[TDHeaderIdRange]) -> "TDEventFrameEthernetBuilder":
        """Set td_header_id_filters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.td_header_id_filters = list(items) if items else []
        return self

    def with_td_pdu_triggerings(self, items: list[PduTriggering]) -> "TDEventFrameEthernetBuilder":
        """Set td_pdu_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.td_pdu_triggerings = list(items) if items else []
        return self


    def add_td_header_id_filter(self, item: TDHeaderIdRange) -> "TDEventFrameEthernetBuilder":
        """Add a single item to td_header_id_filters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.td_header_id_filters.append(item)
        return self

    def clear_td_header_id_filters(self) -> "TDEventFrameEthernetBuilder":
        """Clear all items from td_header_id_filters list.

        Returns:
            self for method chaining
        """
        self._obj.td_header_id_filters = []
        return self

    def add_td_pdu_triggering(self, item: PduTriggering) -> "TDEventFrameEthernetBuilder":
        """Add a single item to td_pdu_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.td_pdu_triggerings.append(item)
        return self

    def clear_td_pdu_triggerings(self) -> "TDEventFrameEthernetBuilder":
        """Clear all items from td_pdu_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.td_pdu_triggerings = []
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


    def build(self) -> TDEventFrameEthernet:
        """Build and return the TDEventFrameEthernet instance with validation."""
        self._validate_instance()
        pass
        return self._obj