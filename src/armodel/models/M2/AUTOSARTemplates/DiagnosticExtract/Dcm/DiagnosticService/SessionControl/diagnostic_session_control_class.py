"""DiagnosticSessionControlClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 93)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_SessionControl.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class DiagnosticSessionControlClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticSessionControlClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    s3_server: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize DiagnosticSessionControlClass."""
        super().__init__()
        self.s3_server: Optional[TimeValue] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticSessionControlClass":
        """Deserialize XML element to DiagnosticSessionControlClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticSessionControlClass object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse s3_server
        child = ARObject._find_child_element(element, "S3-SERVER")
        if child is not None:
            s3_server_value = child.text
            obj.s3_server = s3_server_value

        return obj



class DiagnosticSessionControlClassBuilder:
    """Builder for DiagnosticSessionControlClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticSessionControlClass = DiagnosticSessionControlClass()

    def build(self) -> DiagnosticSessionControlClass:
        """Build and return DiagnosticSessionControlClass object.

        Returns:
            DiagnosticSessionControlClass instance
        """
        # TODO: Add validation
        return self._obj
