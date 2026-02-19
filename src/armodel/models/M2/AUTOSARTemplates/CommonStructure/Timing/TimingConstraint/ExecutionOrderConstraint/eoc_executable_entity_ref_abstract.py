"""EOCExecutableEntityRefAbstract AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class EOCExecutableEntityRefAbstract(Identifiable, ABC):
    """AUTOSAR EOCExecutableEntityRefAbstract."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    direct_successors: list[Any]
    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefAbstract."""
        super().__init__()
        self.direct_successors: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize EOCExecutableEntityRefAbstract to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EOCExecutableEntityRefAbstract, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direct_successors (list to container "DIRECT-SUCCESSORS")
        if self.direct_successors:
            wrapper = ET.Element("DIRECT-SUCCESSORS")
            for item in self.direct_successors:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefAbstract":
        """Deserialize XML element to EOCExecutableEntityRefAbstract object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRefAbstract object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCExecutableEntityRefAbstract, cls).deserialize(element)

        # Parse direct_successors (list from container "DIRECT-SUCCESSORS")
        obj.direct_successors = []
        container = ARObject._find_child_element(element, "DIRECT-SUCCESSORS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.direct_successors.append(child_value)

        return obj



class EOCExecutableEntityRefAbstractBuilder:
    """Builder for EOCExecutableEntityRefAbstract."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRefAbstract = EOCExecutableEntityRefAbstract()

    def build(self) -> EOCExecutableEntityRefAbstract:
        """Build and return EOCExecutableEntityRefAbstract object.

        Returns:
            EOCExecutableEntityRefAbstract instance
        """
        # TODO: Add validation
        return self._obj
