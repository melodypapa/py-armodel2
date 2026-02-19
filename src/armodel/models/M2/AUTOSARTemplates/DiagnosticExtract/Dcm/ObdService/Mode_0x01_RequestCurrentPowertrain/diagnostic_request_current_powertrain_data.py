"""DiagnosticRequestCurrentPowertrainData AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 150)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_ObdService_Mode_0x01_RequestCurrentPowertrain.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_parameter import (
    DiagnosticParameter,
)


class DiagnosticRequestCurrentPowertrainData(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticRequestCurrentPowertrainData."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pid: Optional[DiagnosticParameter]
    request_current: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainData."""
        super().__init__()
        self.pid: Optional[DiagnosticParameter] = None
        self.request_current: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestCurrentPowertrainData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestCurrentPowertrainData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pid
        if self.pid is not None:
            serialized = ARObject._serialize_item(self.pid, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_current
        if self.request_current is not None:
            serialized = ARObject._serialize_item(self.request_current, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-CURRENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRequestCurrentPowertrainData":
        """Deserialize XML element to DiagnosticRequestCurrentPowertrainData object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRequestCurrentPowertrainData object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRequestCurrentPowertrainData, cls).deserialize(element)

        # Parse pid
        child = ARObject._find_child_element(element, "PID")
        if child is not None:
            pid_value = ARObject._deserialize_by_tag(child, "DiagnosticParameter")
            obj.pid = pid_value

        # Parse request_current
        child = ARObject._find_child_element(element, "REQUEST-CURRENT")
        if child is not None:
            request_current_value = child.text
            obj.request_current = request_current_value

        return obj



class DiagnosticRequestCurrentPowertrainDataBuilder:
    """Builder for DiagnosticRequestCurrentPowertrainData."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRequestCurrentPowertrainData = DiagnosticRequestCurrentPowertrainData()

    def build(self) -> DiagnosticRequestCurrentPowertrainData:
        """Build and return DiagnosticRequestCurrentPowertrainData object.

        Returns:
            DiagnosticRequestCurrentPowertrainData instance
        """
        # TODO: Add validation
        return self._obj
