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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticIumprDenominatorGroup, cls).deserialize(element)

        # Parse iumprs (list from container "IUMPRS")
        obj.iumprs = []
        container = ARObject._find_child_element(element, "IUMPRS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.iumprs.append(child_value)

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
