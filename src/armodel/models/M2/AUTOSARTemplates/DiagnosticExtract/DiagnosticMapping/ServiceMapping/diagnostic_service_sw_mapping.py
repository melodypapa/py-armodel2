"""DiagnosticServiceSwMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 238)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
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


class DiagnosticServiceSwMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticServiceSwMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accessed_data_ref: Optional[ARRef]
    diagnostic_data: Optional[DiagnosticDataElement]
    diagnostic: Optional[DiagnosticParameter]
    mapped_bsw: Optional[Any]
    mapped_flat_swc: Optional[Any]
    mapped_swc: Optional[Any]
    parameter: Optional[DiagnosticParameter]
    service_instance: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceSwMapping."""
        super().__init__()
        self.accessed_data_ref: Optional[ARRef] = None
        self.diagnostic_data: Optional[DiagnosticDataElement] = None
        self.diagnostic: Optional[DiagnosticParameter] = None
        self.mapped_bsw: Optional[Any] = None
        self.mapped_flat_swc: Optional[Any] = None
        self.mapped_swc: Optional[Any] = None
        self.parameter: Optional[DiagnosticParameter] = None
        self.service_instance: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceSwMapping":
        """Deserialize XML element to DiagnosticServiceSwMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceSwMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceSwMapping, cls).deserialize(element)

        # Parse accessed_data_ref
        child = ARObject._find_child_element(element, "ACCESSED-DATA")
        if child is not None:
            accessed_data_ref_value = ARObject._deserialize_by_tag(child, "DataPrototype")
            obj.accessed_data_ref = accessed_data_ref_value

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

        # Parse mapped_bsw
        child = ARObject._find_child_element(element, "MAPPED-BSW")
        if child is not None:
            mapped_bsw_value = child.text
            obj.mapped_bsw = mapped_bsw_value

        # Parse mapped_flat_swc
        child = ARObject._find_child_element(element, "MAPPED-FLAT-SWC")
        if child is not None:
            mapped_flat_swc_value = child.text
            obj.mapped_flat_swc = mapped_flat_swc_value

        # Parse mapped_swc
        child = ARObject._find_child_element(element, "MAPPED-SWC")
        if child is not None:
            mapped_swc_value = child.text
            obj.mapped_swc = mapped_swc_value

        # Parse parameter
        child = ARObject._find_child_element(element, "PARAMETER")
        if child is not None:
            parameter_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.parameter = parameter_value

        # Parse service_instance
        child = ARObject._find_child_element(element, "SERVICE-INSTANCE")
        if child is not None:
            service_instance_value = child.text
            obj.service_instance = service_instance_value

        return obj



class DiagnosticServiceSwMappingBuilder:
    """Builder for DiagnosticServiceSwMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceSwMapping = DiagnosticServiceSwMapping()

    def build(self) -> DiagnosticServiceSwMapping:
        """Build and return DiagnosticServiceSwMapping object.

        Returns:
            DiagnosticServiceSwMapping instance
        """
        # TODO: Add validation
        return self._obj
