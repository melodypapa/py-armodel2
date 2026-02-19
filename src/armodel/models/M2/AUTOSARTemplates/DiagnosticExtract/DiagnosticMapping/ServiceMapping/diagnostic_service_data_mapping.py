"""DiagnosticServiceDataMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 228)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_data_element import (
    DiagnosticDataElement,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticServiceDataMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceDataMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_data: Optional[DiagnosticDataElement]
    diagnostic: Optional[DiagnosticParameter]
    mapped_data_ref: Optional[ARRef]
    parameter: Optional[DiagnosticParameter]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceDataMapping."""
        super().__init__()
        self.diagnostic_data: Optional[DiagnosticDataElement] = None
        self.diagnostic: Optional[DiagnosticParameter] = None
        self.mapped_data_ref: Optional[ARRef] = None
        self.parameter: Optional[DiagnosticParameter] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceDataMapping":
        """Deserialize XML element to DiagnosticServiceDataMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceDataMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceDataMapping, cls).deserialize(element)

        # Parse diagnostic_data
        child = ARObject._find_child_element(element, "DIAGNOSTIC-DATA")
        if child is not None:
            diagnostic_data_value = ARObject._deserialize_by_tag(child, "DiagnosticDataElement")
            obj.diagnostic_data = diagnostic_data_value

        # Parse diagnostic
        child = ARObject._find_child_element(element, "DIAGNOSTIC")
        if child is not None:
            diagnostic_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.diagnostic = diagnostic_value

        # Parse mapped_data_ref
        child = ARObject._find_child_element(element, "MAPPED-DATA")
        if child is not None:
            mapped_data_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.mapped_data_ref = mapped_data_ref_value

        # Parse parameter
        child = ARObject._find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.parameter = parameter_value

        return obj



class DiagnosticServiceDataMappingBuilder:
    """Builder for DiagnosticServiceDataMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceDataMapping = DiagnosticServiceDataMapping()

    def build(self) -> DiagnosticServiceDataMapping:
        """Build and return DiagnosticServiceDataMapping object.

        Returns:
            DiagnosticServiceDataMapping instance
        """
        # TODO: Add validation
        return self._obj
