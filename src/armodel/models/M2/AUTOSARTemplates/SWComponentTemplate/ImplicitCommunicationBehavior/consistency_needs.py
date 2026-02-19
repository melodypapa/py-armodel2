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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeeds":
        """Deserialize XML element to ConsistencyNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsistencyNeeds object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse dpg_does_not_refs (list)
        obj.dpg_does_not_refs = []
        for child in ARObject._find_all_child_elements(element, "DPG-DOES-NOTS"):
            dpg_does_not_refs_value = ARObject._deserialize_by_tag(child, "DataPrototypeGroup")
            obj.dpg_does_not_refs.append(dpg_does_not_refs_value)

        # Parse dpg_requirese_refs (list)
        obj.dpg_requirese_refs = []
        for child in ARObject._find_all_child_elements(element, "DPG-REQUIRESES"):
            dpg_requirese_refs_value = ARObject._deserialize_by_tag(child, "DataPrototypeGroup")
            obj.dpg_requirese_refs.append(dpg_requirese_refs_value)

        # Parse reg_does_not_refs (list)
        obj.reg_does_not_refs = []
        for child in ARObject._find_all_child_elements(element, "REG-DOES-NOTS"):
            reg_does_not_refs_value = ARObject._deserialize_by_tag(child, "RunnableEntityGroup")
            obj.reg_does_not_refs.append(reg_does_not_refs_value)

        # Parse reg_requirese_refs (list)
        obj.reg_requirese_refs = []
        for child in ARObject._find_all_child_elements(element, "REG-REQUIRESES"):
            reg_requirese_refs_value = ARObject._deserialize_by_tag(child, "RunnableEntityGroup")
            obj.reg_requirese_refs.append(reg_requirese_refs_value)

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
