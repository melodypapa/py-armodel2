"""BswCompositionTiming AUTOSAR element.

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
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
    BswImplementation,
)


class BswCompositionTiming(TimingExtension):
    """AUTOSAR BswCompositionTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implementations: list[BswImplementation]
    def __init__(self) -> None:
        """Initialize BswCompositionTiming."""
        super().__init__()
        self.implementations: list[BswImplementation] = []
    def serialize(self) -> ET.Element:
        """Serialize BswCompositionTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswCompositionTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implementations (list to container "IMPLEMENTATIONS")
        if self.implementations:
            wrapper = ET.Element("IMPLEMENTATIONS")
            for item in self.implementations:
                serialized = ARObject._serialize_item(item, "BswImplementation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswCompositionTiming":
        """Deserialize XML element to BswCompositionTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswCompositionTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswCompositionTiming, cls).deserialize(element)

        # Parse implementations (list from container "IMPLEMENTATIONS")
        obj.implementations = []
        container = ARObject._find_child_element(element, "IMPLEMENTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.implementations.append(child_value)

        return obj



class BswCompositionTimingBuilder:
    """Builder for BswCompositionTiming."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswCompositionTiming = BswCompositionTiming()

    def build(self) -> BswCompositionTiming:
        """Build and return BswCompositionTiming object.

        Returns:
            BswCompositionTiming instance
        """
        # TODO: Add validation
        return self._obj
