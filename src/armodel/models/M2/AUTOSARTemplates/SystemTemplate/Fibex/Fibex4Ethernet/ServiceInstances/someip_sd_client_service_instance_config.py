"""SomeipSdClientServiceInstanceConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2058)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.initial_sd_delay_config import (
    InitialSdDelayConfig,
)


class SomeipSdClientServiceInstanceConfig(ARElement):
    """AUTOSAR SomeipSdClientServiceInstanceConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "initial_find_behavior": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=InitialSdDelayConfig,
        ),  # initialFindBehavior
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
        "service_find": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # serviceFind
    }

    def __init__(self) -> None:
        """Initialize SomeipSdClientServiceInstanceConfig."""
        super().__init__()
        self.initial_find_behavior: Optional[InitialSdDelayConfig] = None
        self.priority: Optional[PositiveInteger] = None
        self.service_find: Optional[PositiveInteger] = None


class SomeipSdClientServiceInstanceConfigBuilder:
    """Builder for SomeipSdClientServiceInstanceConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipSdClientServiceInstanceConfig = SomeipSdClientServiceInstanceConfig()

    def build(self) -> SomeipSdClientServiceInstanceConfig:
        """Build and return SomeipSdClientServiceInstanceConfig object.

        Returns:
            SomeipSdClientServiceInstanceConfig instance
        """
        # TODO: Add validation
        return self._obj
