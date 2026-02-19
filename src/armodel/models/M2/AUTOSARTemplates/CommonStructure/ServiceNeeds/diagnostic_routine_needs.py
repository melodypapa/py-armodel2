"""DiagnosticRoutineNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 247)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 126)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 780)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticRoutineTypeEnum,
)


class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticRoutineNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diag_routine: Optional[DiagnosticRoutineTypeEnum]
    def __init__(self) -> None:
        """Initialize DiagnosticRoutineNeeds."""
        super().__init__()
        self.diag_routine: Optional[DiagnosticRoutineTypeEnum] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticRoutineNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticRoutineNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diag_routine
        if self.diag_routine is not None:
            serialized = ARObject._serialize_item(self.diag_routine, "DiagnosticRoutineTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAG-ROUTINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticRoutineNeeds":
        """Deserialize XML element to DiagnosticRoutineNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticRoutineNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticRoutineNeeds, cls).deserialize(element)

        # Parse diag_routine
        child = ARObject._find_child_element(element, "DIAG-ROUTINE")
        if child is not None:
            diag_routine_value = DiagnosticRoutineTypeEnum.deserialize(child)
            obj.diag_routine = diag_routine_value

        return obj



class DiagnosticRoutineNeedsBuilder:
    """Builder for DiagnosticRoutineNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticRoutineNeeds = DiagnosticRoutineNeeds()

    def build(self) -> DiagnosticRoutineNeeds:
        """Build and return DiagnosticRoutineNeeds object.

        Returns:
            DiagnosticRoutineNeeds instance
        """
        # TODO: Add validation
        return self._obj
