"""ISignalToIPduMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)


class ISignalToIPduMapping(Identifiable):
    """AUTOSAR ISignalToIPduMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_signal", None, False, False, ISignal),  # iSignal
        ("i_signal_group", None, False, False, ISignalGroup),  # iSignalGroup
        ("packing_byte", None, False, False, ByteOrderEnum),  # packingByte
        ("start_position", None, True, False, None),  # startPosition
        ("transfer_property_enum", None, False, False, TransferPropertyEnum),  # transferPropertyEnum
        ("update", None, True, False, None),  # update
    ]

    def __init__(self) -> None:
        """Initialize ISignalToIPduMapping."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.i_signal_group: Optional[ISignalGroup] = None
        self.packing_byte: Optional[ByteOrderEnum] = None
        self.start_position: Optional[UnlimitedInteger] = None
        self.transfer_property_enum: Optional[TransferPropertyEnum] = None
        self.update: Optional[UnlimitedInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalToIPduMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalToIPduMapping":
        """Create ISignalToIPduMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalToIPduMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalToIPduMapping since parent returns ARObject
        return cast("ISignalToIPduMapping", obj)


class ISignalToIPduMappingBuilder:
    """Builder for ISignalToIPduMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalToIPduMapping = ISignalToIPduMapping()

    def build(self) -> ISignalToIPduMapping:
        """Build and return ISignalToIPduMapping object.

        Returns:
            ISignalToIPduMapping instance
        """
        # TODO: Add validation
        return self._obj
