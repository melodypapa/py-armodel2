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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PermissibleSignalPath, cls).deserialize(element)

        # Parse operations (list from container "OPERATIONS")
        obj.operations = []
        container = ARObject._find_child_element(element, "OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.operations.append(child_value)

        # Parse physical_channels (list from container "PHYSICAL-CHANNELS")
        obj.physical_channels = []
        container = ARObject._find_child_element(element, "PHYSICAL-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.physical_channels.append(child_value)

        # Parse signals (list from container "SIGNALS")
        obj.signals = []
        container = ARObject._find_child_element(element, "SIGNALS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signals.append(child_value)

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
