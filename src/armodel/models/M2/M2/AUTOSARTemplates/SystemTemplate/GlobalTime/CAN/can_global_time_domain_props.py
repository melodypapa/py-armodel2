"""CanGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 864)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_CAN.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CanGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR CanGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize CanGlobalTimeDomainProps."""
        super().__init__()
        self.fup_data_id_list: PositiveInteger = None
        self.ofns_data_id_list: PositiveInteger = None
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None


class CanGlobalTimeDomainPropsBuilder:
    """Builder for CanGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanGlobalTimeDomainProps = CanGlobalTimeDomainProps()

    def build(self) -> CanGlobalTimeDomainProps:
        """Build and return CanGlobalTimeDomainProps object.

        Returns:
            CanGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
