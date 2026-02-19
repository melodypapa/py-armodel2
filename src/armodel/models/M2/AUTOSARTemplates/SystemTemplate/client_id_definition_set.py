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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientIdDefinitionSet, cls).deserialize(element)

        # Parse client_ids (list from container "CLIENT-IDS")
        obj.client_ids = []
        container = ARObject._find_child_element(element, "CLIENT-IDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_ids.append(child_value)

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
