"""BswTriggerDirectImplementation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class BswTriggerDirectImplementation(ARObject):
    """AUTOSAR BswTriggerDirectImplementation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("cat2_isr", None, True, False, None),  # cat2Isr
        ("mastered_trigger", None, False, False, Trigger),  # masteredTrigger
        ("task", None, True, False, None),  # task
    ]

    def __init__(self) -> None:
        """Initialize BswTriggerDirectImplementation."""
        super().__init__()
        self.cat2_isr: Optional[Identifier] = None
        self.mastered_trigger: Optional[Trigger] = None
        self.task: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswTriggerDirectImplementation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswTriggerDirectImplementation":
        """Create BswTriggerDirectImplementation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswTriggerDirectImplementation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswTriggerDirectImplementation since parent returns ARObject
        return cast("BswTriggerDirectImplementation", obj)


class BswTriggerDirectImplementationBuilder:
    """Builder for BswTriggerDirectImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTriggerDirectImplementation = BswTriggerDirectImplementation()

    def build(self) -> BswTriggerDirectImplementation:
        """Build and return BswTriggerDirectImplementation object.

        Returns:
            BswTriggerDirectImplementation instance
        """
        # TODO: Add validation
        return self._obj
