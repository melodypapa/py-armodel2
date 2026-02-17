"""ReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 170)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)


class ReceiverComSpec(RPortComSpec):
    """AUTOSAR ReceiverComSpec."""
    """Abstract base class - do not instantiate directly."""

    composite_networks: list[CompositeNetworkRepresentation]
    data_element: Optional[AutosarDataPrototype]
    handle_out_of_range: Optional[Any]
    max_delta: Optional[PositiveInteger]
    sync_counter_init: Optional[PositiveInteger]
    transformation_coms: list[Any]
    uses_end_to_end: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ReceiverComSpec."""
        super().__init__()
        self.composite_networks: list[CompositeNetworkRepresentation] = []
        self.data_element: Optional[AutosarDataPrototype] = None
        self.handle_out_of_range: Optional[Any] = None
        self.max_delta: Optional[PositiveInteger] = None
        self.sync_counter_init: Optional[PositiveInteger] = None
        self.transformation_coms: list[Any] = []
        self.uses_end_to_end: Optional[Boolean] = None


class ReceiverComSpecBuilder:
    """Builder for ReceiverComSpec."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ReceiverComSpec = ReceiverComSpec()

    def build(self) -> ReceiverComSpec:
        """Build and return ReceiverComSpec object.

        Returns:
            ReceiverComSpec instance
        """
        # TODO: Add validation
        return self._obj
