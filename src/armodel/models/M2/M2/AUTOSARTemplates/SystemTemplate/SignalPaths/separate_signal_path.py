"""SeparateSignalPath AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.signal_path_constraint import (
    SignalPathConstraint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths.swc_to_swc_signal import (
    SwcToSwcSignal,
)


class SeparateSignalPath(SignalPathConstraint):
    """AUTOSAR SeparateSignalPath."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "operations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (SwcToSwcOperation),
        ),  # operations
        "signals": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=SwcToSwcSignal,
        ),  # signals
    }

    def __init__(self) -> None:
        """Initialize SeparateSignalPath."""
        super().__init__()
        self.operations: list[Any] = []
        self.signals: list[SwcToSwcSignal] = []


class SeparateSignalPathBuilder:
    """Builder for SeparateSignalPath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SeparateSignalPath = SeparateSignalPath()

    def build(self) -> SeparateSignalPath:
        """Build and return SeparateSignalPath object.

        Returns:
            SeparateSignalPath instance
        """
        # TODO: Add validation
        return self._obj
