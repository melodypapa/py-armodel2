"""IdsMgrNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class IdsMgrNeeds(ServiceNeeds):
    """AUTOSAR IdsMgrNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("use_smart", None, True, False, None),  # useSmart
    ]

    def __init__(self) -> None:
        """Initialize IdsMgrNeeds."""
        super().__init__()
        self.use_smart: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IdsMgrNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsMgrNeeds":
        """Create IdsMgrNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IdsMgrNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IdsMgrNeeds since parent returns ARObject
        return cast("IdsMgrNeeds", obj)


class IdsMgrNeedsBuilder:
    """Builder for IdsMgrNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsMgrNeeds = IdsMgrNeeds()

    def build(self) -> IdsMgrNeeds:
        """Build and return IdsMgrNeeds object.

        Returns:
            IdsMgrNeeds instance
        """
        # TODO: Add validation
        return self._obj
