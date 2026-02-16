"""ModeErrorBehavior AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeErrorBehavior(ARObject):
    """AUTOSAR ModeErrorBehavior."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "default_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # defaultMode
        "error_reaction": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeErrorReactionPolicyEnum,
        ),  # errorReaction
    }

    def __init__(self) -> None:
        """Initialize ModeErrorBehavior."""
        super().__init__()
        self.default_mode: Optional[ModeDeclaration] = None
        self.error_reaction: Optional[ModeErrorReactionPolicyEnum] = None


class ModeErrorBehaviorBuilder:
    """Builder for ModeErrorBehavior."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeErrorBehavior = ModeErrorBehavior()

    def build(self) -> ModeErrorBehavior:
        """Build and return ModeErrorBehavior object.

        Returns:
            ModeErrorBehavior instance
        """
        # TODO: Add validation
        return self._obj
