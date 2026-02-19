"""DiagnosticIumprGroupIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 211)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class DiagnosticIumprGroupIdentifier(ARObject):
    """AUTOSAR DiagnosticIumprGroupIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    group_id: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize DiagnosticIumprGroupIdentifier."""
        super().__init__()
        self.group_id: Optional[NameToken] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprGroupIdentifier":
        """Deserialize XML element to DiagnosticIumprGroupIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprGroupIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse group_id
        child = ARObject._find_child_element(element, "GROUP-ID")
        if child is not None:
            group_id_value = child.text
            obj.group_id = group_id_value

        return obj



class DiagnosticIumprGroupIdentifierBuilder:
    """Builder for DiagnosticIumprGroupIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprGroupIdentifier = DiagnosticIumprGroupIdentifier()

    def build(self) -> DiagnosticIumprGroupIdentifier:
        """Build and return DiagnosticIumprGroupIdentifier object.

        Returns:
            DiagnosticIumprGroupIdentifier instance
        """
        # TODO: Add validation
        return self._obj
