"""DiagnosticEcuResetClass AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_EcuReset.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService.diagnostic_service_class import (
    DiagnosticServiceClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.EcuReset import (
    DiagnosticResponseToEcuResetEnum,
)


class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """AUTOSAR DiagnosticEcuResetClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    respond_to: Optional[DiagnosticResponseToEcuResetEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticEcuResetClass."""
        super().__init__()
        self.respond_to: Optional[DiagnosticResponseToEcuResetEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEcuResetClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEcuResetClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize respond_to
        if self.respond_to is not None:
            serialized = ARObject._serialize_item(self.respond_to, "DiagnosticResponseToEcuResetEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPOND-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEcuResetClass":
        """Deserialize XML element to DiagnosticEcuResetClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEcuResetClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEcuResetClass, cls).deserialize(element)

        # Parse respond_to
        child = ARObject._find_child_element(element, "RESPOND-TO")
        if child is not None:
            respond_to_value = DiagnosticResponseToEcuResetEnum.deserialize(child)
            obj.respond_to = respond_to_value

        return obj



class DiagnosticEcuResetClassBuilder:
    """Builder for DiagnosticEcuResetClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEcuResetClass = DiagnosticEcuResetClass()

    def build(self) -> DiagnosticEcuResetClass:
        """Build and return DiagnosticEcuResetClass object.

        Returns:
            DiagnosticEcuResetClass instance
        """
        # TODO: Add validation
        return self._obj
