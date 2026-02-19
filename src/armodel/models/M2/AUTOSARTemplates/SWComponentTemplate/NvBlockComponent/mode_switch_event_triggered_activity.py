"""ModeSwitchEventTriggeredActivity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.swc_mode_switch_event import (
    SwcModeSwitchEvent,
)


class ModeSwitchEventTriggeredActivity(ARObject):
    """AUTOSAR ModeSwitchEventTriggeredActivity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    role: Optional[Identifier]
    swc_mode_switch_event: Optional[SwcModeSwitchEvent]
    def __init__(self) -> None:
        """Initialize ModeSwitchEventTriggeredActivity."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.swc_mode_switch_event: Optional[SwcModeSwitchEvent] = None
    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchEventTriggeredActivity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize role
        if self.role is not None:
            serialized = ARObject._serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_mode_switch_event
        if self.swc_mode_switch_event is not None:
            serialized = ARObject._serialize_item(self.swc_mode_switch_event, "SwcModeSwitchEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-MODE-SWITCH-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchEventTriggeredActivity":
        """Deserialize XML element to ModeSwitchEventTriggeredActivity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchEventTriggeredActivity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse swc_mode_switch_event
        child = ARObject._find_child_element(element, "SWC-MODE-SWITCH-EVENT")
        if child is not None:
            swc_mode_switch_event_value = ARObject._deserialize_by_tag(child, "SwcModeSwitchEvent")
            obj.swc_mode_switch_event = swc_mode_switch_event_value

        return obj



class ModeSwitchEventTriggeredActivityBuilder:
    """Builder for ModeSwitchEventTriggeredActivity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeSwitchEventTriggeredActivity = ModeSwitchEventTriggeredActivity()

    def build(self) -> ModeSwitchEventTriggeredActivity:
        """Build and return ModeSwitchEventTriggeredActivity object.

        Returns:
            ModeSwitchEventTriggeredActivity instance
        """
        # TODO: Add validation
        return self._obj
