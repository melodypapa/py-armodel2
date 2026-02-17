"""InitialSdDelayConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 514)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class InitialSdDelayConfig(ARObject):
    """AUTOSAR InitialSdDelayConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "initial_delay_max": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initialDelayMax
        "initial_delay_min": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initialDelayMin
        "initial": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # initial
    }

    def __init__(self) -> None:
        """Initialize InitialSdDelayConfig."""
        super().__init__()
        self.initial_delay_max: Optional[TimeValue] = None
        self.initial_delay_min: Optional[TimeValue] = None
        self.initial: Optional[PositiveInteger] = None


class InitialSdDelayConfigBuilder:
    """Builder for InitialSdDelayConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InitialSdDelayConfig = InitialSdDelayConfig()

    def build(self) -> InitialSdDelayConfig:
        """Build and return InitialSdDelayConfig object.

        Returns:
            InitialSdDelayConfig instance
        """
        # TODO: Add validation
        return self._obj
