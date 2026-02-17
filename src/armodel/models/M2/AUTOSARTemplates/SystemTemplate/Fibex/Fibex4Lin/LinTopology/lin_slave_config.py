"""LinSlaveConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
    LinConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
    LinOrderedConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config_ident import (
    LinSlaveConfigIdent,
)


class LinSlaveConfig(ARObject):
    """AUTOSAR LinSlaveConfig."""

    configured_nad: Optional[Integer]
    function_id: Optional[PositiveInteger]
    ident: Optional[LinSlaveConfigIdent]
    initial_nad: Optional[Integer]
    lin_configurable_frames: list[LinConfigurableFrame]
    lin_error_response: Optional[LinErrorResponse]
    lin_ordereds: list[LinOrderedConfigurableFrame]
    protocol_version: Optional[String]
    supplier_id: Optional[PositiveInteger]
    variant_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize LinSlaveConfig."""
        super().__init__()
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.ident: Optional[LinSlaveConfigIdent] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.protocol_version: Optional[String] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None


class LinSlaveConfigBuilder:
    """Builder for LinSlaveConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSlaveConfig = LinSlaveConfig()

    def build(self) -> LinSlaveConfig:
        """Build and return LinSlaveConfig object.

        Returns:
            LinSlaveConfig instance
        """
        # TODO: Add validation
        return self._obj
