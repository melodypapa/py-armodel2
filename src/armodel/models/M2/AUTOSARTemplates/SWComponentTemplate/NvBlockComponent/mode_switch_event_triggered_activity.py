"""ModeSwitchEventTriggeredActivity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    swc_mode_switch_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ModeSwitchEventTriggeredActivity."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.swc_mode_switch_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchEventTriggeredActivity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchEventTriggeredActivity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
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

        # Serialize swc_mode_switch_event_ref
        if self.swc_mode_switch_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_mode_switch_event_ref, "SwcModeSwitchEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-MODE-SWITCH-EVENT-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchEventTriggeredActivity, cls).deserialize(element)

        # Parse role
        child = SerializationHelper.find_child_element(element, "ROLE")
        if child is not None:
            role_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse swc_mode_switch_event_ref
        child = SerializationHelper.find_child_element(element, "SWC-MODE-SWITCH-EVENT-REF")
        if child is not None:
            swc_mode_switch_event_ref_value = ARRef.deserialize(child)
            obj.swc_mode_switch_event_ref = swc_mode_switch_event_ref_value

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
