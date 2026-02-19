"""DiagnosticServiceMappingDiagTarget AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 234)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DiagnosticServiceMappingDiagTarget(ARObject, ABC):
    """AUTOSAR DiagnosticServiceMappingDiagTarget."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticServiceMappingDiagTarget."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceMappingDiagTarget to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceMappingDiagTarget":
        """Deserialize XML element to DiagnosticServiceMappingDiagTarget object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceMappingDiagTarget object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class DiagnosticServiceMappingDiagTargetBuilder:
    """Builder for DiagnosticServiceMappingDiagTarget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceMappingDiagTarget = DiagnosticServiceMappingDiagTarget()

    def build(self) -> DiagnosticServiceMappingDiagTarget:
        """Build and return DiagnosticServiceMappingDiagTarget object.

        Returns:
            DiagnosticServiceMappingDiagTarget instance
        """
        # TODO: Add validation
        return self._obj
