"""ClientIdDefinitionSet AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.client_id_definition import (
    ClientIdDefinition,
)


class ClientIdDefinitionSet(ARElement):
    """AUTOSAR ClientIdDefinitionSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "client_ids": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ClientIdDefinition,
        ),  # clientIds
    }

    def __init__(self) -> None:
        """Initialize ClientIdDefinitionSet."""
        super().__init__()
        self.client_ids: list[ClientIdDefinition] = []


class ClientIdDefinitionSetBuilder:
    """Builder for ClientIdDefinitionSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ClientIdDefinitionSet = ClientIdDefinitionSet()

    def build(self) -> ClientIdDefinitionSet:
        """Build and return ClientIdDefinitionSet object.

        Returns:
            ClientIdDefinitionSet instance
        """
        # TODO: Add validation
        return self._obj
