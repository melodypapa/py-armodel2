"""SoConIPduIdentifier AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class SoConIPduIdentifier(Referrable):
    """AUTOSAR SoConIPduIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("header_id", None, True, False, None),  # headerId
        ("pdu_collection", None, False, False, any (PduCollection)),  # pduCollection
        ("pdu_collection_trigger", None, False, False, PduCollectionTriggerEnum),  # pduCollectionTrigger
        ("pdu_triggering", None, False, False, PduTriggering),  # pduTriggering
    ]

    def __init__(self) -> None:
        """Initialize SoConIPduIdentifier."""
        super().__init__()
        self.header_id: Optional[PositiveInteger] = None
        self.pdu_collection: Optional[Any] = None
        self.pdu_collection_trigger: Optional[PduCollectionTriggerEnum] = None
        self.pdu_triggering: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SoConIPduIdentifier to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoConIPduIdentifier":
        """Create SoConIPduIdentifier from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SoConIPduIdentifier instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SoConIPduIdentifier since parent returns ARObject
        return cast("SoConIPduIdentifier", obj)


class SoConIPduIdentifierBuilder:
    """Builder for SoConIPduIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoConIPduIdentifier = SoConIPduIdentifier()

    def build(self) -> SoConIPduIdentifier:
        """Build and return SoConIPduIdentifier object.

        Returns:
            SoConIPduIdentifier instance
        """
        # TODO: Add validation
        return self._obj
