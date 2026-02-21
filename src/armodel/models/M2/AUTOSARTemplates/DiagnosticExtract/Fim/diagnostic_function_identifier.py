"""DiagnosticFunctionIdentifier AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticFunctionIdentifier(DiagnosticCommonElement):
    """AUTOSAR DiagnosticFunctionIdentifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticFunctionIdentifier."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticFunctionIdentifier to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticFunctionIdentifier, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticFunctionIdentifier":
        """Deserialize XML element to DiagnosticFunctionIdentifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticFunctionIdentifier object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticFunctionIdentifier, cls).deserialize(element)



class DiagnosticFunctionIdentifierBuilder:
    """Builder for DiagnosticFunctionIdentifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticFunctionIdentifier = DiagnosticFunctionIdentifier()

    def build(self) -> DiagnosticFunctionIdentifier:
        """Build and return DiagnosticFunctionIdentifier object.

        Returns:
            DiagnosticFunctionIdentifier instance
        """
        # TODO: Add validation
        return self._obj
