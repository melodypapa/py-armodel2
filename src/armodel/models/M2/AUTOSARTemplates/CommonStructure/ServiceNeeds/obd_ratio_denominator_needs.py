"""ObdRatioDenominatorNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 802)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticDenominatorConditionEnum,
)


class ObdRatioDenominatorNeeds(DiagnosticCapabilityElement):
    """AUTOSAR ObdRatioDenominatorNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    denominator: Optional[DiagnosticDenominatorConditionEnum]
    def __init__(self) -> None:
        """Initialize ObdRatioDenominatorNeeds."""
        super().__init__()
        self.denominator: Optional[DiagnosticDenominatorConditionEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize ObdRatioDenominatorNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ObdRatioDenominatorNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize denominator
        if self.denominator is not None:
            serialized = ARObject._serialize_item(self.denominator, "DiagnosticDenominatorConditionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DENOMINATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ObdRatioDenominatorNeeds":
        """Deserialize XML element to ObdRatioDenominatorNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ObdRatioDenominatorNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ObdRatioDenominatorNeeds, cls).deserialize(element)

        # Parse denominator
        child = ARObject._find_child_element(element, "DENOMINATOR")
        if child is not None:
            denominator_value = DiagnosticDenominatorConditionEnum.deserialize(child)
            obj.denominator = denominator_value

        return obj



class ObdRatioDenominatorNeedsBuilder:
    """Builder for ObdRatioDenominatorNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ObdRatioDenominatorNeeds = ObdRatioDenominatorNeeds()

    def build(self) -> ObdRatioDenominatorNeeds:
        """Build and return ObdRatioDenominatorNeeds object.

        Returns:
            ObdRatioDenominatorNeeds instance
        """
        # TODO: Add validation
        return self._obj
