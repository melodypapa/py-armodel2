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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    pid_ref: Optional[ARRef]
    request_current_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticRequestCurrentPowertrainData."""
        super().__init__()
        self.pid_ref: Optional[ARRef] = None
        self.request_current_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRequestCurrentPowertrainData to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRequestCurrentPowertrainData, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pid_ref
        if self.pid_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pid_ref, "DiagnosticParameter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PID-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize request_current_ref
        if self.request_current_ref is not None:
            serialized = SerializationHelper.serialize_item(self.request_current_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUEST-CURRENT-REF")
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

        # Parse pid_ref
        child = SerializationHelper.find_child_element(element, "PID-REF")
        if child is not None:
            pid_ref_value = ARRef.deserialize(child)
            obj.pid_ref = pid_ref_value

        # Parse request_current_ref
        child = SerializationHelper.find_child_element(element, "REQUEST-CURRENT-REF")
        if child is not None:
            request_current_ref_value = ARRef.deserialize(child)
            obj.request_current_ref = request_current_ref_value

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
