"""PdurIPduGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 352)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class PdurIPduGroup(FibexElement):
    """AUTOSAR PdurIPduGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    communication: Optional[String]
    i_pdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PdurIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.i_pdu_refs: list[ARRef] = []


class PdurIPduGroupBuilder:
    """Builder for PdurIPduGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PdurIPduGroup = PdurIPduGroup()

    def build(self) -> PdurIPduGroup:
        """Build and return PdurIPduGroup object.

        Returns:
            PdurIPduGroup instance
        """
        # TODO: Add validation
        return self._obj
