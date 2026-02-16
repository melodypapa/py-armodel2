"""ClientServerApplicationErrorMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.application_error import (
    ApplicationError,
)


class ClientServerApplicationErrorMapping(ARObject):
    """AUTOSAR ClientServerApplicationErrorMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "first_application": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationError,
        ),  # firstApplication
        "second": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ApplicationError,
        ),  # second
    }

    def __init__(self) -> None:
        """Initialize ClientServerApplicationErrorMapping."""
        super().__init__()
        self.first_application: Optional[ApplicationError] = None
        self.second: Optional[ApplicationError] = None


class ClientServerApplicationErrorMappingBuilder:
    """Builder for ClientServerApplicationErrorMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientServerApplicationErrorMapping = ClientServerApplicationErrorMapping()

    def build(self) -> ClientServerApplicationErrorMapping:
        """Build and return ClientServerApplicationErrorMapping object.

        Returns:
            ClientServerApplicationErrorMapping instance
        """
        # TODO: Add validation
        return self._obj
