"""DiagnosticConnectedIndicator AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 166)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator.diagnostic_indicator import (
    DiagnosticIndicator,
)


class DiagnosticConnectedIndicator(Identifiable):
    """AUTOSAR DiagnosticConnectedIndicator."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    behavior_indicator_behavior_enum: Optional[Any]
    healing_cycle: Optional[PositiveInteger]
    indicator: Optional[DiagnosticIndicator]
    indicator_failure: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DiagnosticConnectedIndicator."""
        super().__init__()
        self.behavior_indicator_behavior_enum: Optional[Any] = None
        self.healing_cycle: Optional[PositiveInteger] = None
        self.indicator: Optional[DiagnosticIndicator] = None
        self.indicator_failure: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticConnectedIndicator to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticConnectedIndicator, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize behavior_indicator_behavior_enum
        if self.behavior_indicator_behavior_enum is not None:
            serialized = ARObject._serialize_item(self.behavior_indicator_behavior_enum, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR-INDICATOR-BEHAVIOR-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize healing_cycle
        if self.healing_cycle is not None:
            serialized = ARObject._serialize_item(self.healing_cycle, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HEALING-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indicator
        if self.indicator is not None:
            serialized = ARObject._serialize_item(self.indicator, "DiagnosticIndicator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDICATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indicator_failure
        if self.indicator_failure is not None:
            serialized = ARObject._serialize_item(self.indicator_failure, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDICATOR-FAILURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticConnectedIndicator":
        """Deserialize XML element to DiagnosticConnectedIndicator object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticConnectedIndicator object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticConnectedIndicator, cls).deserialize(element)

        # Parse behavior_indicator_behavior_enum
        child = ARObject._find_child_element(element, "BEHAVIOR-INDICATOR-BEHAVIOR-ENUM")
        if child is not None:
            behavior_indicator_behavior_enum_value = child.text
            obj.behavior_indicator_behavior_enum = behavior_indicator_behavior_enum_value

        # Parse healing_cycle
        child = ARObject._find_child_element(element, "HEALING-CYCLE")
        if child is not None:
            healing_cycle_value = child.text
            obj.healing_cycle = healing_cycle_value

        # Parse indicator
        child = ARObject._find_child_element(element, "INDICATOR")
        if child is not None:
            indicator_value = ARObject._deserialize_by_tag(child, "DiagnosticIndicator")
            obj.indicator = indicator_value

        # Parse indicator_failure
        child = ARObject._find_child_element(element, "INDICATOR-FAILURE")
        if child is not None:
            indicator_failure_value = child.text
            obj.indicator_failure = indicator_failure_value

        return obj



class DiagnosticConnectedIndicatorBuilder:
    """Builder for DiagnosticConnectedIndicator."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticConnectedIndicator = DiagnosticConnectedIndicator()

    def build(self) -> DiagnosticConnectedIndicator:
        """Build and return DiagnosticConnectedIndicator object.

        Returns:
            DiagnosticConnectedIndicator instance
        """
        # TODO: Add validation
        return self._obj
