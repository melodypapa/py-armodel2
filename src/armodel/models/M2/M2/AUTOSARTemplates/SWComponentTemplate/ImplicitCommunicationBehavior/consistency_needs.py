"""ConsistencyNeeds AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.runnable_entity_group import (
    RunnableEntityGroup,
)


class ConsistencyNeeds(Identifiable):
    """AUTOSAR ConsistencyNeeds."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "dpg_does_nots": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataPrototypeGroup,
        ),  # dpgDoesNots
        "dpg_requireses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DataPrototypeGroup,
        ),  # dpgRequireses
        "reg_does_nots": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RunnableEntityGroup,
        ),  # regDoesNots
        "reg_requireses": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RunnableEntityGroup,
        ),  # regRequireses
    }

    def __init__(self) -> None:
        """Initialize ConsistencyNeeds."""
        super().__init__()
        self.dpg_does_nots: list[DataPrototypeGroup] = []
        self.dpg_requireses: list[DataPrototypeGroup] = []
        self.reg_does_nots: list[RunnableEntityGroup] = []
        self.reg_requireses: list[RunnableEntityGroup] = []


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
