"""ModeDeclarationGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_error_behavior import (
    ModeErrorBehavior,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_transition import (
    ModeTransition,
)


class ModeDeclarationGroup(ARElement):
    """AUTOSAR ModeDeclarationGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("initial_mode", None, False, False, ModeDeclaration),  # initialMode
        ("modes", None, False, True, ModeDeclaration),  # modes
        ("mode_manager", None, False, False, ModeErrorBehavior),  # modeManager
        ("mode_transition_mode_declaration_groups", None, False, True, ModeTransition),  # modeTransitionModeDeclarationGroups
        ("mode_user_error", None, False, False, ModeErrorBehavior),  # modeUserError
        ("on_transition", None, True, False, None),  # onTransition
    ]

    def __init__(self) -> None:
        """Initialize ModeDeclarationGroup."""
        super().__init__()
        self.initial_mode: Optional[ModeDeclaration] = None
        self.modes: list[ModeDeclaration] = []
        self.mode_manager: Optional[ModeErrorBehavior] = None
        self.mode_transition_mode_declaration_groups: list[ModeTransition] = []
        self.mode_user_error: Optional[ModeErrorBehavior] = None
        self.on_transition: Optional[PositiveInteger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ModeDeclarationGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationGroup":
        """Create ModeDeclarationGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ModeDeclarationGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ModeDeclarationGroup since parent returns ARObject
        return cast("ModeDeclarationGroup", obj)


class ModeDeclarationGroupBuilder:
    """Builder for ModeDeclarationGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationGroup = ModeDeclarationGroup()

    def build(self) -> ModeDeclarationGroup:
        """Build and return ModeDeclarationGroup object.

        Returns:
            ModeDeclarationGroup instance
        """
        # TODO: Add validation
        return self._obj
