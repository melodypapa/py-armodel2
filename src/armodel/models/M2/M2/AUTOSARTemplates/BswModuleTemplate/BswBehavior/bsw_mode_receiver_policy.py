"""BswModeReceiverPolicy AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class BswModeReceiverPolicy(ARObject):
    """AUTOSAR BswModeReceiverPolicy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "enhanced_mode": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # enhancedMode
        "required_mode": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ModeDeclarationGroup,
        ),  # requiredMode
        "supports": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # supports
    }

    def __init__(self) -> None:
        """Initialize BswModeReceiverPolicy."""
        super().__init__()
        self.enhanced_mode: Optional[Boolean] = None
        self.required_mode: Optional[ModeDeclarationGroup] = None
        self.supports: Optional[Boolean] = None


class BswModeReceiverPolicyBuilder:
    """Builder for BswModeReceiverPolicy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModeReceiverPolicy = BswModeReceiverPolicy()

    def build(self) -> BswModeReceiverPolicy:
        """Build and return BswModeReceiverPolicy object.

        Returns:
            BswModeReceiverPolicy instance
        """
        # TODO: Add validation
        return self._obj
