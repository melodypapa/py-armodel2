"""DiagnosticMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 223)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from abc import ABC, abstractmethod


class DiagnosticMapping(DiagnosticCommonElement, ABC):
    """AUTOSAR DiagnosticMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    provider: Optional[CpSoftwareCluster]
    requester: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize DiagnosticMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requester: Optional[CpSoftwareCluster] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticMapping":
        """Deserialize XML element to DiagnosticMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticMapping, cls).deserialize(element)

        # Parse provider
        child = ARObject._find_child_element(element, "PROVIDER")
        if child is not None:
            provider_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.provider = provider_value

        # Parse requester
        child = ARObject._find_child_element(element, "REQUESTER")
        if child is not None:
            requester_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.requester = requester_value

        return obj



class DiagnosticMappingBuilder:
    """Builder for DiagnosticMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMapping = DiagnosticMapping()

    def build(self) -> DiagnosticMapping:
        """Build and return DiagnosticMapping object.

        Returns:
            DiagnosticMapping instance
        """
        # TODO: Add validation
        return self._obj
