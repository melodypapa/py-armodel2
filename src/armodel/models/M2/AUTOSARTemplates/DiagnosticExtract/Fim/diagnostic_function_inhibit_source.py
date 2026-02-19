"""DiagnosticFunctionInhibitSource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 216)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticFunctionInhibitSource(Identifiable):
    """AUTOSAR DiagnosticFunctionInhibitSource."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event: Optional[Any]
    event_group: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticFunctionInhibitSource."""
        super().__init__()
        self.event: Optional[Any] = None
        self.event_group: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionInhibitSource":
        """Deserialize XML element to DiagnosticFunctionInhibitSource object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFunctionInhibitSource object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse event
        child = ARObject._find_child_element(element, "EVENT")
        if child is not None:
            event_value = child.text
            obj.event = event_value

        # Parse event_group
        child = ARObject._find_child_element(element, "EVENT-GROUP")
        if child is not None:
            event_group_value = child.text
            obj.event_group = event_group_value

        return obj



class DiagnosticFunctionInhibitSourceBuilder:
    """Builder for DiagnosticFunctionInhibitSource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionInhibitSource = DiagnosticFunctionInhibitSource()

    def build(self) -> DiagnosticFunctionInhibitSource:
        """Build and return DiagnosticFunctionInhibitSource object.

        Returns:
            DiagnosticFunctionInhibitSource instance
        """
        # TODO: Add validation
        return self._obj
