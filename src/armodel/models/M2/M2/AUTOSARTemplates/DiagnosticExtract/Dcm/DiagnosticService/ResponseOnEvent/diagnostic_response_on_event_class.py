"""DiagnosticResponseOnEventClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ResponseOnEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)


class DiagnosticResponseOnEventClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticResponseOnEventClass."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "max_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNumberOf
        "max_num": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNum
        "max_supported": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxSupported
        "response_on": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # responseOn
        "store_event": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # storeEvent
    }

    def __init__(self) -> None:
        """Initialize DiagnosticResponseOnEventClass."""
        super().__init__()
        self.max_number_of: Optional[PositiveInteger] = None
        self.max_num: Optional[PositiveInteger] = None
        self.max_supported: Optional[PositiveInteger] = None
        self.response_on: Optional[TimeValue] = None
        self.store_event: Optional[Boolean] = None


class DiagnosticResponseOnEventClassBuilder:
    """Builder for DiagnosticResponseOnEventClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticResponseOnEventClass = DiagnosticResponseOnEventClass()

    def build(self) -> DiagnosticResponseOnEventClass:
        """Build and return DiagnosticResponseOnEventClass object.

        Returns:
            DiagnosticResponseOnEventClass instance
        """
        # TODO: Add validation
        return self._obj
