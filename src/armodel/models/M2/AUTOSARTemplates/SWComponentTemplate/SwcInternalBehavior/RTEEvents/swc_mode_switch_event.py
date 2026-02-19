"""SwcModeSwitchEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 544)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration import (
    ModeActivationKind,
)


class SwcModeSwitchEvent(RTEEvent):
    """AUTOSAR SwcModeSwitchEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    activation: Optional[ModeActivationKind]
    def __init__(self) -> None:
        """Initialize SwcModeSwitchEvent."""
        super().__init__()
        self.activation: Optional[ModeActivationKind] = None
    def serialize(self) -> ET.Element:
        """Serialize SwcModeSwitchEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcModeSwitchEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activation
        if self.activation is not None:
            serialized = ARObject._serialize_item(self.activation, "ModeActivationKind")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTIVATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcModeSwitchEvent":
        """Deserialize XML element to SwcModeSwitchEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcModeSwitchEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcModeSwitchEvent, cls).deserialize(element)

        # Parse activation
        child = ARObject._find_child_element(element, "ACTIVATION")
        if child is not None:
            activation_value = ModeActivationKind.deserialize(child)
            obj.activation = activation_value

        return obj



class SwcModeSwitchEventBuilder:
    """Builder for SwcModeSwitchEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcModeSwitchEvent = SwcModeSwitchEvent()

    def build(self) -> SwcModeSwitchEvent:
        """Build and return SwcModeSwitchEvent object.

        Returns:
            SwcModeSwitchEvent instance
        """
        # TODO: Add validation
        return self._obj
