"""DiagnosticComponentNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 816)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticComponentNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticComponentNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize DiagnosticComponentNeeds."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticComponentNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticComponentNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticComponentNeeds":
        """Deserialize XML element to DiagnosticComponentNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticComponentNeeds object
        """
        # Delegate to parent class to handle inherited attributes
        return super(DiagnosticComponentNeeds, cls).deserialize(element)



class DiagnosticComponentNeedsBuilder:
    """Builder for DiagnosticComponentNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticComponentNeeds = DiagnosticComponentNeeds()

    def build(self) -> DiagnosticComponentNeeds:
        """Build and return DiagnosticComponentNeeds object.

        Returns:
            DiagnosticComponentNeeds instance
        """
        # TODO: Add validation
        return self._obj
