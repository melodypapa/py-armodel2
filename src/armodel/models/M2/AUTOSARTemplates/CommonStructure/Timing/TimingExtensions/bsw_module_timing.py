"""BswModuleTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 28)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingExtensions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingExtensions.timing_extension import (
    TimingExtension,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)


class BswModuleTiming(TimingExtension):
    """AUTOSAR BswModuleTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    behavior: Optional[BswInternalBehavior]
    def __init__(self) -> None:
        """Initialize BswModuleTiming."""
        super().__init__()
        self.behavior: Optional[BswInternalBehavior] = None
    def serialize(self) -> ET.Element:
        """Serialize BswModuleTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswModuleTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize behavior
        if self.behavior is not None:
            serialized = ARObject._serialize_item(self.behavior, "BswInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswModuleTiming":
        """Deserialize XML element to BswModuleTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswModuleTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswModuleTiming, cls).deserialize(element)

        # Parse behavior
        child = ARObject._find_child_element(element, "BEHAVIOR")
        if child is not None:
            behavior_value = ARObject._deserialize_by_tag(child, "BswInternalBehavior")
            obj.behavior = behavior_value

        return obj



class BswModuleTimingBuilder:
    """Builder for BswModuleTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswModuleTiming = BswModuleTiming()

    def build(self) -> BswModuleTiming:
        """Build and return BswModuleTiming object.

        Returns:
            BswModuleTiming instance
        """
        # TODO: Add validation
        return self._obj
