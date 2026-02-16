"""IPSecConfigProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
    TimeValue,
)


class IPSecConfigProps(ARElement):
    """AUTOSAR IPSecConfigProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ah_cipher_suites", None, False, True, None),  # ahCipherSuites
        ("dpd_action", None, False, False, IPsecDpdActionEnum),  # dpdAction
        ("dpd_delay", None, True, False, None),  # dpdDelay
        ("esp_cipher_suites", None, False, True, None),  # espCipherSuites
        ("ike_cipher_suite", None, True, False, None),  # ikeCipherSuite
        ("ike_over_time", None, True, False, None),  # ikeOverTime
        ("ike_rand_time", None, True, False, None),  # ikeRandTime
        ("ike_reauth_time", None, True, False, None),  # ikeReauthTime
        ("ike_rekey_time", None, True, False, None),  # ikeRekeyTime
        ("sa_over_time", None, True, False, None),  # saOverTime
        ("sa_rand_time", None, True, False, None),  # saRandTime
        ("sa_rekey_time", None, True, False, None),  # saRekeyTime
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IPSecConfigProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IPSecConfigProps":
        """Create IPSecConfigProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IPSecConfigProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IPSecConfigProps since parent returns ARObject
        return cast("IPSecConfigProps", obj)


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
