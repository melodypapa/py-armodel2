"""ISignalTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal import (
    ISignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_group import (
    ISignalGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_port import (
    ISignalPort,
)


class ISignalTriggering(Identifiable):
    """AUTOSAR ISignalTriggering."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_signal: Optional[ISignal]
    i_signal_group_ref: Optional[ARRef]
    i_signal_ports: list[ISignalPort]
    def __init__(self) -> None:
        """Initialize ISignalTriggering."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.i_signal_group_ref: Optional[ARRef] = None
        self.i_signal_ports: list[ISignalPort] = []


class ISignalTriggeringBuilder:
    """Builder for ISignalTriggering."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ISignalTriggering = ISignalTriggering()

    def build(self) -> ISignalTriggering:
        """Build and return ISignalTriggering object.

        Returns:
            ISignalTriggering instance
        """
        # TODO: Add validation
        return self._obj
