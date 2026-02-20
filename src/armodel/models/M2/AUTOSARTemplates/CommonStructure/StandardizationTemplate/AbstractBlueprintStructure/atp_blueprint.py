"""AtpBlueprint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 305)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 424)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 161)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_AbstractBlueprintStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.blueprint_policy import (
    BlueprintPolicy,
)
from abc import ABC, abstractmethod


class AtpBlueprint(Identifiable, ABC):
    """AUTOSAR AtpBlueprint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    blueprint_policies: list[BlueprintPolicy]
    def __init__(self) -> None:
        """Initialize AtpBlueprint."""
        super().__init__()
        self.blueprint_policies: list[BlueprintPolicy] = []

    def serialize(self) -> ET.Element:
        """Serialize AtpBlueprint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AtpBlueprint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize blueprint_policies (list to container "BLUEPRINT-POLICIES")
        if self.blueprint_policies:
            wrapper = ET.Element("BLUEPRINT-POLICIES")
            for item in self.blueprint_policies:
                serialized = ARObject._serialize_item(item, "BlueprintPolicy")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpBlueprint":
        """Deserialize XML element to AtpBlueprint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpBlueprint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AtpBlueprint, cls).deserialize(element)

        # Parse blueprint_policies (list from container "BLUEPRINT-POLICIES")
        obj.blueprint_policies = []
        container = ARObject._find_child_element(element, "BLUEPRINT-POLICIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.blueprint_policies.append(child_value)

        return obj



class AtpBlueprintBuilder:
    """Builder for AtpBlueprint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpBlueprint = AtpBlueprint()

    def build(self) -> AtpBlueprint:
        """Build and return AtpBlueprint object.

        Returns:
            AtpBlueprint instance
        """
        # TODO: Add validation
        return self._obj
