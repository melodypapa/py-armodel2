"""EcucUriReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 81)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_internal_reference_def import (
    EcucAbstractInternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)


class EcucUriReferenceDef(EcucAbstractInternalReferenceDef):
    """AUTOSAR EcucUriReferenceDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_uri": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucDestinationUriDef,
        ),  # destinationUri
    }

    def __init__(self) -> None:
        """Initialize EcucUriReferenceDef."""
        super().__init__()
        self.destination_uri: Optional[EcucDestinationUriDef] = None


class EcucUriReferenceDefBuilder:
    """Builder for EcucUriReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucUriReferenceDef = EcucUriReferenceDef()

    def build(self) -> EcucUriReferenceDef:
        """Build and return EcucUriReferenceDef object.

        Returns:
            EcucUriReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
