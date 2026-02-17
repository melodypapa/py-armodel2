"""MacSecGlobalKayProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class MacSecGlobalKayProps(ARElement):
    """AUTOSAR MacSecGlobalKayProps."""

    bypass_ether: PositiveInteger
    bypass_vlan: PositiveInteger
    def __init__(self) -> None:
        """Initialize MacSecGlobalKayProps."""
        super().__init__()
        self.bypass_ether: PositiveInteger = None
        self.bypass_vlan: PositiveInteger = None


class MacSecGlobalKayPropsBuilder:
    """Builder for MacSecGlobalKayProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MacSecGlobalKayProps = MacSecGlobalKayProps()

    def build(self) -> MacSecGlobalKayProps:
        """Build and return MacSecGlobalKayProps object.

        Returns:
            MacSecGlobalKayProps instance
        """
        # TODO: Add validation
        return self._obj
