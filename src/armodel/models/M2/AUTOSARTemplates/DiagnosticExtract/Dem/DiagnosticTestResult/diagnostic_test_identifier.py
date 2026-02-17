"""DiagnosticTestIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 205)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticTestIdentifier(ARObject):
    """AUTOSAR DiagnosticTestIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # id
        "uas_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # uasId
    }

    def __init__(self) -> None:
        """Initialize DiagnosticTestIdentifier."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.uas_id: Optional[PositiveInteger] = None


class DiagnosticTestIdentifierBuilder:
    """Builder for DiagnosticTestIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticTestIdentifier = DiagnosticTestIdentifier()

    def build(self) -> DiagnosticTestIdentifier:
        """Build and return DiagnosticTestIdentifier object.

        Returns:
            DiagnosticTestIdentifier instance
        """
        # TODO: Add validation
        return self._obj
