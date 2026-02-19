"""DiagnosticJ1939SpnMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 267)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_DiagnosticJ1939Mapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_spn import (
    DiagnosticJ1939Spn,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal import (
    SystemSignal,
)


class DiagnosticJ1939SpnMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticJ1939SpnMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sending_nodes: list[DiagnosticJ1939Node]
    spn: Optional[DiagnosticJ1939Spn]
    system_signal: Optional[SystemSignal]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939SpnMapping."""
        super().__init__()
        self.sending_nodes: list[DiagnosticJ1939Node] = []
        self.spn: Optional[DiagnosticJ1939Spn] = None
        self.system_signal: Optional[SystemSignal] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939SpnMapping":
        """Deserialize XML element to DiagnosticJ1939SpnMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939SpnMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticJ1939SpnMapping, cls).deserialize(element)

        # Parse sending_nodes (list from container "SENDING-NODES")
        obj.sending_nodes = []
        container = ARObject._find_child_element(element, "SENDING-NODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sending_nodes.append(child_value)

        # Parse spn
        child = ARObject._find_child_element(element, "SPN")
        if child is not None:
            spn_value = ARObject._deserialize_by_tag(child, "DiagnosticJ1939Spn")
            obj.spn = spn_value

        # Parse system_signal
        child = ARObject._find_child_element(element, "SYSTEM-SIGNAL")
        if child is not None:
            system_signal_value = ARObject._deserialize_by_tag(child, "SystemSignal")
            obj.system_signal = system_signal_value

        return obj



class DiagnosticJ1939SpnMappingBuilder:
    """Builder for DiagnosticJ1939SpnMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939SpnMapping = DiagnosticJ1939SpnMapping()

    def build(self) -> DiagnosticJ1939SpnMapping:
        """Build and return DiagnosticJ1939SpnMapping object.

        Returns:
            DiagnosticJ1939SpnMapping instance
        """
        # TODO: Add validation
        return self._obj
