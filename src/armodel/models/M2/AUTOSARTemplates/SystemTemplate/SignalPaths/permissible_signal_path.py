"""PermissibleSignalPath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 256)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SignalPaths.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class PermissibleSignalPath(SignalPathConstraint):
    """AUTOSAR PermissibleSignalPath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operations: list[Any]
    physical_channels: list[PhysicalChannel]
    signals: list[SwcToSwcSignal]
    def __init__(self) -> None:
        """Initialize PermissibleSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channels: list[PhysicalChannel] = []
        self.signals: list[SwcToSwcSignal] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "PermissibleSignalPath":
        """Deserialize XML element to PermissibleSignalPath object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PermissibleSignalPath object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse operations (list)
        obj.operations = []
        for child in ARObject._find_all_child_elements(element, "OPERATIONS"):
            operations_value = child.text
            obj.operations.append(operations_value)

        # Parse physical_channels (list)
        obj.physical_channels = []
        for child in ARObject._find_all_child_elements(element, "PHYSICAL-CHANNELS"):
            physical_channels_value = ARObject._deserialize_by_tag(child, "PhysicalChannel")
            obj.physical_channels.append(physical_channels_value)

        # Parse signals (list)
        obj.signals = []
        for child in ARObject._find_all_child_elements(element, "SIGNALS"):
            signals_value = ARObject._deserialize_by_tag(child, "SwcToSwcSignal")
            obj.signals.append(signals_value)

        return obj



class PermissibleSignalPathBuilder:
    """Builder for PermissibleSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PermissibleSignalPath = PermissibleSignalPath()

    def build(self) -> PermissibleSignalPath:
        """Build and return PermissibleSignalPath object.

        Returns:
            PermissibleSignalPath instance
        """
        # TODO: Add validation
        return self._obj
