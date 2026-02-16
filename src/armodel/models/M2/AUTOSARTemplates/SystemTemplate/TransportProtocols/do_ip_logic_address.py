"""DoIpLogicAddress AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.abstract_do_ip_logic_address_props import (
    AbstractDoIpLogicAddressProps,
)


class DoIpLogicAddress(Identifiable):
    """AUTOSAR DoIpLogicAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "address": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # address
        "do_ip_logic": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AbstractDoIpLogicAddressProps,
        ),  # doIpLogic
    }

    def __init__(self) -> None:
        """Initialize DoIpLogicAddress."""
        super().__init__()
        self.address: Optional[Integer] = None
        self.do_ip_logic: Optional[AbstractDoIpLogicAddressProps] = None


class DoIpLogicAddressBuilder:
    """Builder for DoIpLogicAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpLogicAddress = DoIpLogicAddress()

    def build(self) -> DoIpLogicAddress:
        """Build and return DoIpLogicAddress object.

        Returns:
            DoIpLogicAddress instance
        """
        # TODO: Add validation
        return self._obj
