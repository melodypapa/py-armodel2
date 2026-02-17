"""EcucForeignReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_abstract_external_reference_def import (
    EcucAbstractExternalReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class EcucForeignReferenceDef(EcucAbstractExternalReferenceDef):
    """AUTOSAR EcucForeignReferenceDef."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "destination_type": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # destinationType
    }

    def __init__(self) -> None:
        """Initialize EcucForeignReferenceDef."""
        super().__init__()
        self.destination_type: Optional[String] = None


class EcucForeignReferenceDefBuilder:
    """Builder for EcucForeignReferenceDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucForeignReferenceDef = EcucForeignReferenceDef()

    def build(self) -> EcucForeignReferenceDef:
        """Build and return EcucForeignReferenceDef object.

        Returns:
            EcucForeignReferenceDef instance
        """
        # TODO: Add validation
        return self._obj
