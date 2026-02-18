"""EndToEndProtectionISignalIPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 987)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 384)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_EndToEndProtection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)


class EndToEndProtectionISignalIPdu(ARObject):
    """AUTOSAR EndToEndProtectionISignalIPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_offset: Optional[Integer]
    i_signal_group: Optional[ISignalGroup]
    i_signal_i_pdu: Optional[ISignalIPdu]
    def __init__(self) -> None:
        """Initialize EndToEndProtectionISignalIPdu."""
        super().__init__()
        self.data_offset: Optional[Integer] = None
        self.i_signal_group: Optional[ISignalGroup] = None
        self.i_signal_i_pdu: Optional[ISignalIPdu] = None


class EndToEndProtectionISignalIPduBuilder:
    """Builder for EndToEndProtectionISignalIPdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EndToEndProtectionISignalIPdu = EndToEndProtectionISignalIPdu()

    def build(self) -> EndToEndProtectionISignalIPdu:
        """Build and return EndToEndProtectionISignalIPdu object.

        Returns:
            EndToEndProtectionISignalIPdu instance
        """
        # TODO: Add validation
        return self._obj
