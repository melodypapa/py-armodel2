"""CryptoServiceKey AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.value_specification import (
    ValueSpecification,
)


class CryptoServiceKey(ARElement):
    """AUTOSAR CryptoServiceKey."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "algorithm_family": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # algorithmFamily
        "development": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValueSpecification,
        ),  # development
        "key_generation": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CryptoServiceKey,
        ),  # keyGeneration
        "key_storage_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # keyStorageType
        "length": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # length
    }

    def __init__(self) -> None:
        """Initialize CryptoServiceKey."""
        super().__init__()
        self.algorithm_family: Optional[String] = None
        self.development: Optional[ValueSpecification] = None
        self.key_generation: Optional[CryptoServiceKey] = None
        self.key_storage_type: Optional[String] = None
        self.length: Optional[PositiveInteger] = None


class CryptoServiceKeyBuilder:
    """Builder for CryptoServiceKey."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoServiceKey = CryptoServiceKey()

    def build(self) -> CryptoServiceKey:
        """Build and return CryptoServiceKey object.

        Returns:
            CryptoServiceKey instance
        """
        # TODO: Add validation
        return self._obj
