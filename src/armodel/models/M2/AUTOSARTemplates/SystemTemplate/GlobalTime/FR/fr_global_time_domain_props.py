"""FrGlobalTimeDomainProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 878)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_FR.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.abstract_global_time_domain_props import (
    AbstractGlobalTimeDomainProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class FrGlobalTimeDomainProps(AbstractGlobalTimeDomainProps):
    """AUTOSAR FrGlobalTimeDomainProps."""

    ofs_data_id_list: PositiveInteger
    sync_data_id_list: PositiveInteger
    def __init__(self) -> None:
        """Initialize FrGlobalTimeDomainProps."""
        super().__init__()
        self.ofs_data_id_list: PositiveInteger = None
        self.sync_data_id_list: PositiveInteger = None


class FrGlobalTimeDomainPropsBuilder:
    """Builder for FrGlobalTimeDomainProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FrGlobalTimeDomainProps = FrGlobalTimeDomainProps()

    def build(self) -> FrGlobalTimeDomainProps:
        """Build and return FrGlobalTimeDomainProps object.

        Returns:
            FrGlobalTimeDomainProps instance
        """
        # TODO: Add validation
        return self._obj
