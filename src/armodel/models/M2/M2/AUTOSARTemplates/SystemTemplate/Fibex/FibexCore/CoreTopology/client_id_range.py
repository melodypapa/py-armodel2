"""ClientIdRange AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Limit,
)


class ClientIdRange(ARObject):
    """AUTOSAR ClientIdRange."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "lower_limit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # lowerLimit
        "upper_limit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # upperLimit
    }

    def __init__(self) -> None:
        """Initialize ClientIdRange."""
        super().__init__()
        self.lower_limit: Optional[Limit] = None
        self.upper_limit: Optional[Limit] = None


class ClientIdRangeBuilder:
    """Builder for ClientIdRange."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdRange = ClientIdRange()

    def build(self) -> ClientIdRange:
        """Build and return ClientIdRange object.

        Returns:
            ClientIdRange instance
        """
        # TODO: Add validation
        return self._obj
