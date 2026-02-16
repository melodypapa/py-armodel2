"""ISignalTriggering AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_port import (
    ISignalPort,
)


class ISignalTriggering(Identifiable):
    """AUTOSAR ISignalTriggering."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("i_signal", None, False, False, ISignal),  # iSignal
        ("i_signal_group", None, False, False, ISignalGroup),  # iSignalGroup
        ("i_signal_ports", None, False, True, ISignalPort),  # iSignalPorts
    ]

    def __init__(self) -> None:
        """Initialize ISignalTriggering."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.i_signal_group: Optional[ISignalGroup] = None
        self.i_signal_ports: list[ISignalPort] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ISignalTriggering to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalTriggering":
        """Create ISignalTriggering from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ISignalTriggering instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ISignalTriggering since parent returns ARObject
        return cast("ISignalTriggering", obj)


class ISignalTriggeringBuilder:
    """Builder for ISignalTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalTriggering = ISignalTriggering()

    def build(self) -> ISignalTriggering:
        """Build and return ISignalTriggering object.

        Returns:
            ISignalTriggering instance
        """
        # TODO: Add validation
        return self._obj
