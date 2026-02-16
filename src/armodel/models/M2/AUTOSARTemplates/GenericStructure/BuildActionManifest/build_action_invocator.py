"""BuildActionInvocator AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    VerbatimString,
)


class BuildActionInvocator(ARObject):
    """AUTOSAR BuildActionInvocator."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "command": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # command
    }

    def __init__(self) -> None:
        """Initialize BuildActionInvocator."""
        super().__init__()
        self.command: Optional[VerbatimString] = None


class BuildActionInvocatorBuilder:
    """Builder for BuildActionInvocator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionInvocator = BuildActionInvocator()

    def build(self) -> BuildActionInvocator:
        """Build and return BuildActionInvocator object.

        Returns:
            BuildActionInvocator instance
        """
        # TODO: Add validation
        return self._obj
