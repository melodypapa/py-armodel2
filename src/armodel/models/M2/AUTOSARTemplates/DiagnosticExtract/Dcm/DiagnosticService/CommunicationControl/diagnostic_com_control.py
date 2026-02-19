"""DiagnosticComControl AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 108)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommunicationControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticComControl(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticComControl."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    com_control: Optional[DiagnosticComControl]
    custom_sub: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticComControl."""
        super().__init__()
        self.com_control: Optional[DiagnosticComControl] = None
        self.custom_sub: Optional[PositiveInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComControl":
        """Deserialize XML element to DiagnosticComControl object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComControl object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse com_control
        child = ARObject._find_child_element(element, "COM-CONTROL")
        if child is not None:
            com_control_value = ARObject._deserialize_by_tag(child, "DiagnosticComControl")
            obj.com_control = com_control_value

        # Parse custom_sub
        child = ARObject._find_child_element(element, "CUSTOM-SUB")
        if child is not None:
            custom_sub_value = child.text
            obj.custom_sub = custom_sub_value

        return obj



class DiagnosticComControlBuilder:
    """Builder for DiagnosticComControl."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComControl = DiagnosticComControl()

    def build(self) -> DiagnosticComControl:
        """Build and return DiagnosticComControl object.

        Returns:
            DiagnosticComControl instance
        """
        # TODO: Add validation
        return self._obj
