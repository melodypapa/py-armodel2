"""DiagnosticFreezeFrame AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 192)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticFreezeFrame.classes.json"""

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


class DiagnosticFreezeFrame(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFreezeFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "custom_trigger": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # customTrigger
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
        """Initialize DiagnosticFreezeFrame."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None


class DiagnosticFreezeFrameBuilder:
    """Builder for DiagnosticFreezeFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFreezeFrame = DiagnosticFreezeFrame()

    def build(self) -> DiagnosticFreezeFrame:
        """Build and return DiagnosticFreezeFrame object.

        Returns:
            DiagnosticFreezeFrame instance
        """
        # TODO: Add validation
        return self._obj
