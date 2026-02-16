"""PermissibleSignalPath AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class PermissibleSignalPath(SignalPathConstraint):
    """AUTOSAR PermissibleSignalPath."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operations", None, False, True, any (SwcToSwcOperation)),  # operations
        ("physical_channels", None, False, True, PhysicalChannel),  # physicalChannels
        ("signals", None, False, True, SwcToSwcSignal),  # signals
    ]

    def __init__(self) -> None:
        """Initialize PermissibleSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channels: list[PhysicalChannel] = []
        self.signals: list[SwcToSwcSignal] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PermissibleSignalPath to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PermissibleSignalPath":
        """Create PermissibleSignalPath from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PermissibleSignalPath instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PermissibleSignalPath since parent returns ARObject
        return cast("PermissibleSignalPath", obj)


class PermissibleSignalPathBuilder:
    """Builder for PermissibleSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PermissibleSignalPath = PermissibleSignalPath()

    def build(self) -> PermissibleSignalPath:
        """Build and return PermissibleSignalPath object.

        Returns:
            PermissibleSignalPath instance
        """
        # TODO: Add validation
        return self._obj
