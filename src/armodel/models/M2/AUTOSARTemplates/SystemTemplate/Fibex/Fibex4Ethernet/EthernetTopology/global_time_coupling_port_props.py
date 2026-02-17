"""GlobalTimeCouplingPortProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 875)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class GlobalTimeCouplingPortProps(ARObject):
    """AUTOSAR GlobalTimeCouplingPortProps."""

    propagation: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeCouplingPortProps."""
        super().__init__()
        self.propagation: Optional[TimeValue] = None


class GlobalTimeCouplingPortPropsBuilder:
    """Builder for GlobalTimeCouplingPortProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: GlobalTimeCouplingPortProps = GlobalTimeCouplingPortProps()

    def build(self) -> GlobalTimeCouplingPortProps:
        """Build and return GlobalTimeCouplingPortProps object.

        Returns:
            GlobalTimeCouplingPortProps instance
        """
        # TODO: Add validation
        return self._obj
