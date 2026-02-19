"""DiagnosticEnvBswModeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 90)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition.diagnostic_env_mode_element import (
    DiagnosticEnvModeElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class DiagnosticEnvBswModeElement(DiagnosticEnvModeElement):
    """AUTOSAR DiagnosticEnvBswModeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize DiagnosticEnvBswModeElement."""
        super().__init__()
        self.mode: Optional[ModeDeclaration] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvBswModeElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvBswModeElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mode
        if self.mode is not None:
            serialized = ARObject._serialize_item(self.mode, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvBswModeElement":
        """Deserialize XML element to DiagnosticEnvBswModeElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvBswModeElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEnvBswModeElement, cls).deserialize(element)

        # Parse mode
        child = ARObject._find_child_element(element, "MODE")
        if child is not None:
            mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.mode = mode_value

        return obj



class DiagnosticEnvBswModeElementBuilder:
    """Builder for DiagnosticEnvBswModeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvBswModeElement = DiagnosticEnvBswModeElement()

    def build(self) -> DiagnosticEnvBswModeElement:
        """Build and return DiagnosticEnvBswModeElement object.

        Returns:
            DiagnosticEnvBswModeElement instance
        """
        # TODO: Add validation
        return self._obj
