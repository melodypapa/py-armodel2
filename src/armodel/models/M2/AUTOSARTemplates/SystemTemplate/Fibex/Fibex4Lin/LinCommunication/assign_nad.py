"""AssignNad AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_configuration_entry import (
    LinConfigurationEntry,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class AssignNad(LinConfigurationEntry):
    """AUTOSAR AssignNad."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "new_nad": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # newNad
    }

    def __init__(self) -> None:
        """Initialize AssignNad."""
        super().__init__()
        self.new_nad: Optional[Integer] = None


class AssignNadBuilder:
    """Builder for AssignNad."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AssignNad = AssignNad()

    def build(self) -> AssignNad:
        """Build and return AssignNad object.

        Returns:
            AssignNad instance
        """
        # TODO: Add validation
        return self._obj
