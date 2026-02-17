"""ISignalTriggering AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 330)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 229)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "i_signal": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignal,
        ),  # iSignal
        "i_signal_group": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ISignalGroup,
        ),  # iSignalGroup
        "i_signal_ports": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ISignalPort,
        ),  # iSignalPorts
    }

    def __init__(self) -> None:
        """Initialize ISignalTriggering."""
        super().__init__()
        self.i_signal: Optional[ISignal] = None
        self.i_signal_group: Optional[ISignalGroup] = None
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
