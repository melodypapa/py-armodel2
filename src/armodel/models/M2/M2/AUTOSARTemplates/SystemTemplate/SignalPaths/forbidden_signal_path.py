"""ForbiddenSignalPath AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class ForbiddenSignalPath(SignalPathConstraint):
    """AUTOSAR ForbiddenSignalPath."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "operations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwcToSwcOperation),
        ),  # operations
        "physical_channels": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=PhysicalChannel,
        ),  # physicalChannels
        "signals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcToSwcSignal,
        ),  # signals
    }

    def __init__(self) -> None:
        """Initialize ForbiddenSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.physical_channels: list[PhysicalChannel] = []
        self.signals: list[SwcToSwcSignal] = []


class ForbiddenSignalPathBuilder:
    """Builder for ForbiddenSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ForbiddenSignalPath = ForbiddenSignalPath()

    def build(self) -> ForbiddenSignalPath:
        """Build and return ForbiddenSignalPath object.

        Returns:
            ForbiddenSignalPath instance
        """
        # TODO: Add validation
        return self._obj
