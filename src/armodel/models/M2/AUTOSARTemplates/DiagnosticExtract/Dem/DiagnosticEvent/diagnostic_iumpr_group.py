"""DiagnosticIumprGroup AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_iumpr import (
    DiagnosticIumpr,
)


class DiagnosticIumprGroup(DiagnosticCommonElement):
    """AUTOSAR DiagnosticIumprGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    iumprs: list[DiagnosticIumpr]
    iumpr_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticIumprGroup."""
        super().__init__()
        self.iumprs: list[DiagnosticIumpr] = []
        self.iumpr_group_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIumprGroup":
        """Deserialize XML element to DiagnosticIumprGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIumprGroup object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse iumprs (list)
        obj.iumprs = []
        for child in ARObject._find_all_child_elements(element, "IUMPRS"):
            iumprs_value = ARObject._deserialize_by_tag(child, "DiagnosticIumpr")
            obj.iumprs.append(iumprs_value)

        # Parse iumpr_group_ref
        child = ARObject._find_child_element(element, "IUMPR-GROUP")
        if child is not None:
            iumpr_group_ref_value = ARObject._deserialize_by_tag(child, "DiagnosticIumprGroup")
            obj.iumpr_group_ref = iumpr_group_ref_value

        return obj



class DiagnosticIumprGroupBuilder:
    """Builder for DiagnosticIumprGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIumprGroup = DiagnosticIumprGroup()

    def build(self) -> DiagnosticIumprGroup:
        """Build and return DiagnosticIumprGroup object.

        Returns:
            DiagnosticIumprGroup instance
        """
        # TODO: Add validation
        return self._obj
