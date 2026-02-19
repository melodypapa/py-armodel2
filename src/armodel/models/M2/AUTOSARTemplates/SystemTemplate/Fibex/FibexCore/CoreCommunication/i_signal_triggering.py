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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalTriggering":
        """Deserialize XML element to ISignalTriggering object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalTriggering object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse i_signal
        child = ARObject._find_child_element(element, "I-SIGNAL")
        if child is not None:
            i_signal_value = ARObject._deserialize_by_tag(child, "ISignal")
            obj.i_signal = i_signal_value

        # Parse i_signal_group_ref
        child = ARObject._find_child_element(element, "I-SIGNAL-GROUP")
        if child is not None:
            i_signal_group_ref_value = ARObject._deserialize_by_tag(child, "ISignalGroup")
            obj.i_signal_group_ref = i_signal_group_ref_value

        # Parse i_signal_ports (list)
        obj.i_signal_ports = []
        for child in ARObject._find_all_child_elements(element, "I-SIGNAL-PORTS"):
            i_signal_ports_value = ARObject._deserialize_by_tag(child, "ISignalPort")
            obj.i_signal_ports.append(i_signal_ports_value)

        return obj



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
