"""FlexrayArTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 603)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_node import (
    FlexrayArTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


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
    direct_tp_sdu: Optional[IPdu]
    multicast: Optional[TpAddress]
    reversed_tp_sdu: Optional[IPdu]
    source: Optional[FlexrayArTpNode]
    targets: list[FlexrayArTpNode]
    def __init__(self) -> None:
        """Initialize FlexrayArTpConnection."""
        super().__init__()
        self.connection_prio: Optional[Integer] = None
        self.direct_tp_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.reversed_tp_sdu: Optional[IPdu] = None
        self.source: Optional[FlexrayArTpNode] = None
        self.targets: list[FlexrayArTpNode] = []

    def serialize(self) -> ET.Element:
        """Serialize FlexrayArTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayArTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connection_prio
        if self.connection_prio is not None:
            serialized = ARObject._serialize_item(self.connection_prio, "Integer")
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

        # Serialize direct_tp_sdu
        if self.direct_tp_sdu is not None:
            serialized = ARObject._serialize_item(self.direct_tp_sdu, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-TP-SDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast
        if self.multicast is not None:
            serialized = ARObject._serialize_item(self.multicast, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reversed_tp_sdu
        if self.reversed_tp_sdu is not None:
            serialized = ARObject._serialize_item(self.reversed_tp_sdu, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVERSED-TP-SDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source
        if self.source is not None:
            serialized = ARObject._serialize_item(self.source, "FlexrayArTpNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize targets (list to container "TARGETS")
        if self.targets:
            wrapper = ET.Element("TARGETS")
            for item in self.targets:
                serialized = ARObject._serialize_item(item, "FlexrayArTpNode")
                if serialized is not None:
                    wrapper.append(serialized)
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
        child = ARObject._find_child_element(element, "CONNECTION-PRIO")
        if child is not None:
            connection_prio_value = child.text
            obj.connection_prio = connection_prio_value

        # Parse direct_tp_sdu
        child = ARObject._find_child_element(element, "DIRECT-TP-SDU")
        if child is not None:
            direct_tp_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.direct_tp_sdu = direct_tp_sdu_value

        # Parse multicast
        child = ARObject._find_child_element(element, "MULTICAST")
        if child is not None:
            multicast_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.multicast = multicast_value

        # Parse reversed_tp_sdu
        child = ARObject._find_child_element(element, "REVERSED-TP-SDU")
        if child is not None:
            reversed_tp_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.reversed_tp_sdu = reversed_tp_sdu_value

        # Parse source
        child = ARObject._find_child_element(element, "SOURCE")
        if child is not None:
            source_value = ARObject._deserialize_by_tag(child, "FlexrayArTpNode")
            obj.source = source_value

        # Parse targets (list from container "TARGETS")
        obj.targets = []
        container = ARObject._find_child_element(element, "TARGETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.targets.append(child_value)

        return obj



class FlexrayArTpConnectionBuilder:
    """Builder for FlexrayArTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpConnection = FlexrayArTpConnection()

    def build(self) -> FlexrayArTpConnection:
        """Build and return FlexrayArTpConnection object.

        Returns:
            FlexrayArTpConnection instance
        """
        # TODO: Add validation
        return self._obj
