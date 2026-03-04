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

    _XML_TAG = "FLEXRAY-AR-TP-CONNECTION"


    connection_prio: Optional[Integer]
    direct_tp_sdu_ref: Optional[ARRef]
    multicast_ref: Optional[ARRef]
    reversed_tp_sdu_ref: Optional[ARRef]
    source_ref: Optional[ARRef]
    target_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "CONNECTION-PRIO": lambda obj, elem: setattr(obj, "connection_prio", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "DIRECT-TP-SDU-REF": ("_POLYMORPHIC", "direct_tp_sdu_ref", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "SecuredIPdu", "UserDefinedIPdu"]),
        "MULTICAST-REF": lambda obj, elem: setattr(obj, "multicast_ref", ARRef.deserialize(elem)),
        "REVERSED-TP-SDU-REF": ("_POLYMORPHIC", "reversed_tp_sdu_ref", ["ContainerIPdu", "DcmIPdu", "GeneralPurposeIPdu", "ISignalIPdu", "J1939DcmIPdu", "MultiplexedIPdu", "NPdu", "SecuredIPdu", "UserDefinedIPdu"]),
        "SOURCE-REF": lambda obj, elem: setattr(obj, "source_ref", ARRef.deserialize(elem)),
        "TARGET-REFS": lambda obj, elem: [obj.target_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONNECTION-PRIO":
                setattr(obj, "connection_prio", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "DIRECT-TP-SDU-REF":
                setattr(obj, "direct_tp_sdu_ref", ARRef.deserialize(child))
            elif tag == "MULTICAST-REF":
                setattr(obj, "multicast_ref", ARRef.deserialize(child))
            elif tag == "REVERSED-TP-SDU-REF":
                setattr(obj, "reversed_tp_sdu_ref", ARRef.deserialize(child))
            elif tag == "SOURCE-REF":
                setattr(obj, "source_ref", ARRef.deserialize(child))
            elif tag == "TARGET-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.target_refs.append(ARRef.deserialize(item_elem))

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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "connectionPrio",
        "directTpSdu",
        "multicast",
        "reversedTpSdu",
        "source",
        "target",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FlexrayArTpConnection:
        """Build and return the FlexrayArTpConnection instance with validation."""
        self._validate_instance()
        return self._obj