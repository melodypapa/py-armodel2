"""LinSporadicFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_unconditional_frame import (
    LinUnconditionalFrame,
)


class LinSporadicFrame(LinFrame):
    """AUTOSAR LinSporadicFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("substituteds", None, False, True, LinUnconditionalFrame),  # substituteds
    ]

    def __init__(self) -> None:
        """Initialize LinSporadicFrame."""
        super().__init__()
        self.substituteds: list[LinUnconditionalFrame] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinSporadicFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSporadicFrame":
        """Create LinSporadicFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinSporadicFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinSporadicFrame since parent returns ARObject
        return cast("LinSporadicFrame", obj)


class LinSporadicFrameBuilder:
    """Builder for LinSporadicFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSporadicFrame = LinSporadicFrame()

    def build(self) -> LinSporadicFrame:
        """Build and return LinSporadicFrame object.

        Returns:
            LinSporadicFrame instance
        """
        # TODO: Add validation
        return self._obj
