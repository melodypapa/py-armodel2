"""DiagnosticAging AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 202)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticAging.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class DiagnosticAging(DiagnosticCommonElement):
    """AUTOSAR DiagnosticAging."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aging_cycle_ref: Optional[Any]
    threshold: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticAging."""
        super().__init__()
        self.aging_cycle_ref: Optional[Any] = None
        self.threshold: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAging to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAging, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aging_cycle_ref
        if self.aging_cycle_ref is not None:
            serialized = ARObject._serialize_item(self.aging_cycle_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGING-CYCLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize threshold
        if self.threshold is not None:
            serialized = ARObject._serialize_item(self.threshold, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("THRESHOLD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAging":
        """Deserialize XML element to DiagnosticAging object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAging object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAging, cls).deserialize(element)

        # Parse aging_cycle_ref
        child = ARObject._find_child_element(element, "AGING-CYCLE-REF")
        if child is not None:
            aging_cycle_ref_value = ARRef.deserialize(child)
            obj.aging_cycle_ref = aging_cycle_ref_value

        # Parse threshold
        child = ARObject._find_child_element(element, "THRESHOLD")
        if child is not None:
            threshold_value = child.text
            obj.threshold = threshold_value

        return obj



class DiagnosticAgingBuilder:
    """Builder for DiagnosticAging."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAging = DiagnosticAging()

    def build(self) -> DiagnosticAging:
        """Build and return DiagnosticAging object.

        Returns:
            DiagnosticAging instance
        """
        # TODO: Add validation
        return self._obj
