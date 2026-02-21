"""DtcStatusChangeNotificationNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 776)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DtcStatusChangeNotificationNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    notification_time: Optional[Any]
    def __init__(self) -> None:
        """Initialize DtcStatusChangeNotificationNeeds."""
        super().__init__()
        self.notification_time: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DtcStatusChangeNotificationNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DtcStatusChangeNotificationNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize notification_time
        if self.notification_time is not None:
            serialized = SerializationHelper.serialize_item(self.notification_time, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NOTIFICATION-TIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DtcStatusChangeNotificationNeeds":
        """Deserialize XML element to DtcStatusChangeNotificationNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DtcStatusChangeNotificationNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DtcStatusChangeNotificationNeeds, cls).deserialize(element)

        # Parse notification_time
        child = SerializationHelper.find_child_element(element, "NOTIFICATION-TIME")
        if child is not None:
            notification_time_value = child.text
            obj.notification_time = notification_time_value

        return obj



class DtcStatusChangeNotificationNeedsBuilder:
    """Builder for DtcStatusChangeNotificationNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DtcStatusChangeNotificationNeeds = DtcStatusChangeNotificationNeeds()

    def build(self) -> DtcStatusChangeNotificationNeeds:
        """Build and return DtcStatusChangeNotificationNeeds object.

        Returns:
            DtcStatusChangeNotificationNeeds instance
        """
        # TODO: Add validation
        return self._obj
