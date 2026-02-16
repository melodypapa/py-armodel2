"""IEEE1722TpAcfBusPart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class IEEE1722TpAcfBusPart(Identifiable):
    """AUTOSAR IEEE1722TpAcfBusPart."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("collection_trigger", None, False, False, PduCollectionTriggerEnum),  # collectionTrigger
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfBusPart."""
        super().__init__()
        self.collection_trigger: Optional[PduCollectionTriggerEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAcfBusPart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfBusPart":
        """Create IEEE1722TpAcfBusPart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAcfBusPart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAcfBusPart since parent returns ARObject
        return cast("IEEE1722TpAcfBusPart", obj)


class IEEE1722TpAcfBusPartBuilder:
    """Builder for IEEE1722TpAcfBusPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfBusPart = IEEE1722TpAcfBusPart()

    def build(self) -> IEEE1722TpAcfBusPart:
        """Build and return IEEE1722TpAcfBusPart object.

        Returns:
            IEEE1722TpAcfBusPart instance
        """
        # TODO: Add validation
        return self._obj
