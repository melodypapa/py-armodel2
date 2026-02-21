"""ConfidenceInterval AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 112)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_EventTriggeringConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConfidenceInterval, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lower_bound
        if self.lower_bound is not None:
            serialized = SerializationHelper.serialize_item(self.lower_bound, "MultidimensionalTime")
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
            serialized = SerializationHelper.serialize_item(self.propability, "Float")
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
            serialized = SerializationHelper.serialize_item(self.upper_bound, "MultidimensionalTime")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConfidenceInterval, cls).deserialize(element)

        # Parse lower_bound
        child = SerializationHelper.find_child_element(element, "LOWER-BOUND")
        if child is not None:
            lower_bound_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
            obj.lower_bound = lower_bound_value

        # Parse propability
        child = SerializationHelper.find_child_element(element, "PROPABILITY")
        if child is not None:
            propability_value = child.text
            obj.propability = propability_value

        # Parse upper_bound
        child = SerializationHelper.find_child_element(element, "UPPER-BOUND")
        if child is not None:
            upper_bound_value = SerializationHelper.deserialize_by_tag(child, "MultidimensionalTime")
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
