"""DiagnosticIOControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 118)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_IOControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_identifier import (
    DiagnosticDataIdentifier,
)


class DiagnosticIOControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticIOControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    control_enables: list[Any]
    data_identifier_identifier: Optional[DiagnosticDataIdentifier]
    freeze_current: Optional[Boolean]
    io_control_class: Optional[DiagnosticIOControl]
    reset_to_default: Optional[Boolean]
    short_term: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticIOControl."""
        super().__init__()
        self.control_enables: list[Any] = []
        self.data_identifier_identifier: Optional[DiagnosticDataIdentifier] = None
        self.freeze_current: Optional[Boolean] = None
        self.io_control_class: Optional[DiagnosticIOControl] = None
        self.reset_to_default: Optional[Boolean] = None
        self.short_term: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticIOControl":
        """Deserialize XML element to DiagnosticIOControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticIOControl object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse control_enables (list)
        obj.control_enables = []
        for child in ARObject._find_all_child_elements(element, "CONTROL-ENABLES"):
            control_enables_value = child.text
            obj.control_enables.append(control_enables_value)

        # Parse data_identifier_identifier
        child = ARObject._find_child_element(element, "DATA-IDENTIFIER-IDENTIFIER")
        if child is not None:
            data_identifier_identifier_value = ARObject._deserialize_by_tag(child, "DiagnosticDataIdentifier")
            obj.data_identifier_identifier = data_identifier_identifier_value

        # Parse freeze_current
        child = ARObject._find_child_element(element, "FREEZE-CURRENT")
        if child is not None:
            freeze_current_value = child.text
            obj.freeze_current = freeze_current_value

        # Parse io_control_class
        child = ARObject._find_child_element(element, "IO-CONTROL-CLASS")
        if child is not None:
            io_control_class_value = ARObject._deserialize_by_tag(child, "DiagnosticIOControl")
            obj.io_control_class = io_control_class_value

        # Parse reset_to_default
        child = ARObject._find_child_element(element, "RESET-TO-DEFAULT")
        if child is not None:
            reset_to_default_value = child.text
            obj.reset_to_default = reset_to_default_value

        # Parse short_term
        child = ARObject._find_child_element(element, "SHORT-TERM")
        if child is not None:
            short_term_value = child.text
            obj.short_term = short_term_value

        return obj



class DiagnosticIOControlBuilder:
    """Builder for DiagnosticIOControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticIOControl = DiagnosticIOControl()

    def build(self) -> DiagnosticIOControl:
        """Build and return DiagnosticIOControl object.

        Returns:
            DiagnosticIOControl instance
        """
        # TODO: Add validation
        return self._obj
