"""ConfidenceInterval AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime.multidimensional_time import (
    MultidimensionalTime,
)


class ConfidenceInterval(ARObject):
    """AUTOSAR ConfidenceInterval."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lower_bound: Optional[MultidimensionalTime]
    propability: Optional[Float]
    upper_bound: Optional[MultidimensionalTime]
    def __init__(self) -> None:
        """Initialize ConfidenceInterval."""
        super().__init__()
        self.lower_bound: Optional[MultidimensionalTime] = None
        self.propability: Optional[Float] = None
        self.upper_bound: Optional[MultidimensionalTime] = None

    def serialize(self) -> ET.Element:
        """Serialize ConfidenceInterval to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize lower_bound
        if self.lower_bound is not None:
            serialized = ARObject._serialize_item(self.lower_bound, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOWER-BOUND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize propability
        if self.propability is not None:
            serialized = ARObject._serialize_item(self.propability, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROPABILITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upper_bound
        if self.upper_bound is not None:
            serialized = ARObject._serialize_item(self.upper_bound, "MultidimensionalTime")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPPER-BOUND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConfidenceInterval":
        """Deserialize XML element to ConfidenceInterval object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConfidenceInterval object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse lower_bound
        child = ARObject._find_child_element(element, "LOWER-BOUND")
        if child is not None:
            lower_bound_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.lower_bound = lower_bound_value

        # Parse propability
        child = ARObject._find_child_element(element, "PROPABILITY")
        if child is not None:
            propability_value = child.text
            obj.propability = propability_value

        # Parse upper_bound
        child = ARObject._find_child_element(element, "UPPER-BOUND")
        if child is not None:
            upper_bound_value = ARObject._deserialize_by_tag(child, "MultidimensionalTime")
            obj.upper_bound = upper_bound_value

        return obj



class ConfidenceIntervalBuilder:
    """Builder for ConfidenceInterval."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConfidenceInterval = ConfidenceInterval()

    def build(self) -> ConfidenceInterval:
        """Build and return ConfidenceInterval object.

        Returns:
            ConfidenceInterval instance
        """
        # TODO: Add validation
        return self._obj
