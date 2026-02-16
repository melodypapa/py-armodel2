"""DataPrototypeGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.data_prototype_group import (
    DataPrototypeGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataPrototypeGroup(Identifiable):
    """AUTOSAR DataPrototypeGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_prototype_group_group_in_composition_instance_refs", None, False, True, DataPrototypeGroup),  # dataPrototypeGroupGroupInCompositionInstanceRefs
        ("implicit_datas", None, False, True, VariableDataPrototype),  # implicitDatas
    ]

    def __init__(self) -> None:
        """Initialize DataPrototypeGroup."""
        super().__init__()
        self.data_prototype_group_group_in_composition_instance_refs: list[DataPrototypeGroup] = []
        self.implicit_datas: list[VariableDataPrototype] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataPrototypeGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeGroup":
        """Create DataPrototypeGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataPrototypeGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataPrototypeGroup since parent returns ARObject
        return cast("DataPrototypeGroup", obj)


class DataPrototypeGroupBuilder:
    """Builder for DataPrototypeGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataPrototypeGroup = DataPrototypeGroup()

    def build(self) -> DataPrototypeGroup:
        """Build and return DataPrototypeGroup object.

        Returns:
            DataPrototypeGroup instance
        """
        # TODO: Add validation
        return self._obj
