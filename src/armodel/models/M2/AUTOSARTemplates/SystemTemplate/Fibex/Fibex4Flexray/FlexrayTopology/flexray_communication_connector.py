"""FlexrayCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
)


class FlexrayCommunicationConnector(CommunicationConnector):
    """AUTOSAR FlexrayCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    nm_ready_sleep: Optional[Float]
    wake_up: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize FlexrayCommunicationConnector."""
        super().__init__()
        self.nm_ready_sleep: Optional[Float] = None
        self.wake_up: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize nm_ready_sleep
        if self.nm_ready_sleep is not None:
            serialized = ARObject._serialize_item(self.nm_ready_sleep, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-READY-SLEEP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize wake_up
        if self.wake_up is not None:
            serialized = ARObject._serialize_item(self.wake_up, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WAKE-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayCommunicationConnector":
        """Deserialize XML element to FlexrayCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayCommunicationConnector, cls).deserialize(element)

        # Parse nm_ready_sleep
        child = ARObject._find_child_element(element, "NM-READY-SLEEP")
        if child is not None:
            nm_ready_sleep_value = child.text
            obj.nm_ready_sleep = nm_ready_sleep_value

        # Parse wake_up
        child = ARObject._find_child_element(element, "WAKE-UP")
        if child is not None:
            wake_up_value = child.text
            obj.wake_up = wake_up_value

        return obj



class FlexrayCommunicationConnectorBuilder:
    """Builder for FlexrayCommunicationConnector."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayCommunicationConnector = FlexrayCommunicationConnector()

    def build(self) -> FlexrayCommunicationConnector:
        """Build and return FlexrayCommunicationConnector object.

        Returns:
            FlexrayCommunicationConnector instance
        """
        # TODO: Add validation
        return self._obj
