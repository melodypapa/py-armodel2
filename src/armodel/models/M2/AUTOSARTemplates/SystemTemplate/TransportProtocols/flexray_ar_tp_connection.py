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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

        # Serialize direct_tp_sdu_ref
        if self.direct_tp_sdu_ref is not None:
            serialized = ARObject._serialize_item(self.direct_tp_sdu_ref, "IPdu")
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
            serialized = ARObject._serialize_item(self.multicast_ref, "TpAddress")
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
            serialized = ARObject._serialize_item(self.reversed_tp_sdu_ref, "IPdu")
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
            serialized = ARObject._serialize_item(self.source_ref, "FlexrayArTpNode")
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
                serialized = ARObject._serialize_item(item, "FlexrayArTpNode")
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
        child = ARObject._find_child_element(element, "CONNECTION-PRIO")
        if child is not None:
            connection_prio_value = child.text
            obj.connection_prio = connection_prio_value

        # Parse direct_tp_sdu_ref
        child = ARObject._find_child_element(element, "DIRECT-TP-SDU-REF")
        if child is not None:
            direct_tp_sdu_ref_value = ARRef.deserialize(child)
            obj.direct_tp_sdu_ref = direct_tp_sdu_ref_value

        # Parse multicast_ref
        child = ARObject._find_child_element(element, "MULTICAST-REF")
        if child is not None:
            multicast_ref_value = ARRef.deserialize(child)
            obj.multicast_ref = multicast_ref_value

        # Parse reversed_tp_sdu_ref
        child = ARObject._find_child_element(element, "REVERSED-TP-SDU-REF")
        if child is not None:
            reversed_tp_sdu_ref_value = ARRef.deserialize(child)
            obj.reversed_tp_sdu_ref = reversed_tp_sdu_ref_value

        # Parse source_ref
        child = ARObject._find_child_element(element, "SOURCE-REF")
        if child is not None:
            source_ref_value = ARRef.deserialize(child)
            obj.source_ref = source_ref_value

        # Parse target_refs (list from container "TARGET-REFS")
        obj.target_refs = []
        container = ARObject._find_child_element(element, "TARGET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.target_refs.append(child_value)

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
