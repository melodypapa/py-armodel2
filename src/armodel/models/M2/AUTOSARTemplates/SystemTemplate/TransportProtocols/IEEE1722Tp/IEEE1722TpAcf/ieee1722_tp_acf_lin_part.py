"""IEEE1722TpAcfLinPart AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp.IEEE1722TpAcf.ieee1722_tp_acf_bus_part import (
    IEEE1722TpAcfBusPart,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class IEEE1722TpAcfLinPart(IEEE1722TpAcfBusPart):
    """AUTOSAR IEEE1722TpAcfLinPart."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("lin_identifier", None, True, False, None),  # linIdentifier
        ("sdu", None, False, False, PduTriggering),  # sdu
    ]

    def __init__(self) -> None:
        """Initialize IEEE1722TpAcfLinPart."""
        super().__init__()
        self.lin_identifier: Optional[PositiveInteger] = None
        self.sdu: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IEEE1722TpAcfLinPart to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IEEE1722TpAcfLinPart":
        """Create IEEE1722TpAcfLinPart from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IEEE1722TpAcfLinPart instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IEEE1722TpAcfLinPart since parent returns ARObject
        return cast("IEEE1722TpAcfLinPart", obj)


class IEEE1722TpAcfLinPartBuilder:
    """Builder for IEEE1722TpAcfLinPart."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IEEE1722TpAcfLinPart = IEEE1722TpAcfLinPart()

    def build(self) -> IEEE1722TpAcfLinPart:
        """Build and return IEEE1722TpAcfLinPart object.

        Returns:
            IEEE1722TpAcfLinPart instance
        """
        # TODO: Add validation
        return self._obj
