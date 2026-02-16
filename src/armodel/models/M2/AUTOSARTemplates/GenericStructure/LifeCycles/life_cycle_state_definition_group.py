"""LifeCycleStateDefinitionGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)


class LifeCycleStateDefinitionGroup(ARElement):
    """AUTOSAR LifeCycleStateDefinitionGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lc_states", None, False, True, LifeCycleState),  # lcStates
    ]

    def __init__(self) -> None:
        """Initialize LifeCycleStateDefinitionGroup."""
        super().__init__()
        self.lc_states: list[LifeCycleState] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LifeCycleStateDefinitionGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleStateDefinitionGroup":
        """Create LifeCycleStateDefinitionGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LifeCycleStateDefinitionGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LifeCycleStateDefinitionGroup since parent returns ARObject
        return cast("LifeCycleStateDefinitionGroup", obj)


class LifeCycleStateDefinitionGroupBuilder:
    """Builder for LifeCycleStateDefinitionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleStateDefinitionGroup = LifeCycleStateDefinitionGroup()

    def build(self) -> LifeCycleStateDefinitionGroup:
        """Build and return LifeCycleStateDefinitionGroup object.

        Returns:
            LifeCycleStateDefinitionGroup instance
        """
        # TODO: Add validation
        return self._obj
