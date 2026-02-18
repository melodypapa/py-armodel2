"""AbstractDoIpLogicAddressProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 556)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from abc import ABC, abstractmethod


class AbstractDoIpLogicAddressProps(Identifiable, ABC):
    """AUTOSAR AbstractDoIpLogicAddressProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize AbstractDoIpLogicAddressProps."""
        super().__init__()


class AbstractDoIpLogicAddressPropsBuilder:
    """Builder for AbstractDoIpLogicAddressProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractDoIpLogicAddressProps = AbstractDoIpLogicAddressProps()

    def build(self) -> AbstractDoIpLogicAddressProps:
        """Build and return AbstractDoIpLogicAddressProps object.

        Returns:
            AbstractDoIpLogicAddressProps instance
        """
        # TODO: Add validation
        return self._obj
