"""ConsistencyNeeds AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("dpg_does_nots", None, False, True, DataPrototypeGroup),  # dpgDoesNots
        ("dpg_requireses", None, False, True, DataPrototypeGroup),  # dpgRequireses
        ("reg_does_nots", None, False, True, RunnableEntityGroup),  # regDoesNots
        ("reg_requireses", None, False, True, RunnableEntityGroup),  # regRequireses
    ]

    def __init__(self) -> None:
        """Initialize ConsistencyNeeds."""
        super().__init__()
        self.dpg_does_nots: list[DataPrototypeGroup] = []
        self.dpg_requireses: list[DataPrototypeGroup] = []
        self.reg_does_nots: list[RunnableEntityGroup] = []
        self.reg_requireses: list[RunnableEntityGroup] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ConsistencyNeeds to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsistencyNeeds":
        """Create ConsistencyNeeds from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ConsistencyNeeds instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ConsistencyNeeds since parent returns ARObject
        return cast("ConsistencyNeeds", obj)


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
