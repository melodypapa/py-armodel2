"""DiagnosticAbstractDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from abc import ABC, abstractmethod


class DiagnosticAbstractDataIdentifier(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticAbstractDataIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticAbstractDataIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAbstractDataIdentifier":
        """Deserialize XML element to DiagnosticAbstractDataIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAbstractDataIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        return obj



class DiagnosticAbstractDataIdentifierBuilder:
    """Builder for DiagnosticAbstractDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAbstractDataIdentifier = DiagnosticAbstractDataIdentifier()

    def build(self) -> DiagnosticAbstractDataIdentifier:
        """Build and return DiagnosticAbstractDataIdentifier object.

        Returns:
            DiagnosticAbstractDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
