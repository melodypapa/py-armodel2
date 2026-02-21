"""DiagnosticEnvModeElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 89)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_EnvironmentalCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class DiagnosticEnvModeElement(Referrable, ABC):
    """AUTOSAR DiagnosticEnvModeElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize DiagnosticEnvModeElement."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnvModeElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnvModeElement, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnvModeElement":
        """Deserialize XML element to DiagnosticEnvModeElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnvModeElement object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticEnvModeElement, cls).deserialize(element)



class DiagnosticEnvModeElementBuilder:
    """Builder for DiagnosticEnvModeElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnvModeElement = DiagnosticEnvModeElement()

    def build(self) -> DiagnosticEnvModeElement:
        """Build and return DiagnosticEnvModeElement object.

        Returns:
            DiagnosticEnvModeElement instance
        """
        # TODO: Add validation
        return self._obj
