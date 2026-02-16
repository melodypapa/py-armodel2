"""DiagnosticExtendedDataRecord AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticExtendedDataRecord(DiagnosticCommonElement):
    """AUTOSAR DiagnosticExtendedDataRecord."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "custom_trigger": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # customTrigger
        "record_elements": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DiagnosticParameter,
        ),  # recordElements
        "record_number": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # recordNumber
        "trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticRecordTriggerEnum,
        ),  # trigger
        "update": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # update
    }

    def __init__(self) -> None:
        """Initialize DiagnosticExtendedDataRecord."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_elements: list[DiagnosticParameter] = []
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None


class DiagnosticExtendedDataRecordBuilder:
    """Builder for DiagnosticExtendedDataRecord."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticExtendedDataRecord = DiagnosticExtendedDataRecord()

    def build(self) -> DiagnosticExtendedDataRecord:
        """Build and return DiagnosticExtendedDataRecord object.

        Returns:
            DiagnosticExtendedDataRecord instance
        """
        # TODO: Add validation
        return self._obj
