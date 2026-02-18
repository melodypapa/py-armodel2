"""CommConnectorPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 303)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class CommConnectorPort(Identifiable, ABC):
    """AUTOSAR CommConnectorPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication: Optional[Any]
    def __init__(self) -> None:
        """Initialize CommConnectorPort."""
        super().__init__()
        self.communication: Optional[Any] = None


class CommConnectorPortBuilder:
    """Builder for CommConnectorPort."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CommConnectorPort = CommConnectorPort()

    def build(self) -> CommConnectorPort:
        """Build and return CommConnectorPort object.

        Returns:
            CommConnectorPort instance
        """
        # TODO: Add validation
        return self._obj
