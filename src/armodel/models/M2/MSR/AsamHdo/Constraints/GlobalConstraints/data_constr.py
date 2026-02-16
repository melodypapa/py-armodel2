"""DataConstr AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr_rule import (
    DataConstrRule,
)


class DataConstr(ARElement):
    """AUTOSAR DataConstr."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("data_constr_rules", None, False, True, DataConstrRule),  # dataConstrRules
    ]

    def __init__(self) -> None:
        """Initialize DataConstr."""
        super().__init__()
        self.data_constr_rules: list[DataConstrRule] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataConstr to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataConstr":
        """Create DataConstr from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataConstr instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataConstr since parent returns ARObject
        return cast("DataConstr", obj)


class DataConstrBuilder:
    """Builder for DataConstr."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataConstr = DataConstr()

    def build(self) -> DataConstr:
        """Build and return DataConstr object.

        Returns:
            DataConstr instance
        """
        # TODO: Add validation
        return self._obj
