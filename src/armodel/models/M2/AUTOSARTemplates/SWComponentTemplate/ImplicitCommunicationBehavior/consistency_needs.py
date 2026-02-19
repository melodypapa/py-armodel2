"""ConsistencyNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 221)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 178)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)


class ConsistencyNeeds(Identifiable):
    """AUTOSAR ConsistencyNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dpg_does_not_refs: list[ARRef]
    dpg_requirese_refs: list[ARRef]
    reg_does_not_refs: list[ARRef]
    reg_requirese_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize ConsistencyNeeds."""
        super().__init__()
        self.dpg_does_not_refs: list[ARRef] = []
        self.dpg_requirese_refs: list[ARRef] = []
        self.reg_does_not_refs: list[ARRef] = []
        self.reg_requirese_refs: list[ARRef] = []
    def serialize(self) -> ET.Element:
        """Serialize ConsistencyNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsistencyNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dpg_does_not_refs (list to container "DPG-DOES-NOTS")
        if self.dpg_does_not_refs:
            wrapper = ET.Element("DPG-DOES-NOTS")
            for item in self.dpg_does_not_refs:
                serialized = ARObject._serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize dpg_requirese_refs (list to container "DPG-REQUIRESES")
        if self.dpg_requirese_refs:
            wrapper = ET.Element("DPG-REQUIRESES")
            for item in self.dpg_requirese_refs:
                serialized = ARObject._serialize_item(item, "DataPrototypeGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reg_does_not_refs (list to container "REG-DOES-NOTS")
        if self.reg_does_not_refs:
            wrapper = ET.Element("REG-DOES-NOTS")
            for item in self.reg_does_not_refs:
                serialized = ARObject._serialize_item(item, "RunnableEntityGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reg_requirese_refs (list to container "REG-REQUIRESES")
        if self.reg_requirese_refs:
            wrapper = ET.Element("REG-REQUIRESES")
            for item in self.reg_requirese_refs:
                serialized = ARObject._serialize_item(item, "RunnableEntityGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeeds":
        """Deserialize XML element to ConsistencyNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsistencyNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsistencyNeeds, cls).deserialize(element)

        # Parse dpg_does_not_refs (list from container "DPG-DOES-NOTS")
        obj.dpg_does_not_refs = []
        container = ARObject._find_child_element(element, "DPG-DOES-NOTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dpg_does_not_refs.append(child_value)

        # Parse dpg_requirese_refs (list from container "DPG-REQUIRESES")
        obj.dpg_requirese_refs = []
        container = ARObject._find_child_element(element, "DPG-REQUIRESES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.dpg_requirese_refs.append(child_value)

        # Parse reg_does_not_refs (list from container "REG-DOES-NOTS")
        obj.reg_does_not_refs = []
        container = ARObject._find_child_element(element, "REG-DOES-NOTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reg_does_not_refs.append(child_value)

        # Parse reg_requirese_refs (list from container "REG-REQUIRESES")
        obj.reg_requirese_refs = []
        container = ARObject._find_child_element(element, "REG-REQUIRESES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.reg_requirese_refs.append(child_value)

        return obj



class ConsistencyNeedsBuilder:
    """Builder for ConsistencyNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConsistencyNeeds = ConsistencyNeeds()

    def build(self) -> ConsistencyNeeds:
        """Build and return ConsistencyNeeds object.

        Returns:
            ConsistencyNeeds instance
        """
        # TODO: Add validation
        return self._obj
