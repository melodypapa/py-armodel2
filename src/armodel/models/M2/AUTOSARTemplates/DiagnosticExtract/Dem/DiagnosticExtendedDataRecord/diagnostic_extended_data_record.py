"""DiagnosticExtendedDataRecord AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 190)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticExtendedDataRecord.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticFreezeFrame import (
    DiagnosticRecordTriggerEnum,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_trigger: Optional[String]
    record_elements: list[DiagnosticParameter]
    record_number: Optional[PositiveInteger]
    trigger: Optional[DiagnosticRecordTriggerEnum]
    update: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticExtendedDataRecord."""
        super().__init__()
        self.custom_trigger: Optional[String] = None
        self.record_elements: list[DiagnosticParameter] = []
        self.record_number: Optional[PositiveInteger] = None
        self.trigger: Optional[DiagnosticRecordTriggerEnum] = None
        self.update: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticExtendedDataRecord":
        """Deserialize XML element to DiagnosticExtendedDataRecord object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticExtendedDataRecord object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse custom_trigger
        child = ARObject._find_child_element(element, "CUSTOM-TRIGGER")
        if child is not None:
            custom_trigger_value = child.text
            obj.custom_trigger = custom_trigger_value

        # Parse record_elements (list)
        obj.record_elements = []
        for child in ARObject._find_all_child_elements(element, "RECORD-ELEMENTS"):
            record_elements_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.record_elements.append(record_elements_value)

        # Parse record_number
        child = ARObject._find_child_element(element, "RECORD-NUMBER")
        if child is not None:
            record_number_value = child.text
            obj.record_number = record_number_value

        # Parse trigger
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_value = child.text
            obj.trigger = trigger_value

        # Parse update
        child = ARObject._find_child_element(element, "UPDATE")
        if child is not None:
            update_value = child.text
            obj.update = update_value

        return obj



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
