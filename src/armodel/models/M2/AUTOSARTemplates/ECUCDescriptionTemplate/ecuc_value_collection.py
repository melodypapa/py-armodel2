"""EcucValueCollection AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.system import (
    System,
)


class EcucValueCollection(ARElement):
    """AUTOSAR EcucValueCollection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ecuc_values": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EcucModule),
        ),  # ecucValues
        "ecu_extract": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=System,
        ),  # ecuExtract
    }

    def __init__(self) -> None:
        """Initialize EcucValueCollection."""
        super().__init__()
        self.ecuc_values: list[Any] = []
        self.ecu_extract: Optional[System] = None


class EcucValueCollectionBuilder:
    """Builder for EcucValueCollection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucValueCollection = EcucValueCollection()

    def build(self) -> EcucValueCollection:
        """Build and return EcucValueCollection object.

        Returns:
            EcucValueCollection instance
        """
        # TODO: Add validation
        return self._obj
