"""ModeDeclarationGroupPrototype AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeDeclarationGroupPrototype(Identifiable):
    """AUTOSAR ModeDeclarationGroupPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sw_calibration_access", None, False, False, SwCalibrationAccessEnum),  # swCalibrationAccess
        ("type", None, False, False, ModeDeclarationGroup),  # type
    ]

    def __init__(self) -> None:
        """Initialize ModeDeclarationGroupPrototype."""
        super().__init__()
        self.sw_calibration_access: Optional[SwCalibrationAccessEnum] = None
        self.type: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeDeclarationGroupPrototype to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroupPrototype":
        """Create ModeDeclarationGroupPrototype from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeDeclarationGroupPrototype instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeDeclarationGroupPrototype since parent returns ARObject
        return cast("ModeDeclarationGroupPrototype", obj)


class ModeDeclarationGroupPrototypeBuilder:
    """Builder for ModeDeclarationGroupPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroupPrototype = ModeDeclarationGroupPrototype()

    def build(self) -> ModeDeclarationGroupPrototype:
        """Build and return ModeDeclarationGroupPrototype object.

        Returns:
            ModeDeclarationGroupPrototype instance
        """
        # TODO: Add validation
        return self._obj
