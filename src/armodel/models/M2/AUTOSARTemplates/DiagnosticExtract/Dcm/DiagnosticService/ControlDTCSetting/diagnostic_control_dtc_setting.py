"""DiagnosticControlDTCSetting AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ControlDTCSetting.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticControlDTCSetting(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticControlDTCSetting."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dtc_setting_class: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticControlDTCSetting."""
        super().__init__()
        self.dtc_setting_class: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticControlDTCSetting":
        """Deserialize XML element to DiagnosticControlDTCSetting object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticControlDTCSetting object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dtc_setting_class
        child = ARObject._find_child_element(element, "DTC-SETTING-CLASS")
        if child is not None:
            dtc_setting_class_value = child.text
            obj.dtc_setting_class = dtc_setting_class_value

        return obj



class DiagnosticControlDTCSettingBuilder:
    """Builder for DiagnosticControlDTCSetting."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticControlDTCSetting = DiagnosticControlDTCSetting()

    def build(self) -> DiagnosticControlDTCSetting:
        """Build and return DiagnosticControlDTCSetting object.

        Returns:
            DiagnosticControlDTCSetting instance
        """
        # TODO: Add validation
        return self._obj
