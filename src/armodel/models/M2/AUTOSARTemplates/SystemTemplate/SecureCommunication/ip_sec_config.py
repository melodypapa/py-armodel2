"""IPSecConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 571)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config_props import (
    IPSecConfigProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_rule import (
    IPSecRule,
)


class IPSecConfig(ARObject):
    """AUTOSAR IPSecConfig."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ip_sec_config": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IPSecConfigProps,
        ),  # ipSecConfig
        "ip_sec_rules": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=IPSecRule,
        ),  # ipSecRules
    }

    def __init__(self) -> None:
        """Initialize IPSecConfig."""
        super().__init__()
        self.ip_sec_config: Optional[IPSecConfigProps] = None
        self.ip_sec_rules: list[IPSecRule] = []


class IPSecConfigBuilder:
    """Builder for IPSecConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPSecConfig = IPSecConfig()

    def build(self) -> IPSecConfig:
        """Build and return IPSecConfig object.

        Returns:
            IPSecConfig instance
        """
        # TODO: Add validation
        return self._obj
