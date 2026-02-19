"""EventObdReadinessGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 176)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class EventObdReadinessGroup(ARObject):
    """AUTOSAR EventObdReadinessGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_obd: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize EventObdReadinessGroup."""
        super().__init__()
        self.event_obd: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize EventObdReadinessGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize event_obd
        if self.event_obd is not None:
            serialized = ARObject._serialize_item(self.event_obd, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-OBD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventObdReadinessGroup":
        """Deserialize XML element to EventObdReadinessGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EventObdReadinessGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event_obd
        child = ARObject._find_child_element(element, "EVENT-OBD")
        if child is not None:
            event_obd_value = child.text
            obj.event_obd = event_obd_value

        return obj



class EventObdReadinessGroupBuilder:
    """Builder for EventObdReadinessGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventObdReadinessGroup = EventObdReadinessGroup()

    def build(self) -> EventObdReadinessGroup:
        """Build and return EventObdReadinessGroup object.

        Returns:
            EventObdReadinessGroup instance
        """
        # TODO: Add validation
        return self._obj
