"""DiagnosticJ1939ExpandedFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_J1939.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.J1939.diagnostic_j1939_node import (
    DiagnosticJ1939Node,
)


class DiagnosticJ1939ExpandedFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticJ1939ExpandedFreezeFrame."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    node: Optional[DiagnosticJ1939Node]
    def __init__(self) -> None:
        """Initialize DiagnosticJ1939ExpandedFreezeFrame."""
        super().__init__()
        self.node: Optional[DiagnosticJ1939Node] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticJ1939ExpandedFreezeFrame":
        """Deserialize XML element to DiagnosticJ1939ExpandedFreezeFrame object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticJ1939ExpandedFreezeFrame object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse node
        child = ARObject._find_child_element(element, "NODE")
        if child is not None:
            node_value = ARObject._deserialize_by_tag(child, "DiagnosticJ1939Node")
            obj.node = node_value

        return obj



class DiagnosticJ1939ExpandedFreezeFrameBuilder:
    """Builder for DiagnosticJ1939ExpandedFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticJ1939ExpandedFreezeFrame = DiagnosticJ1939ExpandedFreezeFrame()

    def build(self) -> DiagnosticJ1939ExpandedFreezeFrame:
        """Build and return DiagnosticJ1939ExpandedFreezeFrame object.

        Returns:
            DiagnosticJ1939ExpandedFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
