"""EndToEndProtectionISignalIPdu AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class EndToEndProtectionISignalIPdu(ARObject):
    """AUTOSAR EndToEndProtectionISignalIPdu."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_offset", None, True, False, None),  # dataOffset
        ("i_signal_group", None, False, False, ISignalGroup),  # iSignalGroup
        ("i_signal_i_pdu", None, False, False, ISignalIPdu),  # iSignalIPdu
    ]

    def __init__(self) -> None:
        """Initialize EndToEndProtectionISignalIPdu."""
        super().__init__()
        self.data_offset: Optional[Integer] = None
        self.i_signal_group: Optional[ISignalGroup] = None
        self.i_signal_i_pdu: Optional[ISignalIPdu] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EndToEndProtectionISignalIPdu to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EndToEndProtectionISignalIPdu":
        """Create EndToEndProtectionISignalIPdu from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EndToEndProtectionISignalIPdu instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EndToEndProtectionISignalIPdu since parent returns ARObject
        return cast("EndToEndProtectionISignalIPdu", obj)


class EndToEndProtectionISignalIPduBuilder:
    """Builder for EndToEndProtectionISignalIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionISignalIPdu = EndToEndProtectionISignalIPdu()

    def build(self) -> EndToEndProtectionISignalIPdu:
        """Build and return EndToEndProtectionISignalIPdu object.

        Returns:
            EndToEndProtectionISignalIPdu instance
        """
        # TODO: Add validation
        return self._obj
