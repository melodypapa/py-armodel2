"""IdsmSignatureSupportCp AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)


class IdsmSignatureSupportCp(ARObject):
    """AUTOSAR IdsmSignatureSupportCp."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "authentication": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServicePrimitive,
        ),  # authentication
        "crypto_service_key": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServiceKey,
        ),  # cryptoServiceKey
    }

    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportCp."""
        super().__init__()
        self.authentication: Optional[CryptoServicePrimitive] = None
        self.crypto_service_key: Optional[CryptoServiceKey] = None


class IdsmSignatureSupportCpBuilder:
    """Builder for IdsmSignatureSupportCp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmSignatureSupportCp = IdsmSignatureSupportCp()

    def build(self) -> IdsmSignatureSupportCp:
        """Build and return IdsmSignatureSupportCp object.

        Returns:
            IdsmSignatureSupportCp instance
        """
        # TODO: Add validation
        return self._obj
