"""DynamicPartAlternative AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 411)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class DynamicPartAlternative(ARObject):
    """AUTOSAR DynamicPartAlternative."""

    initial_dynamic: Optional[Boolean]
    i_pdu: Optional[ISignalIPdu]
    selector_field: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DynamicPartAlternative."""
        super().__init__()
        self.initial_dynamic: Optional[Boolean] = None
        self.i_pdu: Optional[ISignalIPdu] = None
        self.selector_field: Optional[Integer] = None


class DynamicPartAlternativeBuilder:
    """Builder for DynamicPartAlternative."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DynamicPartAlternative = DynamicPartAlternative()

    def build(self) -> DynamicPartAlternative:
        """Build and return DynamicPartAlternative object.

        Returns:
            DynamicPartAlternative instance
        """
        # TODO: Add validation
        return self._obj
