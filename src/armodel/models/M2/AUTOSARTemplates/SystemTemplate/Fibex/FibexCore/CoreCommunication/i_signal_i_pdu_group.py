"""ISignalIPduGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu_group import (
    ISignalIPduGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)


class ISignalIPduGroup(FibexElement):
    """AUTOSAR ISignalIPduGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("communication", None, True, False, None),  # communication
        ("containeds", None, False, True, ISignalIPduGroup),  # containeds
        ("i_signal_i_pdus", None, False, True, ISignalIPdu),  # iSignalIPdus
        ("nm_pdus", None, False, True, NmPdu),  # nmPdus
    ]

    def __init__(self) -> None:
        """Initialize ISignalIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.containeds: list[ISignalIPduGroup] = []
        self.i_signal_i_pdus: list[ISignalIPdu] = []
        self.nm_pdus: list[NmPdu] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalIPduGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalIPduGroup":
        """Create ISignalIPduGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalIPduGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalIPduGroup since parent returns ARObject
        return cast("ISignalIPduGroup", obj)


class ISignalIPduGroupBuilder:
    """Builder for ISignalIPduGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalIPduGroup = ISignalIPduGroup()

    def build(self) -> ISignalIPduGroup:
        """Build and return ISignalIPduGroup object.

        Returns:
            ISignalIPduGroup instance
        """
        # TODO: Add validation
        return self._obj
