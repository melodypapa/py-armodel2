"""SeparateSignalPath AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class SeparateSignalPath(SignalPathConstraint):
    """AUTOSAR SeparateSignalPath."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operations", None, False, True, any (SwcToSwcOperation)),  # operations
        ("signals", None, False, True, SwcToSwcSignal),  # signals
    ]

    def __init__(self) -> None:
        """Initialize SeparateSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.signals: list[SwcToSwcSignal] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SeparateSignalPath to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SeparateSignalPath":
        """Create SeparateSignalPath from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SeparateSignalPath instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SeparateSignalPath since parent returns ARObject
        return cast("SeparateSignalPath", obj)


class SeparateSignalPathBuilder:
    """Builder for SeparateSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SeparateSignalPath = SeparateSignalPath()

    def build(self) -> SeparateSignalPath:
        """Build and return SeparateSignalPath object.

        Returns:
            SeparateSignalPath instance
        """
        # TODO: Add validation
        return self._obj
