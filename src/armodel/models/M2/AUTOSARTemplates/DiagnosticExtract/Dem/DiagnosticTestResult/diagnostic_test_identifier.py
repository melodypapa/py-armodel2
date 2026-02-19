"""DiagnosticTestIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 205)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestIdentifier(ARObject):
    """AUTOSAR DiagnosticTestIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    uas_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticTestIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.uas_id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticTestIdentifier":
        """Deserialize XML element to DiagnosticTestIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticTestIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse uas_id
        child = ARObject._find_child_element(element, "UAS-ID")
        if child is not None:
            uas_id_value = child.text
            obj.uas_id = uas_id_value

        return obj



class DiagnosticTestIdentifierBuilder:
    """Builder for DiagnosticTestIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestIdentifier = DiagnosticTestIdentifier()

    def build(self) -> DiagnosticTestIdentifier:
        """Build and return DiagnosticTestIdentifier object.

        Returns:
            DiagnosticTestIdentifier instance
        """
        # TODO: Add validation
        return self._obj
