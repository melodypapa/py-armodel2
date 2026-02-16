"""PdurIPduGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class PdurIPduGroup(FibexElement):
    """AUTOSAR PdurIPduGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication", None, True, False, None),  # communication
        ("i_pdus", None, False, True, PduTriggering),  # iPdus
    ]

    def __init__(self) -> None:
        """Initialize PdurIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.i_pdus: list[PduTriggering] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PdurIPduGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PdurIPduGroup":
        """Create PdurIPduGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PdurIPduGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PdurIPduGroup since parent returns ARObject
        return cast("PdurIPduGroup", obj)


class PdurIPduGroupBuilder:
    """Builder for PdurIPduGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PdurIPduGroup = PdurIPduGroup()

    def build(self) -> PdurIPduGroup:
        """Build and return PdurIPduGroup object.

        Returns:
            PdurIPduGroup instance
        """
        # TODO: Add validation
        return self._obj
