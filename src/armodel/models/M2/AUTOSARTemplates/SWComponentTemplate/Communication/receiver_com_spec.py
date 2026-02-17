"""ReceiverComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 170)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "composite_networks": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=CompositeNetworkRepresentation,
        ),  # compositeNetworks
        "data_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AutosarDataPrototype,
        ),  # dataElement
        "handle_out_of_range": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (HandleOutOfRange),
        ),  # handleOutOfRange
        "max_delta": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxDelta
        "sync_counter_init": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # syncCounterInit
        "transformation_coms": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (TransformationCom),
        ),  # transformationComs
        "uses_end_to_end": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # usesEndToEnd
    }

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
