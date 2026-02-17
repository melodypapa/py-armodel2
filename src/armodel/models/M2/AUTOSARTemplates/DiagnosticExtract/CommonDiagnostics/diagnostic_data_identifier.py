"""DiagnosticDataIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 33)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_abstract_data_identifier import (
    DiagnosticAbstractDataIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_support_info_byte import (
    DiagnosticSupportInfoByte,
)


class DiagnosticDataIdentifier(DiagnosticAbstractDataIdentifier):
    """AUTOSAR DiagnosticDataIdentifier."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # dataElements
        "did_size": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # didSize
        "represents_vin": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # representsVin
        "support_info_byte": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticSupportInfoByte,
        ),  # supportInfoByte
    }

    def __init__(self) -> None:
        """Initialize DiagnosticDataIdentifier."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.did_size: Optional[PositiveInteger] = None
        self.represents_vin: Optional[Boolean] = None
        self.support_info_byte: Optional[DiagnosticSupportInfoByte] = None


class DiagnosticDataIdentifierBuilder:
    """Builder for DiagnosticDataIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticDataIdentifier = DiagnosticDataIdentifier()

    def build(self) -> DiagnosticDataIdentifier:
        """Build and return DiagnosticDataIdentifier object.

        Returns:
            DiagnosticDataIdentifier instance
        """
        # TODO: Add validation
        return self._obj
