"""DdsLatencyBudget AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 532)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)


class DdsLatencyBudget(ARObject):
    """AUTOSAR DdsLatencyBudget."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    latency_budget: Optional[Float]
    def __init__(self) -> None:
        """Initialize DdsLatencyBudget."""
        super().__init__()
        self.latency_budget: Optional[Float] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsLatencyBudget to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize latency_budget
        if self.latency_budget is not None:
            serialized = ARObject._serialize_item(self.latency_budget, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LATENCY-BUDGET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsLatencyBudget":
        """Deserialize XML element to DdsLatencyBudget object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsLatencyBudget object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse latency_budget
        child = ARObject._find_child_element(element, "LATENCY-BUDGET")
        if child is not None:
            latency_budget_value = child.text
            obj.latency_budget = latency_budget_value

        return obj



class DdsLatencyBudgetBuilder:
    """Builder for DdsLatencyBudget."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsLatencyBudget = DdsLatencyBudget()

    def build(self) -> DdsLatencyBudget:
        """Build and return DdsLatencyBudget object.

        Returns:
            DdsLatencyBudget instance
        """
        # TODO: Add validation
        return self._obj
