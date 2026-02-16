"""ModeInBswInstanceRef AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class ModeInBswInstanceRef(ARObject):
    """AUTOSAR ModeInBswInstanceRef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "context_bsw": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswImplementation,
        ),  # contextBsw
        "context_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # contextMode
        "target_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclaration,
        ),  # targetMode
    }

    def __init__(self) -> None:
        """Initialize ModeInBswInstanceRef."""
        super().__init__()
        self.context_bsw: Optional[BswImplementation] = None
        self.context_mode: Optional[ModeDeclarationGroup] = None
        self.target_mode: Optional[ModeDeclaration] = None


class ModeInBswInstanceRefBuilder:
    """Builder for ModeInBswInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeInBswInstanceRef = ModeInBswInstanceRef()

    def build(self) -> ModeInBswInstanceRef:
        """Build and return ModeInBswInstanceRef object.

        Returns:
            ModeInBswInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
