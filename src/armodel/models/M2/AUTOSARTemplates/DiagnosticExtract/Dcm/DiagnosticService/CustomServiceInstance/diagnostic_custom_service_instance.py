"""DiagnosticCustomServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 70)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CustomServiceInstance.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_instance import (
    DiagnosticServiceInstance,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticCustomServiceInstance(DiagnosticServiceInstance):
    """AUTOSAR DiagnosticCustomServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_service_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticCustomServiceInstance."""
        super().__init__()
        self.custom_service_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticCustomServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticCustomServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_service_ref
        if self.custom_service_ref is not None:
            serialized = ARObject._serialize_item(self.custom_service_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCustomServiceInstance":
        """Deserialize XML element to DiagnosticCustomServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCustomServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticCustomServiceInstance, cls).deserialize(element)

        # Parse custom_service_ref
        child = ARObject._find_child_element(element, "CUSTOM-SERVICE-REF")
        if child is not None:
            custom_service_ref_value = ARRef.deserialize(child)
            obj.custom_service_ref = custom_service_ref_value

        return obj



class DiagnosticCustomServiceInstanceBuilder:
    """Builder for DiagnosticCustomServiceInstance."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCustomServiceInstance = DiagnosticCustomServiceInstance()

    def build(self) -> DiagnosticCustomServiceInstance:
        """Build and return DiagnosticCustomServiceInstance object.

        Returns:
            DiagnosticCustomServiceInstance instance
        """
        # TODO: Add validation
        return self._obj
