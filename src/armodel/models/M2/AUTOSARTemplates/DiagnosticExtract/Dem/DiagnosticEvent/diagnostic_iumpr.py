"""DiagnosticIumpr AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 210)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent import (
    DiagnosticIumprKindEnum,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticIumpr(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumpr."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event: Optional[DiagnosticEvent]
    ratio_kind: Optional[DiagnosticIumprKindEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticIumpr."""
        super().__init__()
        self.event: Optional[DiagnosticEvent] = None
        self.ratio_kind: Optional[DiagnosticIumprKindEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumpr":
        """Deserialize XML element to DiagnosticIumpr object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumpr object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event
        child = ARObject._find_child_element(element, "EVENT")
        if child is not None:
            event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.event = event_value

        # Parse ratio_kind
        child = ARObject._find_child_element(element, "RATIO-KIND")
        if child is not None:
            ratio_kind_value = child.text
            obj.ratio_kind = ratio_kind_value

        return obj



class DiagnosticIumprBuilder:
    """Builder for DiagnosticIumpr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumpr = DiagnosticIumpr()

    def build(self) -> DiagnosticIumpr:
        """Build and return DiagnosticIumpr object.

        Returns:
            DiagnosticIumpr instance
        """
        # TODO: Add validation
        return self._obj
