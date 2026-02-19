"""DiagnosticControlDTCSettingClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ControlDTCSetting.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class DiagnosticControlDTCSettingClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticControlDTCSettingClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    control_option: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize DiagnosticControlDTCSettingClass."""
        super().__init__()
        self.control_option: Optional[Boolean] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlDTCSettingClass":
        """Deserialize XML element to DiagnosticControlDTCSettingClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticControlDTCSettingClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticControlDTCSettingClass, cls).deserialize(element)

        # Parse control_option
        child = ARObject._find_child_element(element, "CONTROL-OPTION")
        if child is not None:
            control_option_value = child.text
            obj.control_option = control_option_value

        return obj



class DiagnosticControlDTCSettingClassBuilder:
    """Builder for DiagnosticControlDTCSettingClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlDTCSettingClass = DiagnosticControlDTCSettingClass()

    def build(self) -> DiagnosticControlDTCSettingClass:
        """Build and return DiagnosticControlDTCSettingClass object.

        Returns:
            DiagnosticControlDTCSettingClass instance
        """
        # TODO: Add validation
        return self._obj
