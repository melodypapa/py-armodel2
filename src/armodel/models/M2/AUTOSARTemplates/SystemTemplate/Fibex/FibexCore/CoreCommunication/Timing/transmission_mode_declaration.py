"""TransmissionModeDeclaration AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.Timing.mode_driven_transmission_mode_condition import (
    ModeDrivenTransmissionModeCondition,
)


class TransmissionModeDeclaration(ARObject):
    """AUTOSAR TransmissionModeDeclaration."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mode_drivens", None, False, True, ModeDrivenTransmissionModeCondition),  # modeDrivens
        ("transmission", None, False, False, any (TransmissionMode)),  # transmission
    ]

    def __init__(self) -> None:
        """Initialize TransmissionModeDeclaration."""
        super().__init__()
        self.mode_drivens: list[ModeDrivenTransmissionModeCondition] = []
        self.transmission: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransmissionModeDeclaration to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransmissionModeDeclaration":
        """Create TransmissionModeDeclaration from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransmissionModeDeclaration instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransmissionModeDeclaration since parent returns ARObject
        return cast("TransmissionModeDeclaration", obj)


class TransmissionModeDeclarationBuilder:
    """Builder for TransmissionModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransmissionModeDeclaration = TransmissionModeDeclaration()

    def build(self) -> TransmissionModeDeclaration:
        """Build and return TransmissionModeDeclaration object.

        Returns:
            TransmissionModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
