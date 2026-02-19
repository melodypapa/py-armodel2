"""ClientIdDefinitionSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 44)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.client_id_definition import (
    ClientIdDefinition,
)


class ClientIdDefinitionSet(ARElement):
    """AUTOSAR ClientIdDefinitionSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_ids: list[ClientIdDefinition]
    def __init__(self) -> None:
        """Initialize ClientIdDefinitionSet."""
        super().__init__()
        self.client_ids: list[ClientIdDefinition] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientIdDefinitionSet":
        """Deserialize XML element to ClientIdDefinitionSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientIdDefinitionSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse client_ids (list)
        obj.client_ids = []
        for child in ARObject._find_all_child_elements(element, "CLIENT-IDS"):
            client_ids_value = ARObject._deserialize_by_tag(child, "ClientIdDefinition")
            obj.client_ids.append(client_ids_value)

        return obj



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
