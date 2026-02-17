"""DiagnosticMemoryDestination AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 181)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticMemoryDestination import (
    DiagnosticMemoryEntryStorageTriggerEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticMemoryDestination(DiagnosticCommonElement):
    """AUTOSAR DiagnosticMemoryDestination."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "aging_requires": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # agingRequires
        "clear_dtc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticClearDtc),
        ),  # clearDtc
        "dtc_status": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # dtcStatus
        "event": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticEvent,
        ),  # event
        "max_number_of": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # maxNumberOf
        "memory_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticMemoryEntryStorageTriggerEnum,
        ),  # memoryEntry
        "status_bit": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # statusBit
        "type_of_freeze": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (DiagnosticTypeOf),
        ),  # typeOfFreeze
    }

    def __init__(self) -> None:
        """Initialize DiagnosticMemoryDestination."""
        super().__init__()
        self.aging_requires: Optional[Boolean] = None
        self.clear_dtc: Optional[Any] = None
        self.dtc_status: Optional[PositiveInteger] = None
        self.event: Optional[DiagnosticEvent] = None
        self.max_number_of: Optional[PositiveInteger] = None
        self.memory_entry: Optional[DiagnosticMemoryEntryStorageTriggerEnum] = None
        self.status_bit: Optional[Boolean] = None
        self.type_of_freeze: Optional[Any] = None


class DiagnosticMemoryDestinationBuilder:
    """Builder for DiagnosticMemoryDestination."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticMemoryDestination = DiagnosticMemoryDestination()

    def build(self) -> DiagnosticMemoryDestination:
        """Build and return DiagnosticMemoryDestination object.

        Returns:
            DiagnosticMemoryDestination instance
        """
        # TODO: Add validation
        return self._obj
