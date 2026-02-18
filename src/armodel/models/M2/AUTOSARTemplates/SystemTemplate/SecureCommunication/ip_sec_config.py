"""IPSecConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 571)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config_props import (
    IPSecConfigProps,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_rule import (
        IPSecRule,
    )



class IPSecConfig(ARObject):
    """AUTOSAR IPSecConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ip_sec_config: Optional[IPSecConfigProps]
    ip_sec_rules: list[IPSecRule]
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
