"""CommConnectorPort AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)


class CommConnectorPort(Identifiable):
    """AUTOSAR CommConnectorPort."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "communication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (Communication),
        ),  # communication
    }

    def __init__(self) -> None:
        """Initialize CommConnectorPort."""
        super().__init__()
        self.communication: Optional[Any] = None


class CommConnectorPortBuilder:
    """Builder for CommConnectorPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommConnectorPort = CommConnectorPort()

    def build(self) -> CommConnectorPort:
        """Build and return CommConnectorPort object.

        Returns:
            CommConnectorPort instance
        """
        # TODO: Add validation
        return self._obj
