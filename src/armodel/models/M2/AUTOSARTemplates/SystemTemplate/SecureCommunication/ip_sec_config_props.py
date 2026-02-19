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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecConfigProps":
        """Deserialize XML element to IPSecConfigProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IPSecConfigProps object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ah_cipher_suites (list)
        obj.ah_cipher_suites = []
        for child in ARObject._find_all_child_elements(element, "AH-CIPHER-SUITES"):
            ah_cipher_suites_value = child.text
            obj.ah_cipher_suites.append(ah_cipher_suites_value)

        # Parse dpd_action
        child = ARObject._find_child_element(element, "DPD-ACTION")
        if child is not None:
            dpd_action_value = child.text
            obj.dpd_action = dpd_action_value

        # Parse dpd_delay
        child = ARObject._find_child_element(element, "DPD-DELAY")
        if child is not None:
            dpd_delay_value = child.text
            obj.dpd_delay = dpd_delay_value

        # Parse esp_cipher_suites (list)
        obj.esp_cipher_suites = []
        for child in ARObject._find_all_child_elements(element, "ESP-CIPHER-SUITES"):
            esp_cipher_suites_value = child.text
            obj.esp_cipher_suites.append(esp_cipher_suites_value)

        # Parse ike_cipher_suite
        child = ARObject._find_child_element(element, "IKE-CIPHER-SUITE")
        if child is not None:
            ike_cipher_suite_value = child.text
            obj.ike_cipher_suite = ike_cipher_suite_value

        # Parse ike_over_time
        child = ARObject._find_child_element(element, "IKE-OVER-TIME")
        if child is not None:
            ike_over_time_value = child.text
            obj.ike_over_time = ike_over_time_value

        # Parse ike_rand_time
        child = ARObject._find_child_element(element, "IKE-RAND-TIME")
        if child is not None:
            ike_rand_time_value = child.text
            obj.ike_rand_time = ike_rand_time_value

        # Parse ike_reauth_time
        child = ARObject._find_child_element(element, "IKE-REAUTH-TIME")
        if child is not None:
            ike_reauth_time_value = child.text
            obj.ike_reauth_time = ike_reauth_time_value

        # Parse ike_rekey_time
        child = ARObject._find_child_element(element, "IKE-REKEY-TIME")
        if child is not None:
            ike_rekey_time_value = child.text
            obj.ike_rekey_time = ike_rekey_time_value

        # Parse sa_over_time
        child = ARObject._find_child_element(element, "SA-OVER-TIME")
        if child is not None:
            sa_over_time_value = child.text
            obj.sa_over_time = sa_over_time_value

        # Parse sa_rand_time
        child = ARObject._find_child_element(element, "SA-RAND-TIME")
        if child is not None:
            sa_rand_time_value = child.text
            obj.sa_rand_time = sa_rand_time_value

        # Parse sa_rekey_time
        child = ARObject._find_child_element(element, "SA-REKEY-TIME")
        if child is not None:
            sa_rekey_time_value = child.text
            obj.sa_rekey_time = sa_rekey_time_value

        return obj



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
