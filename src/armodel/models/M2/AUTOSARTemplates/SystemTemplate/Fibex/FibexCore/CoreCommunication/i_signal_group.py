"""ISignalGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 993)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 323)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)


class ISignalGroup(FibexElement):
    """AUTOSAR ISignalGroup."""

    def __init__(self) -> None:
        """Initialize ISignalGroup."""
        super().__init__()
        self.com_based: Optional[DataTransformation] = None
        self.i_signals: list[ISignal] = []
        self.system_signal_group: Optional[SystemSignalGroup] = None
        self.transformation_i_signals: list[Any] = []


class ISignalGroupBuilder:
    """Builder for ISignalGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalGroup = ISignalGroup()

    def build(self) -> ISignalGroup:
        """Build and return ISignalGroup object.

        Returns:
            ISignalGroup instance
        """
        # TODO: Add validation
        return self._obj
