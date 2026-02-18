"""CouplingPortStructuralElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 122)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class CouplingPortStructuralElement(Identifiable, ABC):
    """AUTOSAR CouplingPortStructuralElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize CouplingPortStructuralElement."""
        super().__init__()


class CouplingPortStructuralElementBuilder:
    """Builder for CouplingPortStructuralElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortStructuralElement = CouplingPortStructuralElement()

    def build(self) -> CouplingPortStructuralElement:
        """Build and return CouplingPortStructuralElement object.

        Returns:
            CouplingPortStructuralElement instance
        """
        # TODO: Add validation
        return self._obj
