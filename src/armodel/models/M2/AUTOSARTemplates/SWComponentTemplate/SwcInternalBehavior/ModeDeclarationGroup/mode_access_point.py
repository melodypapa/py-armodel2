"""ModeAccessPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.mode_access_point_ident import (
    ModeAccessPointIdent,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeAccessPoint(ARObject):
    """AUTOSAR ModeAccessPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ident", None, False, False, ModeAccessPointIdent),  # ident
        ("mode_group_instance_ref", None, False, False, ModeDeclarationGroup),  # modeGroupInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize ModeAccessPoint."""
        super().__init__()
        self.ident: Optional[ModeAccessPointIdent] = None
        self.mode_group_instance_ref: Optional[ModeDeclarationGroup] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeAccessPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeAccessPoint":
        """Create ModeAccessPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeAccessPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeAccessPoint since parent returns ARObject
        return cast("ModeAccessPoint", obj)


class ModeAccessPointBuilder:
    """Builder for ModeAccessPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeAccessPoint = ModeAccessPoint()

    def build(self) -> ModeAccessPoint:
        """Build and return ModeAccessPoint object.

        Returns:
            ModeAccessPoint instance
        """
        # TODO: Add validation
        return self._obj
