"""DiagnosticCustomServiceClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_CommonService.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticCustomServiceClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticCustomServiceClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    custom_service: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticCustomServiceClass."""
        super().__init__()
        self.custom_service: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticCustomServiceClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticCustomServiceClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize custom_service
        if self.custom_service is not None:
            serialized = ARObject._serialize_item(self.custom_service, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CUSTOM-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCustomServiceClass":
        """Deserialize XML element to DiagnosticCustomServiceClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCustomServiceClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticCustomServiceClass, cls).deserialize(element)

        # Parse custom_service
        child = ARObject._find_child_element(element, "CUSTOM-SERVICE")
        if child is not None:
            custom_service_value = child.text
            obj.custom_service = custom_service_value

        return obj



class DiagnosticCustomServiceClassBuilder:
    """Builder for DiagnosticCustomServiceClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCustomServiceClass = DiagnosticCustomServiceClass()

    def build(self) -> DiagnosticCustomServiceClass:
        """Build and return DiagnosticCustomServiceClass object.

        Returns:
            DiagnosticCustomServiceClass instance
        """
        # TODO: Add validation
        return self._obj
