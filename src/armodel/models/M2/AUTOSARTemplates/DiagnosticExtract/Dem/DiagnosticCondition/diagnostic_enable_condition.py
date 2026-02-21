"""DiagnosticEnableCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 194)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticCondition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticCondition.diagnostic_condition import (
    DiagnosticCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticEnableCondition(DiagnosticCondition):
    """AUTOSAR DiagnosticEnableCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticEnableCondition."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEnableCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEnableCondition, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticEnableCondition":
        """Deserialize XML element to DiagnosticEnableCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEnableCondition object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticEnableCondition, cls).deserialize(element)



class DiagnosticEnableConditionBuilder:
    """Builder for DiagnosticEnableCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEnableCondition = DiagnosticEnableCondition()

    def build(self) -> DiagnosticEnableCondition:
        """Build and return DiagnosticEnableCondition object.

        Returns:
            DiagnosticEnableCondition instance
        """
        # TODO: Add validation
        return self._obj
