"""TpPort AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)


class TpPort(ARObject):
    """AUTOSAR TpPort."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dynamically": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dynamically
        "port_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # portNumber
    }

    def __init__(self) -> None:
        """Initialize TpPort."""
        super().__init__()
        self.dynamically: Optional[Boolean] = None
        self.port_number: Optional[PositiveInteger] = None


class TpPortBuilder:
    """Builder for TpPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpPort = TpPort()

    def build(self) -> TpPort:
        """Build and return TpPort object.

        Returns:
            TpPort instance
        """
        # TODO: Add validation
        return self._obj
