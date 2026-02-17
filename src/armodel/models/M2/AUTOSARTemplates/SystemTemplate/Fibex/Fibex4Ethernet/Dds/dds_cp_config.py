"""DdsCpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 525)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_domain import (
    DdsCpDomain,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)


class DdsCpConfig(ARElement):
    """AUTOSAR DdsCpConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dds_domains": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DdsCpDomain,
        ),  # ddsDomains
        "dds_qos_profiles": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DdsCpQosProfile,
        ),  # ddsQosProfiles
    }

    def __init__(self) -> None:
        """Initialize DdsCpConfig."""
        super().__init__()
        self.dds_domains: list[DdsCpDomain] = []
        self.dds_qos_profiles: list[DdsCpQosProfile] = []


class DdsCpConfigBuilder:
    """Builder for DdsCpConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsCpConfig = DdsCpConfig()

    def build(self) -> DdsCpConfig:
        """Build and return DdsCpConfig object.

        Returns:
            DdsCpConfig instance
        """
        # TODO: Add validation
        return self._obj
