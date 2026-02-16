"""ISignalIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu_timing import (
    IPduTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)


class ISignalIPdu(IPdu):
    """AUTOSAR ISignalIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_pdu_timing", None, False, False, IPduTiming),  # iPduTiming
        ("i_signal_to_pdus", None, False, True, ISignalToIPduMapping),  # iSignalToPdus
        ("unused_bit", None, True, False, None),  # unusedBit
    ]

    def __init__(self) -> None:
        """Initialize ISignalIPdu."""
        super().__init__()
        self.i_pdu_timing: Optional[IPduTiming] = None
        self.i_signal_to_pdus: list[ISignalToIPduMapping] = []
        self.unused_bit: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalIPdu":
        """Create ISignalIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalIPdu since parent returns ARObject
        return cast("ISignalIPdu", obj)


class ISignalIPduBuilder:
    """Builder for ISignalIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalIPdu = ISignalIPdu()

    def build(self) -> ISignalIPdu:
        """Build and return ISignalIPdu object.

        Returns:
            ISignalIPdu instance
        """
        # TODO: Add validation
        return self._obj
