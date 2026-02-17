"""TpAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 588)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class TpAddress(Identifiable):
    """AUTOSAR TpAddress."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "tp_address": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # tpAddress
    }

    def __init__(self) -> None:
        """Initialize TpAddress."""
        super().__init__()
        self.tp_address: Optional[Integer] = None


class TpAddressBuilder:
    """Builder for TpAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TpAddress = TpAddress()

    def build(self) -> TpAddress:
        """Build and return TpAddress object.

        Returns:
            TpAddress instance
        """
        # TODO: Add validation
        return self._obj
