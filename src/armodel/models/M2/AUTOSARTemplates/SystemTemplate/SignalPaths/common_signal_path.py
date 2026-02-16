"""CommonSignalPath AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class CommonSignalPath(SignalPathConstraint):
    """AUTOSAR CommonSignalPath."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operations", None, False, True, any (SwcToSwcOperation)),  # operations
        ("signals", None, False, True, SwcToSwcSignal),  # signals
    ]

    def __init__(self) -> None:
        """Initialize CommonSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.signals: list[SwcToSwcSignal] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CommonSignalPath to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommonSignalPath":
        """Create CommonSignalPath from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CommonSignalPath instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CommonSignalPath since parent returns ARObject
        return cast("CommonSignalPath", obj)


class CommonSignalPathBuilder:
    """Builder for CommonSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommonSignalPath = CommonSignalPath()

    def build(self) -> CommonSignalPath:
        """Build and return CommonSignalPath object.

        Returns:
            CommonSignalPath instance
        """
        # TODO: Add validation
        return self._obj
