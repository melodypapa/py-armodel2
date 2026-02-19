"""DiagnosticCapabilityElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 236)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 753)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.service_needs import (
    ServiceNeeds,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticAudienceEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DiagRequirementIdString,
    PositiveInteger,
)
from abc import ABC, abstractmethod


class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """AUTOSAR DiagnosticCapabilityElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    audiences: list[DiagnosticAudienceEnum]
    diag: Optional[DiagRequirementIdString]
    security_access: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticCapabilityElement."""
        super().__init__()
        self.audiences: list[DiagnosticAudienceEnum] = []
        self.diag: Optional[DiagRequirementIdString] = None
        self.security_access: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCapabilityElement":
        """Deserialize XML element to DiagnosticCapabilityElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCapabilityElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse audiences (list)
        obj.audiences = []
        for child in ARObject._find_all_child_elements(element, "AUDIENCES"):
            audiences_value = child.text
            obj.audiences.append(audiences_value)

        # Parse diag
        child = ARObject._find_child_element(element, "DIAG")
        if child is not None:
            diag_value = child.text
            obj.diag = diag_value

        # Parse security_access
        child = ARObject._find_child_element(element, "SECURITY-ACCESS")
        if child is not None:
            security_access_value = child.text
            obj.security_access = security_access_value

        return obj



class DiagnosticCapabilityElementBuilder:
    """Builder for DiagnosticCapabilityElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCapabilityElement = DiagnosticCapabilityElement()

    def build(self) -> DiagnosticCapabilityElement:
        """Build and return DiagnosticCapabilityElement object.

        Returns:
            DiagnosticCapabilityElement instance
        """
        # TODO: Add validation
        return self._obj
