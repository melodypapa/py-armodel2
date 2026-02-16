"""BswQueuedDataReceptionPolicy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class BswQueuedDataReceptionPolicy(ARObject):
    """AUTOSAR BswQueuedDataReceptionPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("queue_length", None, True, False, None),  # queueLength
    ]

    def __init__(self) -> None:
        """Initialize BswQueuedDataReceptionPolicy."""
        super().__init__()
        self.queue_length: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswQueuedDataReceptionPolicy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswQueuedDataReceptionPolicy":
        """Create BswQueuedDataReceptionPolicy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswQueuedDataReceptionPolicy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswQueuedDataReceptionPolicy since parent returns ARObject
        return cast("BswQueuedDataReceptionPolicy", obj)


class BswQueuedDataReceptionPolicyBuilder:
    """Builder for BswQueuedDataReceptionPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswQueuedDataReceptionPolicy = BswQueuedDataReceptionPolicy()

    def build(self) -> BswQueuedDataReceptionPolicy:
        """Build and return BswQueuedDataReceptionPolicy object.

        Returns:
            BswQueuedDataReceptionPolicy instance
        """
        # TODO: Add validation
        return self._obj
