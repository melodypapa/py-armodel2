"""GeneralPurposeConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class GeneralPurposeConnection(ARElement):
    """AUTOSAR GeneralPurposeConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("pdu_triggerings", None, False, True, PduTriggering),  # pduTriggerings
    ]

    def __init__(self) -> None:
        """Initialize GeneralPurposeConnection."""
        super().__init__()
        self.pdu_triggerings: list[PduTriggering] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert GeneralPurposeConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GeneralPurposeConnection":
        """Create GeneralPurposeConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            GeneralPurposeConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to GeneralPurposeConnection since parent returns ARObject
        return cast("GeneralPurposeConnection", obj)


class GeneralPurposeConnectionBuilder:
    """Builder for GeneralPurposeConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GeneralPurposeConnection = GeneralPurposeConnection()

    def build(self) -> GeneralPurposeConnection:
        """Build and return GeneralPurposeConnection object.

        Returns:
            GeneralPurposeConnection instance
        """
        # TODO: Add validation
        return self._obj
