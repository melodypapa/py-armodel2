"""CanNmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 684)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)


class CanNmNode(NmNode):
    """AUTOSAR CanNmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    all_nm_messages: Optional[Boolean]
    nm_car_wake_up: Optional[Boolean]
    nm_msg_cycle: Optional[TimeValue]
    nm_msg: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize CanNmNode."""
        super().__init__()
        self.all_nm_messages: Optional[Boolean] = None
        self.nm_car_wake_up: Optional[Boolean] = None
        self.nm_msg_cycle: Optional[TimeValue] = None
        self.nm_msg: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize CanNmNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanNmNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize all_nm_messages
        if self.all_nm_messages is not None:
            serialized = ARObject._serialize_item(self.all_nm_messages, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALL-NM-MESSAGES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_car_wake_up
        if self.nm_car_wake_up is not None:
            serialized = ARObject._serialize_item(self.nm_car_wake_up, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CAR-WAKE-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_msg_cycle
        if self.nm_msg_cycle is not None:
            serialized = ARObject._serialize_item(self.nm_msg_cycle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MSG-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_msg
        if self.nm_msg is not None:
            serialized = ARObject._serialize_item(self.nm_msg, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-MSG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanNmNode":
        """Deserialize XML element to CanNmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanNmNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanNmNode, cls).deserialize(element)

        # Parse all_nm_messages
        child = ARObject._find_child_element(element, "ALL-NM-MESSAGES")
        if child is not None:
            all_nm_messages_value = child.text
            obj.all_nm_messages = all_nm_messages_value

        # Parse nm_car_wake_up
        child = ARObject._find_child_element(element, "NM-CAR-WAKE-UP")
        if child is not None:
            nm_car_wake_up_value = child.text
            obj.nm_car_wake_up = nm_car_wake_up_value

        # Parse nm_msg_cycle
        child = ARObject._find_child_element(element, "NM-MSG-CYCLE")
        if child is not None:
            nm_msg_cycle_value = child.text
            obj.nm_msg_cycle = nm_msg_cycle_value

        # Parse nm_msg
        child = ARObject._find_child_element(element, "NM-MSG")
        if child is not None:
            nm_msg_value = child.text
            obj.nm_msg = nm_msg_value

        return obj



class CanNmNodeBuilder:
    """Builder for CanNmNode."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanNmNode = CanNmNode()

    def build(self) -> CanNmNode:
        """Build and return CanNmNode object.

        Returns:
            CanNmNode instance
        """
        # TODO: Add validation
        return self._obj
