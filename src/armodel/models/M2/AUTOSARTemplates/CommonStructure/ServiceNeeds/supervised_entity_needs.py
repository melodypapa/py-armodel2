"""SupervisedEntityNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class SupervisedEntityNeeds(ServiceNeeds):
    """AUTOSAR SupervisedEntityNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("activate_at_start", None, True, False, None),  # activateAtStart
        ("checkpointses", None, False, True, any (SupervisedEntity)),  # checkpointses
        ("enable", None, True, False, None),  # enable
        ("expected_alive", None, True, False, None),  # expectedAlive
        ("max_alive_cycle", None, True, False, None),  # maxAliveCycle
        ("min_alive_cycle", None, True, False, None),  # minAliveCycle
        ("tolerated_failed", None, True, False, None),  # toleratedFailed
    ]

    def __init__(self) -> None:
        """Initialize SupervisedEntityNeeds."""
        super().__init__()
        self.activate_at_start: Optional[Boolean] = None
        self.checkpointses: list[Any] = []
        self.enable: Optional[Boolean] = None
        self.expected_alive: Optional[TimeValue] = None
        self.max_alive_cycle: Optional[TimeValue] = None
        self.min_alive_cycle: Optional[TimeValue] = None
        self.tolerated_failed: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SupervisedEntityNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SupervisedEntityNeeds":
        """Create SupervisedEntityNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SupervisedEntityNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SupervisedEntityNeeds since parent returns ARObject
        return cast("SupervisedEntityNeeds", obj)


class SupervisedEntityNeedsBuilder:
    """Builder for SupervisedEntityNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SupervisedEntityNeeds = SupervisedEntityNeeds()

    def build(self) -> SupervisedEntityNeeds:
        """Build and return SupervisedEntityNeeds object.

        Returns:
            SupervisedEntityNeeds instance
        """
        # TODO: Add validation
        return self._obj
