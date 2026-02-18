"""IPSecConfigProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 572)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    IPsecDpdActionEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)


class IPSecConfigProps(ARElement):
    """AUTOSAR IPSecConfigProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ah_cipher_suites: list[String]
    dpd_action: Optional[IPsecDpdActionEnum]
    dpd_delay: Optional[TimeValue]
    esp_cipher_suites: list[String]
    ike_cipher_suite: Optional[String]
    ike_over_time: Optional[TimeValue]
    ike_rand_time: Optional[PositiveInteger]
    ike_reauth_time: Optional[TimeValue]
    ike_rekey_time: Optional[TimeValue]
    sa_over_time: Optional[PositiveInteger]
    sa_rand_time: Optional[TimeValue]
    sa_rekey_time: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize IPSecConfigProps."""
        super().__init__()
        self.ah_cipher_suites: list[String] = []
        self.dpd_action: Optional[IPsecDpdActionEnum] = None
        self.dpd_delay: Optional[TimeValue] = None
        self.esp_cipher_suites: list[String] = []
        self.ike_cipher_suite: Optional[String] = None
        self.ike_over_time: Optional[TimeValue] = None
        self.ike_rand_time: Optional[PositiveInteger] = None
        self.ike_reauth_time: Optional[TimeValue] = None
        self.ike_rekey_time: Optional[TimeValue] = None
        self.sa_over_time: Optional[PositiveInteger] = None
        self.sa_rand_time: Optional[TimeValue] = None
        self.sa_rekey_time: Optional[TimeValue] = None


class IPSecConfigPropsBuilder:
    """Builder for IPSecConfigProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IPSecConfigProps = IPSecConfigProps()

    def build(self) -> IPSecConfigProps:
        """Build and return IPSecConfigProps object.

        Returns:
            IPSecConfigProps instance
        """
        # TODO: Add validation
        return self._obj
