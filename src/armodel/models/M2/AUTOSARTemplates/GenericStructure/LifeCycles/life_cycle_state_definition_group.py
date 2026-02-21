"""LifeCycleStateDefinitionGroup AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 388)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 196)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)


class LifeCycleStateDefinitionGroup(ARElement):
    """AUTOSAR LifeCycleStateDefinitionGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    lc_states: list[LifeCycleState]
    def __init__(self) -> None:
        """Initialize LifeCycleStateDefinitionGroup."""
        super().__init__()
        self.lc_states: list[LifeCycleState] = []

    def serialize(self) -> ET.Element:
        """Serialize LifeCycleStateDefinitionGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCycleStateDefinitionGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize lc_states (list to container "LC-STATES")
        if self.lc_states:
            wrapper = ET.Element("LC-STATES")
            for item in self.lc_states:
                serialized = SerializationHelper.serialize_item(item, "LifeCycleState")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleStateDefinitionGroup":
        """Deserialize XML element to LifeCycleStateDefinitionGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleStateDefinitionGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCycleStateDefinitionGroup, cls).deserialize(element)

        # Parse lc_states (list from container "LC-STATES")
        obj.lc_states = []
        container = SerializationHelper.find_child_element(element, "LC-STATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lc_states.append(child_value)

        return obj



class LifeCycleStateDefinitionGroupBuilder:
    """Builder for LifeCycleStateDefinitionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleStateDefinitionGroup = LifeCycleStateDefinitionGroup()

    def build(self) -> LifeCycleStateDefinitionGroup:
        """Build and return LifeCycleStateDefinitionGroup object.

        Returns:
            LifeCycleStateDefinitionGroup instance
        """
        # TODO: Add validation
        return self._obj
