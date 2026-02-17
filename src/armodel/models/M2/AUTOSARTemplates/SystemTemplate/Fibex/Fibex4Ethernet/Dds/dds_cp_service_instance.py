"""DdsCpServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 472)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_topic import (
    DdsCpTopic,
)


class DdsCpServiceInstance(AbstractServiceInstance):
    """AUTOSAR DdsCpServiceInstance."""
    """Abstract base class - do not instantiate directly."""

    def __init__(self) -> None:
        """Initialize DdsCpServiceInstance."""
        super().__init__()
        self.dds_field_reply: Optional[DdsCpTopic] = None
        self.dds_field: Optional[DdsCpTopic] = None
        self.dds_method: Optional[DdsCpTopic] = None
        self.dds_service_qos: Optional[DdsCpQosProfile] = None
        self.service_instance: Optional[PositiveInteger] = None
        self.service_interface: Optional[String] = None


class DdsCpServiceInstanceBuilder:
    """Builder for DdsCpServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpServiceInstance = DdsCpServiceInstance()

    def build(self) -> DdsCpServiceInstance:
        """Build and return DdsCpServiceInstance object.

        Returns:
            DdsCpServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
