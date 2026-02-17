"""TargetIPduRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 841)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Multiplatform.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Multiplatform.pdu_mapping_default_value import (
    PduMappingDefaultValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class TargetIPduRef(ARObject):
    """AUTOSAR TargetIPduRef."""

    default_value: Optional[PduMappingDefaultValue]
    target_i_pdu: Optional[PduTriggering]
    def __init__(self) -> None:
        """Initialize TargetIPduRef."""
        super().__init__()
        self.default_value: Optional[PduMappingDefaultValue] = None
        self.target_i_pdu: Optional[PduTriggering] = None


class TargetIPduRefBuilder:
    """Builder for TargetIPduRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TargetIPduRef = TargetIPduRef()

    def build(self) -> TargetIPduRef:
        """Build and return TargetIPduRef object.

        Returns:
            TargetIPduRef instance
        """
        # TODO: Add validation
        return self._obj
