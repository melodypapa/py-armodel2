"""DiagnosticIumprDenominatorGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 211)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprDenominatorGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumprDenominatorGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    iumprs: list[DiagnosticIumpr]
    def __init__(self) -> None:
        """Initialize DiagnosticIumprDenominatorGroup."""
        super().__init__()
        self.iumprs: list[DiagnosticIumpr] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprDenominatorGroup":
        """Deserialize XML element to DiagnosticIumprDenominatorGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprDenominatorGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse iumprs (list)
        obj.iumprs = []
        for child in ARObject._find_all_child_elements(element, "IUMPRS"):
            iumprs_value = ARObject._deserialize_by_tag(child, "DiagnosticIumpr")
            obj.iumprs.append(iumprs_value)

        return obj



class DiagnosticIumprDenominatorGroupBuilder:
    """Builder for DiagnosticIumprDenominatorGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprDenominatorGroup = DiagnosticIumprDenominatorGroup()

    def build(self) -> DiagnosticIumprDenominatorGroup:
        """Build and return DiagnosticIumprDenominatorGroup object.

        Returns:
            DiagnosticIumprDenominatorGroup instance
        """
        # TODO: Add validation
        return self._obj
