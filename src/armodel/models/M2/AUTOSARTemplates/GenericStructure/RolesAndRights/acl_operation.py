"""AclOperation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 384)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 159)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_RolesAndRights.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class AclOperation(ARElement):
    """AUTOSAR AclOperation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implieds: list[AclOperation]
    def __init__(self) -> None:
        """Initialize AclOperation."""
        super().__init__()
        self.implieds: list[AclOperation] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AclOperation":
        """Deserialize XML element to AclOperation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AclOperation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AclOperation, cls).deserialize(element)

        # Parse implieds (list from container "IMPLIEDS")
        obj.implieds = []
        container = ARObject._find_child_element(element, "IMPLIEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implieds.append(child_value)

        return obj



class AclOperationBuilder:
    """Builder for AclOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AclOperation = AclOperation()

    def build(self) -> AclOperation:
        """Build and return AclOperation object.

        Returns:
            AclOperation instance
        """
        # TODO: Add validation
        return self._obj
