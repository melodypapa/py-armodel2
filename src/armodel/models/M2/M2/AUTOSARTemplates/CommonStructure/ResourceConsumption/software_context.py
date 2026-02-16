"""SoftwareContext AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SoftwareContext(ARObject):
    """AUTOSAR SoftwareContext."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "input": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # input
        "state": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # state
    }

    def __init__(self) -> None:
        """Initialize SoftwareContext."""
        super().__init__()
        self.input: Optional[String] = None
        self.state: Optional[String] = None


class SoftwareContextBuilder:
    """Builder for SoftwareContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoftwareContext = SoftwareContext()

    def build(self) -> SoftwareContext:
        """Build and return SoftwareContext object.

        Returns:
            SoftwareContext instance
        """
        # TODO: Add validation
        return self._obj
