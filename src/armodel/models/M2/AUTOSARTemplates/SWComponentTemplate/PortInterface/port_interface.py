"""PortInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 87)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2046)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 27)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 457)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ServiceProviderEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class PortInterface(ARElement, ABC):
    """AUTOSAR PortInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    is_service: Optional[Boolean]
    service_kind: Optional[ServiceProviderEnum]
    def __init__(self) -> None:
        """Initialize PortInterface."""
        super().__init__()
        self.is_service: Optional[Boolean] = None
        self.service_kind: Optional[ServiceProviderEnum] = None


class PortInterfaceBuilder:
    """Builder for PortInterface."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortInterface = PortInterface()

    def build(self) -> PortInterface:
        """Build and return PortInterface object.

        Returns:
            PortInterface instance
        """
        # TODO: Add validation
        return self._obj
