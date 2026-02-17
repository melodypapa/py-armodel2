"""RtePluginProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 971)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class RtePluginProps(ARObject):
    """AUTOSAR RtePluginProps."""

    def __init__(self) -> None:
        """Initialize RtePluginProps."""
        super().__init__()
        self.associated: Optional[EcucContainerValue] = None
        self.associated_rte: Optional[EcucContainerValue] = None


class RtePluginPropsBuilder:
    """Builder for RtePluginProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RtePluginProps = RtePluginProps()

    def build(self) -> RtePluginProps:
        """Build and return RtePluginProps object.

        Returns:
            RtePluginProps instance
        """
        # TODO: Add validation
        return self._obj
