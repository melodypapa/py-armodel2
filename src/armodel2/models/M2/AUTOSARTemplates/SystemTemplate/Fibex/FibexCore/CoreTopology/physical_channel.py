"""PhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 58)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame_triggering import (
    FrameTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_triggering import (
    ISignalTriggering,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PhysicalChannel(Identifiable, ABC):
    """AUTOSAR PhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    _comm_connector_refs: list[ARRef]
    frame_triggerings: list[FrameTriggering]
    i_signal_triggerings: list[ISignalTriggering]
    managed_physical_channel_refs: list[ARRef]
    pdu_triggerings: list[PduTriggering]
    _DESERIALIZE_DISPATCH = {
        "COMM-CONNECTORS": ("_POLYMORPHIC_LIST", "_comm_connector_refs", ["AbstractCanCommunicationConnector", "EthernetCommunicationConnector", "FlexrayCommunicationConnector", "LinCommunicationConnector", "UserDefinedCommunicationConnector"]),
        "FRAME-TRIGGERINGS": ("_POLYMORPHIC_LIST", "frame_triggerings", ["CanFrameTriggering", "EthernetFrameTriggering", "FlexrayFrameTriggering", "LinFrameTriggering"]),
        "I-SIGNAL-TRIGGERINGS": lambda obj, elem: obj.i_signal_triggerings.append(SerializationHelper.deserialize_by_tag(elem, "ISignalTriggering")),
        "MANAGED-PHYSICAL-CHANNELS": ("_POLYMORPHIC_LIST", "managed_physical_channel_refs", ["AbstractCanPhysicalChannel", "EthernetPhysicalChannel", "FlexrayPhysicalChannel", "LinPhysicalChannel"]),
        "PDU-TRIGGERINGS": lambda obj, elem: obj.pdu_triggerings.append(SerializationHelper.deserialize_by_tag(elem, "PduTriggering")),
    }


    def __init__(self) -> None:
        """Initialize PhysicalChannel."""
        super().__init__()
        self._comm_connector_refs: list[ARRef] = []
        self.frame_triggerings: list[FrameTriggering] = []
        self.i_signal_triggerings: list[ISignalTriggering] = []
        self.managed_physical_channel_refs: list[ARRef] = []
        self.pdu_triggerings: list[PduTriggering] = []
    @property
    @ref_conditional("COMM-CONNECTORS")
    def comm_connector_refs(self) -> list[ARRef]:
        """Get comm_connector_refs with ref_conditional wrapper."""
        return self._comm_connector_refs

    @comm_connector_refs.setter
    def comm_connector_refs(self, value: list[ARRef]) -> None:
        """Set comm_connector_refs with ref_conditional wrapper."""
        self._comm_connector_refs = value


    def serialize(self) -> ET.Element:
        """Serialize PhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_connector_refs (list to container "COMM-CONNECTORS")
        if self.comm_connector_refs:
            wrapper = ET.Element("COMM-CONNECTORS")
            for item in self.comm_connector_refs:
                serialized = SerializationHelper.serialize_item(item, "CommunicationConnector")
                if serialized is not None:
                    # Wrap in COMMUNICATION-CONNECTOR-REF-CONDITIONAL
                    conditional = ET.Element("COMMUNICATION-CONNECTOR-REF-CONDITIONAL")
                    ref_elem = ET.Element("COMMUNICATION-CONNECTOR-REF")
                    if hasattr(serialized, 'attrib'):
                        ref_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        ref_elem.text = serialized.text
                    for child in serialized:
                        ref_elem.append(child)
                    conditional.append(ref_elem)
                    wrapper.append(conditional)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize frame_triggerings (list to container "FRAME-TRIGGERINGS")
        if self.frame_triggerings:
            wrapper = ET.Element("FRAME-TRIGGERINGS")
            for item in self.frame_triggerings:
                serialized = SerializationHelper.serialize_item(item, "FrameTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_signal_triggerings (list to container "I-SIGNAL-TRIGGERINGS")
        if self.i_signal_triggerings:
            wrapper = ET.Element("I-SIGNAL-TRIGGERINGS")
            for item in self.i_signal_triggerings:
                serialized = SerializationHelper.serialize_item(item, "ISignalTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize managed_physical_channel_refs (list to container "MANAGED-PHYSICAL-CHANNEL-REFS")
        if self.managed_physical_channel_refs:
            wrapper = ET.Element("MANAGED-PHYSICAL-CHANNEL-REFS")
            for item in self.managed_physical_channel_refs:
                serialized = SerializationHelper.serialize_item(item, "PhysicalChannel")
                if serialized is not None:
                    child_elem = ET.Element("MANAGED-PHYSICAL-CHANNEL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_triggerings (list to container "PDU-TRIGGERINGS")
        if self.pdu_triggerings:
            wrapper = ET.Element("PDU-TRIGGERINGS")
            for item in self.pdu_triggerings:
                serialized = SerializationHelper.serialize_item(item, "PduTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PhysicalChannel":
        """Deserialize XML element to PhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PhysicalChannel, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "COMM-CONNECTORS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-CAN-COMMUNICATION-CONNECTOR":
                        obj._comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractCanCommunicationConnector"))
                    elif concrete_tag == "ETHERNET-COMMUNICATION-CONNECTOR":
                        obj._comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetCommunicationConnector"))
                    elif concrete_tag == "FLEXRAY-COMMUNICATION-CONNECTOR":
                        obj._comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayCommunicationConnector"))
                    elif concrete_tag == "LIN-COMMUNICATION-CONNECTOR":
                        obj._comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinCommunicationConnector"))
                    elif concrete_tag == "USER-DEFINED-COMMUNICATION-CONNECTOR":
                        obj._comm_connector_refs.append(SerializationHelper.deserialize_by_tag(child[0], "UserDefinedCommunicationConnector"))
            elif tag == "FRAME-TRIGGERINGS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CAN-FRAME-TRIGGERING":
                        obj.frame_triggerings.append(SerializationHelper.deserialize_by_tag(child[0], "CanFrameTriggering"))
                    elif concrete_tag == "ETHERNET-FRAME-TRIGGERING":
                        obj.frame_triggerings.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetFrameTriggering"))
                    elif concrete_tag == "FLEXRAY-FRAME-TRIGGERING":
                        obj.frame_triggerings.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayFrameTriggering"))
                    elif concrete_tag == "LIN-FRAME-TRIGGERING":
                        obj.frame_triggerings.append(SerializationHelper.deserialize_by_tag(child[0], "LinFrameTriggering"))
            elif tag == "I-SIGNAL-TRIGGERINGS":
                obj.i_signal_triggerings.append(SerializationHelper.deserialize_by_tag(child, "ISignalTriggering"))
            elif tag == "MANAGED-PHYSICAL-CHANNELS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ABSTRACT-CAN-PHYSICAL-CHANNEL":
                        obj.managed_physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "AbstractCanPhysicalChannel"))
                    elif concrete_tag == "ETHERNET-PHYSICAL-CHANNEL":
                        obj.managed_physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "EthernetPhysicalChannel"))
                    elif concrete_tag == "FLEXRAY-PHYSICAL-CHANNEL":
                        obj.managed_physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayPhysicalChannel"))
                    elif concrete_tag == "LIN-PHYSICAL-CHANNEL":
                        obj.managed_physical_channel_refs.append(SerializationHelper.deserialize_by_tag(child[0], "LinPhysicalChannel"))
            elif tag == "PDU-TRIGGERINGS":
                obj.pdu_triggerings.append(SerializationHelper.deserialize_by_tag(child, "PduTriggering"))

        return obj



class PhysicalChannelBuilder(IdentifiableBuilder):
    """Builder for PhysicalChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PhysicalChannel = PhysicalChannel()


    def with_comm_connectors(self, items: list[CommunicationConnector]) -> "PhysicalChannelBuilder":
        """Set comm_connectors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors = list(items) if items else []
        return self

    def with_frame_triggerings(self, items: list[FrameTriggering]) -> "PhysicalChannelBuilder":
        """Set frame_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.frame_triggerings = list(items) if items else []
        return self

    def with_i_signal_triggerings(self, items: list[ISignalTriggering]) -> "PhysicalChannelBuilder":
        """Set i_signal_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signal_triggerings = list(items) if items else []
        return self

    def with_managed_physical_channels(self, items: list[PhysicalChannel]) -> "PhysicalChannelBuilder":
        """Set managed_physical_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.managed_physical_channels = list(items) if items else []
        return self

    def with_pdu_triggerings(self, items: list[PduTriggering]) -> "PhysicalChannelBuilder":
        """Set pdu_triggerings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = list(items) if items else []
        return self


    def add_comm_connector(self, item: CommunicationConnector) -> "PhysicalChannelBuilder":
        """Add a single item to comm_connectors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors.append(item)
        return self

    def clear_comm_connectors(self) -> "PhysicalChannelBuilder":
        """Clear all items from comm_connectors list.

        Returns:
            self for method chaining
        """
        self._obj.comm_connectors = []
        return self

    def add_frame_triggering(self, item: FrameTriggering) -> "PhysicalChannelBuilder":
        """Add a single item to frame_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.frame_triggerings.append(item)
        return self

    def clear_frame_triggerings(self) -> "PhysicalChannelBuilder":
        """Clear all items from frame_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.frame_triggerings = []
        return self

    def add_i_signal_triggering(self, item: ISignalTriggering) -> "PhysicalChannelBuilder":
        """Add a single item to i_signal_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signal_triggerings.append(item)
        return self

    def clear_i_signal_triggerings(self) -> "PhysicalChannelBuilder":
        """Clear all items from i_signal_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.i_signal_triggerings = []
        return self

    def add_managed_physical_channel(self, item: PhysicalChannel) -> "PhysicalChannelBuilder":
        """Add a single item to managed_physical_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.managed_physical_channels.append(item)
        return self

    def clear_managed_physical_channels(self) -> "PhysicalChannelBuilder":
        """Clear all items from managed_physical_channels list.

        Returns:
            self for method chaining
        """
        self._obj.managed_physical_channels = []
        return self

    def add_pdu_triggering(self, item: PduTriggering) -> "PhysicalChannelBuilder":
        """Add a single item to pdu_triggerings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings.append(item)
        return self

    def clear_pdu_triggerings(self) -> "PhysicalChannelBuilder":
        """Clear all items from pdu_triggerings list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_triggerings = []
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


    @abstractmethod
    def build(self) -> PhysicalChannel:
        """Build and return the PhysicalChannel instance (abstract)."""
        raise NotImplementedError