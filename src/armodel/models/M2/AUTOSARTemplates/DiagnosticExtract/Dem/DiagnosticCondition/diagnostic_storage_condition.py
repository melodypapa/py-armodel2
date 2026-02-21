"""DiagnosticStorageCondition AUTOSAR element.

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
from armodel.serialization import SerializationHelper


class DiagnosticStorageCondition(DiagnosticCondition):
    """AUTOSAR DiagnosticStorageCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticStorageCondition."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStorageCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStorageCondition, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageCondition":
        """Deserialize XML element to DiagnosticStorageCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageCondition object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticStorageCondition, cls).deserialize(element)



class DiagnosticStorageConditionBuilder:
    """Builder for DiagnosticStorageCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageCondition = DiagnosticStorageCondition()

    def build(self) -> DiagnosticStorageCondition:
        """Build and return DiagnosticStorageCondition object.

        Returns:
            DiagnosticStorageCondition instance
        """
        # TODO: Add validation
        return self._obj
