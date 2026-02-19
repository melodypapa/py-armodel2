"""LifeCycleInfoSet AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 391)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 195)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_info import (
    LifeCycleInfo,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_period import (
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state import (
    LifeCycleState,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles.life_cycle_state_definition_group import (
    LifeCycleStateDefinitionGroup,
)


class LifeCycleInfoSet(ARElement):
    """AUTOSAR LifeCycleInfoSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_lc_state: LifeCycleState
    default_period: Optional[LifeCyclePeriod]
    life_cycle_infos: list[LifeCycleInfo]
    used_life_cycle: LifeCycleStateDefinitionGroup
    def __init__(self) -> None:
        """Initialize LifeCycleInfoSet."""
        super().__init__()
        self.default_lc_state: LifeCycleState = None
        self.default_period: Optional[LifeCyclePeriod] = None
        self.life_cycle_infos: list[LifeCycleInfo] = []
        self.used_life_cycle: LifeCycleStateDefinitionGroup = None
    def serialize(self) -> ET.Element:
        """Serialize LifeCycleInfoSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LifeCycleInfoSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_lc_state
        if self.default_lc_state is not None:
            serialized = ARObject._serialize_item(self.default_lc_state, "LifeCycleState")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-LC-STATE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize default_period
        if self.default_period is not None:
            serialized = ARObject._serialize_item(self.default_period, "LifeCyclePeriod")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize life_cycle_infos (list to container "LIFE-CYCLE-INFOS")
        if self.life_cycle_infos:
            wrapper = ET.Element("LIFE-CYCLE-INFOS")
            for item in self.life_cycle_infos:
                serialized = ARObject._serialize_item(item, "LifeCycleInfo")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize used_life_cycle
        if self.used_life_cycle is not None:
            serialized = ARObject._serialize_item(self.used_life_cycle, "LifeCycleStateDefinitionGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-LIFE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCycleInfoSet":
        """Deserialize XML element to LifeCycleInfoSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCycleInfoSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LifeCycleInfoSet, cls).deserialize(element)

        # Parse default_lc_state
        child = ARObject._find_child_element(element, "DEFAULT-LC-STATE")
        if child is not None:
            default_lc_state_value = ARObject._deserialize_by_tag(child, "LifeCycleState")
            obj.default_lc_state = default_lc_state_value

        # Parse default_period
        child = ARObject._find_child_element(element, "DEFAULT-PERIOD")
        if child is not None:
            default_period_value = ARObject._deserialize_by_tag(child, "LifeCyclePeriod")
            obj.default_period = default_period_value

        # Parse life_cycle_infos (list from container "LIFE-CYCLE-INFOS")
        obj.life_cycle_infos = []
        container = ARObject._find_child_element(element, "LIFE-CYCLE-INFOS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.life_cycle_infos.append(child_value)

        # Parse used_life_cycle
        child = ARObject._find_child_element(element, "USED-LIFE-CYCLE")
        if child is not None:
            used_life_cycle_value = ARObject._deserialize_by_tag(child, "LifeCycleStateDefinitionGroup")
            obj.used_life_cycle = used_life_cycle_value

        return obj



class LifeCycleInfoSetBuilder:
    """Builder for LifeCycleInfoSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCycleInfoSet = LifeCycleInfoSet()

    def build(self) -> LifeCycleInfoSet:
        """Build and return LifeCycleInfoSet object.

        Returns:
            LifeCycleInfoSet instance
        """
        # TODO: Add validation
        return self._obj
