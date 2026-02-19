"""DiagnosticJ1939Spn AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 219)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticJ1939Spn(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939Spn."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    spn: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939Spn."""
        super().__init__()
        self.spn: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939Spn":
        """Deserialize XML element to DiagnosticJ1939Spn object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939Spn object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse spn
        child = ARObject._find_child_element(element, "SPN")
        if child is not None:
            spn_value = child.text
            obj.spn = spn_value

        return obj



class DiagnosticJ1939SpnBuilder:
    """Builder for DiagnosticJ1939Spn."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939Spn = DiagnosticJ1939Spn()

    def build(self) -> DiagnosticJ1939Spn:
        """Build and return DiagnosticJ1939Spn object.

        Returns:
            DiagnosticJ1939Spn instance
        """
        # TODO: Add validation
        return self._obj
