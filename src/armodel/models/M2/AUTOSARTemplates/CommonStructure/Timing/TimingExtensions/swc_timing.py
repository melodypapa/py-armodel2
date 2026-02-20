"""SwcTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 25)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.swc_internal_behavior import (
    SwcInternalBehavior,
)


class SwcTiming(TimingExtension):
    """AUTOSAR SwcTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    behavior_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcTiming."""
        super().__init__()
        self.behavior_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize behavior_ref
        if self.behavior_ref is not None:
            serialized = ARObject._serialize_item(self.behavior_ref, "SwcInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcTiming":
        """Deserialize XML element to SwcTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcTiming, cls).deserialize(element)

        # Parse behavior_ref
        child = ARObject._find_child_element(element, "BEHAVIOR-REF")
        if child is not None:
            behavior_ref_value = ARRef.deserialize(child)
            obj.behavior_ref = behavior_ref_value

        return obj



class SwcTimingBuilder:
    """Builder for SwcTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcTiming = SwcTiming()

    def build(self) -> SwcTiming:
        """Build and return SwcTiming object.

        Returns:
            SwcTiming instance
        """
        # TODO: Add validation
        return self._obj
