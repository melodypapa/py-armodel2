"""DiagnosticAuthTransmitCertificateEvaluation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 101)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)


class DiagnosticAuthTransmitCertificateEvaluation(Identifiable):
    """AUTOSAR DiagnosticAuthTransmitCertificateEvaluation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    evaluation_id: Optional[PositiveInteger]
    function: Optional[String]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificateEvaluation."""
        super().__init__()
        self.evaluation_id: Optional[PositiveInteger] = None
        self.function: Optional[String] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthTransmitCertificateEvaluation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthTransmitCertificateEvaluation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize evaluation_id
        if self.evaluation_id is not None:
            serialized = ARObject._serialize_item(self.evaluation_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVALUATION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize function
        if self.function is not None:
            serialized = ARObject._serialize_item(self.function, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificateEvaluation":
        """Deserialize XML element to DiagnosticAuthTransmitCertificateEvaluation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthTransmitCertificateEvaluation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthTransmitCertificateEvaluation, cls).deserialize(element)

        # Parse evaluation_id
        child = ARObject._find_child_element(element, "EVALUATION-ID")
        if child is not None:
            evaluation_id_value = child.text
            obj.evaluation_id = evaluation_id_value

        # Parse function
        child = ARObject._find_child_element(element, "FUNCTION")
        if child is not None:
            function_value = child.text
            obj.function = function_value

        return obj



class DiagnosticAuthTransmitCertificateEvaluationBuilder:
    """Builder for DiagnosticAuthTransmitCertificateEvaluation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificateEvaluation = DiagnosticAuthTransmitCertificateEvaluation()

    def build(self) -> DiagnosticAuthTransmitCertificateEvaluation:
        """Build and return DiagnosticAuthTransmitCertificateEvaluation object.

        Returns:
            DiagnosticAuthTransmitCertificateEvaluation instance
        """
        # TODO: Add validation
        return self._obj
