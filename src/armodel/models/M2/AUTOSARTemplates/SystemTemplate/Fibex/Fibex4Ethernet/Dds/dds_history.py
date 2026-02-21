"""DdsHistory AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 537)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsHistoryKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DdsHistory(ARObject):
    """AUTOSAR DdsHistory."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    history_kind: Optional[DdsHistoryKindEnum]
    history_order: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DdsHistory."""
        super().__init__()
        self.history_kind: Optional[DdsHistoryKindEnum] = None
        self.history_order: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsHistory to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsHistory, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize history_kind
        if self.history_kind is not None:
            serialized = SerializationHelper.serialize_item(self.history_kind, "DdsHistoryKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HISTORY-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize history_order
        if self.history_order is not None:
            serialized = SerializationHelper.serialize_item(self.history_order, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HISTORY-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsHistory":
        """Deserialize XML element to DdsHistory object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsHistory object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsHistory, cls).deserialize(element)

        # Parse history_kind
        child = SerializationHelper.find_child_element(element, "HISTORY-KIND")
        if child is not None:
            history_kind_value = DdsHistoryKindEnum.deserialize(child)
            obj.history_kind = history_kind_value

        # Parse history_order
        child = SerializationHelper.find_child_element(element, "HISTORY-ORDER")
        if child is not None:
            history_order_value = child.text
            obj.history_order = history_order_value

        return obj



class DdsHistoryBuilder:
    """Builder for DdsHistory."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsHistory = DdsHistory()

    def build(self) -> DdsHistory:
        """Build and return DdsHistory object.

        Returns:
            DdsHistory instance
        """
        # TODO: Add validation
        return self._obj
