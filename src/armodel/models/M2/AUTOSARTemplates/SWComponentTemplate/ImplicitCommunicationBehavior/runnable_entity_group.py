"""RunnableEntityGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 222)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 206)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_ImplicitCommunicationBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.runnable_entity import (
    RunnableEntity,
)


class RunnableEntityGroup(Identifiable):
    """AUTOSAR RunnableEntityGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    runnable_entities: list[RunnableEntity]
    runnable_entity_group_group_in_composition_instance_ref_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize RunnableEntityGroup."""
        super().__init__()
        self.runnable_entities: list[RunnableEntity] = []
        self.runnable_entity_group_group_in_composition_instance_ref_refs: list[ARRef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RunnableEntityGroup":
        """Deserialize XML element to RunnableEntityGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RunnableEntityGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RunnableEntityGroup, cls).deserialize(element)

        # Parse runnable_entities (list from container "RUNNABLE-ENTITIES")
        obj.runnable_entities = []
        container = ARObject._find_child_element(element, "RUNNABLE-ENTITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runnable_entities.append(child_value)

        # Parse runnable_entity_group_group_in_composition_instance_ref_refs (list from container "RUNNABLE-ENTITY-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REFS")
        obj.runnable_entity_group_group_in_composition_instance_ref_refs = []
        container = ARObject._find_child_element(element, "RUNNABLE-ENTITY-GROUP-GROUP-IN-COMPOSITION-INSTANCE-REFS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.runnable_entity_group_group_in_composition_instance_ref_refs.append(child_value)

        return obj



class RunnableEntityGroupBuilder:
    """Builder for RunnableEntityGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RunnableEntityGroup = RunnableEntityGroup()

    def build(self) -> RunnableEntityGroup:
        """Build and return RunnableEntityGroup object.

        Returns:
            RunnableEntityGroup instance
        """
        # TODO: Add validation
        return self._obj
