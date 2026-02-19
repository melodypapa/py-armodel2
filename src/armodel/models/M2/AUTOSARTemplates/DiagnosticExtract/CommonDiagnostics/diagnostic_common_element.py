"""DiagnosticCommonElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 32)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_CommonDiagnostics.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DiagnosticCommonElement(ARElement, ABC):
    """AUTOSAR DiagnosticCommonElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticCommonElement."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticCommonElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticCommonElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCommonElement":
        """Deserialize XML element to DiagnosticCommonElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCommonElement object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticCommonElement, cls).deserialize(element)



class DiagnosticCommonElementBuilder:
    """Builder for DiagnosticCommonElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCommonElement = DiagnosticCommonElement()

    def build(self) -> DiagnosticCommonElement:
        """Build and return DiagnosticCommonElement object.

        Returns:
            DiagnosticCommonElement instance
        """
        # TODO: Add validation
        return self._obj
