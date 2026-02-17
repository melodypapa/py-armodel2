"""IPSecConfigProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 572)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ah_cipher_suites": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # ahCipherSuites
        "dpd_action": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IPsecDpdActionEnum,
        ),  # dpdAction
        "dpd_delay": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dpdDelay
        "esp_cipher_suites": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # espCipherSuites
        "ike_cipher_suite": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ikeCipherSuite
        "ike_over_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ikeOverTime
        "ike_rand_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ikeRandTime
        "ike_reauth_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ikeReauthTime
        "ike_rekey_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # ikeRekeyTime
        "sa_over_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # saOverTime
        "sa_rand_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # saRandTime
        "sa_rekey_time": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # saRekeyTime
    }

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
