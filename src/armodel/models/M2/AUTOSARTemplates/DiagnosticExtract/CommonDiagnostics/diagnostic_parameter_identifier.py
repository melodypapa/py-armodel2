"""DiagnosticParameterIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 149)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_support_info_byte import (
    DiagnosticSupportInfoByte,
)


class DiagnosticParameterIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticParameterIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_elements: list[DiagnosticParameter]
    id: Optional[PositiveInteger]
    pid_size: Optional[PositiveInteger]
    support_info_byte: Optional[DiagnosticSupportInfoByte]
    def __init__(self) -> None:
        """Initialize DiagnosticParameterIdentifier."""
        super().__init__()
        self.data_elements: list[DiagnosticParameter] = []
        self.id: Optional[PositiveInteger] = None
        self.pid_size: Optional[PositiveInteger] = None
        self.support_info_byte: Optional[DiagnosticSupportInfoByte] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticParameterIdentifier":
        """Deserialize XML element to DiagnosticParameterIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticParameterIdentifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse data_elements (list)
        obj.data_elements = []
        for child in ARObject._find_all_child_elements(element, "DATA-ELEMENTS"):
            data_elements_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.data_elements.append(data_elements_value)

        # Parse id
        child = ARObject._find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse pid_size
        child = ARObject._find_child_element(element, "PID-SIZE")
        if child is not None:
            pid_size_value = child.text
            obj.pid_size = pid_size_value

        # Parse support_info_byte
        child = ARObject._find_child_element(element, "SUPPORT-INFO-BYTE")
        if child is not None:
            support_info_byte_value = ARObject._deserialize_by_tag(child, "DiagnosticSupportInfoByte")
            obj.support_info_byte = support_info_byte_value

        return obj



class DiagnosticParameterIdentifierBuilder:
    """Builder for DiagnosticParameterIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticParameterIdentifier = DiagnosticParameterIdentifier()

    def build(self) -> DiagnosticParameterIdentifier:
        """Build and return DiagnosticParameterIdentifier object.

        Returns:
            DiagnosticParameterIdentifier instance
        """
        # TODO: Add validation
        return self._obj
